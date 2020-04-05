bash:
	# Entra no container
	docker-compose exec notebook bash

requirements:
	# Verifica os pacotes instalados.
	docker-compose exec notebook pip freeze

install:
	# Adiciona um novo pacote
	docker-compose exec notebook pip install ${package}

remove:
	# Remove um pacote existente
	docker-compose exec notebook pip uninstall ${package}

convert:
	# Converte um arquivo.ipynb para html
	# html, pdf, markdown
	ipython nbconvert --to html ${file} --output-dir=htmls
