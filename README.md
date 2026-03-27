# 📌 Avaliação Técnica - Juristec+

Este repositório contém as respostas desenvolvidas para o **case técnico de estágio em desenvolvimento da Juristec+**, conforme especificado no arquivo de instruções .

O objetivo deste projeto é demonstrar habilidades em **programação, análise de dados, banco de dados e resolução de problemas reais**.

---

## 🧠 Sobre o Desafio

A avaliação é composta por **6 questões práticas**, envolvendo:

* Web Scraping e análise de problemas
* Programação orientada a objetos
* Tratamento e limpeza de dados
* SQL
* Modelagem com ORM
* Coleta de dados em tempo real (INMET)

---

## 📁 Estrutura do Repositório

```
.
├── avaliacao_tecnica.md
├── Questão 1 - Juristec+.pdf
├── Questao_2_Juristec.py
├── Questao_3_Juristec.py
├── Questao_4_Juristec.sql
├── Questao_5_Juristec.py
└── Questao_6_Juristec.py
```

---

## 📄 Descrição das Respostas

### ✅ Questão 1 – Web Scraping (Análise)

Resposta descritiva explicando:

* Identificação de conteúdo dinâmico (JavaScript)
* Uso de ferramentas como DevTools
* Estratégias com `requests`, `Playwright` e sessões HTTP
* Tratamento de bloqueios (erro 403)

📌 Arquivo: `avaliacao_tecnica.md`
📎 Exemplo de abordagem detalhada disponível em: 

---

### 📺 Questão 2 – Classe Televisão

Implementação de uma classe orientada a objetos com:

* Controle de canais válidos
* Controle de volume (com limite)
* Função de mudo com restauração do volume anterior

📌 Arquivo: `Questao_2_Juristec.py`
📎 Código disponível em: 

---

### 📊 Questão 3 – Tratamento de Dados com Pandas

Processamento de dados "sujos", incluindo:

* Conversão para DataFrame
* Remoção de valores nulos
* Padronização de texto
* Conversão de valores monetários para numérico

📌 Arquivo: `Questao_3_Juristec.py`
📎 Código disponível em: 

---

### 🗃️ Questão 4 – Query SQL

Consulta SQL que:

* Relaciona clientes e processos
* Filtra por estado (`SP`)
* Considera apenas processos de 2023
* Exclui clientes sem processos

📌 Arquivo: `Questao_4_Juristec.sql`
📎 Query disponível em: 

---

### 🏗️ Questão 5 – Modelagem com SQLAlchemy

Definição de models utilizando ORM:

* Relacionamento entre `Cliente` e `Processo`
* Uso de chaves primárias e estrangeiras
* Mapeamento objeto-relacional

📌 Arquivo: `Questao_5_Juristec.py`
📎 Código disponível em: 

---

### 🌦️ Questão 6 – Coleta de Dados do INMET

Implementação de scraping com renderização JavaScript:

* Uso de `Playwright` para páginas dinâmicas
* Extração de temperatura e umidade
* Normalização e tratamento dos dados
* Retorno estruturado em dicionário

📌 Arquivo: `Questao_6_Juristec.py`
📎 Código disponível em: 

---

## ⚙️ Tecnologias Utilizadas

* Python 3.10+
* Pandas
* Playwright
* SQL (PostgreSQL/MySQL)
* SQLAlchemy

---

## 🚀 Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Instale as dependências

```bash
pip install pandas playwright sqlalchemy
playwright install
```

### 3. Execute os scripts

Exemplo:

```bash
python Questao_6_Juristec.py
```

---

## 💡 Considerações

Durante o desenvolvimento, foi priorizado:

* Clareza de código
* Organização
* Robustez das soluções
* Adaptação a cenários reais (como scraping dinâmico e dados inconsistentes)

---

## 📬 Entrega

O link deste repositório deve ser enviado conforme instruções do desafio.
