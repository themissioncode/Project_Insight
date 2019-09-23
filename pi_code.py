import schedule
import urllib.request, json
from microdotphat import HEIGHT, scroll,  write_string, scroll_vertical, show, clear
import time


text=""

def job():
    with urllib.request.urlopen("https://api.nasa.gov/insight_weather/?api_key=irvJZWTRZKHJLAt8YsvJ5LTxYSbrvSnAoOJ8Ayac&feedtype=json&ver=1.0") as url:
        data = json.loads(url.read())
        days=list(data.keys())
        res=[]
        for el in days:
            try:
                res.append(int(el))
            except ValueError:
                pass
            print(res)

            for i in data[str(res[-1])].values():
                mn = int((i["mn"]))
                mx= int(i["mx"])
                break
    text = "The live temp on Mars on day "+str(res[-1])+" is max: "+str(mx)+"c and min: "+str(mn)+"c          "
    print(text)
    write_string(text, offset_x= 0,kerning=False)
    show()


job()
schedule.every().day.at("00:00").do(job)
while True:
    schedule.run_pending()
    scroll(amount_x=8)
    show()
    time.sleep(0.2)
time.sleep(1)
