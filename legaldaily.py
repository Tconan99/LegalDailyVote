import requests
import time, threading

number = 1

def vote():
    url = 'http://zbz.legaldaily.com.cn/works/index.php/home/works/addVote'
    # w_id 45
    params = {
        'w_id': 45
    }

    response = requests.post(url, data=params)
    global number
    print(number, "->", response.text)
    number = number + 1

def loop():
    vote()
    global timer
    timer = threading.Timer(0.05, loop)
    timer.start()

timer = threading.Timer(0.1, loop)
timer.start()