from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd
def prepare_data(df):
     x = df["text"]
     y= df["label"]

     vectorizer = TfidfVectorizer()
     x = vectorizer.fit_transform(x)  # To convert all prompts into numbers that computer can use to understand
     x_train, x_test, y_train, y_test = train_test_split(
     x, y, test_size= 0.2, random_state = 42
                )

     return x_train, x_test, y_train, y_test, vectorizer



def main():

    df = pd.read_parquet("Files/train-00000-of-00001.parquet")#read file
    print(df.head())#read top of columns

    print(df.columns)#determine columns
    print(df.shape)#determine the shape
    print(df.info())
    print(df.tail())

    print(df["label"].value_counts())# determine the labels 0 means safe, 1 means unsafe
    print(df["category"].value_counts())#determine the category of all data in the filep
    clean_data(df)
    x_train, x_test, y_train,y_test,vectorizer= prepare_data(df)


    model = train_model(x_train, y_train)
    accuracy =  evaluate_model(model, x_test, y_test)
    print(accuracy)

    prompt = input("please enter your prompt: ")
    prompt_vector = vectorizer.transform([prompt])
    prompt_predict = model.predict(prompt_vector)
    print("Actual: " , df["label"].iloc[0])
    print("Predicted: ", prompt_predict[0])
    print(prompt_predict)
    if prompt_predict[0] == 1:
         print("Unsafe")
    else:
         print ("Safe")
    print(df["text"].iloc[0])
    print(df["label"].iloc[0])




def clean_data(df):

        print(df.isnull().sum())

        print(df.dtypes)
        print(df.tail())
        print(df["tags"].iloc[0])
        print(df["text"].duplicated().sum())



def train_model(x_train, y_train):# This define function  to train the model on all things that made in prepare data function
     model = LogisticRegression()
     model.fit(x_train, y_train)
     return model

def evaluate_model(model, x_test, y_test):
     predictions = model.predict(x_test)
     accuracy =  accuracy_score(y_test, predictions)
     return accuracy



if __name__ == "__main__":
     main()
