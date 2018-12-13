# pytorch-imagefolder
Create an Image Folder dataset layout from a CSV file with labeled filenames and classes (e.g. from Kaggle Data Science Bowl 2015 Plankton)

# What it does
If you have a labeled csv file like the following:

* file_name,class
* image01.jpg,0
* image02.jpg,1
* image03.jpg,2
* etc..

Then this script can create the following structure:

```
data/
  - train/
      - class_1 folder/
          - img1.png
          - img2.png
      - class_2 folder/
      .....
      - class_n folder/
  - val/
      - class_1 folder/
      - class_2 folder/
      ......
      - class_n folder/
```

# How to use

The following example might give you an overview on how to use this script or change it to work for your needs.

* csv file named `labels.csv` with column 1 being `file names` and column 2 being `class names`
* dataset that is used for training, use `train`
* image files in folder `train_images`
* are currently in directory of `labels.csv`

You would use the following execution of our script:
`/ImageFolderPyTorch.sh train_onelabel.csv train train_images`

# Where is this useful?

I used it for a Applied Machine Learning course where we had to do image classification for [this kaggle project](https://www.kaggle.com/c/1st-national-data-science-bowl-f18/leaderboard) and [PyTorch's ImageFolder Dataset class structure](https://pytorch.org/docs/stable/torchvision/datasets.html#imagefolder).
