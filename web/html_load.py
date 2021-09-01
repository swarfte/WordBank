'''
Author: Chau Lap Tou
Date: 2021-08-31 12:07:12
LastEditors: Chau Lap Tou
LastEditTime: 2021-09-01 22:52:43
python_exe: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
java_class: javac -encoding utf-8 file_name.java
java_jar: jar -cvmf manifest.txt name.jar *.class
GithubName: Swarfte
'''
import bs4
import re
import pygtrans as PT
import opencc as OC

def load_file(path):
    with open(path, "r") as f:
        text = f.read()
    return text

def htmlfilter(htmlfile):
    native = bs4.BeautifulSoup(load_file(htmlfile),"html.parser")#*解析為html格式的檔案
    word = native.find_all("span",class_ = "hw_txt gfont")
    state = native.find_all("span",class_ = "fl")
    choose = re.compile(r"[a-zA-Z]+\s?[a-zA-Z]*")#*找出對應的字符
    
    chinese = []
    english_word = []
    english_state = []
    package = [chinese,english_word,english_state]#*反回該生字的中文,不同詞性的英文,以及詞性
    
    for x in word:#*對每個符合的字都處理
        filter_word = x.text
        get_word = re.search(choose,filter_word).group()#*用正則表達式找出真正的字
        use_word = get_word.strip()#*去除多餘的空白
        english_word.append(use_word)
    
    word = native.find_all("h2",class_ = "ure")#*查找剩下的生字
    for x in word:
        filter_word = x.text
        use_word = filter_word[2:]
        english_word.append(use_word)
    
    for x in state:
        use_word = x.text
        english_state.append(use_word)
    
    chinese_translator = PT.Translate()#*英文轉中文翻譯器
    S_chinese_word = chinese_translator.translate(english_word[0])
    # cc = OC.OpenCC("s2t")#*簡轉繁
    # use_chinese_word = cc.convert(S_chinese_word)
    
    chinese.append(S_chinese_word.translatedText)
    
    return package

if __name__ == "__main__":
    print(htmlfilter("../data/source.html"))