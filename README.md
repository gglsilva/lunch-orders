# Django Boilerplate v.2

Este projeto trata-se de um boilerplate django, com as principais ferramentas usadas em conjunto com django, rodando em containers docker.

## Começando

Estas instruções fornecerão uma cópia do projeto em execução em sua máquina local para fins de desenvolvimento e teste. Consulte implantação para obter notas sobre como implantar o projeto em um sistema ativo.

### Pré-requisitos

As coisas que você precisa antes de instalar o software.

* Docker

### Instalação

O sistema foi desenvolvido no ambiente linux, mas você pode seguir um processo semelhante em outro sistema operacional.

1. Crie um diretório raiz do projeto em sua máquina local
```bash
mkdir <project_name> 
```

2. Clone o projeto neste diretório <project_name> (você também pode usar o ssh)
```bash
cd <project_name>
git clone https://github.com/gglsilva/boilerplate-v2.0.git
```

3. Crie um arquivo chamado .env 
```bash
python3 backend/contrib/eng_gen.py 
```

4. Inicie o projeto rodando o docker
```bash
docker-compose up --build
```

4.1 Caso seja necessario execute o comando como super user
```bash
sudo docker-compose up --build
```


## Uso

Alguns exemplos de comandos e/ou tarefas úteis.

Manage makemigrations
```bash
docker-compose run --rm web python manage.py makemigrations
```

Manage migrate
```bash
docker-compose run --rm web python manage.py migrate
```

Manage create super user
Manage migrate
```bash
docker-compose run --rm web python manage.py createsuperuser
```

## Implantação

Notas adicionais sobre como implantar isso em um sistema ativo ou de lançamento. Explicando os ramos mais importantes, quais pipelines eles acionam e como atualizar o banco de dados (se houver algo especial).

### Server

* Gunicorn:
* Nginx:


### Branches

* main:
