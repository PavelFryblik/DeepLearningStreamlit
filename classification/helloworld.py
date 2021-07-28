import streamlit as st
import texts

# TensorFlow and tf.keras
import tensorflow as tf

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

class My_Callback(tf.keras.callbacks.Callback):
    epoch = 0

    # def on_train_begin(self, logs={}):
    #     return
    #
    # def on_train_end(self, logs={}):
    #     return

    # def on_epoch_begin(self, logs={}):
    #     return

    def on_epoch_end(self, epoch, logs={}):
        def on_epoch_end(self, epoch, logs=None):
            logs = logs or {}
            for k in self.params['metrics']:
                if k in logs:
                    st.write("Name: %s, Value: %s" % (k, logs[k]))


    # def on_batch_begin(self, batch, logs={}):
    #     return

    # def on_batch_end(self, batch, logs={}):
    #     self.losses.append(logs.get('loss'))
    #     return

def write():
    text_agent =  texts.czechtext.text_agent()

    st.header(text_agent.text_clasification_header)
    st.write(text_agent.text_clasification_intro)

    st.sidebar.title("Filters")
    pic_num = st.sidebar.slider('Obrazek')

    st.write('TensorFlow __version__')
    st.write(tf.__version__)

    st.write(text_agent.text_clasification_importdata)

    fashion_mnist = tf.keras.datasets.fashion_mnist
    # st.write(fashion_mnist)
    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

    col1, col2, col3 = st.beta_columns((2,1,1))

    col1.write('Picture example')
    col1.write(train_images[pic_num])
    col1.write('Label example')
    col1.write(train_labels[pic_num])

    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
    col2.write(class_names)


    fig = plt.figure()
    plt.imshow(train_images[pic_num])
    plt.colorbar()
    plt.grid(False)
    col3.pyplot(fig)

    fig2 = plt.figure(figsize=(10,10))
    for i in range(25):
        plt.subplot(5,5,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(train_images[pic_num + i], cmap=plt.cm.binary)
        plt.xlabel(class_names[train_labels[pic_num + i]])
    col3.pyplot(fig2)


    st.header('Model')
    st.write("model = tf.keras.Sequential([ \
            tf.keras.layers.Flatten(input_shape=(28, 28)),\
            tf.keras.layers.Dense(128, activation='relu'),\
            tf.keras.layers.Dense(10)\
            ])")

    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(10)])

    model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

    model.fit(train_images, train_labels, epochs=10, callbacks=[My_Callback()])

    test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)

    st.write('\nTest accuracy:', test_acc)
