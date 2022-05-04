# programa que busca as informações em html dos sites
# import requests
# pagina_html = urlopen("https://sempreupdate.com.br")
# print(pagina_html.read())#
#
#
from urllib.request import urlopen
from bs4 import BeautifulSoup

# pagina_html = urlopen("http://localhost:8000/teste2.html")
# objeto_site = BeautifulSoup(pagina_html.read(), "html.parser")

#
# print(objeto_site.h1)
# print(objeto_site.html.h1)
# print(objeto_site.title)

# Neste primeiro caso, apenas retorna o valor da primeira ocorrência do H1.
# Para encontrar todas as ocorrências, existe outro método.


# print(objeto_site.find_all("h2"))


# para listar os links contidos no site:
# for link in objeto_site.find_all('a'):
#     print(link)

# Porém essa abordagem não é interessante, uma vez que traz os valores com as tags.
# Para isso, usaremos método get para retornarmos apenas o links pelo href.
# for link in objeto_site.find_all('a'):
#     print(link.get('href'))


# Com isso, agora é possível retornar todos os links contidos no site Globo.com.
pagina_html = urlopen("http://www.globo.com.br")
objeto_site = BeautifulSoup(pagina_html.read(), "html.parser")
for link in objeto_site.find_all('a'):
    print(link.get('href'))

