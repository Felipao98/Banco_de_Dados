create table veiculo(
    modelo varchar(50) NOT NULL,
    ano int NOT NULL,
    /*peso decimal(4,2) NOT NULL,*/
    tipo char(2) NOT NULL,
    preco decimal(7,2) NOT NULL,
    codigoFIPE varchar(8) PRIMARY KEY NOT NULL,
    marca varchar(12) NOT NULL
);

create table carro(
    hp int NOT NULL,
    /*tempo_0_100 int NOT NULL,*/
    cambio varchar(10) NOT NULL,
    carro_FIPE varchar(8) PRIMARY KEY NOT NULL
);

create table moto(
    cc int NOT NULL,
    partida varchar(20) NOT NULL,
    moto_FIPE varchar(8) PRIMARY KEY NOT NULL
);

create table preco(
    preco_mes decimal(7,2),
    mes_referencia date NOT NULL,
    desvalorizacao decimal(2,2),
);

create table usuario(
    identificador int(2) PRIMARY KEY default '00' and default '01', /*Estudar*/
    nome varchar(50) NOT NULL,
    cpf varchar(15) NOT NULL,
    data_nasc date NOT NULL,
    tipo char(3) NOT NULL
);

create table administrador(
    ID_adm int PRIMARY KEY NOT NULL
);

create table usuario_comum(
    ID_usuario_comum int PRIMARY KEY NOT NULL
);
/*INSERIR VALORES*/
/*CARRO*/
INSERT INTO veiculo
VALUES ('golf Highline 250 TSI 1.4 Flex 16V Gasolina', '2018', 'C', '128475', '005495-0', 'Volkswagen');

INSERT INTO carro
VALUES ('150', 'Automatico', '005495-0');

INSERT INTO preco
VALUES ('128475', '05-2023', '0.03');
/*MOTO*/
INSERT INTO veiculo
VALUES ('Mt 09 850Cc Abs Gasolina', '2023', 'M', '57728', '827094-5', 'Yamaha');

INSERT INTO moto
VALUES ('850', 'injecao eletronica', '827094-5');

INSERT INTO preco
VALUES ('57728', '05-2023', '1.10');

/*USUARIO*/
INSERT INTO usuario
VALUES ('00', 'Luis Felipe', '103164286-20', '12-02-1998', 'ADM');

/*DELETAR VALORES*/
DELETE FROM veiculo
WHERE peso; /*???*/

DELETE FROM carro
WHERE tempo_0_100;

/*CONSULTAR VALORES E ALTERAÇÃO NOS FORMATOS*/
SELECT date_format(data, '%Y') as ano
FROM veiculo;

SELECT date_format(data, 'MM-YYYY') as mes_referencia
FROM preco;

SELECT date_format(data, 'DD-MM-YYYY') as data_nasc
FROM usuario;

/*

TABELA FIPE primaria - https://tabelafipecarros.com.br/veiculo/7064/101/YAMAHA/MT/MT+09+850cc+ABS/2023/Gasolina?utm_source=Motos&utm_medium=undefined&utm_campaign=ORGANIC

TABELA FIPE secundaria - https://tabelacarros.com/motos/YAMAHA/MT-09-850CC-ABS/2022

TABELA DE DESVALORIZACAO - https://www.tabelafipebrasil.com/motos/YAMAHA/MT-09-850CC-ABS/2023
*/