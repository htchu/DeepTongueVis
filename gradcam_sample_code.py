from keras.preprocessing import image
import numpy as np
import keras
from keras.models import Model
import matplotlib.pyplot as plt
from vis.utils import utils
from vis.visualization import visualize_activation,visualize_saliency,overlay,visualize_cam
from keras import activations

preprocessed_input = load_image(IMAGE_FILE_NAME)
model = keras.models.load_model(MODEL_FILE_NAME)

predictions = model.predict(preprocessed_input)
predicted_class = np.argmax(predictions)

heatmap = visualize_cam(model=model, layer_idx=-1, filter_indices=predicted_class, seed_input=preprocessed_input, penultimate_layer_idx=utils.find_layer_idx(model, 'activation_49'))
img_init=utils.load_img(IMAGE_FILE, target_size=(224, 224))
plt.imshow(overlay(img_init, heatmap))
plt.savefig(GRADCAM_RESULT_IMAGE_FILE_NAME)
