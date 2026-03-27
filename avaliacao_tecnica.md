## Case Técnico - Estágio em desenvolvimento | Juristec|

Olá!

Parabéns por ter sido selecionado para a etapa de análise técnica.

Este desafio foi pensado para entendermos melhor como você resolve problemas, organiza seu código e trabalha com dados e desenvolvimento no dia a dia.

### Instruções

- **Prazo de entrega:** até o dia 27/03/2026 às 23:59:59
- **Formato da entrega:** repositório público no GitHub
- **Linguagem:** Python (versão 3.10 ou superior)

Envie o link do repositório para: vinicius.s@juristecplus.com

**Importante:** Não esperamos e nem queremos perfeição. Queremos entender o seu raciocínio. Logo, quanto mais claro e mais estruturado o seu código (quando se aplica), melhor. Se não conseguir finalizar alguma parte, explique a sua abordagem.

### O desafio
O desafio é composto por seis atividades baseadas em situações reais que enfrentamos no cotidiano da Juristec.

#### Questão 1
Você escreveu um script de Web Scraping utilizando *Requests* que parou de funcionar. Você constatou as seguintes questões:
- A tabela de dados não aparece mais no HTML retornado. Ao abrir o site no seu navegador normalmente, a tabela demora uns 2 segundo para aparecer na tela.
- Após você tentar rodar o script algumas vezes para testar, o site começou a bloquear suas requisições e retornar o erro 403 para a sua máquina.

Explique, em texto (não é necessário código, apenas a lógica), como você investigaria e resolveria esses dois problemas de forma autônoma. Quais ferramentas, bibliotecas Python ou estratégias você utilizaria para contornar essa situação? Por quê?

### Questão 2
Construa uma classe em Python que represente uma televisão. Deve ser possível:
- Alterar os canais
- Alterar o volume
- Alternar a função 'mudo'

### Questão 3
Suponha que, após uma extração de dados jurídicos, você recebeu o seguinte dicionário com dados 'sujos' e inconsistentes:
```python
dados_extraidos = {
    'id_processo': [101, 102, None, 104, 105],
    'valor_causa': ['R$ 1.500,00', '2000', 'R$ 350,50', '5000.00', None],
    'status': ['Ativo', 'encerrado', 'ATIVO', 'Arquivado', 'Ativo'],
    'estado': ['SP', 'RJ', 'sp', 'MG', 'SP']
}
```

Escreva um código utilizando a biblioteca pandas que:
- Transforme esse dicionário em um DataFrame
- Remova as linhas onde o id_processo for nulo
- Padronize a coluna status para que todas as palavras fiquem com a primeira letra maiúscula
- Limpe a coluna valor_causa, convertendo todos os valores para o tipo numérico

### Questão 4
Considere o seguinte cenário relacional com duas tabelas: clientes e processos.

**Tabela clientes:** id_cliente (INT, PK), nome (VARCHAR), estado (VARCHAR)

**Tabela processos:** id_processo (INT, PK), id_cliente (INT, FK), assunto (VARCHAR), data_abertura (DATE)

**Observação:** considere que no banco existem clientes cadastrados que ainda não possuem nenhum processo vinculado.

Escreva uma query em SQL puro (padrão Postgres ou MySQL) que retorne o nome do cliente, o assunto do processo e a data_abertura, mas apenas para os processos que foram abertos no ano de 2023 e cujos clientes sejam do estado de São Paulo ('SP')

**Importante:** a sua query deve garantir que clientes sem processos **não** apareçam no resultado final

Adicione um arquivo .sql no GitHub com a resposta desse exercício.

### Questão 5
Para integrar nossa aplicação Python com o banco de dados, usamos ORMs e bancos não relacionais. Escolha UMA das opções abaixo para responder (A ou B):
- **Opção A (SQLAlchemy):** Utilizando o SQLAlchemy no Python, escreva o código que define as classes (Models) para as tabelas clientes e processos descritas na Questão 3.
- **Opção B (Firestore):** Como você estruturaria (modelaria) esses mesmos dados de Clientes e Processos em um banco de dados orientado a documentos como o Firestore? Descreva a estrutura em formato JSON.

Caso opção A: Adicione um arquivo .py com os modelos no github.

Caso opção B: Adicione um arquivo .json com a estrutura do banco.

### Questão 6
Através do site do INMET (https://portal.inmet.gov.br), construa uma função (ou classe) que, dado o nome de um município e a sigla de seu estado (Ex: Belo Horizonte, MG), colete dados de medições de temperatura e umidade relativa do dia atual, retornando um dicionário cujas chaves são a hora do dia no padrão “HH:MM” e os valores, tuplas no padrão “(T, U)”, onde “T” é a temperatura e “U” a umidade.

## Critérios de avaliação

O que vamos observar na sua entrega:
- Organização do código
- Lógica de programação
- Domínio das ferramentas
- Fundamentos de banco de dados
- Capacidades analítica

Desejamos boa sorte na resolução das atividades. Estamos ansiosos para ver o seu código.