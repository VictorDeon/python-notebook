install:
	# Instala uma nova dependência
	docker compose exec notebook pip3 install ${package}

remove:
	# Remove um pacote
	docker compose exec notebook pip3 uninstall ${package}

requirements:
	# Verifica todas as dependências
	docker compose exec notebook pip3 freeze

bash:
	# Entrar dentro do container
	docker compose exec notebook bash

shell:
	# Entra no shell do python
	docker compose exec notebook ipython

logs:
	# Visualiza os logs
	docker compose logs -ft notebook

packages:
	# Copiar os pacotes do docker para o localhost
	# Vai no settings.json do vscode e insere:
	# python.analysis.extraPaths": [".ignore/site-packages"]
	sudo docker cp notebook:/usr/local/lib/python3.9/site-packages .ignore