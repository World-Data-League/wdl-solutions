"""
Functions for data generators
"""

from PIL import Image
import numpy as np
import tensorflow as tf


"""
This function generates data from our dataframe/images to feed the train of our deep learning models.
    
Returns:
    generator:  a list of images with the true label
"""

def train_generator(datagen,train, images="image", y_true="irrelevant_infer", class_type="raw"):
    train_gen=datagen.flow_from_dataframe(
    dataframe=train,
    directory="data/images/",
    x_col=images,
    y_col=y_true,
    batch_size=32,
    seed=42,
    shuffle=True,
    class_mode=class_type,
    target_size=(224,224))
    
    return train_gen


"""
This function generates data from our dataframe/images to feed the test of our deep learning models.
    
Returns:
    generator:  a list of images with the true label
"""

def test_generator(test_datagen,test, images="image", y_true="irrelevant_infer", class_type="raw", BS=32):
    test_gen=test_datagen.flow_from_dataframe(
    dataframe=test,
    directory="data/images/",
    x_col=images,
    y_col=y_true,
    batch_size=BS,
    seed=42,
    shuffle=False,
    class_mode=class_type,
    target_size=(224,224))
    return test_gen


"""
This function generates multitask data from our dataframe/images to feed the train and test of our deep learning models.
    
Returns:
    generator:  a list of images with the true label for both tasks.
"""
def multitask_generator(data, batch_size=32):
        imagePath = "images/"

        swID = len(data.street_width.unique())
        ptID = len(data.pavement_type.unique())
        images, sws,pts = [], [], []
        while True:
            for i in range(0, data.shape[0]):
                r = data.iloc[i]
                name, sw, pt = r['image'], r['street_width'], r['pavement_type']
                im = Image.open(imagePath+name)
                im = im.resize((224, 224))
                im = np.array(im) / 255.0
                images.append(im)
                sws.append(tf.keras.utils.to_categorical(sw, swID))
                pts.append(tf.keras.utils.to_categorical(pt, ptID))
                if len(images) >= batch_size:
                    yield np.array(images), [np.array(sws), np.array(pts)]
                    images, sws, pts = [], [], []
