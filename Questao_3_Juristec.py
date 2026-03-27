import pandas as pd

dados_extraidos = {
    'id_processo': [101, 102, None, 104, 105],
    'valor_causa': ['R$ 1.500,00', '2000', 'R$ 350,50', '5000.00', None],
    'status': ['Ativo', 'encerrado', 'ATIVO', 'Arquivado', 'Ativo'],
    'estado': ['SP', 'RJ', 'sp', 'MG', 'SP']
}

df = pd.DataFrame(dados_extraidos)

# Remove IDs nulos
df = df.dropna(subset=['id_processo'])

# Garante que id_processo é inteiro
df['id_processo'] = df['id_processo'].astype(int)

# Padroniza status
df['status'] = df['status'].str.capitalize()

# Função para limpar valores monetários corretamente
def limpar_valor(valor):
    if pd.isna(valor):
        return None
    
    valor = valor.replace('R$', '').strip()
    
    # Formato brasileiro
    if ',' in valor:
        valor = valor.replace('.', '').replace(',', '.')
    
    return float(valor)

df['valor_causa'] = df['valor_causa'].apply(limpar_valor)