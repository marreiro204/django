# Deploy de Projeto Django no PythonAnywhere

Este guia mostra como fazer o deploy de um projeto Django no PythonAnywhere passo a passo.

---

## Pré-requisitos

* Conta no [PythonAnywhere](https://www.pythonanywhere.com/)
* Projeto Django pronto no GitHub
* Git instalado no seu computador (opcional, caso faça deploy via Git clone)
* Conhecimento básico em Django

---

## Passo 1: Criar uma conta e login

1.  Crie uma conta gratuita ou faça login no [PythonAnywhere](https://www.pythonanywhere.com/).
2.  Após o login, você será direcionado ao **Dashboard**.

---

## Passo 2: Clonar o projeto no PythonAnywhere

1.  Vá para a aba **Files**.
2.  Abra um **Bash console** (na aba **Consoles**).
3.  Clone seu repositório do GitHub.

    Exemplo:
    ```bash
    git clone [https://github.com/seu_usuario/seu_repositorio.git](https://github.com/seu_usuario/seu_repositorio.git)
    ```

    Entre na pasta do projeto:
    ```bash
    cd nome_da_sua_pasta
    ```

---

## Passo 3: Criar e ativar o virtual environment

1.  Crie um virtualenv para seu projeto:
    ```bash
    python3.11 -m venv myvenv
    ```

2.  Ative o ambiente virtual:
    ```bash
    source myvenv/bin/activate
    ```

3.  Instale as dependências do seu projeto:
    ```bash
    pip install -r requirements.txt
    ```

---

## Passo 4: Configurar o Django

1.  Abra o arquivo `settings.py` do seu projeto.

2.  Adicione a configuração do **STATIC_ROOT**:
    ```python
    import os

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    ```

3.  Configure o **ALLOWED_HOSTS** com seu domínio do PythonAnywhere:
    ```python
    ALLOWED_HOSTS = ['seu_usuario.pythonanywhere.com']
    ```

4.  Colete os arquivos estáticos:
    ```bash
    python manage.py collectstatic
    ```

---

## Passo 5: Criar o Web App no PythonAnywhere

1.  Vá para a aba **Web** e clique em **Add a new web app**.
2.  Escolha **Manual configuration** → **Python 3.x**.

3.  Configure o path do **WSGI**:
    * Exemplo: `/home/seu_usuario/seu_projeto/seu_projeto/wsgi.py`

4.  Configure o virtualenv:
    * Exemplo: `/home/seu_usuario/seu_projeto/myvenv/`

---

## Passo 6: Configurar arquivos estáticos no PythonAnywhere

1.  Ainda na aba **Web**, vá até **Static files**.
2.  Configure:

    | URL        | Directory                            |
    | ---------- | ------------------------------------ |
    | /static/   | /home/seu_usuario/seu_projeto/staticfiles |

3.  Salve as alterações e clique em **Reload** para aplicar.

---

## Passo 7: Testar o site

1.  Abra seu navegador e acesse:
    ```
    https://seu_[usuario.pythonanywhere.com/](https://usuario.pythonanywhere.com/)
    ```

2.  Seu site Django deve estar funcionando com os arquivos CSS carregados.

 veja o projeto em funcionamento [aqui](https://matheus23.pythonanywhere.com).

