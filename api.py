import requests
import requests
from bs4 import BeautifulSoup


class MobileRecharge:
    def __init__(self):
        self.circle={'--ALL--':'all','Andhra Pradesh':'andhra-pradesh','Assam':'assam','Bihar-Jharkhand':'bihar-jharkhand','Chennai':'chennai','Delhi NCR':'delhi','Gujrat':'gujrat','Haryana':'haryana','Himachal Pradesh':'himachal-pradesh','Jammu Kashmir':'jammu-kashmir','Karnataka':'karnataka','Kerala':'kerala','Kolkata':'kolkata','Madhya Pradesh Chattisgarh':'madhya-pradesh','Maharashtra':'maharashtra','Mumbai':'mumbai','North East':'north-east','Odisha':'odisha','Punjab':'punjab','Rajasthan':'rajasthan','Tamil Nadu':'tamil-nadu','UP East':'uttar-pradesh-east','UP West':'uttar-pradesh-west','West Bengal':'west-bengal'}
        self.operator={'--ALL--':'all','Airtel':'airtel','BSNL':'bsnl','Jio':'reliance-jio','MTNL':'mtnl','VI':'vi'}
        self.plans={'--ALL--':'','2G Data':'2g-data-plans','3G Data':'3g-data-plans','4G Data':'4g-data-plans','Full Talktime':'full-talktime-plans','ISD':'isd-plans','Local':'local-plans','Other':'other-plans','SMS':'sms-plans','STD':'std-plans','Top Up ':'top-up-plans'}       


    def get_data(self, circle='andhra-pradesh', operator='airtel',plan=''):
        datas = []
        temp = []
        try:
            for i in range(1, 1000):
                if plan=="":
                    url = f"https://telecom.economictimes.indiatimes.com/recharge-plans/{circle}/{operator}/{i}"
                else:
                    url = f"https://telecom.economictimes.indiatimes.com/recharge-plans/{circle}/{plan}-{operator}/{i}"    
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
            print(e)
            return {'circle': None, 'operator': None, 'plans': None, 'data': None}
