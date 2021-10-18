'''
Author: Chau Lap Tou
Date: 2021-08-31 14:36:06
LastEditors: Please set LastEditors
LastEditTime: 2021-10-08 13:10:02
python_exe: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
java_class: javac -encoding utf-8 file_name.java
java_jar: jar -cvmf manifest.txt name.jar *.class
GithubName: Swarfte
'''
import pdfplumber as PP
import re
import json

def get_pdf_data(path,rule = "default"):#*選取pdf檔案中的英文規則
    native_word = []
    choice = re.compile(r"[0-9]{1,2}\.\s{2}[a-zA-Z]+(\s[a-zA-Z]+)*|[0-9]{3}\.\s[a-zA-Z]+(\s[a-zA-Z]+)*")
    word = []
    if rule == "default":
        choose = re.compile(choice)
    else:
        choose = re.compile(rule)
    first_page_word = ""
    with PP.open(path) as pdf:
        first_page = pdf.pages[0]#*讀取第一版的內容
        first_page_word = first_page.extract_text()#*文本內容
    try:
        while True:
            string = re.search(choose,first_page_word).group()
            native_word.append(string)
            first_page_word = first_page_word.replace(string,"")#*更新文本
    except:#*跑到空類型(無法掘替換時自動退出)
        pass
    
    #native_word.sort()
    
    word_rule = re.compile(r"[a-zA-Z]+(\s[a-zA-Z]+)*")#*選取最終的生字
    for x in native_word:
        english = re.search(word_rule,x).group()
        word.append(english)

    return word

def get_word_json(english_word,pdf_path): #生成自動補全用的生字庫
    json_path = pdf_path.replace(".pdf",".json")
    word_dict = {"english_word":english_word}
    j_dict = json.loads(json.dumps(word_dict)) #變成json檔用的格式
    with open(json_path,"w",encoding="utf-8") as j :
        json.dump(j_dict,j)

if __name__ == "__main__":
    pdf_file = "08 21-22 MENG111 Word Bank U3 (1).pdf"
    english_word = get_pdf_data(pdf_file)
    get_word_json(english_word,pdf_file)
    # use = json.dumps(english)
    # print(use)