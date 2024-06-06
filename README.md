# X ray Image Classification

#### In this project, a machine learning model based on a deep learning CNN architecture for computer vision is developed. This model will classify any X-ray image to determine whether a disease Pnemonia is present, aiding doctors in making better decisions. Various MLOps tools have been used to automate the entire ML cycle, and the model has been deployed in the cloud.

## Data Preprocessing

#### Data augmentation generates synthetic datasets through image transformations to enhance the training and test data. For training data, augmentations include Resize, CenterCrop, ColorJitter, RandomHorizontalFlip, RandomRotation, ToTensor, and Normalize. These steps resize images, crop them centrally, adjust brightness/contrast/saturation/hue, flip and rotate images randomly, convert them to tensors, and normalize them using mean and standard deviation.

## Model Architecture

#### Custom CNN architecture have been used
- First Layer is the input layer consisting of 3 input channels and output channels with kernel_size of 3X3, padding=0 and bias=True. The activation function we are using is ReLU and performing batch normalization.
- Then we are performing max pooling to extract the important features out of the image.
- Similarly we are passing our model through 9 convolutional layers.
- Finally we are passing out passing our model through a output layer in which we are getting binary classification.

## Model Evaluation

#### Confusion matrices is used for binary classification problem

![Confusion Matrices][confusion_matrix.png]

## Workflows

- constants
- config_entity
- artifact_entity
- components
- pipeline
- main

## How to setup

```bash
conda create venv python==3.8
```
### Run streamlit app
```
streamlit run app.py
```
## AWS CLI Command

### To update the system
```
sudo apt-get update -y
```
### To upgrade the system
```
sudo apt-get upgrade
```
### To download the docker file
```
curl -fsSL https://get.docker.com -o get-docker.sh
```
### To execute docker file
```
sudo sh get-docker.sh
```
#### Docker is installed in machine
### To grant permisson for docker image
```
sudo usermod -aG docker ubuntu
```
### To create new group
```
newgrp docker
```