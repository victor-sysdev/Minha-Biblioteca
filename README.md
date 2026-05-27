# 📚 Biblioteca Tech

Sistema web desenvolvido com Python + Flask + MySQL para gerenciamento de livros técnicos.

---

# 🚀 Tecnologias

- Python
- Flask
- MySQL
- HTML5
- CSS3

---

# 📂 Estrutura do Projeto

```bash
biblioteca/
│
├── app.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

# ⚙️ Instalação

## Clonar repositório

```bash
git clone https://github.com/victor-sysdev/biblioteca-tech.git
```

```bash
cd biblioteca-tech
```

---

# 🐍 Ambiente Virtual

## Linux

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

## Windows Git Bash

```bash
python -m venv venv
```

```bash
source venv/Scripts/activate
```

---

# 📦 Instalar dependências

```bash
pip install flask mysql-connector-python
```

---

# ▶️ Executar aplicação

```bash
python app.py
```

Servidor:

```bash
http://127.0.0.1:5000
```

---

# 🛢️ Banco de Dados

## Criar database

```sql
CREATE DATABASE IF NOT EXISTS biblioteca;
```

```sql
USE biblioteca;
```

---

# 📚 Criar tabela

```sql
CREATE TABLE IF NOT EXISTS livros (
    idlivros INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255),
    autor VARCHAR(100),
    categoria VARCHAR(100),
    preco DECIMAL(10,2)
);
```

---

# 🧹 Limpar dados

```sql
DELETE FROM livros;
```

---

# 🔄 Resetar AUTO_INCREMENT

```sql
ALTER TABLE livros AUTO_INCREMENT = 1;
```

---

# 📥 Inserir livros

```sql
INSERT INTO livros (nome, autor, categoria, preco)
VALUES 
('Computer Networking: A Top-Down Approach', 'James Kurose', 'Redes', 250.00),

('CCNA 200-301 Official Cert Guide', 'Cisco', 'Redes', 220.00),

('How Linux Works', 'Brian Ward', 'Linux', 180.00),

('The Linux Command Line', 'William Shotts', 'Linux', 170.00),

('Web Application Hackers Handbook', 'Dafydd Stuttard', 'Cyber Security', 210.00),

('Hacking: The Art of Exploitation', 'Jon Erickson', 'Cyber Security', 190.00),

('Practical Malware Analysis', 'Michael Sikorski', 'Cyber Security', 240.00),

('Clean Code', 'Robert C. Martin', 'Programação', 150.00),

('Automate the Boring Stuff with Python', 'Al Sweigart', 'Python', 130.00),

('English Grammar in Use', 'Raymond Murphy', 'Inglês', 120.00),

('Technical English for Computers and the Internet', 'Unknown', 'Inglês Técnico', 140.00);
```

---

# 🔎 Mostrar livros

```sql
SELECT * FROM livros;
```

---

# 💲 Atualizar preço

```sql
UPDATE livros
SET preco = 250.00
WHERE idlivros = 1;
```

---

# ❌ Deletar livro

```sql
DELETE FROM livros
WHERE idlivros = 1;
```

---

# 🔍 Pesquisa

O sistema permite pesquisar por:

- Nome
- Autor
- Categoria

---

# 📖 Funcionalidades

- [x] Integração Flask + MySQL
- [x] Pesquisa dinâmica
- [x] Frontend HTML/CSS
- [x] Sistema CRUD parcial
- [ ] Login
- [ ] API REST
- [ ] Painel Admin
- [ ] Docker

---

# 🔐 Futuras Implementações

- SQL Injection Lab
- XSS
- CSRF
- Broken Authentication

---

# 👨‍💻 Desenvolvedor

Victor Merencio

GitHub:
https://github.com/victor-sysdev
