# land-use-classification-sentinel-2-images
Land Use Classification - Sentinel 2 satellite images (27k RGB images, 10 class)

## This notebook is just for me to discover and try concepts and methods learnt from online courses and might contain mistakes and substandard practices.

The initial 27k images were splitted into 3 sets. Training (70%), Validation (15%), and Test (15%).
The initial split of test data were performed using simple python script while the validation split was performed using ImageDataGenerator built-in validation split function.
This problem were approached in 3 different ways.
1. Transfer Learning (VGG16 with imagenet weights) - 97.14% training accuracy, 93.10% validation accuracy, 90.76% test accuracy
2. Multi-layer Perceptron (MLP) - 57.44% training accuracy, 58.59% validation accuracy, 52.24% test accuracy
3. Custom built Convolutional Neural Network(CNN) - 96.77% training accuracy, 92.44% validation accuracy, 92.67% test accuracy


Data Source: http://madm.dfki.de/downloads
- German Research Centre for Artificial Intelligence
