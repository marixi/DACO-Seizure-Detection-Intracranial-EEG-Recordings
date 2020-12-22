"""
Seizure Prediction from intracranial EEG
DACO 2020/2021

This file reads all the data from the training and test set.

@authors: Ana Maria Sousa, Mariana Xavier, Rui Santos
"""

import os
import scipy.io
import random
import numpy as np
from scipy.fft import rfft, rfftfreq
from matplotlib import pyplot as plt

# Read training set.
def readTrainFiles():
    
    # Lists to store the values.
    data_EEG = []
    number_channels = []
    labels = []
    
    # Run the training dir.
    for dirname, _, filenames in os.walk('train'):
        
        # Random the training files.
        random.seed(30)
        random.shuffle(filenames)
        
        # Read each of the files.
        for filename in filenames:
            
            # Load the data from each file.
            data = scipy.io.loadmat(os.path.join(dirname, filename))
           
            # Get the field corresponding to the segments.
            train_data = data.get(list(data.keys())[3])
            
            # Get in a separate array the values of EEG for the different channels.
            data = train_data['data'][0][0]
            data_EEG.append(data)
            
            # Get the number of channels of a file.
            channels = train_data['channels'][0][0]
            number_channels.append(np.size(channels))
    
            # Obtain the corresponding labels.
            if 'interictal' in filename:
                labels.append(0)
            else:
                labels.append(1)
    
    # Zip the two lists together.
    train = list(zip(data_EEG, number_channels, labels))
   
    return train

def Preprocessing_fft(zip_data):
    data_EEG, number_channels, labels = zip(*zip_data)
   
    data_EEG=list(data_EEG)
    N=5000*600
    SAMPLE_RATE=5000
    xf = rfftfreq(N, 1 / SAMPLE_RATE)
    
    #pre-processing using FFT (fast Fourier transform)
    for j in range (len(data_EEG)):
        #for each signal
        
        channel=data_EEG[j] 
        data_channels_fft=[]
        for i in range (len(channel)):
            #for each channel
            yf = rfft(channel[i])
            # plt.plot(xf, np.abs(yf))
            # plt.show()
            data_channels_fft.append(yf)

        data_EEG[j]= np.array((data_channels_fft))
        
    data_EEG=tuple(data_EEG)
    train2 = list(zip(data_EEG, number_channels, labels))
    return train2
    

train=readTrainFiles()
print(train)

train=Preprocessing_fft(train)
print(train)