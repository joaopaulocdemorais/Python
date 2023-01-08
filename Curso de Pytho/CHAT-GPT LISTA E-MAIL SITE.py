import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Inicie a lista de URLs a serem visitadas
urls_to_visit = ['https://aciapporangatu.com.br/']

# Crie uma lista para armazenar os endereços de e-mail encontrados
emails = []

# Enquanto houver URLs na lista de URLs a serem visitadas
while len(urls_to_visit) > 0:
    # Remova o primeiro URL da lista
    url = urls_to_visit.pop(0)

    # Faça a solicitação da página
    page = requests.get(url)

    # Crie um objeto BeautifulSoup para análise da página
    soup = BeautifulSoup(page.text, 'html.parser')

    # Encontre todos os endereços de e-mail na página
    new_emails = soup.find_all(string=re.compile(r'[\w\.-]+@[\w\.-]+'))

    # Adicione os endereços de e-mail encontrados à lista de endereços de e-mail
    emails.extend(new_emails)

    # Encontre todos os links na página
    links = soup.find_all('a')

    # Adicione os links ao final da lista de URLs a serem visitadas
    for link in links:
        link_url = link.get('href')
        if link_url is not None:
            link_url = urljoin(url, link_url)
            if urlparse(link_url).netloc == 'www.example.com':
                urls_to_visit.append(link_url)

# Imprima os endereços de e-mail encontrados
for email in emails:
    print(email)
