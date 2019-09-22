bash:
	# Entra no container
	docker-compose exec notebook bash

requirements:
	# Verifica os pacotes instalados.
	docker-compose exec notebook pip freeze

update:
	# Atualiza os pacotes no requirements
	docker-compose exec notebook pip freeze > requirements.txt

install:
	# Adiciona um novo pacote
	docker-compose exec notebook pip install ${package}
	docker-compose exec notebook pip freeze > requirements.txt

remove:
	# Remove um pacote existente
	docker-compose exec notebook pip uninstall ${package}
	docker-compose exec notebook pip freeze > requirements.txt
