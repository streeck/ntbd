CREATE TABLE agregado1a (
    chave serial PRIMARY KEY,
    qtdViews int NOT NULL,
    categoria varchar NOT NULL,
    continente varchar NOT NULL,
    pais varchar NOT NULL,
    ano int NOT NULL,
    sexo char
);

CREATE TABLE agregado1b (
    chave serial PRIMARY KEY,
    qtdViews int NOT NULL,
    categoria varchar NOT NULL,
    continente varchar NOT NULL,
    pais varchar NOT NULL,
    diaNum int NOT NULL,
    diaSemana varchar NOT NULL,
    diaAbreviado varchar NOT NULL,
    mesNum int NOT NULL,
    mesExtenso varchar NOT NULL,
    mesAbreviado varchar NOT NULL,
    ano int NOT NULL,
    fds boolean NOT NULL,
    sexo char,
);
