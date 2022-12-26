# Sentiment Analysis using Flask and Deployed to Google Cloud Platform as a Docker container

## Live Webapp

Jump to this [page](https://container-p2hmrfwsdq-uw.a.run.app) to view the live webapp.

## Description

This is a small scale application that takes a sentence as input and detects if it is a Positive or Negative sentiment. A [Kaggle dataset](https://www.kaggle.com/datasets/kazanova/sentiment140) containing 1.6 million tweets is preprocessed and used for training an XGBoost Classifier. The Flask app calls the model prediction on receiving input from the text field. This app is dockerized as a container and stored in Google Cloud Registry (GCR). The objective of this project is to understand and learn the fundamentals of Flask, Docker, and Google Cloud Platform.

## Sample Video

https://user-images.githubusercontent.com/59926447/209587889-17c8dc3e-45ab-4c7c-998b-be4655db4fb4.MP4

## Usage

To clone this repository via HTTPS, use the below command in a new terminal.

```
git clone https://github.com/vishaln15/sentiment-analysis.git
```

Alternatively, we can clone this repository via SSH.

```
git clone git@github.com:vishaln15/sentiment-analysis.git
```

Change directory into this repository.

```
cd sentiment-analysis/
```

With Anaconda, we can create a new environment with Python 3.10.8 and install the requirements.

```
conda create -n ENV_NAME python=3.10
pip install -r requirements.txt
```

Install Docker for the platform that you are using. The docker container for this project was built on an Ubuntu 22.04.01 LTS platform.

To build this container on Linux, there were various bugs that needed to be dealt with. Run the following command on Linux platform to build the container.

```
docker buildx build --platform linux/amd64 -t sent_analysis .
```

To run the container locally in a development server, execute the following command.

```
docker run sent_analysis
```

Connect your machine with Google Cloud after creating credentials and installing `gcloud-cli`.

After creating a container in Google Cloud Registry, submit the container build image to gcr by running the following command.

```
gcloud builds submit --tag gcr.io/PROJECT_ID/CONTAINER_NAME
```

Run the following command to deploy the app from cli.

```
gcloud run deploy --image gcr.io/sentiment-analysis-flask-app/container --platform managed
```

## Acknowledgements

- This project used resources such as StackOverflow, [YouTube](https://youtu.be/zGP_nYmZd9c), and [Medium](https://towardsdatascience.com/deploy-a-dockerized-flask-app-to-google-cloud-platform-71d91b39b25e).
- Dataset used for this project was taken from [Kaggle](https://www.kaggle.com/datasets/kazanova/sentiment140).
