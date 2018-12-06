BEGIN TRANSACTION;
CREATE TABLE cidades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cidade TEXT,
    uf VARCHAR(2)
);
INSERT INTO "cidades" VALUES(1,'Campinas','SP');
INSERT INTO "cidades" VALUES(2,'Sao Paulo','SP');
INSERT INTO "cidades" VALUES(3,'Rio de Janeiro','RJ');
CREATE TABLE clientes (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf VARCHAR(11) NOT NULL,
    email TEXT NOT NULL,
    cidade_id INTEGER,
    criado_em DATE NOT NULL, bloqueado BOOLEAN,
    FOREIGN KEY (cidade_id) REFERENCES cidades(id)
);
INSERT INTO "clientes" VALUES(1,'Regis','01119239423','regis_novo@gmail.com',1,'2014-06-11',NULL);
INSERT INTO "clientes" VALUES(2,'Aloisio','02320322932','aloisio@email.com',2,'2014-06-09',NULL);
INSERT INTO "clientes" VALUES(3,'Bruna','11239428344','bruna@email.com',2,'2014-06-09',NULL);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('cidades',3);
INSERT INTO "sqlite_sequence" VALUES('clientes',4);
COMMIT;
