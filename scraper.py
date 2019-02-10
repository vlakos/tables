import requests
import lxml.html as lh
import pandas as pd
url='http://www.acas.rs/acasPublic/pretragaPrilogaLica.htm'
#Create a handle, page, to handle the contents of the website
page = requests.get(url)
#Store the contents of the website under doc
doc = lh.fromstring(page.content)
#Parse data that are stored between <tr>..</tr> of HTML
tr_elements = doc.xpath('//tr')
#Check the length of the first 12 rows
[len(T) for T in tr_elements[:12]]
This is a template for a Python scraper on morph.io (https://morph.io)
