CREATE USER docker WITH PASSWORD 'docker' SUPERUSER;

CREATE DATABASE cadastros;

\c cadastros;

CREATE TABLE "tabela" (
    "id" INT NOT NULL,
    "email" VARCHAR(200) NOT NULL,
    CONSTRAINT "PK_tabela" PRIMARY KEY ("id")
);