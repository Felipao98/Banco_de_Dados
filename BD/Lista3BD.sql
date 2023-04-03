create table aluno(
    nome varchar(50),
    numero_aluno int,
    tipo_aluno int,
    curso char(5),
    PRIMARY KEY (numero_aluno)
);
create table disciplina(
    nome_disciplina varchar(20),
    numero_disciplina char(10),
    creditos int,
    departamento char(5),
    PRIMARY KEY (numero_disciplina)
);
create table turma(
    PRIMARY KEY identificacao_turma int,
    FOREIGN KEY (numero_disciplina) REFERENCES disciplina,
    semestre varchar(15),
    ano int,
    professor varchar(20)
);
create table historico_escolar(
    FOREIGN KEY (numero_aluno) REFERENCES aluno,
    FOREIGN KEY (identificacao_turma) REFERENCES turma,
    nota char(1)
);
create table pre_requisito(
    FOREIGN KEY (numero_disciplina) REFERENCES disciplina,
    numero_pre_requisito char(10)
);
SELECT tipo_aluno
FROM aluno
where tipo_aluno = '4';

SELECT ano , professor
FROM turma
WHERE professor = 'Kleber' and ano >= '07'and ano <= '08';

SELECT professor, numero_disciplina, semestre, ano, identificacao_turma
FROM turma
WHERE professor = 'Kleber';

/* 2) d)*/
SELECT nome, tipo_aluno, numero_aluno, identificacao_turma, nota,  numero_disciplina, semestre, ano, nome_disciplina
FROM aluno
INNER JOIN historico_escolar ON 
WHERE tipo_aluno = '4';

/*3) a) */
INSERT INTO aluno
VALUES
('Alves','25','1','MAT');

UPDATE aluno
SET tipo_aluno = '2'
WHERE nome = 'Silva';

INSERT INTO disciplina
VALUES
('Engenharia do conhecimento', 'CC4390','3','CC');

DELETE FROM aluno
WHERE nome = 'Silva' and numero_aluno = '17';