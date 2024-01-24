import os
from fastapi import FastAPI
import nltk
import spacy
nltk.download('stopwords')
spacy.load('en_core_web_sm')

from app.resume import inference_matcher_fulltext, inference_parser, inference_matcher_from_parser

VOLUMN_PATH = os.environ['VOLUMN_PATH']

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/service/matcher-fulltext")
def api_inference_matcher_fulltext(cv_path: str, jd_path: str, model_id: int = 1):
    respone = inference_matcher_fulltext(cv_path, jd_path, model_id)
    return respone

@app.get("/service/parser")
def api_inference_parser(cv_path : str):
    respone = inference_parser(cv_path)
    return respone

@app.get("/service/matcher-from-parser")
def api_inference_matcher_from_parser(cv_path : str, jd_path: str, model_id: int = 1):
    respone = inference_matcher_from_parser(cv_path, jd_path, model_id)
    return respone