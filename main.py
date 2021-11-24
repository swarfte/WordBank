import web.web_search as WWS
import web.html_load as WHL
import pdf.load_pdf as PLP
import word.sort_data as WSD
import word.create_docx as WCD
import web.YDTranslate as WYT
import tools.auto as TA

# 這個方法不太穩定
def pdf_to_word_all_done(html="./data/source.html", pdf="./pdf/englishword.pdf", setting="./data/setting.json",
                         docx="./word/englishword.docx"):
    native_word = PLP.get_pdf_data(pdf)  # *獲取pdf的生字
    word_list = []
    for x in range(len(native_word)):
        try:
            current_word = WWS.connect(native_word[x], html, setting, wait_time=4)  # *對每一個生字進行搜索
            text = WHL.htmlfilter(html)  # *獲取過濾後的生字
            word = WSD.sort_word(text)  # *按word表格排序生字
            word_list.append(word)
        except Exception as ex:
            print(f"{x}出現了錯誤")
            print(f"{ex}")
    WCD.build_docx_file_all(docx, word_list)  # *在word檔中生成生字


def output_chinese_and_english(setting):#只輸出中文和英文 方便製作quizlet
    pdf_file = TA.get_pdf_file_path(setting)
    word_list = TA.get_word_file_path(setting)
    for x in range(len(pdf_file)):
        english_word = PLP.get_pdf_data(pdf_file[x])
        chinese_word = WYT.translates(english_word)
        mix_word = [english_word,chinese_word]
        WCD.build_chinese_and_english(word_list[x],mix_word)


if __name__ == "__main__":
    pdf_to_word_all_done()
    setting = "./data/setting.json"
    # output_chinese_and_english(setting)
    #print(TA.get_word_file_path(setting))