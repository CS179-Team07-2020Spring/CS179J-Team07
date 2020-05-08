import tensorflow as tf
import random
import cv2
import numpy as np
import PIL

# left, right, straight
ACTIONS = 3

# learning rate
GAMMA = 0.99

# used for updating the gradient
INITIAL_EPSILON = 1.0
FINAL_EPSILON = 0.05

# frames to anneal epsilon
EXPLORE = 500000
OBSERVE = 50000

# stored experience
REPLAY = 500000

# batch size to train on
BATCH = 100

def createGraph():

    # convolution layers and bias vectors
    W_conv1 = tf.Variable(tf.zeros([8, 8, 4, 32]))
    b_conv1 = tf.Variable(tf.zeros([32]))
    W_conv2 = tf.Variable(tf.zeros([4, 4, 32, 64]))
    b_conv2 = tf.Variable(tf.zeros([64]))
    W_conv3 = tf.Variable(tf.zeros([3, 3, 64, 64]))
    b_conv3 = tf.Variable(tf.zeros([64]))

    W_fc4 = tf.Variable(tf.zeros([3136, 784]))
    b_fc4 = tf.Variable(tf.zeros([784]))
    W_fc5 = tf.Variable(tf.zeros([784, ACTIONS]))
    b_fc5 = tf.Variable(tf.zeros([ACTIONS]))

    # input for pixel data
    s = tf.placeholder("float", [None, 84, 84, 4])

    # computed using RELU activation function
    conv1 = tf.nn.relu(tf.nn.conv2d(s, W_conv1, strides = [1, 4, 4, 1], padding = "VALID") + b_conv1)
    conv2 = tf.nn.relu(tf.nn.conv2d(conv1, W_conv2, strides = [1, 2, 2, 1], padding = "VALID") + b_conv2)
    conv3 = tf.nn.relu(tf.nn.conv2d(conv2, W_conv3, strides = [1, 1, 1, 1], padding = "VALID") + b_conv3)

    conv3_flat = tf.reshape(conv3, [-1, 3136])
    fc4 = tf.nn.relu(tf.matmul(conv3_flat, W_fc4) + b_fc4)
    fc5 = tf.matmul(fc4, W_fc5) + b_fc5

    return s, fc5

def trainGraph(inp, out, sess):
    argmax = tf.placeholder("float", [None, ACTIONS])
    gt = tf.placeholder("float", [None])

    action = tf.reduce_sum(tf.multiply(out, argmax), reduction_indices = 1)
    cost = tf.reduce_mean(tf.square(action - gt))
    train_step = tf.train.AdamOptimizer(1e-6).minimize(cost)

    D = deque()
    frame = pass
    inp_t = np.stack((frame, frame, frame, frame), axis = 2)

    saver = tf.train.Saver()
    sess.run(tf.initialize_all_variables())
    t = 0
    epsilon = INITIAL_EPSILON


def main():
    """TODO: Docstring for main.
    :returns: TODO

    """
    sess = tf.InteractiveSession()
    # test = tf.Variable(tf.zeros([8, 8, 4, 32]))
    # sess.run(tf.global_variables_initializer())
    inp, out = createGraph()
    # print(.eval())
    print(inp.eval())
    print(out.eval())
    sess.close()


if __name__ == "__main__":
    main()
