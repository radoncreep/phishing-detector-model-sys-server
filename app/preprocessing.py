from time import strftime
import requests
from bs4 import BeautifulSoup
import re
import whois
from datetime import date
from urllib.parse import urlparse
import pandas as pd

df = pd.read_csv('datasets/phishtanksites.csv')
phised_sites = df['url'].values

# rows = []
# for row in csv_reader:
#     rows.append(row)
# print(rows)

labels = {
    "legitimate": 1,
    "phished": -1,
    "suspicious": 0
}

# print(pd.DataFrame(labels['val'].T))

req_urls_values = []
urls = []
test_str = "http"
test_str2 = "https"

class WebContentPreprocessor():
    def __init__(self):
        # self.content_data = dict()
        self.SFH = None
        self.popUpWindow = None
        self.SSLfinal_state = None
        self.Request_URL = None
        self.URL_of_Anchor = None
        self.web_traffic = None
        self.URL_Length = None
        self.age_of_domain = None
        self.having_IP_Address = None 

        pass

    def derive_age_of_domain(self, url):
        domain = urlparse(url).netloc
        print('domain ', domain)

        flags = 0
        flags = flags | whois.NICClient.WHOIS_QUICK

        whois_info = whois.whois(domain, flags=flags)
        
        date_time_of_site_creation = whois_info.creation_date
        year_of_site_creation = str(date_time_of_site_creation).split(" ")[0].split("-")[0]
        current_year = date.today().strftime('%Y-%m-%d').split("-")[0]

        age_of_site = int(current_year) - int(year_of_site_creation)

        if age_of_site > 1:
            self.content_data["age_of_domain"] = "legitimate"
        else:
            self.content_data["age_of_domain"] = "phished"

        print(year_of_site_creation)
        # print("Domain registrar ", whois_info)
        return self.content_data["age_of_domain"]



    def longUrl(self, baseUrl):
        if len(baseUrl) < 54:
            self.content_data["longUrl"] = "legitimate"
        elif len(baseUrl) > 54 and len(baseUrl) <= 75:
            self.content_data["longUrl"] = "suspicious"
        else:
            self.content_data["longUrl"] = "phished"

    # calculate the request url percentage
    def scrapeReqUrl(baseUrl):
        html_doc = requests.get(baseUrl)

        text_format = BeautifulSoup(html_doc.text, "html.parser")

        for i in text_format.find_all("a"):
            href = i.attrs['href']

            if test_str in href:
                urls.append(labels["phished"])
            elif test_str2 in href:
                urls.append(labels["suspicious"])
            else:
                urls.append(labels["legitimate"])

            if href.startswith("/"):
                site = baseUrl + href
                if site not in urls:
                    urls.append(site)
                    print(urls)


    def reqUrl(self, baseUrl):
        print('here')

        html_doc = requests.get(baseUrl)
        text_format = BeautifulSoup(html_doc.text, "html.parser")

        for image in text_format.find_all("img"):
            source = image.attrs['src']
            print('here')

            print(source)
        return

    def url_of_anchor(self, baseUrl):
        if '@' in baseUrl:
            return -1

    def having_ip_address(self, url):
        validity = url.contains('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
        print('vali ', validity)
        return

# testing = [WebContentPreprocessor(1, 0, -1, 1, 1, 1, 0, 0, -1)]
testing =   WebContentPreprocessor()
# testing.having_ip_address('leetcode.com')



# testing.reqUrl('https://gogoanime.pe/')