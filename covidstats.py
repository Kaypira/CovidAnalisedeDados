import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-cities.csv"
dados_covid = pd.read_csv(url)

cidade_mais_casos = dados_covid.loc[dados_covid['totalCases'].idxmax()]['city']

cidade_menos_casos = dados_covid.loc[dados_covid['totalCases'].idxmin()]['city']

estado_mais_casos = dados_covid.groupby('state')['totalCases'].sum().idxmax()

estado_menos_casos = dados_covid.groupby('state')['totalCases'].sum().idxmin()

cidade_mais_mortes = dados_covid.loc[dados_covid['deaths'].idxmax()]['city']

cidade_menos_mortes = dados_covid.loc[dados_covid['deaths'].idxmin()]['city']

estado_mais_mortes = dados_covid.groupby('state')['deaths'].sum().idxmax()

estado_menos_mortes = dados_covid.groupby('state')['deaths'].sum().idxmin()

total_casos_brasil = dados_covid['totalCases'].sum()

total_mortes_brasil = dados_covid['deaths'].sum()

dados_top_mortes = dados_covid.groupby('state')['deaths'].sum().nlargest(5)
plt.bar(dados_top_mortes.index, dados_top_mortes.values)
plt.title('5 Estados com Mais Mortes por COVID-19')
plt.xlabel('Estado')
plt.ylabel('Número de Mortes')
plt.show()

dados_bottom_mortes = dados_covid.groupby('state')['deaths'].sum().nsmallest(5)
plt.bar(dados_bottom_mortes.index, dados_bottom_mortes.values)
plt.title('5 Estados com Menos Mortes por COVID-19')
plt.xlabel('Estado')
plt.ylabel('Número de Mortes')
plt.show()

print("1. Cidade com mais casos de COVID-19:", cidade_mais_casos)
print("2. Cidade com menos casos de COVID-19:", cidade_menos_casos)
print("3. Estado com mais casos de COVID-19:", estado_mais_casos)
print("4. Estado com menos casos de COVID-19:", estado_menos_casos)
print("5. Cidade com mais mortes por COVID-19:", cidade_mais_mortes)
print("6. Cidade com menos mortes por COVID-19:", cidade_menos_mortes)
print("7. Estado com mais mortes por COVID-19:", estado_mais_mortes)
print("8. Estado com menos mortes por COVID-19:", estado_menos_mortes)
print("9. Total de casos de COVID-19 no Brasil:", total_casos_brasil)
print("10. Total de mortes por COVID-19 no Brasil:", total_mortes_brasil)