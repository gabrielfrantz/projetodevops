CREATE database cadastros;

\c cadastros;

CREATE TABLE "tabela" (
    id SERIAL PRIMARY KEY,
    email VARCHAR(200) UNIQUE NOT NULL
);