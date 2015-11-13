-- Consulta 1. a)

-- Consulta Agregado 1 - Perido mes e ano

SELECT avg(qtdViews)AS media
FROM perfilTempoAgregado
WHERE categoria = 'Musica'
AND mesNum >= 11 AND mesNum <= 12 AND ano = 2014
AND continente = 'Americas'
AND pais = 'Brazil'

-- Consulta 1. b)
-- Consulta Agregado 2 - Periodo Anual
SELECT avg(qtdViews)AS media
FROM perfilTempoAgregado
WHERE categoria = 'Educacao'
AND ano = 2014
AND sexo = 'F'

-- Consulta 2.a)
-- Agregado 4 - Canal e Perfil
SELECT avg(qtdViews)AS media
FROM perfilCanalAgregado
WHERE qtdViews > 1000
AND canal = 'UCxD2E-bVoUbaVFL0Q3PvJTg'
AND ano = 2013
AND sexo = 'M'

-- Consulta 2.b)
-- Agregado 4 - Perfil e Canal
SELECT avg(qtdViews)AS media
FROM perfilCanalAgregado
WHERE qtdViews > 1000
AND canal = 'UCxD2E-bVoUbaVFL0Q3PvJTg'
AND ano = 2013
AND continente = 'Americas'

 -- Consulta 2.c)
-- Agregado 3 - Canal e Categoria
SELECT avg(qtdViews)AS media
FROM canalCategoriaAgregado
WHERE qtdViews > 200
AND canal = 'UCHkj014U2CQ2Nv0UZeYpE_A'
AND categoria = 'Musica'
AND ano = 2013

-- Consulta 3
-- Agregado 3 - Canal e Categoria
SELECT avg(qtdGostei)AS media
FROM canalCategoriaAgregado
WHERE qtdGostei > 300
AND canal = 'UCHkj014U2CQ2Nv0UZeYpE_A'
AND categoria = 'Musica'
