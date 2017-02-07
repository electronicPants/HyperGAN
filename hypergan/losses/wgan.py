import tensorflow as tf
from hypergan.util.ops import *
from hypergan.util.hc_tf import *
import hyperchamber as hc

def config():
    selector = hc.Selector()
    selector.set("reduce", [tf.reduce_mean])#reduce_sum, reduce_logexp work

    selector.set('create', create)

    return selector.random_config()

def create(config, gan):
    d_real = gan.graph.d_real
    d_fake = gan.graph.d_fake 

    d_real = config.reduce(d_real, axis=1)
    d_fake = config.reduce(d_fake, axis=1)
    d_loss = d_real - d_fake
    g_loss = d_fake
    d_fake_loss = -d_fake
    d_real_loss = d_real

    gan.graph.d_fake_loss=d_fake_loss
    gan.graph.d_real_loss=d_real_loss

    return [d_loss, g_loss]




