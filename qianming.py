import random
from tkinter import *
import requests
from PIL import Image, ImageTk


def get_headers():
    # user_agent列表
    user_agent_list = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36'
    ]
    headers = {
        'User-Agent': random.choice(user_agent_list),
    }
    return headers


def sign():
    name = entry.get()
    url = "http://www.yishuzi.com/b/re13.php"
    data = {
        'id': name,
        'zhenbi': '20191123',
        'id1': '904',
        'id2': '#FFFFFF',
        'id4': '#FF0000',
        'id6': '#0000FF'
    }
    html = requests.post(url=url, data=data, headers=get_headers()).text
    req = '<img src="(.*?)">'
    img_url = re.findall(req, html)
    res = requests.get(url=img_url[0], headers=get_headers())
    if res.status_code == 200:
        with open('{}.gif'.format(name), 'wb') as f:
            f.write(res.content)
    bg = ImageTk.PhotoImage(file='{}.gif'.format(entry.get()))
    bg_label = Label(root, image=bg)
    bg_label.bg = bg
    bg_label.grid(row=2, columnspan=2)


# 创建窗口
root = Tk()
# 创建窗口大小
root.geometry("450x400+400+150")
# 标题
root.title('签名设计')
label = Label(root, text="签名", font=('微软雅黑', 18))
label.grid(row=0, column=0)
entry = Entry(root, font=('微软雅黑', 18))
entry.grid(row=0, column=1)
button = Button(root, text='设计签名', font=('微软雅黑', 18), command=sign)
button.grid(row=1, column=1)
# 显示窗口
root.mainloop()
