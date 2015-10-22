DROP TABLE Video;
DROP TABLE Tempo;
DROP TABLE Perfil;
DROP TABLE Canal;


CREATE TABLE Tempo (
    chaveTempo int PRIMARY KEY,
    diaNum int NOT NULL,
    diaSemana varchar NOT NULL,
    diaAbreviado varchar NOT NULL,
    mesNum int NOT NULL,
    mesExtenso varchar NOT NULL,
    mesAbreviado varchar NOT NULL,
    ano int NOT NULL,
    fds boolean NOT NULL
);

CREATE TABLE Perfil (
    chavePerfil int PRIMARY KEY,
    continente varchar NOT NULL,
    pais varchar NOT NULL,
    estado varchar DEFAULT 'undefined',
    sexo char
);

CREATE TABLE Canal (
    chaveCanal int PRIMARY KEY,
    canal varchar NOT NULL,
    qtdInscritos int NOT NULL
);

CREATE TABLE Video (
    chaveTempo int NOT NULL,
    chavePerfil int NOT NULL,
    chaveCanal int NOT NULL,
    qtdViews int NOT NULL,
    video varchar NOT NULL,
    nome varchar NOT NULL,
    qtdGostei int NOT NULL,
    qtdNaoGostei int NOT NULL,
    FOREIGN KEY(chaveTempo) REFERENCES Tempo(chaveTempo),
    FOREIGN KEY(chavePerfil) REFERENCES Perfil(chavePerfil),
    FOREIGN KEY(chaveCanal) REFERENCES Canal(chaveCanal),
    PRIMARY KEY(chaveTempo, chavePerfil, chaveCanal, video)
);
