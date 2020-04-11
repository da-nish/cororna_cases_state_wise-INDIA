from django.shortcuts import redirect
import requests
from bs4 import BeautifulSoup
from datetime import date
from django.db import IntegrityError
from django.shortcuts import render


def getstate():
    page = requests.get("https://www.mohfw.gov.in/#site-advisories").text
    soup = BeautifulSoup(page,'lxml')
    # print(soup.prettify())

    My_table = soup.find('table',{'class':'table-striped'})
    t1 = My_table.find_all('tr')
    counter = 1
    total_positive =0
    total_cured =0
    total_death =0
    data = []
    for t in t1:
        li = []
        c=0

        for t1 in t.find_all('td'):
            if counter > 32:
                pass
                
            else:
                li.append(t1.get_text())
                print(t1.get_text())
        if len(li) is not 0:
            data.append(li)
            counter= counter+1

    mapdata = {}
    counter=1
    Name_Count = []
    for d1 in data:
        li1 = []
        li1.append(d1[1])
        li1.append(d1[2])
        Name_Count.append(li1)

    #print('--->',Name_Coun#t)
    return Name_Count