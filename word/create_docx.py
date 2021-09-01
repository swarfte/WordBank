'''
Author: Chau Lap Tou
Date: 2021-08-31 16:33:37
LastEditors: Chau Lap Tou
LastEditTime: 2021-08-31 17:25:49
python_exe: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
java_class: javac -encoding utf-8 file_name.java
java_jar: jar -cvmf manifest.txt name.jar *.class
GithubName: Swarfte
'''
import docx
import docx.shared as DS
import docx.oxml.ns as DON

def build_docx_file(path,value,row = 1 , col = 5):#*108+1行
    doc = docx.Document()#*創建一個doc文件
    table = doc.add_table(rows=row, cols=col)#*創建一個表格
    hdr_cells = table.rows[0].cells#*設置為頭頂的行
    hdr_cells[0].text = "Chinese"#*cell表示列
    hdr_cells[1].text = "adjective"
    hdr_cells[2].text = "noun"
    hdr_cells[3].text = "verb"
    hdr_cells[4].text = 'adverb'
    
    data = value
    
    for a,b,c,d,e in data:
        row_cells = table.add_row().cells#*用作表示表格的列
        row_cells[0].text = a #*第一列
        row_cells[1].text = b #*第二列
        row_cells[2].text = c #*第三列
        row_cells[3].text = d #*第四列
        row_cells[4].text = e #*第五列
            
    doc.save(path)#*保存文件
    
    
if __name__ == "__main__":
    build_docx_file("englishword.docx")