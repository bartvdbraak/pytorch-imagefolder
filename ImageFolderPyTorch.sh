#!/bin/bash

#set -x

if [ "$#" -ne 3 ]; then
    echo "Usage: $0 labels set imagefolder"
    echo "Example usage: $0 "folder/labels.csv" "train" "imagefolder" "
    exit
fi

csv_file=$1
set=$2
imagefolder=$3

mkdir -p $set

count=0
while IFS=, read -r col1 col2
do
    #echo "I got:$col1|$col2"
    if [[ count -gt 0 ]]; then
        mkdir -p $set/$col2
        cp $imagefolder/$col1 $set/$col2/$col1
    fi
    count=$((count+1))
done < $csv_file