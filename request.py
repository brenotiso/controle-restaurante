import requests
from time import sleep

def login():
	URL = "http://35.247.232.28/authentication/token/"
	data = {'username' : "breno", 
			'password' : "123"} 
	r = requests.post(url = URL, data=data) 
	data = r.json() 
	token = data['access_token']
	return token
token = login()

def get_adicionais():
	URL = "http://35.247.232.28/adicionais"
	headers = {"Authorization": "Bearer "+token}
	r = requests.get(url = URL, headers=headers)
	data = r.json() 
	print (data)
	
def get_num_adicionais():
	num = input()
	URL = "http://35.247.232.28/adicionais/"+num
	headers = {"Authorization": "Bearer "+token}
	r = requests.get(url = URL, headers=headers)
	data = r.json() 
	print (data)
	
	
def delete_adicionais():
	num = input()
	URL = "http://35.247.232.28/adicionais/"+num
	headers = {"Authorization": "Bearer "+token}
	r = requests.delete(url = URL, headers=headers)
	if r.status_code == 404:
		print("Produto nao encontrado! Não foi possivel fazer a remoção")
	else:
		print("Produto removido com sucesso")
	
def post_adicionais():
	URL = "http://35.247.232.28/adicionais"
	adicional = input()
	data = {'nome' : adicional}
	headers = {"Authorization": "Bearer "+token}
	r = requests.post(url = URL, data=data, headers=headers)
	data = r.json() 
	print (data)
	
def put_adicionais():
	num = input()
	URL = "http://35.247.232.28/adicionais/"+num
	adicional = input()
	data = {'nome' : adicional}
	headers = {"Authorization": "Bearer "+token}
	r = requests.put(url = URL, data=data, headers=headers)
	data = r.json() 
	print (data)

#get_adicionais()
#post_adicionais()
#delete_adicionais()
#put_adicionais()


#############################################
######### Metodos das Mesas #################
############################################

def get_mesas():
	URL = "http://35.247.232.28/mesas"
	headers = {"Authorization": "Bearer "+token}
	r = requests.get(url = URL, headers=headers)
	data = r.json() 
	print (data)
	
def get_num_mesas():
	num = input()
	URL = "http://35.247.232.28/mesas/"+num
	headers = {"Authorization": "Bearer "+token}
	r = requests.get(url = URL, headers=headers)
	data = r.json() 
	print (data)

def delete_mesas():
	num = input()
	URL = "http://35.247.232.28/mesas/"+num
	headers = {"Authorization": "Bearer "+token}
	r = requests.delete(url = URL, headers=headers)
	if r.status_code == 404:
		print("Mesa nao encontrada! Não foi possivel fazer a remoção")
	else:
		print("Mesa removida com sucesso")
	
def post_mesas():
	URL = "http://35.247.232.28/mesas"
	disponivel = bool(input())
	data = {'disponivel' : disponivel}
	headers = {"Authorization": "Bearer "+token}
	r = requests.post(url = URL, data=data, headers=headers)
	data = r.json() 
	print (data)
	
def put_mesas():
	num = input()
	URL = "http://35.247.232.28/mesas/"+num
	disponivel = bool(input())
	if disponivel == True:
		data = {'disponivel' : True}
	else:
		data = {'disponivel' : False}
	headers = {"Authorization": "Bearer "+token}
	r = requests.put(url = URL, data=data, headers=headers)
	data = r.json() 
	print (data)
	

#get_mesas()
#post_mesas()
#put_mesas()
#delete_mesas()


#############################################
######## Metodos das Categorias #############
############################################

def get_categorias():
	URL = "http://35.247.232.28/categorias"
	headers = {"Authorization": "Bearer "+token}
	r = requests.get(url = URL, headers=headers)
	data = r.json() 
	print (data)
	
def get_num_categorias():
	num = input()
	URL = "http://35.247.232.28/categorias/"+num
	headers = {"Authorization": "Bearer "+token}
	r = requests.get(url = URL, headers=headers)
	data = r.json() 
	print (data)

	
def delete_categorias():
	num = input()
	URL = "http://35.247.232.28/categorias/"+num
	headers = {"Authorization": "Bearer "+token}
	r = requests.delete(url = URL, headers=headers)
	if r.status_code == 404:
		print("Mesa nao encontrada! Não foi possivel fazer a remoção")
	else:
		print("Mesa removida com sucesso")
	
def post_categorias():
	URL = "http://35.247.232.28/categorias"
	nome  = input()
	descricao = input()
	adicionais = int(input())
	data = {'nome' : nome,
			'descricao' : descricao,
			'adicionais' : adicionais
			}
	headers = {"Authorization": "Bearer "+token}
	r = requests.post(url = URL, data=data, headers=headers)
	data = r.json() 
	print (data)
	
def put_categorias():
	num = input()
	URL = "http://35.247.232.28/categorias/"+num
	nome  = input()
	descricao = input()
	adicionais = int(input())
	data = {'nome' : nome,
			'descricao' : descricao,
			'adicionais' : adicionais
			}
	headers = {"Authorization": "Bearer "+token}
	r = requests.put(url = URL, data=data, headers=headers)
	data = r.json()
	print (data)
	
#get_categorias()
#post_categorias()
#put_categorias()
#delete_categorias()
	
#############################################
######## Metodos das Produtos #################
############################################

def get_produtos():
	URL = "http://35.247.232.28/produtos"
	headers = {"Authorization": "Bearer "+token}
	r = requests.get(url = URL, headers=headers)
	data = r.json() 
	print (data)
	
def get_num_produtos():
	num = input()
	URL = "http://35.247.232.28/produtos/"+num
	headers = {"Authorization": "Bearer "+token}
	r = requests.get(url = URL, headers=headers)
	data = r.json() 
	print (data)
	
def delete_produtos():
	num = input()
	URL = "http://35.247.232.28/produtos/"+num
	headers = {"Authorization": "Bearer "+token}
	r = requests.delete(url = URL, headers=headers)
	if r.status_code == 404:
		print("produto no encontrado! Não foi possivel fazer a remoção")
	else:
		print("produto removido com sucesso")
	
def post_produtos():
	URL = "http://35.247.232.28/produtos"
	nome  = input()
	descricao = input()
	preco = float(input())
	ativo = input()
	categoria = int(input())
	data = {'nome' : nome,
			'descricao' : descricao,
			'preco' : preco,
			'ativo' : ativo,
			'categoria' : categoria
			}
	headers = {"Authorization": "Bearer "+token}
	r = requests.post(url = URL, data=data, headers=headers)
	data = r.json() 
	print (data)
	
def put_produtos():
	num = input()
	URL = "http://35.247.232.28/produtos/"+num
	nome  = input()
	descricao = input()
	preco = float(input())
	ativo = input()
	categoria = int(input())
	data = {'nome' : nome,
			'descricao' : descricao,
			'preco' : preco,
			'ativo' : ativo,
			'categoria' : categoria
			}
	headers = {"Authorization": "Bearer "+token}
	r = requests.put(url = URL, data=data, headers=headers)
	data = r.json() 
	print (data)


#get_produtos()
#post_produtos()
#put_produtos()
#delete_produtos()



#############################################
#### Metodos dos detalhes do produto ########
############################################

def get_pedidos_detalhe():
	URL = "http://35.247.232.28/pedidos_detalhe"
	headers = {"Authorization": "Bearer "+token}
	r = requests.get(url = URL, headers=headers)
	data = r.json() 
	print (data)
	
def get_num_pedidos_detalhe():
	num = input()
	URL = "http://35.247.232.28/pedidos_detalhe/"+num
	headers = {"Authorization": "Bearer "+token}
	r = requests.get(url = URL, headers=headers)
	data = r.json() 
	print (data)
	
def delete_pedidos_detalhe():
	num = input()
	URL = "http://35.247.232.28/pedidos_detalhe/"+num
	headers = {"Authorization": "Bearer "+token}
	r = requests.delete(url = URL, headers=headers)
	if r.status_code == 404:
		print("produto no encontrado! Não foi possivel fazer a remoção")
	else:
		print("produto removido com sucesso")
	
def post_pedidos_detalhe():
	URL = "http://35.247.232.28/pedidos_detalhe"
	produto = int(input())
	observacao = input()
	quantidade = int(input())
	data = {'produto' : produto,
			'observacao' : observacao,
			'quantidade' : quantidade
			}
	headers = {"Authorization": "Bearer "+token}
	r = requests.post(url = URL, data=data, headers=headers)
	data = r.json() 
	print (data)
	
def put_pedidos_detalhe():
	num = input()
	URL = "http://35.247.232.28/pedidos_detalhe/"+num
	produto = int(input())
	observacao = input()
	quantidade = int(input())
	data = {'produto' : produto,
			'observacao' : observacao,
			'quantidade' : quantidade
			}
	headers = {"Authorization": "Bearer "+token}
	r = requests.put(url = URL, data=data, headers=headers)
	data = r.json() 
	print (data)


#get_pedidos_detalhe()
#post_pedidos_detalhe()
#put_pedidos_detalhe()
#delete_pedidos_detalhe()


#############################################
#### Metodos dos pedidos ########
############################################

def get_pedidos():
	URL = "http://35.247.232.28/pedidos"
	headers = {"Authorization": "Bearer "+token}
	r = requests.get(url = URL, headers=headers)
	data = r.json()
	print(data)
	return data
	

def get_pedidos_visto():
	URL = "http://35.247.232.28/pedidos?visto=false"
	headers = {"Authorization": "Bearer "+token}
	r = requests.get(url = URL, headers=headers)
	data = r.json()
	return data


def get_num_pedidos():
	num = int(input())
	URL = "http://35.247.232.28/pedidos/"+num
	headers = {"Authorization": "Bearer "+token}
	r = requests.get(url = URL, headers=headers)
	data = r.json()
	print(data)
	return data
	
def delete_pedidos():
	num = input()
	URL = "http://35.247.232.28/pedidos/"+num
	headers = {"Authorization": "Bearer "+token}
	r = requests.delete(url = URL, headers=headers)
	if r.status_code == 404:
		print("produto no encontrado! Não foi possivel fazer a remoção")
	else:
		print("produto removido com sucesso")
	
def post_pedidos():
	URL = "http://35.247.232.28/pedidos"
	mesa = int(input())
	pedido_detalhe = list(map(int, input().split(' ')))
	baixa = input()
	data = {'mesa' : mesa,
			'pedido_detalhe' : pedido_detalhe,
			'baixa' : baixa
			}
	headers = {"Authorization": "Bearer "+token}
	r = requests.post(url = URL, data=data, headers=headers)
	data = r.json() 
	print (data)
	
def put_pedidos():
	num = input()
	URL = "http://35.247.232.28/pedidos/"+num
	mesa = int(input())
	pedido_detalhe = list(map(int, input().split(' ')))
	baixa = input()
	headers = {"Authorization": "Bearer "+token}
	data = {'mesa' : mesa,
			'pedido_detalhe' : pedido_detalhe,
			'baixa' : baixa
			}
	r = requests.put(url = URL, data=data, headers=headers)
	data = r.json() 
	print (data)
	
def print_pedido(num):
	headers = {"Authorization": "Bearer "+token}
	URL = "http://35.247.232.28/pedidos/"+str(num)
	data = {'visto' : True
			}
	r = requests.patch(url = URL, data=data, headers=headers)
	data = r.json()
	print (data)
	for i in data['pedido_detalhe']:
		URL = "http://35.247.232.28/pedidos_detalhe/"+str(i)
		r = requests.get(url = URL, headers=headers)
		data = r.json()
		print (data)
		URL = "http://35.247.232.28/produtos/"+str(data['produto'])
		r = requests.get(url = URL, headers=headers)
		data = r.json()
		print (data)
	print("\n\n")

#get_pedidos()
#post_pedidos()
#put_pedidos()
#delete_pedidos()

def main():
	while(True):
		data = get_pedidos_visto()
		if data != []:
			for i in data:
				print_pedido(i['id'])
		sleep(10)

main()

