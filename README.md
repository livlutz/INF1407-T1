# Primeiro trabalho de Programção para a web (INF1407) de 2025.2

![Contributors](https://img.shields.io/github/contributors/livlutz/INF1407-T1)
![Python](https://img.shields.io/badge/python-3670A0?style=plastic&logo=python&logoColor=ffdd54)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=plastic&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/css-%231572B6.svg?style=plastic&logo=css3&logoColor=white)
![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=plastic&logo=gnu-bash&logoColor=white)

## 🤝 Membros da Dupla

* **Lívia Lutz dos Santos** - 2211055
* **Luiza Marcondes Paes Leme** - 2210275



## Receitinhas da Vovó
Este é um projeto de um site de receitas. Neste site, os usuarios podem:

* Ver receitas públicas postadas por outros usuarios
* Fazer seu cadastro no sistema informando nome de usuário, email e uma senha
* Adicionar receitas tanto públicas (permitindo que outros usuários a vejam) quanto privadas (criando a receita apenas para visualização própria)


# ⚙️ Configuração do Ambiente

Para rodar este projeto, é necessário configurar um **ambiente virtual (venv)**.

Com o intuito de facilitar a configuração do ambiente, apenas rode o script run.sh no terminal da seguinte forma:

```bash
    ./run.sh
```

Ou, alternativamente, siga os passos abaixo para configurar e executar o projeto:

* **Crie o ambiente virtual**:
    ```bash
    python -m venv venv
    ```

* **Ative o ambiente virtual**:
    ```bash
    source venv/bin/activate
    ```

* **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```

* **Verifique a instalação e a versão do Django**:
    ```bash
    django-admin --version
    ```

* **Mude para o diretório onde o manage.py está**:
    ```bash
    cd site-receitas/
    ```

* **Aplique as migrações do banco de dados**:
    ```bash
    python manage.py migrate
    ```

* **Execute o servidor de desenvolvimento**:
    ```bash
    python manage.py runserver
    ```

Após executar este comando, você poderá acessar o site em `http://127.0.0.1:8000/` no seu navegador, ou ir na aba Portas do terminal e clicar no link da porta 8000, ou clicar no pop up que aparecerá no canto direito inferior da tela no botão "Abrir no navegador"

# ❗Quando mudanças que afetam o banco de dados forem realizadas (Mudanças nos modelos), siga os seguintes passos:

* **Após adicionar classes no models.py**:
    ```bash
    python manage.py makemigrations
    ```
    e depois

    ```bash
    python manage.py migrate
    ```