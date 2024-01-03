import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

# Load the handwriting recognition model
model = load_model('handwriting_recognition.h5')

# Define a function to perform image recognition
def recognize_image(image):
    # Convert the image to a numpy array
    image = img_to_array(image)
    # Reshape the image to match the model's expected input shape
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    # Preprocess the image
    image = image / 255.0
    # Perform inference on the image
    prediction = model.predict(image)
    # Return the predicted label
    return np.argmax(prediction)

# Example usage
image = 'path/to/image.jpg'
label = recognize_image(image)
print(f'The image is labeled as {label}')