/*1*/
drop table veiculo;

select date_format(date, 'YYYY') as ano;
select date_format(mes_referencia, '%m/%Y') as Mes_referencia from preco;
select date_format(data_nasc, '%m/%Y') as Data_nasc from usuario;

drop table carro;
/*2*/
drop table moto;
/*3*/
drop table valor_medio;
/*4*/
drop table usuario;
/*5*/
delete from preco where desvalorizacao='0.00';
alter table usuario modify column tipo char(4);
/*INSERT*/
insert into veiculo
values ('Golf Variant High. 250 1.4 TSI Flex Aut.', '2018', '110533.00', '005498-4', 'Volkswagen');
insert into veiculo
values ('HURACAN STO 5.2 V10', '2022', '5879990.00', '078021-9', 'Lamborghini');

insert into veiculo
values ('MT-09 TRACER 900 GT', '2023', '65633.00', '827110-0', 'Yamaha'),
('CBR 1000 RR Fireblade', '2020', '93207.00', '811073-5', 'Honda'),
('NINJA H2 SX SE 998cc', '2020', '181218.00', '817081-9', 'Kawasaki');


insert into carro
values ('139', 'Automatico', '001489-3'),
('243', 'Automatico', '003336-7'),
('640', 'Automatico', '078021-9');

insert into moto
values ('1000', 'Injecao eletrica', '811073-5'),
('998', 'Injecao eletrica', '817081-9'),
('900', 'Injecao eletrica', '827110-0');

insert into preco
values
('65633.00', '2023/05/22', '0.24'),
('93207.00', '2023/05/22', '1.48'),
('181218.00', '2023/05/22', '0.15');

insert into usuario
values ('115424626', 'Raul', '574824547-54', '2001/12/15', 'U_C'),
('115424548', 'Luana', '574824536-44', '2000/04/24', 'U_C'),
('118454626', 'Rafael', '574824457-54', '2011/11/11', 'U_C');
