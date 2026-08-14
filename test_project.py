from project import train_model, prepare_data, evaluate_model, clean_data
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import pytest
def test_train_model():
    x_train = ["helo", "good morning" , "bad prompt", "dangerous prompt"]
    y_train = [0,0,1,1]

    vectorizer = TfidfVectorizer()
    x_train = vectorizer.fit_transform(x_train)
    model = train_model(x_train, y_train)
    assert model is not None

def test_evaluate_model():
     df = pd.DataFrame ({
         "text" :["hello", "good morning", "bad prompt", "dangerous prompt"],
         "label" : [0,0,1,1]
     })

     x_train, x_test , y_train , y_test, vectorizer = prepare_data(df)
     model = train_model (x_train ,y_train)


     accuracy = evaluate_model(model, x_test , y_test)




     assert 0 <= accuracy <= 1

def test_clean_data():
    df = pd.DataFrame({
        "text": ["hello" , "badprompt"],
        "label" : [0,1],
        "tags": ["safe", "unsafe"]
     })
    clean_data(df)
