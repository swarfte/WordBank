'''
Author: Chau Lap Tou
Date: 2021-09-01 21:02:33
LastEditors: Chau Lap Tou
LastEditTime: 2021-09-01 21:23:19
python_exe: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
java_class: javac -encoding utf-8 *.java
java_jar: jar -cvmf manifest.txt name.jar *.class
GithubName: Swarfte
'''
def sort_word(ArrayList):#*排序過濾後的元素
    comparetor = ["chinese","adjective","noun","verb","adverb"]
    use_list = ["" for x in range(5)]#*用作預留空白
    use_list[0] = (ArrayList[0][0])#*先加入中文
    
    
    for x in range(len(ArrayList[2])):
        for y in range(len(comparetor)) :
            if (ArrayList[2][x] == comparetor[y]):#*填入對應的詞性的格
                use_list[y] = ArrayList[1][x]
            
    return use_list

if __name__ == "__main__":
    test = [["完成"],#測試生字
            ["complete","complete","completely","completeness"],
            ["adjective","adverb","noun","verb"]]
    print(sort_word(test))