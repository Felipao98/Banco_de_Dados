/*1)a) */
SELECT Dnome, COUNT(*)
FROM DEPARTAMENTO, FUNCIONARIO
WHERE AVG(Salario > '30000')

/*b) Essa consulta pode ser especificada utilizando JOIN*/

SELECT COUNT(*)
FROM (FUNCIONARIO JOIN DEPARTAMENTO) ON Dnr=Dnumero
WHERE Sexo = 'M', Salario > '30000' 

/*2)a) */
SELECT Pnome, Unome
FROM (FUNCIONARIO JOIN DEPARTAMENTO)
WHERE Cpf_supervisor = MAX(Salario)

/*b) */
SELECT Pnome, Unome
FROM (FUNCIONARIO JOIN DEPARTAMENTO) ON Cpf_supervisor = Cpf_gerente
WHERE Cpf_supervisor = '88866555576'

/*c) */
SELECT Pnome, Unome
FROM FUNCIONARIO
WHERE MIN(Salario) AND MIN(Salario) > '10000'

/*3)a) */
CREATE VIEW visao
AS SELECT Dnome, Pnome, Unome, Salario
FROM DEPARTAMENTO, FUNCIONARIO
