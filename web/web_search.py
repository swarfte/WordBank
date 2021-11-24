
import pyppeteer as PT
import asyncio as AN
import json


def load_json(path):
    with open(path, "r",encoding='utf-8') as f:
        file = json.load(f)
    return file


def save_file(data, path):
    with open(path, "w+",encoding='utf-8') as f:
        f.write(data)


async def search(word, html_path, setting_path, wait_time=5):
    browser = await PT.launch(headless=True, args=['--disable-infobars', '--start-maximized'], dumpio=True)  # *創建瀏覽器
    try:

    # !headless設為False即可視化
    # browser = await PT.launch(headless = False,args=['--disable-infobars','--start-maximized'],dumpio = True)#*創建瀏覽器
        print(f"正在查找{word}的詞性")
        page = await browser.newPage()  # *創建頁面
        setting = load_json(setting_path)
        await page.setViewport({  # *設置畫面的視窗大小
            "width": setting["width"],
            "height": setting["height"]
        })
        await page.setUserAgent(setting["user-agent"])  # *設置用戶代理
        await page.goto(setting["URL"])  # *進入指定網頁

        await page.type("[name = ld_search_inp]", word)  # *輸入生字
        await page.click("[class = search_btn]")  # *查找生字
        await AN.sleep(wait_time)  # *等待加載畫面

        text = await page.content()  # *獲取網頁源代碼
        save_file(text, html_path)  # *生成一個原始html檔
    except Exception as ex:
        print(f"生字 :{word} 獲取資料時出現錯誤")
        print(f"error : {ex}")
    finally:
        await browser.close()  # *關閉瀏覽器



def connect(word, html_path="../data/source.html", setting_path="../data/setting.json", wait_time=3):
    use_word = word.split(" ")
    html = AN.get_event_loop().run_until_complete(search(use_word[0], html_path, setting_path, wait_time))
    return word


if __name__ == "__main__":
    connect("complete")
