"""
Seizure Prediction from intracranial EEG
DACO 2020/2021

This file reads all the data from the training set and stores it in two lists.

@authors: Ana Maria Sousa, Mariana Xavier, Rui Santos
"""

import os
import scipy.io

# Lists to store the values.
data_EEG = []
channels_names = []

# Run the training dir.
for dirname, _, filenames in os.walk('train'):
    for filename in filenames:
        # Load the data from each file.
        data = scipy.io.loadmat(os.path.join(dirname, filename))
        # Search for the field corresponding to the segments.
        j = 0
        for key in data.keys(): 
            if (key == 3): 
                key_name = key
            j = j + 1
        # Get the field corresponding to the segments.
        train_data = data.get(key)
        # Get in separate arrays the values for the data, the length in seconds,
        # the sampling frequency, the channels and the number of the sequence.
        data = train_data['data'][0][0]
        data_EEG.append(data)
        data_length_sec = train_data['data_length_sec'][0][0][0][0]
        sampling_frequency = train_data['sampling_frequency'][0][0][0][0]
        channels = train_data['channels'][0][0][0]
        channels_names.append(data)
        sequence = train_data['sequence'][0][0][0][0]