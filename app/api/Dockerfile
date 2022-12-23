FROM python:3.10.8

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN python -c "import nltk; nltk.download('omw-1.4'); nltk.download('wordnet'); nltk.download('stopwords')"

COPY . .

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]