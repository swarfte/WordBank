'''
Author: Chau Lap Tou
Date: 2021-08-31 11:07:27
LastEditors: Chau Lap Tou
LastEditTime: 2021-09-01 22:57:11
python_exe: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
java_class: javac -encoding utf-8 file_name.java
java_jar: jar -cvmf manifest.txt name.jar *.class
GithubName: Swarfte
'''
import web.web_search as WWS
import web.html_load as WHL
import pdf.load_pdf as PLP
import word.sort_data as WSD
import word.create_docx as WCD
import web.YDTranslate as WYT


def pdf_to_word_all_done(html="./data/source.html", pdf="./pdf/englishword.pdf", setting="./data/setting.json",
                         docx="./word/englishword.docx"):
    native_word = PLP.get_pdf_data(pdf)  # *獲取pdf的生字
    word_list = []
    for x in range(len(native_word)):
        WWS.connect(native_word[x], html, setting, wait_time=4)  # *對每一個生字進行搜索
        text = WHL.htmlfilter(html)  # *獲取過濾後的生字
        word = WSD.sort_word(text)  # *按word表格排序生字
        word_list.append(word)
    WCD.build_docx_file_all(docx, word_list)  # *在word檔中生成生字


def output_chinese_and_english(pdf="./pdf/englishword.pdf", docx="./word/englishword.docx"):#只輸出中文和英文 方便製作quizlet
    english_word = PLP.get_pdf_data(pdf)
    chinese_word = WYT.translates(english_word)
    mix_word = [english_word,chinese_word]
    WCD.build_chinese_and_english(docx,mix_word)


if __name__ == "__main__":
    # pdf_to_word_all_done()
    output_chinese_and_english()
