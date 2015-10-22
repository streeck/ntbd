#!/usr/bin/python

# CÓDIGO QUE SEPARA O JSON E INSERE NO BANCO DE DADOS

import re
import json
import psycopg2

if __name__ == "__main__":

	try:
		conn = psycopg2.connect("dbname='teste' user='postgres' host='localhost' ")
	except:
		print "Nao foi possivel conectar no SGDB!"
		exit()

	cur = conn.cursor()
	videoList = open('data.json','r')
	for value in json.loads(videoList.read())["rows"]:
		cur.execute("INSERT INTO hue (hue1,hue2,hue3,hue4) VALUES (%(str)s, %(str2)s, %(int3)s, %(int4)s);",{'str':re.sub('-',"",value[0]), 'str2':value[1], 'int3': value[2], 'int4': value[3]})
	conn.commit()
	cur.close()
	conn.close()		
