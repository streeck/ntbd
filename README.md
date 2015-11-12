# Projeto de Novas Tecnologias de Bancos de Dados

### Tema

O tema proposto para a construção deste projeto é o YouTube que é uma plataforma de compartilhamento de vídeos em formato digital. Os dados serão retirados através da API do YouTube com *scripts* desenvolvidos na linguagem Python.

### Objetivo

Gerar um *Business Intelligence*, isto é, uma forma de analisar e apresentar a informação de maneira útil e proveitosa para que as melhores decisões nos negócios possam ser tomadas por uma agência de publicidade, auxiliando seus clientes na tomada de decisão ao selecionar abordagens de publicidade e propaganda de seus produtos. Proporcionando ainda informações sobre o perfil dos usuários da plataforma, através da análise de dados como: visualizações, “Gostei”, compartilhamentos, inscrições, categoria e região.

### Requisitos de Negócio

1. Média de visualizações de uma amostragem de vídeos, por categoria e período, considerando:
    * região do telespectador
    * sexo do telespectador
2. Média de visualizações de todos os vídeos de um canal, acima de um limiar e por período, considerando:
    * o sexo dos telespectadores;
    * região (continente, pais e estado) dos telespectadores;
    * categoria do vídeo;
3. Média de “Gostei” de todos os vídeos de um canal, de mesma categoria, acima de um limiar.


### Hierarquias

+ Ano -> Mês -> Dia
+ Ano -> Mês -> Fim de Semana
+ Continente -> País -> Estado
+ Perfil -> Sexo
