import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
import re

nltk.download('stopwords')

data = {
    'text': ['This is Bangladesh!', 
             'We can not fight for our rights #101', 
             'Data Science is amazing, especially for NLP!', 
             'But in our country no one care about data and cleaning $lol$']
}
df = pd.DataFrame(data)

stop_words_english = set(stopwords.words('english')) 

def display_menu():
    print("\nText Data Preprocessing Menu:")
    print("1. Identify Null Values")
    print("2. Remove Special Characters")
    print("3. Remove Stop Words")
    print("4. Tokenization")
    print("5. Remove Numbers")
    print("6. Exit")

def identify_null_values(df):
    print("\nOriginal DataFrame:")
    print(df)
    print("\nIdentifying Null Values")
    print(df.isnull()) 

def remove_special_characters(df):
    print("\nOriginal DataFrame:")
    print(df)
    
    df['clean_text'] = df['text'].apply(lambda x: re.sub(r'[^a-zA-Z\s]', '', x))
    print("\nRemoving Special Characters:")
    print(df)

def remove_stop_words(df):
    print("\nOriginal DataFrame:")
    print(df)
    
    df['clean_text'] = df['text'].apply(lambda x: ' '.join([word for word in x.split() if word.lower() not in stop_words_english]))
    print("\nDataFrame After Removing Stop Words:")
    print(df)

def tokenization(df):
    print("\nOriginal DataFrame:")
    print(df)
    
    df['tokens'] = df['text'].apply(lambda x: x.split())
    print("\nDataFrame After Tokenization:")
    print(df)

def convert_to_lowercase(df):
    print("\nOriginal DataFrame:")
    print(df)
    
    df['clean_text'] = df['text'].apply(lambda x: x.lower())
    print("\nDataFrame After Converting to Lowercase:")
    print(df)

def convert_to_uppercase(df):
    print("\nOriginal DataFrame:")
    print(df)
    
    df['clean_text'] = df['text'].apply(lambda x: x.upper())
    print("\nDataFrame After Converting to Uppercase:")
    print(df)

def remove_numbers(df):
    print("\nOriginal DataFrame:")
    print(df)

    df['clean_text'] = df['text'].apply(lambda x: re.sub(r'\d+', '', x))
    print("\nDataFrame After Removing Numbers:")
    print(df)

def main():
    while True:
        display_menu()
        choice = input("\nEnter the number of your choice: ")

        if choice == "1":
            identify_null_values(df)
        elif choice == "2":
            remove_special_characters(df)
        elif choice == "3":
            remove_stop_words(df)
        elif choice == "4":
            tokenization(df)
        elif choice == "5":
            remove_numbers(df)
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
