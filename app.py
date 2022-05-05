# programa que busca as informações em html dos sites
# import requests
# pagina_html = urlopen("https://sempreupdate.com.br")
# print(pagina_html.read())#
#
#
# from urllib.error import HTTPError, URLError
import requests
# from urllib.request import urlopen
# from bs4 import BeautifulSoup

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
# pagina_html = urlopen("http://www.sempreupdate.com.br")
# objeto_site = BeautifulSoup(pagina_html.read(), "html.parser")
# for link in objeto_site.find_all('a'):
#     print(link.get('href'))

# # Para tratamento de erros causados em momento de requisição devem ser tratados pelo programa
# pagina_html = urlopen("http://www.sempreupdate.com.br")
# print(f'HTML - {pagina_html}')
#
# try:
#     pagina_html = urlopen("http://www.udemy.com/erro")
#     print(f'HTML - {pagina_html}')
# except HTTPError as erro:
#     print(erro)
#
# # Em vez de algum erro ser apresentando pelo servidor, o erro for na URL,
# # existirá outra a classe URLError da biblioteca urllib
#
# try:
#     pagina_html = urlopen("http://www.abracaadabra.com")
#     print(f'HTML - {pagina_html}')
# except URLError as erro:
#     print(erro)


# Erros também podem ser gerados na tag pesquisa no site. Caso isso aconteça,
# o retorno será none. Mas, se dentro dessa tag for pesquisado um atributo inexistente,
# será lançada uma exceção de atributo. -   print(objeto_site.h4.div)
# AttributeError: 'NoneType' object has no attribute 'div'
# pagina_html = urlopen("http://www.sempreupdate.com.br")
# objeto_site = BeautifulSoup(pagina_html.read(), "html.parser")
# print(objeto_site.h4)
#
# # Colocando dentro de uma exceção:
# try:
#     print(objeto_site.h4.div)
# except AttributeError as erro:
#     print("Erro no atributo")




# # Testando o site da Scielo.org
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# pagina_html = urlopen("https://search.scielo.org/")
# objeto_site = BeautifulSoup(pagina_html, "html.parser")
# print(objeto_site.form)
# # print(objeto_site.find_all(form))
#
