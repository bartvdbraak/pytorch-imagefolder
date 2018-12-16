#!/usr/bin/python

import argparse
import pandas as pd
import os, os.path

TRAIN_NAME = 'train_labels.csv'
VAL_NAME = 'validation_labels.csv'

parser = argparse.ArgumentParser(description='Splitting training set for validation or testing.')
parser.add_argument('-t','--train', help='Your training fraction (0.8 means 80% will be used for training).', required=True)
parser.add_argument('-c','--csv', help='Your training label csv file and location. (e.g. "folder/train_labels.csv")', required=True)
parser.add_argument('-tn','--trainname', help='CSV file name after splitting for training set. (DEFAULT = "train_labels.csv")', required=False)
parser.add_argument('-vn','--valname', help='CSV file name after splitting for validation set. (DEFAULT = "validation_labels.csv")', required=False)

args = vars(parser.parse_args())

if args['trainname']: 
    TRAIN_NAME = args['trainname']
    if not TRAIN_NAME.endswith((".csv", "_files")):
        TRAIN_NAME += '.csv'

if args['valname']:
    VAL_NAME = args['valname']
    if not VAL_NAME.endswith((".csv", "_files")):
        VAL_NAME += '.csv'

train_frac = float(args['train'])
assert (0 < train_frac), "Your training fraction is not between 0 and 1."
val_frac = 1-train_frac

csv_file = args['csv']
assert os.path.exists(csv_file) == 1, 'Your specified filepath did not exist or our execution does not have enough permission to access it.'

training_labels = pd.read_csv(csv_file)

val_set = training_labels.sample(frac=val_frac)
train_set = training_labels.drop(val_set.index)

df = pd.merge(val_set, train_set, on='image', suffixes=['_1', '_2']) #check if any items are both in test and train

val_set.to_csv(path_or_buf=VAL_NAME, index=False)
train_set.to_csv(path_or_buf=TRAIN_NAME, index=False)