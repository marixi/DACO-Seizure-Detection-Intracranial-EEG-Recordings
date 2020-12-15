"""
Seizure Prediction from intracranial EEG
DACO 2020/2021

This file reads all the data from the training and test set.

@authors: Ana Maria Sousa, Mariana Xavier, Rui Santos
"""

import os
import scipy.io
import random

# Read training set.
def readTrainFiles():
    
    # Lists to store the values.
    data_EEG = []
    labels = []
    
    # Run the training dir.
    for dirname, _, filenames in os.walk('train'):
        
        # Read each of the files.
        for filename in filenames:
            
            # Load the data from each file.
            data = scipy.io.loadmat(os.path.join(dirname, filename))
           
            # Get the field corresponding to the segments.
            train_data = data.get(list(data.keys())[3])
            
            # Get in a separate array the values of EEG for the different channels.
            data = train_data['data'][0][0]
    
            # Considering all the different channels as representative of the EEG.
            for channel in range (data.shape[0]):
                data_EEG.append(data[channel])
                # Obtain the corresponding labels.
                if 'interictal' in filename:
                    labels.append(0)
                else:
                    labels.append(1)
    
    # Zip the two lists together.
    train = list(zip(data_EEG, labels))
    
    # Random the training files.
    random.seed(30)
    random.shuffle(train)
    
    return train