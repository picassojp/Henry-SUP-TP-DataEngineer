from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def first():
    return {'Output': 'My first API'}
        
@app.get('/title_word/{word}')
def title_word(word:str):
    import pandas as pd
    plat = ['Datasets\amazon_prime_titles-score-mod.csv', 'Datasets\disney_plus_titles-score-mod.csv', 'Datasets\hulu_titles-score (2)-mod.csv', 'Datasets\netflix_titles-score-mod.csv']
    for i in plat:
        df = pd.read_csv(i)
        print(df.title.str.contains(pat=word).sum())