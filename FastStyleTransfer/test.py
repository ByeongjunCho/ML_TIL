import tensorflow as tf
from utils import tensor_to_image
from models import TransformModel

if __name__ == "__main__":
    model_save_path = 'la_muse_models'

    transfer = TransformModel()
    ckpt = tf.train.Checkpoint(step=tf.Variable(0), optimizer=opt, net=model)
    manager = tf.train.CheckpointManager(ckpt, './'+model_save_path, max_to_keep=3)
    ckpt.restore(manager.latest_checkpoint)

    transfer = ckpt.net
    