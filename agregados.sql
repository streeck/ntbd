CREATE TABLE agregado1a (
    chave serial PRIMARY KEY,
    qtdViews int NOT NULL,
    categoria varchar NOT NULL,
    continente varchar NOT NULL,
    pais varchar NOT NULL,
    estado varchar DEFAULT 'undefined',
    diaNum int NOT NULL,
    diaSemana varchar NOT NULL,
    mesNum int NOT NULL,
    ano int NOT NULL,
    fds boolean NOT NULL
);
