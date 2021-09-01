'''
Author: Chau Lap Tou
Date: 2021-08-31 11:07:27
LastEditors: Chau Lap Tou
LastEditTime: 2021-09-01 22:29:43
python_exe: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
java_class: javac -encoding utf-8 file_name.java
java_jar: jar -cvmf manifest.txt name.jar *.class
GithubName: Swarfte
'''
import web.web_search as WS
import web.html_load as HL
import pdf.load_pdf as LP
import word.sort_data as SD
import word.create_docx as CD

def start(html= "./data/source.html",pdf = "./pdf/englishword.pdf" ,setting ="./data/setting.json",docx = "./word/englishword.docx" ):
    
    native_word = LP.get_pdf_data(pdf)#*獲取pdf的生字
    word_list = []
    #for x in range(len(native_word)):
    for x in range(5):
        WS.connect(native_word[x],html,setting,wait_time = 5)#*對每一個生字進行搜索
        text = HL.htmlfilter(html)#*獲取過濾後的生字
        word = SD.sort_word(text)#*按word表格排序生字
        word_list.append(word)
    
    CD.build_docx_file(docx,word_list)#*在word檔中生成生字
        
if __name__ == "__main__":
    start()
