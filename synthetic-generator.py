import sys
import json
import random
import psycopg2
from datetime import date, datetime, timedelta
from collections import OrderedDict

profileKeysMale = {'USM': 41, 'BRM': 45, 'GBM': 17}
profileKeysFemale = {'USF': 42, 'BRF': 46, 'GBF': 18}
profileKeysMale = OrderedDict(sorted(profileKeysMale.items(), key=lambda t: t[1]))
profileKeysFemale = OrderedDict(sorted(profileKeysFemale.items(), key=lambda t: t[1]))

categoriesDict = {'1': "Filmes e desenhos", '2': "Automoveis", '10': "Musica", '15': "Animais",
                  '17': "Esportes", '18': "Curtas", '19': "Viagens e eventos", '20': "Jogos",
                  '21': "Videoblog", '22': "Pessoas e blogs", '23': "Comedia", '24': "Entretenimento",
                  '25': "Noticias e politica", '26': "Guias e Estilo", '27': "Educacao",
                  '28': "Ciencia e tecnologia", '30': "Filmes", '31': "Desenho/animacao",
                  '32': "Acao/aventura", '33': "Classicos", '34': "Comedia", '35': "Documentario",
                  '36': "Drama", '37': "Familia", '38': "Estrangeiro", '39': "Terror",
                  '40': "Ficcao cientifica/fantasia", '41': "Suspense", '42': "Curtas",
                  '43': "Programas", '44': "Trailers"}

class Video(object):

    def __init__(self, id, date, channelId, title, views, likes, dislikes, category):
        self.id = id
        self.date = date
        self.channelId = channelId
        self.title = title
        self.views = views
        self.likes = likes
        self.dislikes = dislikes
        self.category = categoriesDict['{}'.format(category)]

    def __repr__(self):
        print self.id
        print self.date
        print self.channelId
        print self.title
        print self.views
        print self.likes
        print self.dislikes
        print self.category

    def average(self, stat):
        pubDate = datetime.strptime(self.date, "%Y-%m-%d")
        endDate = datetime(2015, 10, 21)
        dateDiff = (endDate - pubDate).days

        return stat/dateDiff

    def ranges(self):
        random.seed()

        dic = {}

        dic['GB'] = random.uniform(0, 0.34)
        dic['BR'] = random.uniform(0, 0.22)
        dic['US'] = 1 - (dic['GB'] + dic['BR'])

        for key in profileKeysMale.keys():
            dic['{}'.format(key)] = random.uniform(0, 1)

        for key in profileKeysFemale.keys():
            dic['{}'.format(key)] = 1 - dic['{:.2}M'.format(key)]

        return dic

    def daterange(self, start_date, end_date):
        for n in range(int ((end_date - start_date).days)):
            yield start_date + timedelta(n)

    def insertion(self, cur):
        random.seed()

        viewsAvg = self.average(self.views)
        likesAvg = self.average(self.likes)
        dislikesAvg = self.average(self.dislikes)

        dic = self.ranges()

        pubDate = datetime.strptime(self.date, "%Y-%m-%d")
        endDate = datetime(2015, 10, 21)

        for day in self.daterange(pubDate, endDate):
            for key in profileKeysFemale.keys():
                cur.execute("INSERT INTO Video VALUES ({chaveTempo}, {chavePerfil}, {chaveCanal}, {qtdViews}, '{video}', '{categoria}', '{nome}', {qtdGostei}, {qtdNaoGostei});".format(
                       chaveTempo=getChaveTempo(cur, day),
                       chavePerfil=profileKeysFemale[key],
                       chaveCanal=getChaveCanal(cur, self.channelId),
                       qtdViews=int(random.randint(int(viewsAvg*0.8),int(viewsAvg*1.2)) * dic['{:.2}'.format(key)] * dic[key]),
                       video=self.id, categoria=self.category, nome=self.title,
                       qtdGostei=int(random.randint(int(likesAvg*0.8), int(likesAvg*1.2)) * dic['{:.2}'.format(key)] * dic[key]),
                       qtdNaoGostei=int(random.randint(int(dislikesAvg*0.8), int(dislikesAvg*1.2)) * dic['{:.2}'.format(key)] * dic[key])))

            for key in profileKeysMale.keys():
                cur.execute("INSERT INTO Video VALUES ({chaveTempo}, {chavePerfil}, {chaveCanal}, {qtdViews}, '{video}', '{categoria}', '{nome}', {qtdGostei}, {qtdNaoGostei});".format(
                       chaveTempo=getChaveTempo(cur, day),
                       chavePerfil=profileKeysMale[key],
                       chaveCanal=getChaveCanal(cur, self.channelId),
                       qtdViews=int(random.randint(int(viewsAvg*0.8),int(viewsAvg*1.2)) * dic['{:.2}'.format(key)] * dic[key]),
                       video=self.id, categoria=self.category, nome=self.title,
                       qtdGostei=int(random.randint(int(likesAvg*0.8), int(likesAvg*1.2)) * dic['{:.2}'.format(key)] * dic[key]),
                       qtdNaoGostei=int(random.randint(int(dislikesAvg*0.8), int(dislikesAvg*1.2)) * dic['{:.2}'.format(key)] * dic[key])))

        conn.commit()


def getChaveTempo(cur, date):
    cur.execute("SELECT chaveTempo FROM Tempo WHERE diaNum={dia} AND mesNum={mes} AND ano={ano}".format(dia=date.day, mes=date.month, ano=date.year))

    key = cur.fetchall()
    return key[0][0]

def getChaveCanal(cur, channel_id):
    cur.execute("SELECT chaveCanal FROM Canal WHERE canal='{}'".format(channel_id))

    key = cur.fetchall()

    return key[0][0]

def updateChannels(cur, videoList):
    for video in videoList:
        cur.execute("SELECT * FROM Canal WHERE canal='{}'".format(video.channelId))
        if not cur.fetchone():
            cur.execute("INSERT INTO Canal(canal, qtdInscritos) VALUES ('{channelId}', 0)".format(channelId=video.channelId))
            conn.commit()


if __name__ == "__main__":

    videoList = []

    with open('synthetic-data.json', 'r') as fileInput:
        for video in json.loads(fileInput.read())["videos"]:
            aux = Video(video["id"], video["date"], video["channelId"],
                        video["title"], video["stats"]["views"],
                        video["stats"]["likes"], video["stats"]["dislikes"], video["category"])
            videoList.append(aux)

    try:
        conn = psycopg2.connect(database="youtubiu", user="charles", password="asdf", host="127.0.0.1", port="5432")
    except:
        print "Nao foi possivel conectar no SGDB!"
        exit()

    cur = conn.cursor()

    updateChannels(cur, videoList)

    print "Synthetic data generation and insertion has begun!"

    for video in videoList:
        print "Currently generating data for video: {}...".format(video.id),
        try:
            video.insertion(cur)
            print "Done!"
        except:
            print "\n\tError: data already exists!"

