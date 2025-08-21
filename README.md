# Deploy de Projeto Django no PythonAnywhere

Este guia mostra como fazer o deploy de um projeto Django no PythonAnywhere passo a passo.

## Pré-requisitos

- Conta no [PythonAnywhere](https://www.pythonanywhere.com/)
- Projeto Django pronto no GitHub
- Git instalado no seu computador (opcional, caso faça deploy via Git clone)
- Conhecimento básico em Django

---

## Passo 1: Criar uma conta e login

1. Crie uma conta gratuita ou faça login no [PythonAnywhere](https://www.pythonanywhere.com/).
2. Após o login, você será direcionado ao **Dashboard**.

---

## Passo 2: Clonar o projeto no PythonAnywhere

1. Vá para a aba **Files**.
2. Abra um **Bash console** (na aba **Consoles**).
3. Clone seu repositório do GitHub:

```bash

Exemplo:

git clone https://github.com/matheus23/django.git


Entre na pasta do projeto:

cd django

Passo 3: Criar e ativar o virtual environment

Crie um virtualenv para seu projeto:

python3.11 -m venv myvenv


Ative o ambiente virtual:

source myvenv/bin/activate


Instale as dependências do seu projeto:

pip install -r requirements.txt

Passo 4: Configurar o Django

Abra o arquivo settings.py do seu projeto.

Adicione a configuração do STATIC_ROOT:

import os

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


Configure o ALLOWED_HOSTS com seu domínio do PythonAnywhere:

ALLOWED_HOSTS = ['matheus23.pythonanywhere.com']


Colete os arquivos estáticos:

python manage.py collectstatic

Passo 5: Criar o Web App no PythonAnywhere

Vá para a aba Web e clique em Add a new web app.

Escolha Manual configuration → Python 3.x.

Configure o path do WSGI:
Exemplo: /home/matheus23/django/django/wsgi.py

Configure o virtualenv:
Exemplo: /home/matheus23/django/myvenv/

Passo 6: Configurar arquivos estáticos no PythonAnywhere

Ainda na aba Web, vá até Static files.

Configure:

URL	Directory
/static/	/home/matheus23/django/staticfiles

Salve as alterações e clique em Reload para aplicar.

Passo 7: Testar o site

Abra seu navegador e acesse:

https://matheus23.pythonanywhere.com/


Seu site Django deve estar funcionando com os arquivos CSS carregados.
git clone https://github.com/seu_usuario/seu_repositorio.git

