import os
import json
def get_pdf_file_path(path):
    now_path = os.getcwd()
    with open(path) as s:
        pdf_folder = json.load(s)
    file_list = os.listdir(pdf_folder["pdf_path"])
    pdf_list = []
    for x in file_list :
        if ".pdf" in x :
            path = now_path + "\\" + pdf_folder["pdf_path"][2:] + "\\" + x
            pdf_list.append(path)
    return pdf_list

def get_word_file_path(path):
    pdf = get_pdf_file_path(path)
    word_list = []
    for x in pdf:
        word = x.replace(".pdf",".docx").replace("pdf","word")
        word_list.append(word)
    return word_list