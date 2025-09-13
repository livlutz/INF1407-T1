# Primeiro trabalho de Programção para a web (INF1407) 2025.2

## Receitinhas de Vovó
Este é um projeto de um site de receitas, desenvolvido com Django. add descricao melhor depois

## 🤝 Membros da Dupla

* **Lívia Lutz dos Santos** - 2211055
* **Luiza Marcondes Paes Leme** - 2210275

# ⚙️ Configuração do Ambiente

Para rodar este projeto, você precisará configurar um **ambiente virtual (venv)**.

### ❗Observações
O projeto foi desenvolvido em ambiente Linux por meio do Github Codespaces.

A instalção do pacote Pillow será necessário para usar ImageTextField, para isso, no ambiente virtual:

```bash
    pip install Pillow
```

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

* **Aplique as migrações do banco de dados**:
    ```bash
    python manage.py migrate
    ```

* **Execute o servidor de desenvolvimento**:
    ```bash
    python manage.py runserver
    ```

Após executar este comando, você poderá acessar o site em `http://127.0.0.1:8000/` no seu navegador, ou ir na aba Ports do terminal e clicar no link da porta 8000, ou clicar no pop up que aparecerá no canto direito inferior da tela no botão "open in browser"

* ❗💀 Superusuário do Django

    Usuário : livialuiza

    email : llutz@aluno.puc-rio.br

    senha : 12345

* **Após adicionar classes no models.py**:
    ```bash
    python manage.py makemigrations
    ```
    e depois

    ```bash
    python manage.py migrate
    ```