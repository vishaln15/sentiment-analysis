FROM python:3.10.8

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN pip install pipenv

# RUN pipenv install --deploy --system

RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | tee /usr/share/keyrings/cloud.google.gpg && apt-get update -y && apt-get install google-cloud-sdk -y

RUN python -m nltk.downloader wordnet -d /usr/local/nltk_data/

RUN python -m nltk.downloader omw-1.4 -d /usr/local/nltk_data/

COPY . .

EXPOSE 5000

CMD ["python3", "app.py"]
