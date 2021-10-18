import requests
import json
import opencc as OC


def translate(word):
    # 有道词典 api
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    # 传输的参数，其中 i 为需要翻译的内容
    key = {
        'type': "AUTO",
        'i': word,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }
    # key 这个字典为发送给有道词典服务器的内容
    response = requests.post(url, data=key)
    # 判断服务器是否相应成功
    if response.status_code == 200:
        # 然后相应的结果
        return response.text
    else:
        print("有道词典调用失败")
        # 相应失败就返回空
        return None


def ch_translate(word):
    list_trans = translate(word)
    result = json.loads(list_trans)
    result = result['translateResult'][0][0]['tgt']
    return result

def tw_translate(word):
    ch_word = ch_translate(word)
    cc = OC.OpenCC("s2t")  # *簡轉繁
    zh_word = cc.convert(ch_word)
    return zh_word

def translates(word_list):
    chinese_word = []
    for x in word_list:
        chinese_word.append(tw_translate(x))
    return chinese_word

if __name__ == "__main__":
    print(tw_translate("apple"))