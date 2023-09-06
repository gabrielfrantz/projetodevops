CREATE DATABASE cadastros;

\c cadastros;

CREATE TABLE "tabela" (
    "id" serial PRIMARY KEY,
    "email" VARCHAR(200) UNIQUE NOT NULL
);