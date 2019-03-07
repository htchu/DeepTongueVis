System architecture:
![alt text](https://github.com/htchu/DeepTongueVis/blob/master/system_architecture.png)

Design steps:
1. Transfer learning for tongue fissures: an ImageNet-pretrained ResNet50 model is used to perform a transfer learning for images with tongue fissures and images without tongue fissures. That is, only the last one layer is replaced with a binary classifier and retrained. Other layers are intact without any modification.
2. Tongue fissure visualization: apply grad-CAM to the trained model to visualize tongue fissures. An example is here:
        DeepTongueVis/gradcam_sample_code.py
        https://github.com/htchu/DeepTongueVis/blob/master/gradcam_sample_code.py

Sample results:
![alt text](https://github.com/htchu/DeepTongueVis/blob/master/result.png)
