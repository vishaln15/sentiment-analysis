FROM python:3.10.8

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN pip install pipenv

# RUN pipenv install --deploy --system

RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | tee /usr/share/keyrings/cloud.google.gpg && apt-get update -y && apt-get install google-cloud-sdk -y


RUN python -c "import nltk; nltk.download('omw-1.4'); nltk.download('wordnet'); nltk.download('stopwords')"

COPY . .

EXPOSE 8080

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
