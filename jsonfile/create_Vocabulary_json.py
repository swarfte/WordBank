import json
import pdf.load_pdf as PL
import os


def get_word_json(english_word, pdf_path):  # 生成自動補全用的生字庫
    json_path = pdf_path.replace(".pdf", ".json").replace("pdf","jsonfile")
    word_dict = {"english_word": english_word}
    j_dict = json.loads(json.dumps(word_dict))  # 變成json檔用的格式
    with open(json_path, "w", encoding="utf-8") as j:
        json.dump(j_dict, j)


if __name__ == "__main__":#自動化讀取pdf檔案夾中的生字pdf
    json_local = os.getcwd()#json路徑
    pdf_local = json_local[:len(json_local) - 8] + "pdf" + "\\"#pdf路徑
    native_file = os.listdir("../pdf")
    pdf_file = [x for x in native_file if ".pdf" in x]#篩選檔案
    for x in pdf_file:
        file_name = pdf_local + x #合併路徑和檔案名
        english_word = PL.get_pdf_data(file_name)
        get_word_json(english_word, file_name)
