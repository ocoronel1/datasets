"""General-purpose training script for image-to-image translation.

This script works for various models (with option '--model': e.g., pix2pix, cyclegan, colorization) and
different datasets (with option '--dataset_mode': e.g., aligned, unaligned, single, colorization).
You need to specify the dataset ('--dataroot'), experiment name ('--name'), and model ('--model').

It first creates model, dataset, and visualizer given the option.
It then does standard network training. During the training, it also visualize/save the images, print/save the loss plot, and save models.
The script supports continue/resume training. Use '--continue_train' to resume your previous training.

Example:
    Train a CycleGAN model:
        python train.py --dataroot ./datasets/maps --name maps_cyclegan --model cycle_gan
    Train a pix2pix model:
        python train.py --dataroot ./datasets/facades --name facades_pix2pix --model pix2pix --direction BtoA

See options/base_options.py and options/train_options.py for more training options.
See training and test tips at: https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix/blob/master/docs/tips.md
See frequently asked questions at: https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix/blob/master/docs/qa.md
"""
import time
from options.train_options import TrainOptions
from data import create_dataset
from models import create_model
from util.visualizer import Visualizer
from collections import defaultdict
#from ax import optimize
from skopt.space import Real
from skopt.utils import use_named_args
from skopt import gp_minimize
from skopt import dump, load
from skopt import callbacks
from skopt.callbacks import CheckpointSaver

# python train.py --dataroot /home/w210/gan/pytorch-CycleGAN-and-pix2pix/pytorch-CycleGAN-and-pix2pix/dataroot --model cycle_gan --gpu_ids -1 --n_epochs 0 --n_epochs_decay 1

def run_all(opt):
    for i in range(3):
        print(i)
        model = run_model(opt)
        test_loss = run_test(opt.dataroot, model)
        print(test_loss)

def run_model2(opt):
    model = run_model(opt)
    losses = model.get_current_losses()
    loss = losses['idt_A'] # D_A, G_A, cycle_A, idt_A

    return loss, model

def run_test(dataroot, model):
    opt = TrainOptions().parse()
    # hard-code some parameters for test
    opt.num_threads = 0   # test code only supports num_threads = 1
    opt.batch_size = 1    # test code only supports batch_size = 1
    opt.serial_batches = True  # disable data shuffling; comment this line if results on randomly chosen images are needed.
    opt.no_flip = True    # no flip; comment this line if results on flipped images are needed.
    opt.display_id = -1   # no visdom display; the test code saves the results to a HTML file.

    # New options
    opt.dataroot = dataroot #'../road-scanner/Image/Image/test'
    opt.name = ''
    opt.phase = 'test'
    opt.direction = 'AtoB'
    opt.serial_batches = True
    opt.isTrain = False

    dataset = create_dataset(opt)
    model.eval()
    losses = defaultdict(float)

    for _, data in enumerate(dataset):
        model.set_input(data)
        model.calculate_loss()
        current_losses = model.get_current_losses()
        losses['total_loss'] += float(model.loss_G)

        for k in current_losses.keys():
            losses[k] += current_losses[k]

        return losses

def run_model(opt):
    #import pdb; pdb.set_trace()
    dataset = create_dataset(opt)  # create a dataset given opt.dataset_mode and other options
    dataset_size = len(dataset)    # get the number of images in the dataset.
    print('The number of training images = %d' % dataset_size)

    model = create_model(opt)      # create a model given opt.model and other options
    model.setup(opt)               # regular setup: load and print networks; create schedulers
    visualizer = Visualizer(opt)   # create a visualizer that display/save images and plots
    total_iters = 0                # the total number of training iterations

    for epoch in range(opt.epoch_count, opt.n_epochs + opt.n_epochs_decay + 1):    # outer loop for different epochs; we save the model by <epoch_count>, <epoch_count>+<save_latest_freq>
        epoch_start_time = time.time()  # timer for entire epoch
        iter_data_time = time.time()    # timer for data loading per iteration
        epoch_iter = 0                  # the number of training iterations in current epoch, reset to 0 every epoch
        visualizer.reset()              # reset the visualizer: make sure it saves the results to HTML at least once every epoch

        for i, data in enumerate(dataset):  # inner loop within one epoch
            iter_start_time = time.time()  # timer for computation per iteration
            if total_iters % opt.print_freq == 0:
                t_data = iter_start_time - iter_data_time

            total_iters += opt.batch_size
            epoch_iter += opt.batch_size
            model.set_input(data)         # unpack data from dataset and apply preprocessing
            model.optimize_parameters()   # calculate loss functions, get gradients, update network weights

            if total_iters % opt.display_freq == 0:   # display images on visdom and save images to a HTML file
                save_result = total_iters % opt.update_html_freq == 0
                model.compute_visuals()
                visualizer.display_current_results(model.get_current_visuals(), epoch, save_result)

            if total_iters % opt.print_freq == 0:    # print training losses and save logging information to the disk
                losses = model.get_current_losses()
                t_comp = (time.time() - iter_start_time) / opt.batch_size
                visualizer.print_current_losses(epoch, epoch_iter, losses, t_comp, t_data)
                if opt.display_id > 0:
                    visualizer.plot_current_losses(epoch, float(epoch_iter) / dataset_size, losses)

            if total_iters % opt.save_latest_freq == 0:   # cache our latest model every <save_latest_freq> iterations
                print('saving the latest model (epoch %d, total_iters %d)' % (epoch, total_iters))
                save_suffix = 'iter_%d' % total_iters if opt.save_by_iter else 'latest'
                model.save_networks(save_suffix)

            iter_data_time = time.time()
        if epoch % opt.save_epoch_freq == 0:              # cache our model every <save_epoch_freq> epochs
            print('saving the model at the end of epoch %d, iters %d' % (epoch, total_iters))
            model.save_networks('latest')
            model.save_networks(epoch)

        print('End of epoch %d / %d \t Time Taken: %d sec' % (epoch, opt.n_epochs + opt.n_epochs_decay, time.time() - epoch_start_time))
        model.update_learning_rate()                     # update learning rates at the end of every epoch.

    return model

def train_evaluate(lambda_a, lambda_b, lambda_identity, opt):
    print(f'lambda_a: {lambda_a}, lambda_b: {lambda_b}, lambda_identity: {lambda_identity}')
    opt.lambda_A = lambda_a
    opt.lambda_B = lambda_b
    opt.lambda_identity = lambda_identity

    model = run_model(opt)
    test_losses = run_test(opt.dataroot, model)
    print(test_losses)
    print()
    print(f"Loss: {test_losses['total_loss']}")

    return test_losses['total_loss']

def run_ax_optimization():
    opt = TrainOptions().parse()   # get training options
    best_parameters, best_values, experiment, model = optimize(
        parameters=[
          {
            "name": "lambda_A",
            "type": "range",
            "bounds": [0.0, 100.0],
          },
          {
            "name": "lambda_B",
            "type": "range",
            "bounds": [0.0, 100.0],
          },
          {
            "name": "lambda_identity",
            "type": "range",
            "bounds": [0.0, 100.0],
          },
        ],
        # Booth function
        evaluation_function=lambda p: train_evaluate(p['lambda_A'], p['lambda_B'], p['lambda_identity'], opt),
        minimize=True,
    ) 

    print(best_parameters)   

def optimize():
    opt = TrainOptions().parse()   # get training options
    search_space = [
        Real(0, 30, name='lambda_A'),
        Real(0, 30, name='lambda_B'),
        Real(0, 0.1, name='lambda_identity')
    ]
    checkpoint_saver = CheckpointSaver("./checkpoint_optimization.pkl", store_objective=False, compress=9) 

    @use_named_args(search_space)
    def objective_fn(lambda_A, lambda_B, lambda_identity):
        return train_evaluate(lambda_A, lambda_B, lambda_identity, opt)

    res = gp_minimize(objective_fn, 
        search_space, 
        acq_func="EI", # the acquisition function
        n_calls=15, # the number of evaluations of f
        n_random_starts=5, # the number of random initialization points
        callback=[checkpoint_saver])

    return res


if __name__ == '__main__':
    #opt = TrainOptions().parse()   # get training options
    res = optimize()
    print(res)
    dump(res, 'result.pkl', store_objective=False)


    #model = run_all(opt)


