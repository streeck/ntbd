#!/usr/bin/python

# CODIGO QUE SEPARA O JSON E INSERE NO BANCO DE DADOS

import re
import json
import psycopg2

if __name__ == "__main__":
	nameList = open('videos.json','r')
	nameVideo = []
	for a in json.loads(nameList.read()):
		nameVideo.append(a[0])

	try:
		conn = psycopg2.connect("dbname='teste' user='postgres' host='localhost' ")
	except:
		print "Nao foi possivel conectar no SGDB!"
		exit()
	
	cur = conn.cursor()
	for video in nameVideo:
		try:
			videoList = open('data-video-'+video+'.json','r')
			with videoList:
				for value in json.loads(videoList.read())["rows"]:
					cur.execute("INSERT INTO Video (chaveTempo,chavePerfil, chaveCanal, qtdViews, video, nome, qtdGostei, qtdNaoGostei) VALUES (%(chaveTempo)s, %(chavePerfil)s, %(chaveCanal)s, %(qtdViews)s, %(video)s,%(nome)s,%(qtdGostei)s,%(qtdNaoGostei)s);",{'chaveTempo':re.sub('-',"",value[0]), 'chavePerfil':hehehe1, 'chaveCanal':hehehe2, 'qtdViews':value[1], 'video':video,'nome':hehehe3, 'qtdGostei': value[2], 'qtdNaoGostei': value[3]})
				conn.commit()
				print "Video assimilado no banco de dados..."+a
		except IOError:
			print "Video provavelmente privado..."+a
	cur.close()
	conn.close()		
