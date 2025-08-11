from flask import Flask,render_template
import tensorflow as tf
import numpy as np

app = Flask(__name__)

model = tf.keras.models.load_model(r'C:\Users\wilsen\OneDrive\Desktop\image classification\notebook\model_bunga.h5')


@app.route('/')
def home():
    return render_template("index.html")

def image_getter():
    return ""


def predict_image(gambar_bunga):
    input_image = tf.keras.utils.load_img(gambar_bunga, 
                                      target_size=(180,180))
    input_image_array = tf.keras.utils.img_to_array(input_image)
    input_image_exp_dmn = tf.expand_dims(input_image_array, 0)
    predic = model.predict(input_image_exp_dmn)
    result = tf.nn.softmax(predic[0])
    acc = np.max(result)*100
    return result,acc

if __name__ == "__main__":
    app.run()
    