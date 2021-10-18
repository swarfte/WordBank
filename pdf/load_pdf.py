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

def get_pdf_data(path,rule = r"[0-9]{1,2}\.\s{2}[a-zA-Z]+\s?[a-zA-Z]*|[0-9]{3}\.\s[a-zA-Z]+\s?[a-zA-Z]*"):#*選取pdf檔案中的英文規則
    native_word = []
    word = []
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
    
    word_rule = re.compile(r"[a-zA-Z]+|[a-zA-Z]+\s[a-zA-Z]+")#*選取最終的生字
    for x in native_word:
        english = re.search(word_rule,x).group()
        word.append(english)

    return word
    
if __name__ == "__main__":
    english = get_pdf_data("englishword.pdf")
    use = [x.replace("'","\"") for x in english]
    print(english)