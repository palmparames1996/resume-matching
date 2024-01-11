import PyPDF2, pdfplumber
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pyresparser import ResumeParser

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

def MatchPercentageText(text1,text2,round_digit=2): 
    feature_model = CountVectorizer()
    count_matrix = feature_model.fit_transform([text1, text2])
    MatchPercentage = cosine_similarity(count_matrix)[0][1]*100
    MatchPercentage = round(MatchPercentage,round_digit)
    return MatchPercentage

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

def inferencing_matching(list_jd_path: list, list_cv_path: list):
    list_respone = []
    for jd_path in list_jd_path :
        jd_text = preprocessingToText(jd_path)
        for cv_path in list_cv_path :
            cv_text = preprocessingToText(cv_path)
            matching_percent = MatchPercentageText(jd_text, cv_text)
            list_respone.append({'jd_path' : jd_path, 'cv_path' : cv_path, 'matching_percent' : matching_percent})
    return list_respone

def inferencing_extract(list_cv_path: list, skill_list_path: str = None):
    list_respone = []
    for cv_path in list_cv_path:
        respone = {'cv_path':cv_path}
        respone.update(extract_job_attributes(cv_path))
        list_respone.append(respone)
    return list_respone