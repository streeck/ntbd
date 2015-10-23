#!/usr/bin/python

import sys
import psycopg2
from datetime import timedelta, date

wkd = ["Segunda", "Terca", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo"]
wkdAbr = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]

mth = ["Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
mthAbr = ["Jan", "Fev", "Mar", "Abr", "Maio", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

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

    start_date = date(2005, 2, 18)
    end_date = date(2015, 10, 21)

    for single_date in daterange(start_date, end_date):
        if single_date.weekday() in [5, 6]:
            queries.append("INSERT INTO Tempo VALUES ({chave}, {diaNum}, '{diaSemana}', '{diaAbreviado}', {mesNum}, '{mesExtenso}', '{mesAbreviado}', {ano}, '{fds}')".format(chave=counter, diaNum=single_date.day, diaSemana=wkd[single_date.weekday()], diaAbreviado=wkdAbr[single_date.weekday()], mesNum=single_date.month, mesExtenso=mth[single_date.month-1], mesAbreviado=mthAbr[single_date.month-1], ano=single_date.year, fds='t'))
        else:
            queries.append("INSERT INTO Tempo VALUES ({chave}, {diaNum}, '{diaSemana}', '{diaAbreviado}', {mesNum}, '{mesExtenso}', '{mesAbreviado}', {ano}, '{fds}')".format(chave=counter, diaNum=single_date.day, diaSemana=wkd[single_date.weekday()], diaAbreviado=wkdAbr[single_date.weekday()], mesNum=single_date.month, mesExtenso=mth[single_date.month-1], mesAbreviado=mthAbr[single_date.month-1], ano=single_date.year, fds='f'))
        counter += 1
    return queries

writeData()
