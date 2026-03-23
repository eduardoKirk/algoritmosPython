USE BD12022674;
-- 2)
CREATE TABLE IF NOT EXISTS funcionarios(id INT PRIMARY KEY AUTO_INCREMENT,
 nome VARCHAR(100) NOT NULL,
 cargo VARCHAR(50) NOT NULL, 
 salario DECIMAL(10,2) NOT NULL);

 INSERT INTO funcionarios(nome, cargo, salario) VALUES ("Pedro Silva", "rh", 6000.00), ("Matheus De Santana", "gerente", 10000.00);
 
 -- 3)
 
 ALTER TABLE funcionarios ADD data_admissao DATE NOT NULL DEFAULT '2026-01-01';
 INSERT INTO funcionarios(nome, cargo, salario, data_admissao) VALUES ("Sérgio Silva", "rh", 6500.00, "2024-04-20"), ("André De Santana", "gerente", 7000.00, "2025-09-23");
 
 -- 4)
 
 ALTER TABLE funcionarios DROP COLUMN cargo;
 INSERT INTO funcionarios(nome, salario, data_admissao) VALUES ("Gabriel Santino", 2000.00, "2021-03-10"), ("Paulo Oliveira", 3000.00, "2018-10-02");
 
 -- 5)
 
 ALTER TABLE funcionarios MODIFY COLUMN salario DECIMAL(12,2);
 INSERT INTO funcionarios(nome, salario, data_admissao) VALUES ("Bruno Silva", 2000.00, "2020-02-15"), ("Maria Santino", 3000.00, "2026-01-02");
 -- 6)
 
 CREATE TABLE departamentos (id INT PRIMARY KEY AUTO_INCREMENT,
 nome VARCHAR(100) NOT NULL);
 
 ALTER TABLE funcionarios ADD COLUMN departamentoID INT;
 
 ALTER TABLE funcionarios 
 ADD CONSTRAINT FK_departamentoFuncionario 
 FOREIGN KEY (departamentoID) REFERENCES departamentos(id);

 INSERT INTO funcionarios(nome, salario, data_admissao, departamentoID) VALUES ("Heitor", 12000.00, "2026-01-01", 2), ("Lucas", 20000.00, "2017-09-24", 1);
 
 -- 7)
 
 ALTER TABLE departamentos ADD COLUMN orcamento DECIMAL(12,2);
 INSERT INTO departamentos(nome, orcamento) VALUES ("Publicidade", 25000.00), ("Telemarketing", 30000.00);
 
 -- 8)
 
 ALTER TABLE departamentos DROP COLUMN orcamento;
 INSERT INTO departamentos(nome) VALUES ("Logistica"), ("Financeiro");
 
 -- 9)
 
 ALTER TABLE departamentos MODIFY COLUMN nome VARCHAR(150);
 INSERT INTO departamentos(nome) VALUES ("RH"), ("Produção");
 -- 10)
 
 ALTER TABLE departamentos RENAME TO setores;
 INSERT INTO setores(nome) VALUES ("Transporte"), ("Treinamentos");

 -- 11)
 ALTER TABLE funcionarios DROP FOREIGN KEY FK_departamentoFuncionario;
 ALTER TABLE funcionarios DROP COLUMN departamentoID;
 DROP TABLE setores;
 INSERT INTO funcionarios(nome, salario, data_admissao) VALUES ("Roberto", 8000.00, "2015-03-17"), ("Roberta", 3000.00, "2024-01-02");
 
 -- 12)
 
 ALTER TABLE funcionarios ADD COLUMN status VARCHAR(20) DEFAULT "Ativo";
 INSERT INTO funcionarios(nome, salario, data_admissao, status) VALUES ("Márcio", 9000.00, "2019-04-15", "Ativo"), ("Fernanda", 4000.00, "2024-05-02", "Inativo");
