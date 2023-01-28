import smtplib

import requests
from bs4 import BeautifulSoup

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
ACCEPT_LANGUAGE = "es-US,es;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3,es-419;q=0.2"

headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE
}
url = "https://www.amazon.com/WIZMAX-Gaming-Keyboard-Wired-Mechanical/dp/B09HRTM8RC/ref=sr_1_2_sspa?keywords=gaming+keyboard&pd_rd_r=a4fbbd28-2be4-4c81-889f-712185138139&pd_rd_w=BlKCP&pd_rd_wg=Jp7wM&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=6TWWS4YDZS8N3HFZ9WG5&qid=1642362412&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExTzFYWFlENFREWjBTJmVuY3J5cHRlZElkPUEwMzgyMjUxM1Y5UlpJRlhOWDJZUyZlbmNyeXB0ZWRBZElkPUEwMzgwNjAxM0pRVEVSUDIxSThQRyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
response = requests.get(url=url,headers=headers)
soup = BeautifulSoup(response.text,"html.parser")
price = float(soup.find(name="span",id="price_inside_buybox").text.split("$")[1].strip())
if price < 100:
    passwordG = "Ivan1234"
    my_email = "idiomas51231@gmail.com"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=passwordG)
        connection.sendmail(from_addr=my_email, to_addrs="antonio61231@gmail.com",
                            msg=f"Subject:Ofertas mamon comprele perro\n\n {url} \nEsta en oferta compralos ahora", )