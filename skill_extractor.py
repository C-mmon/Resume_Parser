import nltk

nltk.download('stopwords')
nlp = spacy.load('en_core_web_sm')
doc=nlp(text)
import  pandas as pd
data=pd.read_csv("skills.csv")
SKILLS_DB=['CAT']
df=pd.DataFrame(data)
for index,row in df.iterrows():
    SKILLS_DB.append(row['Skills'])

def extract_skills(input_text):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    word_tokens = nltk.tokenize.word_tokenize(input_text)

    nlp_text=nlp(text)
    skillset=[]
    # removing stop words and implementing word tokenization
    tokens = [token.text for token in nlp_text if not token.is_stop]
    # check for one-grams (example: python)
    for token in tokens:
        if token in SKILLS_DB:
            skillset.append(token)
    
    
    return skillset
