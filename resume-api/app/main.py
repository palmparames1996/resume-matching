import os
from fastapi import FastAPI
import nltk
import spacy
nltk.download('stopwords')
spacy.load('en_core_web_sm')

from app.resume import inferencing_matching, inferencing_extract

VOLUMN_PATH = os.environ['VOLUMN_PATH']

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/resume_matching")
def inference_resume_match(jd_path: str, cv_path: str, model_id: int = 1):
    list_jd_path = [os.path.join(VOLUMN_PATH,i) for i in jd_path.split(',')]
    list_cv_path = [os.path.join(VOLUMN_PATH,i) for i in cv_path.split(',')]
    matching_result = inferencing_matching(list_jd_path, list_cv_path, model_id)
    extract_result = inferencing_extract(list_cv_path)
    return {'matching_result' : matching_result, 'extract_result' : extract_result}