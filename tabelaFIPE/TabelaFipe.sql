/*1*/
drop table veiculo;

select date_format(date, 'YYYY') as ano;

drop table carro;
/*2*/
drop table moto;
/*3*/
drop table valor_medio;
/*4*/
drop table usuario;
/*5*/
delete from veiculo where preco='99999.99';
alter table veiculo modify column preco decimal(9,2);
/*INSERT*/
insert into veiculo
values ('Golf Variant High. 250 1.4 TSI Flex Aut.', '2018', '110533.00', '005498-4', 'Volkswagen');
insert into veiculo
values ('HURACAN STO', '2022', '5879990.00', '078021-9', 'Lamborghini');
