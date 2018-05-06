import tensorflow as tf
from PIL import Image
import numpy as np
import sys
import os

from data import train_images, train_labels, test_labels, test_images


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

img = Image.open(sys.stdin.buffer.raw).convert('L') # 读取图片并灰度化
# img = Image.open('./174.jpg').convert('L') # 读取图片并灰度化

img = img.crop((2, 5, 45, 17)) # 裁掉边变成 64x21


# 分离数字
# 分离数字
img1 = img.crop((0, 0, 12, 12))
img2 = img.crop((10, 0, 22, 12))
img3 = img.crop((20, 0, 32, 12))
img4 = img.crop((30, 0, 42, 12))


img1 = np.array(img1).flatten()
img1 = list(map(lambda x: 1 if x <= 180 else 0, img1))
img2 = np.array(img2).flatten()
img2 = list(map(lambda x: 1 if x <= 180 else 0, img2))
img3 = np.array(img3).flatten()
img3 = list(map(lambda x: 1 if x <= 180 else 0, img3))
img4 = np.array(img4).flatten()
img4 = list(map(lambda x: 1 if x <= 180 else 0, img4))


DLEN = len(train_images.data[0])
DNUM = len(train_images.data)

x = tf.placeholder(tf.float32, [None, DLEN])

W = tf.Variable(tf.zeros([DLEN, 36]))
b = tf.Variable(tf.zeros([36]))
y = tf.nn.softmax(tf.matmul(x, W) + b)

saver = tf.train.Saver()

sess = tf.Session()
sess.run(tf.global_variables_initializer())

save_path="model/model"

saver.restore(sess, save_path)

correct_prediction = tf.argmax(y, 1)
result = sess.run(correct_prediction, feed_dict={x: [img1, img2, img3, img4]})
sess.close()

for code in result:
    if code < 10:
        print(code ,end = '')
    else:
        print(chr(code +97-10) ,end = '')
   

