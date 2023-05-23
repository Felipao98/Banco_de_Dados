/*Tabelas*/
create table veiculo(
	modelo varchar(50),
    ano int,
    preco decimal(7,2),
    codigoFIPE varchar(8) primary key,
    marca varchar(12)
);

create table carro(
	hp int,
    cambio varchar(15),
    carro_FIPE varchar(8) primary key
);

create table moto(
	cc int,
    partida varchar(20),
    moto_FIPE varchar(8) primary key
);

create table preco(
	preco_mes decimal(7,2),
    mes_referencia date,
    desvalorizacao decimal(2,2)
);

create table usuario(
	id int(2),
    nome varchar(50),
    cpf varchar(15),
    data_nasc date,
    tipo char(2)
);