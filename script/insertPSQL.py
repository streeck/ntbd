#!/usr/bin/python

# CODIGO QUE SEPARA O JSON E INSERE NO BANCO DE DADOS

countries = ['GB', 'US', 'BR']

chaves = {'US': 41, 'BR': 45, 'GB': 17}

import re
import json
import psycopg2
import datetime
from datetime import datetime

def getChaveTempo(cur, date):
	cur.execute("SELECT chaveTempo FROM Tempo WHERE diaNum={dia} AND mesNum={mes} AND ano={ano}".format(dia=date.day, mes=date.month, ano=date.year))

	key = cur.fetchall()
	return key[0][0]

def getChaveCanal(cur, channel_id):
	cur.execute("SELECT chaveCanal FROM Canal WHERE canal='{}'".format(channel_id))

	key = cur.fetchall()

	return key[0][0]


if __name__ == "__main__":
	nameList = open('videos.json','r')
	nameVideo = []

	for a in json.loads(nameList.read()):
		nameVideo.append(a[0])

	try:
		conn = psycopg2.connect(database="youtubiu", user="charles", password="asdf", host="127.0.0.1", port="5432")
	except:
		print "Nao foi possivel conectar no SGDB!"
		exit()

	f = open('channel.json', 'r')
	channel_id = json.loads(f.read())

	cur = conn.cursor()

	channel_id = getChaveCanal(cur, channel_id)

	for video in nameVideo:
		for country in countries:
			try:
				videoList = open('data-video-{id};country=={code}.json'.format(id=video, code=country),'r')

				jasao = json.loads(videoList.read())

				with videoList:
					if 'rows' in jasao:
						for value in jasao["rows"]:
							date = datetime.strptime(value[0], "%Y-%m-%d")
							cur.execute("INSERT INTO Video VALUES ({chaveTempo}, {chavePerfil}, {chaveCanal}, {qtdViews}, '{video}', '{nome}', {qtdGostei}, {qtdNaoGostei});".format(chaveTempo=getChaveTempo(cur, date), chavePerfil=chaves[country], chaveCanal=channel_id, qtdViews=value[1], video=video, nome='teste', qtdGostei=value[2], qtdNaoGostei=value[3]))

							# cur.execute("INSERT INTO Video VALUES (%(chaveTempo)s, %(chavePerfil)s, %(chaveCanal)s, %(qtdViews)s, %(video)s,%(nome)s,%(qtdGostei)s,%(qtdNaoGostei)s);",{'chaveTempo':re.sub('-',"",value[0]), 'chavePerfil':hehehe1, 'chaveCanal':hehehe2, 'qtdViews':value[1], 'video':video,'nome':hehehe3, 'qtdGostei': value[2], 'qtdNaoGostei': value[3]})
						conn.commit()
						print "Video assimilado no banco de dados..."+video
			except IOError:
				print "Video provavelmente privado..."+video
	cur.close()
	conn.close()
