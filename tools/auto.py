import os
import json
import platform


def get_pdf_file_path(path):
    system = platform.system()
    now_path = os.getcwd()
    with open(path) as s:
        pdf_folder = json.load(s)
    file_list = os.listdir(pdf_folder["pdf_path"])
    pdf_list = []
    for x in file_list:
        if ".pdf" in x:
            if system == "Windows":
                path = now_path + "\\" + pdf_folder["pdf_path"][2:] + "\\" + x
            elif system == "Linux":
                path = now_path + "/" + pdf_folder["pdf_path"][2:] + "/" + x
            pdf_list.append(path)
    return pdf_list


def get_word_file_path(path):
    pdf = get_pdf_file_path(path)
    word_list = []
    for x in pdf:
        word = x.replace(".pdf", ".docx").replace("pdf", "word")
        word_list.append(word)
    return word_list
