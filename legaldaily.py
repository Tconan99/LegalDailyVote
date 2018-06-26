import requests
import time, threading

number = 1

def vote():
    url = 'http://zbz.legaldaily.com.cn/works/index.php/home/works/addVote'
    # w_id 45
    params = {
        'w_id': 45
    }

    headers = {
        'Accept': '*/*',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,ru;q=0.7',
        'Connection':'Keep-Alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'zbz.legaldaily.com.cn',
        'Origin':'http://zbz.legaldaily.com.cn',
        'Referer':'http://zbz.legaldaily.com.cn/works/index.php',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    response = requests.post(url, data=params, headers=headers)
    global number
    print(number, "->", eval("u'" + response.text + "'"))
    number = number + 1

def loop():
    vote()
    global timer
    timer = threading.Timer(5, loop)
    timer.start()

timer = threading.Timer(0.1, loop)
timer.start()