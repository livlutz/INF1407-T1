# Primeiro trabalho de Programção para a web (INF1407) 2025.2

## Receitinhas de Vovó
Este é um projeto de um site de receitas, desenvolvido com Django. add descricao melhor depois

## 🤝 Membros da Dupla

* **Lívia Lutz dos Santos** - 2211055
* **Luiza Marcondes Paes Leme** - 2210275

# ⚙️ Configuração do Ambiente

Para rodar este projeto, você precisará configurar um **ambiente virtual (venv)**.

### ❗Observação
O projeto foi desenvolvido em ambiente Linux por meio do Github Codespaces.

Nome do ambiente virtual: `venv`

---

## Comandos Úteis

Siga os passos abaixo para configurar e executar o projeto:

* **Crie o ambiente virtual**:
    ```bash
    python -m venv venv
    ```

* **Ative o ambiente virtual**:
    ```bash
    source venv/bin/activate
    ```

* **Instale as dependências (incluindo o Django)**:
    ```bash
    pip install -r requirements.txt
    ```

* **Verifique a instalação e a versão do Django**:
    ```bash
    django-admin --version
    ```

* **Se for a primeira vez, crie a estrutura inicial do projeto**:
    ```bash
    django-admin startproject receitas_website
    ```

* **Se for a primeira vez, crie a aplicação `receitas`**:
    ```bash
    python manage.py startapp receitas
    ```

* **Aplique as migrações do banco de dados**:
    ```bash
    python manage.py migrate
    ```

* **Execute o servidor de desenvolvimento**:
    ```bash
    python manage.py runserver
    ```

Após executar este comando, você poderá acessar o site em `http://127.0.0.1:8000/` no seu navegador.