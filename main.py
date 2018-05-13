#feito por PHD
#Somente para fins de estudo
#Sistema basico
from bs4 import BeautifulSoup
import requests
#Descobrir valor dolar
link = "https://financeone.com.br/moedas/dolar-hoje/"
r = requests.get(link)
soup = BeautifulSoup(r.text, 'lxml')
dolar = soup.find('span', class_="valor")
dolarValor= dolar.next_element
dolarValor = dolarValor.replace("R$ ","")
dolarValor = dolarValor.replace(",",".")
valorDolar = float(dolarValor)

#Calcular
valor1 = float(input('Digite o valor, em dolar, que deseja saber o valor em real : '))
print ("{} dolares e correspondente a R$ {}".format(valor1,valorDolar*valor1))
