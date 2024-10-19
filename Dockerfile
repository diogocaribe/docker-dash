FROM python:3.12-slim

# Copiando todo o projeto para a imagem
COPY . /docker_dash

# Instalar dependências necessárias
RUN apt-get update

# Instalar o Poetry
RUN pip3 install poetry

WORKDIR /docker_dash

RUN poetry config virtualenvs.create false

# Instale as dependências do projeto usando o Poetry
RUN poetry install --no-dev

CMD ["gunicorn", "-b", "0.0.0.0:8050", "docker_dash.app:server", "--timeout", "1200"]
