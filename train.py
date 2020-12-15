"""
Seizure Prediction from intracranial EEG
DACO 2020/2021

This file implements the training of the model.

@authors: Ana Maria Sousa, Mariana Xavier, Rui Santos
"""

from readFiles import readTrainFiles

# Read training set - list of pairs (signal, label).
train_data = readTrainFiles()