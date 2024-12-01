#!/usr/bin/python3

### SCRIPT PARA EXTRAER PRECIO DEL DOLAR ###

from bs4 import BeautifulSoup as b
import requests, warnings, os, sys, time
from colorama import Fore, Style, init
init(autoreset=True)
WHITE=f'{Fore.WHITE}{Style.BRIGHT}'
GREEN=f'{Fore.GREEN}{Style.BRIGHT}'
os.system('cls' if os.name == 'nt' else 'clear')
warnings.filterwarnings("ignore", message="Unverified HTTPS request")

mensaje='Buscando el precio de distintas monedas\nPor Favor espere...'

for letra in mensaje:
 sys.stdout.write(letra)
 sys.stdout.flush()
 time.sleep(0.04)

print('\n')


url = 'https://www.bcv.org.ve/'
moneda = []
valor = []
r = requests.get(url, verify=False)
soup = b(r.content, 'html.parser')
buscar = soup.find_all('div', class_="col-sm-6 col-xs-6")

for i in buscar:
 spans = i.find_all('span')
 for span in spans:
  moneda.append(span.get_text(strip=True))

n=1
soup = b(r.content, 'html.parser')
buscar = soup.find_all('strong')
for i in buscar:
 if n > 2:
  valor.append(i.get_text(strip=True))
 n=n+1

from bs4 import BeautifulSoup as f
url='https://www.google.com/search?q=precio+del+dolar+paralelo+actualidad&client=firefox-b-lm&sca_esv=31c6f1c3e8feaf77&ei=eYBMZ5HbD6yMwbkPn466oAE&ved=0ahUKEwjR--ia8YaKAxUsRjABHR-HDhQQ4dUDCA8&uact=5&oq=precio+del+dolar+paralelo+actualidad&gs_lp=Egxnd3Mtd2l6LXNlcnAiJHByZWNpbyBkZWwgZG9sYXIgcGFyYWxlbG8gYWN0dWFsaWRhZDIFEAAYgAQyBRAAGIAEMgUQABiABEilL1CXD1inLnACeAGQAQCYAdMGoAHDEaoBCTMtMS4xLjEuMbgBA8gBAPgBAZgCBKACmwnCAgoQABiwAxjWBBhHwgINEAAYgAQYsAMYQxiKBcICDhAAGLADGOQCGNYE2AEBwgIZEC4YgAQYsAMY0QMYQxjHARjIAxiKBdgBAcICCBAAGIAEGLEDwgIOEAAYgAQYsQMYgwEYigXCAgQQABgDmAMAiAYBkAYTugYGCAEQARgJkgcLMS4xLjAuMS4wLjGgB9sQ&sclient=gws-wiz-serp'
r = requests.get(url)
soup = f(r.content, 'html.parser')
buscar = soup.find_all('span', class_="FCUp0c rQMQod")
n=1
for i in buscar:
 if n == 1:
  paralelo=f'{WHITE}USD ={GREEN} {i.text.split()[0]} Bs'
 n=n+1

for a, b in zip(moneda, valor):
 entero, decimal = b.split(',')
 print(f"{WHITE}{a} = {GREEN}{entero},{decimal[:2]} Bs")
print(paralelo)
