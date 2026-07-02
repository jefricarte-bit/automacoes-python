import pandas as pd
from datetime import datetime

print("🔄 Starting report automation...")

dados_vendas = {
    'Produto': ['Notebook', 'Mouse Gamer', 'Teclado Mecânico', 'Monitor 24"', 'Notebook'],
    'Quantidade': [2, 5, 3, 1, 1],
    'Preco_Unitario': [3500.00, 150.00, 250.00, 900.00, 3500.00]
}

df = pd.DataFrame(dados_vendas)

df['Faturamento_Total'] = df['Quantidade'] * df['Preco_Unitario']

data_atual = datetime.now().strftime('%Y-%m-%d')
nome_arquivo = f'management_report_{data_atual}.xlsx'

df.to_excel(nome_arquivo, index=False)
print(f"📊 Report successfully generated: {nome_arquivo}")

print("📧 Report ready to be automatically sent to decision-makers!")
