-- inserção do agregado completo
INSERT INTO perfilTempoAgregado
(qtdViews, categoria, continente, pais, diaNum,
diaSemana, mesNum, ano, fds, sexo)
 SELECT Video.qtdViews, Video.categoria, Perfil.continente,
 Perfil.pais, Tempo.diaNum, Tempo.diaSemana,
 Tempo.mesNum, Tempo.ano, Tempo.fds, Perfil.sexo
 FROM Video, Perfil, Tempo
 WHERE Video.chaveTempo = Tempo.chaveTempo
 AND Video.chavePerfil = Perfil.chavePerfil
 GROUP BY Video.qtdViews, Video.categoria, Perfil.continente,
 Perfil.pais, Tempo.diaNum, Tempo.diaSemana, Tempo.mesNum,
 Tempo.ano, Tempo.fds, Perfil.sexo;

-- inserção só com ano
INSERT INTO perfilAnoAgregado (qtdViews, categoria, continente, pais,
ano, sexo)
SELECT a.SUM, a.categoria, a.continente, a.pais, a.ano, a.sexo
FROM(
 SELECT SUM(Video.qtdViews), Video.categoria, Perfil.continente,
 Perfil.pais, Tempo.ano, Perfil.sexo, Video.nome
 FROM Video, Perfil, Tempo
 WHERE Video.chaveTempo = Tempo.chaveTempo
 AND Video.chavePerfil = Perfil.chavePerfil
 GROUP BY Video.categoria, Perfil.continente,
 Perfil.pais, Tempo.ano, Perfil.sexo, Video.nome
) AS a;

-- inserção canalCategoriaAgregado
-- terceira consulta
INSERT INTO canalCategoriaAgregado (qtdViews, categoria, canal, ano,
 video, qtdGostei)
 SELECT SUM(Video.qtdViews), Video.categoria,
 Canal.canal, Tempo.ano, Video.video, Video.qtdGostei
 FROM Video, Canal, Tempo
 WHERE Video.chaveTempo = Tempo.chaveTempo
 AND Video.chaveCanal = Canal.chaveCanal
 GROUP BY Video.categoria, Video.qtdGostei, Canal.canal, Tempo.ano,
 Video.video;


INSERT INTO perfilCanalAgregado (qtdViews, video, canal,
 continente, pais, ano, sexo)
 SELECT SUM(Video.qtdViews), Video.video, Canal.canal,
 Perfil.continente, Perfil.pais, Tempo.ano, Perfil.sexo
 FROM Video, Canal, Tempo, Perfil
 WHERE Video.chaveTempo = Tempo.chaveTempo
 AND Video.chaveCanal = Canal.chaveCanal
 AND Video.chavePerfil = Perfil.chavePerfil
 GROUP BY Video.video,Canal.canal, Perfil.continente,
 Perfil.pais, Tempo.ano, Perfil.sexo;


