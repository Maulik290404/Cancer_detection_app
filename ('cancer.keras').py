# coding: utf-8
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# image size and batch size
image_size = (512, 512,3)                   #height,width,color channels
batch_size = 32

# Directory for the training set
train_dir = "D:\ML\archive\melanoma_cancer_dataset\train"
                                                        #ADD PATH 
# Directory for the testing set
test_dir = "D:\ML\archive\melanoma_cancer_dataset\test"

# ImageDataGenerator for rescaling and image augmentation (helps reduce overfitting)
train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2,                # 20% of the training data will be used for validation
                                    rotation_range=20,                                  # Randomly rotate images
                                    width_shift_range=0.2,                              # Randomly shift images horizontally
                                    height_shift_range=0.2,                             # Randomly shift images vertically
                                    shear_range=0.2,                                    # (basically sliding image)
                                    zoom_range=0.2,                                     # Zoom in/out on images
                                    horizontal_flip=True,                               # Flip images horizontally
                                    fill_mode='nearest')              

# Load training data
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=image_size,  
    batch_size=batch_size,
    class_mode='binary',                 #only 2 output classes
    subset='training'                    #this is for the actual training data (80%)
)

# Load validation data
validation_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=image_size,  # Updated to use 'image_size'
    batch_size=batch_size,
    class_mode='binary',
    subset='validation'  # Use this for the validation data (20%)
)
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# image size and batch size
image_size = (512, 512,3)                   #height,width,color channels
batch_size = 32

# Directory for the training set
train_dir = "D:/ML/archive/melanoma_cancer_dataset/train"
                                                        #ADD PATH 
# Directory for the testing set
test_dir = "D:/ML/archive/melanoma_cancer_dataset/test"

# ImageDataGenerator for rescaling and image augmentation (helps reduce overfitting)
train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2,                # 20% of the training data will be used for validation
                                    rotation_range=20,                                  # Randomly rotate images
                                    width_shift_range=0.2,                              # Randomly shift images horizontally
                                    height_shift_range=0.2,                             # Randomly shift images vertically
                                    shear_range=0.2,                                    # (basically sliding image)
                                    zoom_range=0.2,                                     # Zoom in/out on images
                                    horizontal_flip=True,                               # Flip images horizontally
                                    fill_mode='nearest')              

# Load training data
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=image_size,  
    batch_size=batch_size,
    class_mode='binary',                 #only 2 output classes
    subset='training'                    #this is for the actual training data (80%)
)

# Load validation data
validation_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=image_size,  # Updated to use 'image_size'
    batch_size=batch_size,
    class_mode='binary',
    subset='validation'  # Use this for the validation data (20%)
)
inputs = layers.Input(shape=isize)                # the input layer of our model

x = layers.Conv2D(32, (3, 3), activation='relu')(inputs)
x = layers.Conv2D(32, (3, 3), activation='relu')(inputs)                       #32 kernel of 3*3 size
x = layers.MaxPooling2D(pool_size=(2, 2))(x)                                   

x = layers.Conv2D(64, (3, 3), activation='relu')(x)
x = layers.Conv2D(64, (3, 3), activation='relu')(inputs)   
x = layers.MaxPooling2D(pool_size=(2, 2))(x)

x = layers.Conv2D(128, (3, 3), activation='relu')(x)
x = layers.Conv2D(128, (3, 3), activation='relu')(x)                            # 10 convolution layers
x = layers.MaxPooling2D(pool_size=(2, 2))(x)

x = layers.Conv2D(256, (3, 3), activation='relu')(x)
x = layers.Conv2D(256, (3, 3), activation='relu')(x)
x = layers.MaxPooling2D(pool_size=(2, 2))(x)

x = layers.Conv2D(512, (3, 3), activation='relu')(x)
x = layers.Conv2D(512, (3, 3), activation='relu')(x)
x = layers.MaxPooling2D(pool_size=(2, 2))(x)

global_max_pool = layers.GlobalMaxPooling2D()(x)                              #This layer takes the maximum value from each feature map


global_avg_pool = layers.GlobalAveragePooling2D()(x)                          #This layer calculates the average value across all feature map dimensions

#Note: since global_max_pool and global_avg_pool both result in 1-D structure , skipped flatten layer

output_max_pool = layers.Dense(1, activation='sigmoid', name='max_pool_output')(global_max_pool)
#Dense to create 'fully connected layer', 1 refers to single neuron,'sigmoid'(best for binary classification)
                                                                                                                        #CHOOSE 1 BASED ON ACC
output_avg_pool = layers.Dense(1, activation='sigmoid', name='avg_pool_output')(global_avg_pool)
#Dense to create 'fully connected layer', 1 refers to single neuron,'sigmoid'(best for binary classification)
inputs = layers.Input(shape=image_size)                # the input layer of our model

x = layers.Conv2D(32, (3, 3), activation='relu')(inputs)
x = layers.Conv2D(32, (3, 3), activation='relu')(inputs)                       #32 kernel of 3*3 size
x = layers.MaxPooling2D(pool_size=(2, 2))(x)                                   

x = layers.Conv2D(64, (3, 3), activation='relu')(x)
x = layers.Conv2D(64, (3, 3), activation='relu')(inputs)   
x = layers.MaxPooling2D(pool_size=(2, 2))(x)

x = layers.Conv2D(128, (3, 3), activation='relu')(x)
x = layers.Conv2D(128, (3, 3), activation='relu')(x)                            # 10 convolution layers
x = layers.MaxPooling2D(pool_size=(2, 2))(x)

x = layers.Conv2D(256, (3, 3), activation='relu')(x)
x = layers.Conv2D(256, (3, 3), activation='relu')(x)
x = layers.MaxPooling2D(pool_size=(2, 2))(x)

x = layers.Conv2D(512, (3, 3), activation='relu')(x)
x = layers.Conv2D(512, (3, 3), activation='relu')(x)
x = layers.MaxPooling2D(pool_size=(2, 2))(x)

global_max_pool = layers.GlobalMaxPooling2D()(x)                              #This layer takes the maximum value from each feature map


global_avg_pool = layers.GlobalAveragePooling2D()(x)                          #This layer calculates the average value across all feature map dimensions

#Note: since global_max_pool and global_avg_pool both result in 1-D structure , skipped flatten layer

output_max_pool = layers.Dense(1, activation='sigmoid', name='max_pool_output')(global_max_pool)
#Dense to create 'fully connected layer', 1 refers to single neuron,'sigmoid'(best for binary classification)
                                                                                                                        #CHOOSE 1 BASED ON ACC
output_avg_pool = layers.Dense(1, activation='sigmoid', name='avg_pool_output')(global_avg_pool)
#Dense to create 'fully connected layer', 1 refers to single neuron,'sigmoid'(best for binary classification)
model_max = models.Model(inputs=inputs, outputs=output_max_pool)                    # Model is from keras and creates a model taking input and output architecture of cnn
model_avg = models.Model(inputs=inputs, outputs=output_avg_pool) 
# Compile the max model
model_max.compile(optimizer='nadam',                        #Nesterov ADAM                         
              loss='binary_crossentropy',                  #as binary classification                
              metrics=['accuracy'])


# Compile the avg model
model_avg.compile(optimizer='nadam',                                                 
              loss='binary_crossentropy',                                 
              metrics=['accuracy'])
cnn1 = model_max.fit(
    train_generator,
    epochs=10,
    validation_data=validation_generator,
    verbose=1                                            # output control
)

cnn2 = model_avg.fit(
    train_generator,
    epochs=10,
    validation_data=validation_generator,
    verbose=1                                            # output control
)
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# image size and batch size
image_size = (512, 512,3)                   #height,width,color channels
batch_size = 32

# Directory for the training set
train_dir = "D:/ML/archive/melanoma_cancer_dataset/train"
                                                        #ADD PATH 
# Directory for the testing set
test_dir = "D:/ML/archive/melanoma_cancer_dataset/test"

# ImageDataGenerator for rescaling and image augmentation (helps reduce overfitting)
train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2,                # 20% of the training data will be used for validation
                                    rotation_range=20,                                  # Randomly rotate images
                                    width_shift_range=0.2,                              # Randomly shift images horizontally
                                    height_shift_range=0.2,                             # Randomly shift images vertically
                                    shear_range=0.2,                                    # (basically sliding image)
                                    zoom_range=0.2,                                     # Zoom in/out on images
                                    horizontal_flip=True,                               # Flip images horizontally
                                    fill_mode='nearest')              

# Load training data
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=image_size[:2],  
    batch_size=batch_size,
    class_mode='binary',                 #only 2 output classes
    subset='training'                    #this is for the actual training data (80%)
)

# Load validation data
validation_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=image_size[:2],  # Updated to use 'image_size'
    batch_size=batch_size,
    class_mode='binary',
    subset='validation'  # Use this for the validation data (20%)
)
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# image size and batch size
image_size = (512, 512,3)                   #height,width,color channels
batch_size = 32

# Directory for the training set
train_dir = "D:/ML/archive/melanoma_cancer_dataset/train"
                                                        #ADD PATH 
# Directory for the testing set
test_dir = "D:/ML/archive/melanoma_cancer_dataset/test"

# ImageDataGenerator for rescaling and image augmentation (helps reduce overfitting)
train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2,                # 20% of the training data will be used for validation
                                    rotation_range=20,                                  # Randomly rotate images
                                    width_shift_range=0.2,                              # Randomly shift images horizontally
                                    height_shift_range=0.2,                             # Randomly shift images vertically
                                    shear_range=0.2,                                    # (basically sliding image)
                                    zoom_range=0.2,                                     # Zoom in/out on images
                                    horizontal_flip=True,                               # Flip images horizontally
                                    fill_mode='nearest')              

# Load training data
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=image_size[:2],  
    batch_size=batch_size,
    class_mode='binary',                 #only 2 output classes
    subset='training'                    #this is for the actual training data (80%)
)

# Load validation data
validation_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=image_size[:2],  # Updated to use 'image_size'
    batch_size=batch_size,
    class_mode='binary',
    subset='validation'  # Use this for the validation data (20%)
)
inputs = layers.Input(shape=image_size)                # the input layer of our model

x = layers.Conv2D(32, (3, 3), activation='relu')(inputs)
x = layers.Conv2D(32, (3, 3), activation='relu')(inputs)                       #32 kernel of 3*3 size
x = layers.MaxPooling2D(pool_size=(2, 2))(x)                                   

x = layers.Conv2D(64, (3, 3), activation='relu')(x)
x = layers.Conv2D(64, (3, 3), activation='relu')(inputs)   
x = layers.MaxPooling2D(pool_size=(2, 2))(x)

x = layers.Conv2D(128, (3, 3), activation='relu')(x)
x = layers.Conv2D(128, (3, 3), activation='relu')(x)                            # 10 convolution layers
x = layers.MaxPooling2D(pool_size=(2, 2))(x)

x = layers.Conv2D(256, (3, 3), activation='relu')(x)
x = layers.Conv2D(256, (3, 3), activation='relu')(x)
x = layers.MaxPooling2D(pool_size=(2, 2))(x)

x = layers.Conv2D(512, (3, 3), activation='relu')(x)
x = layers.Conv2D(512, (3, 3), activation='relu')(x)
x = layers.MaxPooling2D(pool_size=(2, 2))(x)

global_max_pool = layers.GlobalMaxPooling2D()(x)                              #This layer takes the maximum value from each feature map


global_avg_pool = layers.GlobalAveragePooling2D()(x)                          #This layer calculates the average value across all feature map dimensions

#Note: since global_max_pool and global_avg_pool both result in 1-D structure , skipped flatten layer

output_max_pool = layers.Dense(1, activation='sigmoid', name='max_pool_output')(global_max_pool)
#Dense to create 'fully connected layer', 1 refers to single neuron,'sigmoid'(best for binary classification)
                                                                                                                        #CHOOSE 1 BASED ON ACC
output_avg_pool = layers.Dense(1, activation='sigmoid', name='avg_pool_output')(global_avg_pool)
#Dense to create 'fully connected layer', 1 refers to single neuron,'sigmoid'(best for binary classification)
model_max = models.Model(inputs=inputs, outputs=output_max_pool)                    # Model is from keras and creates a model taking input and output architecture of cnn
model_avg = models.Model(inputs=inputs, outputs=output_avg_pool) 
# Compile the max model
model_max.compile(optimizer='nadam',                        #Nesterov ADAM                         
              loss='binary_crossentropy',                  #as binary classification                
              metrics=['accuracy'])


# Compile the avg model
model_avg.compile(optimizer='nadam',                                                 
              loss='binary_crossentropy',                                 
              metrics=['accuracy'])
cnn1 = model_max.fit(
    train_generator,
    epochs=10,
    validation_data=validation_generator,
    verbose=1                                            # output control
)

cnn2 = model_avg.fit(
    train_generator,
    epochs=10,
    validation_data=validation_generator,
    verbose=1                                            # output control
)
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# image size and batch size
image_size = (256, 256,3)                   #height,width,color channels
batch_size = 32

# Directory for the training set
train_dir = "D:/ML/archive/melanoma_cancer_dataset/train"
                                                        #ADD PATH 
# Directory for the testing set
test_dir = "D:/ML/archive/melanoma_cancer_dataset/test"

# ImageDataGenerator for rescaling and image augmentation (helps reduce overfitting)
train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2,                # 20% of the training data will be used for validation
                                    rotation_range=20,                                  # Randomly rotate images
                                    width_shift_range=0.2,                              # Randomly shift images horizontally
                                    height_shift_range=0.2,                             # Randomly shift images vertically
                                    shear_range=0.2,                                    # (basically sliding image)
                                    zoom_range=0.2,                                     # Zoom in/out on images
                                    horizontal_flip=True,                               # Flip images horizontally
                                    fill_mode='nearest')              

# Load training data
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=image_size[:2],  
    batch_size=batch_size,
    class_mode='binary',                 #only 2 output classes
    subset='training'                    #this is for the actual training data (80%)
)

# Load validation data
validation_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=image_size[:2],  # Updated to use 'image_size'
    batch_size=batch_size,
    class_mode='binary',
    subset='validation'  # Use this for the validation data (20%)
)
inputs = layers.Input(shape=image_size)                # the input layer of our model

x = layers.Conv2D(32, (3, 3), activation='relu')(inputs)
x = layers.Conv2D(32, (3, 3), activation='relu')(inputs)                       #32 kernel of 3*3 size
x = layers.MaxPooling2D(pool_size=(2, 2))(x)                                   

x = layers.Conv2D(64, (3, 3), activation='relu')(x)
x = layers.Conv2D(64, (3, 3), activation='relu')(inputs)   
x = layers.MaxPooling2D(pool_size=(2, 2))(x)

x = layers.Conv2D(128, (3, 3), activation='relu')(x)
x = layers.Conv2D(128, (3, 3), activation='relu')(x)                            # 10 convolution layers
x = layers.MaxPooling2D(pool_size=(2, 2))(x)

x = layers.Conv2D(256, (3, 3), activation='relu')(x)
x = layers.Conv2D(256, (3, 3), activation='relu')(x)
x = layers.MaxPooling2D(pool_size=(2, 2))(x)

x = layers.Conv2D(512, (3, 3), activation='relu')(x)
x = layers.Conv2D(512, (3, 3), activation='relu')(x)
x = layers.MaxPooling2D(pool_size=(2, 2))(x)

global_max_pool = layers.GlobalMaxPooling2D()(x)                              #This layer takes the maximum value from each feature map


global_avg_pool = layers.GlobalAveragePooling2D()(x)                          #This layer calculates the average value across all feature map dimensions

#Note: since global_max_pool and global_avg_pool both result in 1-D structure , skipped flatten layer

output_max_pool = layers.Dense(1, activation='sigmoid', name='max_pool_output')(global_max_pool)
#Dense to create 'fully connected layer', 1 refers to single neuron,'sigmoid'(best for binary classification)
                                                                                                                        #CHOOSE 1 BASED ON ACC
output_avg_pool = layers.Dense(1, activation='sigmoid', name='avg_pool_output')(global_avg_pool)
#Dense to create 'fully connected layer', 1 refers to single neuron,'sigmoid'(best for binary classification)
model_max = models.Model(inputs=inputs, outputs=output_max_pool)                    # Model is from keras and creates a model taking input and output architecture of cnn
model_avg = models.Model(inputs=inputs, outputs=output_avg_pool) 
# Compile the max model
model_max.compile(optimizer='nadam',                        #Nesterov ADAM                         
              loss='binary_crossentropy',                  #as binary classification                
              metrics=['accuracy'])


# Compile the avg model
model_avg.compile(optimizer='nadam',                                                 
              loss='binary_crossentropy',                                 
              metrics=['accuracy'])
cnn1 = model_max.fit(
    train_generator,
    epochs=10,
    validation_data=validation_generator,
    verbose=1                                            # output control
)

cnn2 = model_avg.fit(
    train_generator,
    epochs=10,
    validation_data=validation_generator,
    verbose=1                                            # output control
)
test_datagen = ImageDataGenerator(rescale=1./255)      #rescaling our test data
test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=image_size[:2],
    batch_size=batch_size,
    class_mode='binary',
    shuffle=False  # Important to maintain order for evaluation
)
test_loss_max, test_accuracy_max = model_max.evaluate(test_generator)               #max model
print(f'Test Loss: {test_loss_max}, Test Accuracy: {test_accuracy_max}')            #checking accuracy of model
plt.figure(figsize=(12, 5))

# Plotting training and validation accuracy
plt.subplot(1, 2, 1)
plt.plot(model_max.model_max['accuracy'], label='Training Accuracy')
plt.plot(model_max.model_max['val_accuracy'], label='Validation Accuracy')
plt.title('ModelAccuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(model_max.model_max['loss'], label='Training Loss')
plt.plot(model_max.model_max['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend()
plt.figure(figsize=(12, 5))

# Plotting training and validation accuracy
plt.subplot(1, 2, 1)
plt.plot(cnn1.cnn1['accuracy'], label='Training Accuracy')
plt.plot(cnn1.cnn1['val_accuracy'], label='Validation Accuracy')
plt.title('ModelAccuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(cnn1.cnn1['loss'], label='Training Loss')
plt.plot(cnn1.cnn1['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend()
plt.figure(figsize=(12, 5))

# Plotting training and validation accuracy
plt.subplot(1, 2, 1)
plt.plot(cnn1.history['accuracy'], label='Training Accuracy')
plt.plot(cnn1.history['val_accuracy'], label='Validation Accuracy')
plt.title('ModelAccuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(cnn1.history['loss'], label='Training Loss')
plt.plot(cnn1.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend()
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# image size and batch size
image_size = (224, 224,3)                   #height,width,color channels
batch_size = 32

# Directory for the training set
train_dir = "D:/ML/archive/melanoma_cancer_dataset/train"
                                                        #ADD PATH 
# Directory for the testing set
test_dir = "D:/ML/archive/melanoma_cancer_dataset/test"

# ImageDataGenerator for rescaling and image augmentation (helps reduce overfitting)
train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2,                # 20% of the training data will be used for validation
                                    rotation_range=20,                                  # Randomly rotate images
                                    width_shift_range=0.2,                              # Randomly shift images horizontally
                                    height_shift_range=0.2,                             # Randomly shift images vertically
                                    shear_range=0.2,                                    # (basically sliding image)
                                    zoom_range=0.2,                                     # Zoom in/out on images
                                    horizontal_flip=True,                               # Flip images horizontally
                                    fill_mode='nearest')              

# Load training data
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=image_size[:2],  
    batch_size=batch_size,
    class_mode='binary',                 #only 2 output classes
    subset='training'                    #this is for the actual training data (80%)
)

# Load validation data
validation_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=image_size[:2],  # Updated to use 'image_size'
    batch_size=batch_size,
    class_mode='binary',
    subset='validation'  # Use this for the validation data (20%)
)
inputs = layers.Input(shape=image_size)                # the input layer of our model

x = layers.Conv2D(16, (3, 3), activation='relu')(inputs)
x = layers.Conv2D(16, (3, 3), activation='relu')(x)                       #32 kernel of 3*3 size
x = layers.MaxPooling2D(pool_size=(2, 2))(x)                                   

x = layers.Conv2D(32, (3, 3), activation='relu')(x)
x = layers.Conv2D(32, (3, 3), activation='relu')(x)   
x = layers.MaxPooling2D(pool_size=(2, 2))(x)

x = layers.Conv2D(64, (3, 3), activation='relu')(x)
x = layers.Conv2D(64, (3, 3), activation='relu')(x)                            # 10 convolution layers
x = layers.MaxPooling2D(pool_size=(2, 2))(x)

x = layers.Conv2D(128, (3, 3), activation='relu')(x)
x = layers.Conv2D(128, (3, 3), activation='relu')(x)
x = layers.MaxPooling2D(pool_size=(2, 2))(x)

x = layers.Conv2D(256, (3, 3), activation='relu')(x)
x = layers.Conv2D(256, (3, 3), activation='relu')(x)
x = layers.MaxPooling2D(pool_size=(2, 2))(x)

global_max_pool = layers.GlobalMaxPooling2D()(x)                              #This layer takes the maximum value from each feature map


global_avg_pool = layers.GlobalAveragePooling2D()(x)                          #This layer calculates the average value across all feature map dimensions

#Note: since global_max_pool and global_avg_pool both result in 1-D structure , skipped flatten layer

output_max_pool = layers.Dense(1, activation='sigmoid', name='max_pool_output')(global_max_pool)
#Dense to create 'fully connected layer', 1 refers to single neuron,'sigmoid'(best for binary classification)
                                                                                                                        #CHOOSE 1 BASED ON ACC
output_avg_pool = layers.Dense(1, activation='sigmoid', name='avg_pool_output')(global_avg_pool)
#Dense to create 'fully connected layer', 1 refers to single neuron,'sigmoid'(best for binary classification)
model_max = models.Model(inputs=inputs, outputs=output_max_pool)                    # Model is from keras and creates a model taking input and output architecture of cnn
model_avg = models.Model(inputs=inputs, outputs=output_avg_pool) 
# Compile the max model
model_max.compile(optimizer='nadam',                        #Nesterov ADAM                         
              loss='binary_crossentropy',                  #as binary classification                
              metrics=['accuracy'])


# Compile the avg model
model_avg.compile(optimizer='nadam',                                                 
              loss='binary_crossentropy',                                 
              metrics=['accuracy'])
# Compile the max model
model_max.compile(optimizer='nadam',                        #Nesterov ADAM                         
              loss='binary_crossentropy',                  #as binary classification                
              metrics=['accuracy'])


# Compile the avg model
model_avg.compile(optimizer='nadam',                                                 
              loss='binary_crossentropy',                                 
              metrics=['accuracy'])
cnn1 = model_max.fit(
    train_generator,
    epochs=10,
    validation_data=validation_generator,
    verbose=1                                            # output control
)

cnn2 = model_avg.fit(
    train_generator,
    epochs=10,
    validation_data=validation_generator,
    verbose=1                                            # output control
)
inputs = layers.Input(shape=image_size)                # the input layer of our model

x = layers.Conv2D(16, (3, 3), activation='relu')(inputs)
x = layers.Conv2D(16, (3, 3), activation='relu')(x)                       #32 kernel of 3*3 size
x = layers.MaxPooling2D(pool_size=(2, 2))(x)                                   

x = layers.Conv2D(32, (3, 3), activation='relu')(x)
x = layers.Conv2D(32, (3, 3), activation='relu')(x)   
x = layers.MaxPooling2D(pool_size=(2, 2))(x)

x = layers.Conv2D(64, (3, 3), activation='relu')(x)
x = layers.Conv2D(64, (3, 3), activation='relu')(x)                            # 10 convolution layers
x = layers.MaxPooling2D(pool_size=(2, 2))(x)

x = layers.Conv2D(128, (3, 3), activation='relu')(x)
x = layers.Conv2D(128, (3, 3), activation='relu')(x)
x = layers.MaxPooling2D(pool_size=(2, 2))(x)

x = layers.Conv2D(256, (3, 3), activation='relu')(x)
x = layers.Conv2D(256, (3, 3), activation='relu')(x)
x = layers.MaxPooling2D(pool_size=(2, 2))(x)
x = layers.Dropout(0.5)(x) 
global_max_pool = layers.GlobalMaxPooling2D()(x)                              #This layer takes the maximum value from each feature map


#Note: since global_max_pool and global_avg_pool both result in 1-D structure , skipped flatten layer

output_max_pool = layers.Dense(1, activation='sigmoid', name='max_pool_output')(global_max_pool)
#Dense to create 'fully connected layer', 1 refers to single neuron,'sigmoid'(best for binary classification)
                                                                                                                       
model_max = models.Model(inputs=inputs, outputs=output_max_pool)                    # Model is from keras and creates a model taking input and output architecture of cnn
model_avg = models.Model(inputs=inputs, outputs=output_avg_pool) 
# Compile the max model
model_max.compile(optimizer='nadam',                        #Nesterov ADAM                         
              loss='binary_crossentropy',                  #as binary classification                
              metrics=['accuracy'])


# Compile the avg model
model_avg.compile(optimizer='nadam',                                                 
              loss='binary_crossentropy',                                 
              metrics=['accuracy'])
# Compile the max model
model_max.compile(optimizer='nadam',                        #Nesterov ADAM                         
              loss='binary_crossentropy',                  #as binary classification                
              metrics=['accuracy'])
# Compile the max model
model_max.compile(optimizer='nadam',                        #Nesterov ADAM                         
              loss='binary_crossentropy',                  #as binary classification                
              metrics=['accuracy'])
cnn1 = model_max.fit(
    train_generator,
    epochs=10,
    validation_data=validation_generator,
    verbose=1                                            # output control
)

cnn2 = model_avg.fit(
    train_generator,
    epochs=10,
    validation_data=validation_generator,
    verbose=1                                            # output control
)
test_datagen = ImageDataGenerator(rescale=1./255)      #rescaling our test data
test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=image_size[:2],
    batch_size=batch_size,
    class_mode='binary',
    shuffle=False  # Important to maintain order for evaluation
)
test_loss_max, test_accuracy_max = model_max.evaluate(test_generator)               #max model
print(f'Test Loss: {test_loss_max}, Test Accuracy: {test_accuracy_max}')            #checking accuracy of model
plt.figure(figsize=(12, 5))

# Plotting training and validation accuracy
plt.subplot(1, 2, 1)
plt.plot(cnn1.history['accuracy'], label='Training Accuracy')
plt.plot(cnn1.history['val_accuracy'], label='Validation Accuracy')
plt.title('ModelAccuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(cnn1.history['loss'], label='Training Loss')
plt.plot(cnn1.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend()
