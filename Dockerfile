#################################
### STAGE 1: Build do projeto ###
#################################

# Cria a imagem do python3
FROM python:3.6 as builder

# Remove o delay do log
ENV PYTHONUNBUFFERED 1

# Instala algumas dependências do sistema operacional
RUN apt-get update && pip3 install --upgrade pip && apt-get install -y \
    pandoc \
    texlive-xetex \
    texlive-fonts-recommended \
    texlive-generic-recommended

# Cria a pasta notebook dentro do docker
RUN mkdir /notebook

# Faz a pasta notebook ser o diretorio principal
WORKDIR /notebook

# Adiciona os requirements dentro da pasta notebook
ADD ./requirements.txt /notebook

# Instala as dependências
RUN pip3 install -r requirements.txt

# Insere tudo dentro da pasta notebook
ADD . /notebook

# Roda o script para popular a pasta htmls
RUN python3 convert.py

#########################################
### STAGE 2: Configuração do Servidor ###
#########################################

# Inserindo a imagem do NGINX
FROM nginx:latest

#Removando arquivo de configuração default do nginx
RUN rm -rf /etc/nginx/conf.d/*

# Copiando o arquivo de configuração do nginx para dentro do container
COPY ./nginx.conf /etc/nginx/conf.d/nginx.conf

# Removendo a página default do nginx
RUN rm -rf /usr/share/nginx/html/*

# Do container 'builder' pegar os artefatos da pasta dist e inserindo dentro do repositorio do nginx
# para que elas sejam servidas
COPY --from=builder /notebook/htmls /usr/share/nginx/html

# Exportando a porta 80
EXPOSE 80

# Rodando o servidor
CMD ["nginx", "-g", "daemon off;"]
