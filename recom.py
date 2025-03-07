import numpy as numpy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from google.colab import drive
drive.mount('/content/drive')
import pandas as pd
df= pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Untitled folder/drama - Sheet1.csv')
df["Genre"]= df["Genre"].str.lower()
vectorizer = TfidfVectorizer()
genre_matrix = vectorizer.fit_transform(df["Genre"])
similarity_matrix = cosine_similarity(genre_matrix)
def recommendation(genre_name,num_recommendations=10):
    genre_name = genre_name.lower()
    genre_vector = vectorizer.transform([genre_name])
    genre_similarity = cosine_similarity(genre_vector, genre_matrix).flatten()
    sorted_indices = genre_similarity.argsort()[::-1][:num_recommendations]
    recommendations = df.iloc[sorted_indices]["Movie Name"].tolist()
    return recommendations


while 1:
    print("1: Action")
    print("2: Adventure")
    print("3: Comedy")
    print("4: Drama")
    print("5: Fantasy")
    print("6: Horror")
    print("7: Romance")
    print("8: Sci-Fi")
    print("9: Thriller")
    print("10: Western")
    print("11: Crime")
    print("12: Mystery")
    print("13: Biography")
    print("14: History")
    print("15: Music")
    print("16: War")
    print("17: Sports")
    print("18: Musical")
    print("19: Family")
    print("20: Animation")
    print("21: Reality")
    print("22: Documentry")
    print("23: Suspense")



    genre_name = input("Enter your preference in Movie Genre from list or type exit to quit").strip()
    if genre_name.lower()=="exit":
        print("Byeeeeeeeeeeeeeeeeeeeeeeee.......................")
        break
    recommendations = recommendation(genre_name)
    if isinstance(recommendations,list):
        print(f"This one is similar to '{genre_name}': {recommendations}")
    else:
        print(f"{recommendations}")