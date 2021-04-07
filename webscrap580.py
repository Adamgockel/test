# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 14:48:46 2021

@author: ajgoc
"""

import urllib.request as url
from bs4 import BeautifulSoup
import re
import pandas as pd

html = url.urlopen('http://gp.specagro.ru/region/3630/2/31/12/2020')
soup = BeautifulSoup(html, "html.parser")


row = ['Stimulating the development of priority sub-sectors of the agro-industrial complex and the development of small businesses',
       'Support for agricultural production in selected subsectors of crop and livestock production',
       'Total Development of branches of the agro-industrial complex',
       'Support for investment lending in the agro-industrial complex',
       'Reimbursement of part of the direct costs incurred for the creation and (or) modernization of agricultural facilities',
       'Total Promotion of investment activities in the agro-industrial complex',
       'Subsidies for the implementation of measures in the field of reclamation of agricultural land',
       'Total Development of land reclamation for agricultural land in Russia',
       'Subsidies for improving the housing conditions of citizens living in rural areas',
       'Subsidies for the provision of financial support in the fulfillment of the expenditure obligations of municipalities for the construction of housing provided under a residential lease agreement',
       'Subsidies for the arrangement of engineering infrastructure facilities and the improvement of sites located in rural areas for compact housing development',
       'Providing assistance to agricultural producers (except for citizens with personal subsidiary plots) operating in rural areas, in the provision of qualified specialists',
       'Subsidies for the implementation of measures for the improvement of rural areas',
       'Subsidies for the development of engineering infrastructure in rural areas where investment projects in the agricultural sector are being implemented',
       'Subsidies for the implementation of projects for integrated development of rural areas',
       'Total Integrated development of rural areas',
       'Creation of a support system for farmers and development of rural cooperation',
       'Total Creation of a support system for farmers and development of rural cooperation',
       'Subsidy to stimulate increased production of oilseeds',
       'Total Federal project "Export of agricultural products"',
       'Total',]


c23 = soup.find_all('td' , class_='table_row')
c1 = soup.find_all('td' , class_='table_dark_row')

column1 = []
column2 = []
column3 = []

count = 0 

for tag  in c23:
    
    if (count%2 >0):
        if tag.text=='-':
           column3.append(0)
        else:
            column3.append(int(tag.text.replace(" ", "")))
    
    else :
        if tag.text=='-':
           column2.append(0)
        else:
            column2.append(int(tag.text.replace(" ", "")))
        
    count += 1 
    
column3.append(sum(column3)/2)
column2.append(sum(column2)/2)
    
    
for tag  in c1:
    if tag.text=='-':
        column1.append(0)
    else:
        column1.append(int(tag.text.replace(" ", "")))
    
    
data = {'Rownames' : row,
        'Total' : column1,
        'Federal Budget' : column2,
        'The budget of the constituent entity of the Russian Federation' : column3}

df = pd.DataFrame (data, columns = ['Rownames','Total','Federal Budget','The budget of the constituent entity of the Russian Federation'])



Region_names = soup.find('div' , class_='titleBlock').text.replace("\n", "")
    
Region_names = Region_names.replace("  ", " ")

bad = re.findall('  .*' , Region_names)

Region_names = Region_names.replace(bad[0], "")











