import random
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

a, n, lis = 'ABCDEFG', 0, []
	
google = webdriver.Chrome('C:/Users/User/Documents/Coisas/software/chromedriver.exe')
google.get('http://127.0.0.1:5000/')

while len(lis) < 60:

	m = 0
	while m < 2:

		c = random.sample(a, 4)
		c = c[0] + c[1] + c[2] + c[3]
		if c not in lis:

			time.sleep(2)
			google.find_element_by_id('sub_new').submit()
			time.sleep(2)

			itens = ['n','sn', 'i', 'p', 'a', 'l', 'ps']
			numerico = ['i', 'p', 'a']
			for item in itens:
				if item in numerico:
					id_n = google.find_element_by_id(item)
					id_n.send_keys(random.randint(1,10))
				else:	
					id_p = google.find_element_by_id(item)
					id_p.send_keys(str(c))

			time.sleep(2)

			google.find_element_by_id('sub_novo').submit()

			lis.append(c)
			m = m + 1

		else:
			pass

	time.sleep(2)

	usuario = random.sample(lis, 1)
	login = ['login_tela', 'password_tela']
	for itens in login:

		id_l = google.find_element_by_id(itens)
		id_l.send_keys(str(usuario[0]))

	google.find_element_by_id('sub_logi').submit()
	
	lista_escolha = [0,1]
	escolha = random.sample(lista_escolha, 1)

	if escolha[0] == 0:
		google.find_element_by_id('sair').submit()
	else:

		google.find_element_by_id('conf').submit()
		time.sleep(2)
		lista_escolha_1 = [0,1]
		escolha1 = random.sample(lista_escolha_1, 1)

		if escolha1[0] == 0:

			d = random.sample(a, 4)
			d = d[0] + d[1] + d[2] + d[3]
			novo_user = ['novo', 'senha1', 'senha2']

			for itens in novo_user:
				id_new = google.find_element_by_id(itens)
				id_new.send_keys(str(d))

			time.sleep(2)
			google.find_element_by_id('troca').submit()
			time.sleep(2)
			google.switch_to.alert.accept()
			lis.remove(usuario[0])
			lis.append(d)
			time.sleep(2)

		else:
			
			google.find_element_by_id('del').submit()
			time.sleep(2)
			google.switch_to.alert.accept()
			time.sleep(2)
			google.switch_to.alert.accept()
			lis.remove(usuario[0])
			time.sleep(2)
