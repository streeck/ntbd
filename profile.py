#!/usr/bin/python

import sys
import psycopg2
from datetime import timedelta, date

continents = {'002': 'Africa', '019': 'Americas', '142': 'Asia', '150': 'Europe', '009': 'Oceania'}

countries = {'002': {'EG': 'Egypt', 'SN': 'Senegal', 'ZW': 'Zimbabwe', 'AO': 'Angola', 'RW': 'Rwanda', 'BW': 'Botswana'},
             '019': {'BR': 'Brazil', 'CU': 'Cuba', 'US' :'United States'},
             '142': {'IN': 'India', 'HK': 'Hong Kong', 'JP': 'Japan'},
             '150': {'DK': 'Denmark', 'BE': 'Belgium', 'DE': 'Germany', 'FR': 'France', 'IT': 'Italy', 'IE': 'Ireland', 'PL': 'Poland', 'SE': 'Sweden', 'GB': 'United Kingdom'},
             '009': {'VU': 'Vanuatu', 'AU': 'Australia'}}

sex = ['M', 'F']

def writeData():
    conn = psycopg2.connect(database="youtubiu", user="charles", password="asdf", host="127.0.0.1", port="5432")
    cur = conn.cursor()

    queries = createSQL()

    for query in queries:
        cur.execute(query)

    conn.commit()
    print "Records created successfully"

    conn.close()

def createSQL():
    queries = []

    counter = 1

    for continent in countries:
        for country in countries[continent].values():
            for value in sex:
                queries.append("INSERT INTO Perfil VALUES ({chave}, '{continent}', '{country}', '{nothing}', '{sex}')".format(chave=counter, continent=continents[continent], country=country, sex=value, nothing="undefined"))
                counter += 1

    return queries

writeData()
