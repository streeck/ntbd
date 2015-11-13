
-- agregado completo
CREATE TABLE perfilTempoAgregado(
    chave serial PRIMARY KEY,
    qtdViews int NOT NULL,
    categoria varchar NOT NULL,
    continente varchar NOT NULL,
    pais varchar NOT NULL,
    diaNum int NOT NULL,
    diaSemana varchar NOT NULL,
    mesNum int NOT NULL,
    ano int NOT NULL,
    fds boolean NOT NULL,
    sexo varchar NOT NULL
);

-- agregado só com ano
CREATE TABLE perfilAnoAgregado(
    chave serial PRIMARY KEY,
    qtdViews int NOT NULL,
    categoria varchar NOT NULL,
    continente varchar NOT NULL,
    pais varchar NOT NULL,
    ano int NOT NULL,
    sexo varchar NOT NULL

);

-- agregado segunda consulta
-- para a terceira consulta também
CREATE TABLE canalCategoriaAgregado (
    chave serial PRIMARY KEY,
    qtdViews int NOT NULL,
    categoria varchar NOT NULL,
    canal varchar NOT NULL,
    ano int NOT NULL,
    video varchar NOT NULL,
    qtdGostei int NOT NULL
);

-- agregado segunda consulta b)
CREATE TABLE perfilCanalAgregado (
    chave serial PRIMARY KEY,
    qtdViews int NOT NULL,
    video varchar NOT NULL,
    canal varchar NOT NULL,
    continente varchar NOT NULL,
    pais varchar NOT NULL,
    ano int NOT NULL,
    sexo varchar NOT NULL
);

