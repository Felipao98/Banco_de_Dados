CREATE TABLE tipo_veiculo(
    tipo varchar(10)
);
CREATE TABLE modelo(
    modelo varchar(15),
    ano int(4),
    motorizacao varchar(10),
    combustivel varchar(20),
    torque varchar(10),
    potencia int(4),
    valvulas int(3),
    cambio varchar(15),
    codigoFipe varchar(8)
);
CREATE TABLE preco(
    preco_medio decimal(8,2),
    mes_referencia date,
);
/*
API em formato JSON

MARCAS DOS VEICULOS
https://apifipe.com.br/api/carros/token

MODELOS
https://apifipe.com.br/api/carros/7/token

ANO
https://apifipe.com.br/api/carros/7/8946/token

VALOR
https://apifipe.com.br/api/carros/7/8946/2021-1/token

CODIGO FIPE
https://apifipe.com.br/api/fipe/009258-4/token

CODIGOFIPE + ANO
https://apifipe.com.br/api/fipe/009258-4/2021-1/token
*/