from third_party.chartink import ChartInk

import requests


class BTST(ChartInk):
    def btst_15_min(self):
        chart_ink = ChartInk()
        url = "https://chartink.com/screener/process"
        referer = 'https://chartink.com/screener/btst-15'
        payload = "scan_clause=(+%7Bcash%7D+(+latest+close+%3E+latest+ema(+close%2C100+)+and+latest+volume+%3E+500000+and+latest+close+%3E+100+and+latest+rsi(+14+)+%3E+55+and+latest+close+%3E+1+day+ago+high+and+latest+volume+%3E+latest+sma(+volume%2C10+)+*+2+)+)+"
        headers = {
            'authority': 'chartink.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-IN,en-GB;q=0.9,en;q=0.8,en-US;q=0.7',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': chart_ink.cookie,
            'origin': 'https://chartink.com',
            'referer': referer,
            'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42',
            'x-csrf-token': chart_ink.csrf_token,
            'x-requested-with': 'XMLHttpRequest'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return response
