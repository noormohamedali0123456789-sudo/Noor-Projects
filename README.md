### PromptGuard


###Video Demo:

https://youtu.be/q6Yis5DHUKs







###Description :





This project analyzes all prompts taken from the user. Prompts can be safe or unsafe. This is very useful to classify all prompts that can be useless and that can take all personal information from the program, and it threatens the privacy of persons.

Details:

To begin explaining this project, you can see that simple machine learning was used to train the model for prompts only, and the main programming language of this program is Python.

You can see the Folder Files, which contain all files with all prompt data.


The project uses the Scikit-learn library
Pandas is used to organize the data.
There are many functions that handle the data of prompts
You can see clean data that handles all data and see all columns and data from head to tail.
You can see prepared data, which contains a Vectorizer that converts all prompts into numbers that computer programs use to understand
You can infer from the if condition that all safe data have a value of 0 and all unsafe data have a value of 1
The most difficult thing that makes me feel confused is that the project has many trials for training this model
 in train_model function.
 evaluate_model function to test the model  by put predictions and accuracy to calculate the accuracy of the programm
 clean_data function  .isnull() to calculate all missing values in the coloumn  .sum() to calculate the number of missing values in the column .duplicated() to check all duplicated prompts,   and other information about the data.
  The main define function main()
  The train_model function uses Logistic Regression to train the model on the prepared training data.
