# deeplearning-workshop

Workshop on using deep learning in health tech.

## Requirements

* Python 3.5+
* Keras 2.2.2
* tensorflow 1.9
* See below for how to install python requirements
* It's really nice to have a nvidia gpu, otherwise you'll have some waiting to do.

## Getting started

# Installing dependencies
Install dependencies with:

	$ pip3 install -r requirements.txt

You can do it in a virtual environment.

# Running on Amazon

If you want to create an AWS instance with the required GPU support and requirements already installed have a look at:

[Amazons deep learning AMI](https://aws.amazon.com/marketplace/pp/B077GCH38C)

The cheapest option is the `p2.xlarge` machine, $1 / hour.

Once running create a ssh tunnel to the instance and start your notebook:

```
ssh -L 8000:localhost:8888 <url_to_aws_instance>
source activate tensorflow_p36
jupyter notebook
```

Now a notebook should be available on `localhost:8000`.

## Data sets
* Cats vs. dogs: Download through [kaggle](https://www.kaggle.com/c/dogs-vs-cats/data) (profile required)
* ISIC melanoma classification: Download using [this repo](https://github.com/GalAvineri/ISIC-Archive-Downloader)
