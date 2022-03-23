import requests
import requests
from bs4 import BeautifulSoup


class MobileRecharge:
    def __init__(self):
        self.url = "https://telecom.economictimes.indiatimes.com/recharge-plans/"
        r = requests.get(self.url)
        try:
            self.soup = BeautifulSoup(r.content, 'html5lib')
            circle = self.soup.find('ul', attrs={'aria-labelledby': 'circleoptions'})
            self.circle = {item.text: item['href'] for item in circle.findAll('a')}
            operator = self.soup.find('ul', attrs={'aria-labelledby': 'operatorptions'})
            self.operator = {item.text: item['href'] for item in operator.findAll('a')}
            recharge = self.soup.find('ul', attrs={'aria-labelledby': 'rechargeoptions'})
            self.plans = {item.text: item['href'] for item in recharge.findAll('a')}
        except Exception as e:
            pass

    def get_data(self, circle='andhra-pradesh', operator='airtel'):
        datas = []
        temp = []
        try:
            for i in range(1, 1000):
                url = f"https://telecom.economictimes.indiatimes.com/recharge-plans/{circle}/{operator}/{i}"
                r = requests.get(url)
                soup = BeautifulSoup(r.content, 'html5lib')
                all = soup.find('div', attrs={'class': 'tbl_outr'})
                if all.find('h4') != None:
                    break
                else:
                    data = soup.find('div', attrs={'class': 'tbl_outr'})
                    for table in data.find('tbody').find_all('tr'):
                        for td in table.find_all('td'):
                            temp.append(td.text)
                        datas.append(temp.copy())
                        temp.clear()

            return {'circle': self.circle, 'operator': self.operator, 'plans': self.plans, 'data': datas}
        except Exception as e:
            return {'circle': None, 'operator': None, 'plans': None, 'data': None}


mob = MobileRecharge()
dict = mob.get_data(circle='asaam')
