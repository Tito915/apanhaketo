from pytrends.request import TrendReq
import pandas as pd

# Conectar ao Google Trends
pytrends = TrendReq(hl='en-US', tz=360)

# Lista de produtos a pesquisar
product_list = ["produto1", "produto2", "produto3", ..., "produto100"]  # Substitua por uma lista real de produtos

# Dicionário para armazenar o interesse total de cada produto
interest_dict = {}

# Iterar sobre a lista de produtos
for product in product_list:
    pytrends.build_payload([product], timeframe='now 15-d', geo='US-NY')
    data = pytrends.interest_over_time()
    
    if not data.empty:
        # Somando o interesse total nos últimos 15 dias
        total_interest = data[product].sum()
        interest_dict[product] = total_interest

# Converter o dicionário em DataFrame
df = pd.DataFrame(list(interest_dict.items()), columns=['Product', 'Interest'])
df = df.sort_values(by='Interest', ascending=False)

# Mostrar os 100 produtos mais pesquisados
print(df.head(100))