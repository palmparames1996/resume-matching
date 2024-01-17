import PyPDF2, pdfplumber
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pyresparser import ResumeParser
import difflib
import jellyfish
from fuzzywuzzy import fuzz

def pdfToText(path):
    open_session = open(path,'rb')
    reader_session = PyPDF2.PdfReader(open_session)
    pages = reader_session._get_num_pages()
    text_respone = []
    with pdfplumber.open(open_session) as pdf:
        for i in range (0,pages):
            page = pdf.pages[i]
            text_page = page.extract_text()
            text_respone.append(text_page)
    
    text_respone =''.join(text_respone)
    text_respone = text_respone.replace("\n"," ")
    return text_respone

def MatchPercentageText(text1,text2,model_id,round_digit=2): 
    if model_id == 1:
        feature_model = CountVectorizer()
        count_matrix = feature_model.fit_transform([text1, text2])
        MatchPercentage = cosine_similarity(count_matrix)[0][1]*100
        MatchPercentage = round(MatchPercentage,round_digit)
    elif model_id == 2:
        MatchPercentage = difflib.SequenceMatcher(None, text1, text2).ratio()*100
        MatchPercentage = round(MatchPercentage,round_digit)
    elif model_id == 3:
        MatchPercentage = jellyfish.levenshtein_distance(text1, text2) ## 3000+
    elif model_id == 4:
        MatchPercentage = fuzz.ratio(text1, text2) 
    elif model_id == 5:
        MatchPercentage = fuzz.partial_ratio(text1, text2) # same 4
    elif model_id == 6:
        MatchPercentage = fuzz.token_sort_ratio(text1, text2)
    elif model_id == 7:
        MatchPercentage = fuzz.token_set_ratio(text1, text2)
    return round(MatchPercentage,round_digit)

def preprocessingToText(path):
    if '.pdf' in path:
        text = pdfToText(path)
    elif '.txt' in path:
        f = open(path, "r")
        text = f.read()
    else:
        raise Exception("Sorry, file type not support")
    return text

def extract_job_attributes(file_path):
    session_resume = ResumeParser(file_path)
    data = session_resume.get_extracted_data()
    return data

def inferencing_matching(list_jd_path: list, list_cv_path: list, model_id: int):
    list_respone = []
    for jd_path in list_jd_path :
        jd_text = preprocessingToText(jd_path)
        for cv_path in list_cv_path :
            cv_text = preprocessingToText(cv_path)
            matching_percent = MatchPercentageText(jd_text, cv_text, model_id)
            list_respone.append({'jd_path' : jd_path, 'cv_path' : cv_path, 'matching_percent' : matching_percent})
    return list_respone

def inferencing_extract(list_cv_path: list, skill_list_path: str = None):
    list_respone = []
    for cv_path in list_cv_path:
        respone = {'cv_path':cv_path}
        respone.update(extract_job_attributes(cv_path))
        list_respone.append(respone)
    return list_respone