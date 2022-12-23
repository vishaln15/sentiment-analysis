# Imports

from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

import re
import pickle

stop = set(stopwords.words("english"))

lemmatizer = WordNetLemmatizer()

def predict_pipeline(text):
    return predict(text)

emojis = {':)': 'smile', ':-)': 'smile', ';d': 'wink', ':-E': 'vampire', ':(': 'sad', 
          ':-(': 'sad', ':-<': 'sad', ':P': 'raspberry', ':O': 'surprised',
          ':-@': 'shocked', ':@': 'shocked',':-$': 'confused', ':\\': 'annoyed', 
          ':#': 'mute', ':X': 'mute', ':^)': 'smile', ':-&': 'confused', '$_$': 'greedy',
          '@@': 'eyeroll', ':-!': 'confused', ':-D': 'smile', ':-0': 'yell', 'O.o': 'confused',
          '<(-_-)>': 'robot', 'd[-_-]b': 'dj', ":'-)": 'sadsmile', ';)': 'wink', 
          ';-)': 'wink', 'O:-)': 'angel','O*-)': 'angel','(:-D': 'gossip', '=^.^=': 'cat'}


def preprocess(text):
    processed_text = []
    
    url_pattern = r"((http://)[^ ]*|(https://)[^ ]*|( www\.)[^ ]*)"
    user_pattern = '@[^\s]+'
    alpha_pattern = "[^a-zA-Z0-9]"
    sequence_pattern = r"(.)\1\1+"
    seq_replace_pattern = r"\1\1"
    
    for tweet in text:
        tweet = tweet.lower()
        tweet = re.sub(url_pattern, " URL", tweet)
        
        for emoji in emojis.keys():
            tweet = tweet.replace(emoji, "EMOJI" + emojis[emoji])
        
        tweet = re.sub(user_pattern, " USER", tweet)
        tweet = re.sub(alpha_pattern, " ", tweet)
        tweet = re.sub(sequence_pattern, seq_replace_pattern, tweet)
        processed_words = []
        
        for word in tweet.split():
            if len(word) > 1 and word not in stop:
                word = lemmatizer.lemmatize(word)
                processed_words.append(word)
                
        processed_text.append(" ".join(processed_words))
        
    return processed_text

with open("models/pipeline.pkl", "rb") as f:
    pipe = pickle.load(f)

def predict(text):
    preprocessed_text = preprocess(text)
    preds = pipe.predict(preprocessed_text)
    
    pred_to_label = {0: "Negative",
                     1: "Positive"}
    data = []
    for t, pred in zip(text, preds):
        data.append(
            {
                "text": t,
                "pred": int(pred),
                "label": pred_to_label[pred]
            }
        )
        
    return data

if __name__=="__main__":
    text = ["I hate pineapple on pizza!", "I love you so much!"]
    predictions = predict_pipeline(text)
    print(predictions)