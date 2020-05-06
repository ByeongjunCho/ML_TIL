import tensorflow as tf
import time
import PIL.Image
import numpy as np
import os

from utils import tensor_to_image, load_batch_image
from models import TransformModel
def test(model_save_path):
    model = TransformModel()
    transfer = TransformModel()
    ckpt = tf.train.Checkpoint(step=tf.Variable(0), net=model)
    manager = tf.train.CheckpointManager(ckpt, './'+model_save_path, max_to_keep=3)
    ckpt.restore(manager.latest_checkpoint)

    start = time.time()
    model = ckpt.net
    for image_name in os.listdir('./content'):
        test_image = PIL.Image.open('./content/' + image_name)
        test_image = np.array(test_image, dtype=np.float32)

        # 흑백 사진인 경우
        if len(test_image.shape) == 2:
            test_image = np.stack((test_image, test_image, test_image))
        # Channel=4 인 경우
        elif test_image.shape[-1] == 4:
            test_image = PIL.Image.open('./content/' + image_name).convert('RGB')
            test_image = np.array(test_image, dtype=np.float32)
        # Channel=2 인 경우
        elif test_image.shape[-1] == 2:
            test_image = 255.-test_image[:,:,1]
            test_image = np.stack((test_image, test_image, test_image))
        # batch_size 추가 (tensorflow는 4차원 tensor가 입력으로 주어짐)
        test_image = np.expand_dims(test_image, axis=0)
    
        with tf.device('/cpu:0'):
            image = tensor_to_image(model(test_image))
            image.save('./test/'+image_name[:-4]+'_' + model_save_path + '_transform.jpg')
    end = time.time()

    print(end-start)

if __name__ == "__main__":
    path = ["wave", "la_muse_models", "rain_princess", "udnie"]
    for p in path:
        test(p)