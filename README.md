# Receitinhas da Vovó
## Primeiro trabalho de Programação para a Web (INF1407) - 2025.2

![Contributors](https://img.shields.io/github/contributors/livlutz/INF1407-T1)
![Python](https://img.shields.io/badge/python-3670A0?style=plastic&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=plastic&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=plastic&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/css-%231572B6.svg?style=plastic&logo=css3&logoColor=white)
![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=plastic&logo=gnu-bash&logoColor=white)

## 👥 Membros da Dupla

| Nome | Matrícula |
|------|-----------|
| **Lívia Lutz dos Santos** | 2211055 |
| **Luiza Marcondes Paes Leme** | 2210275 |

---

## Escopo do Projeto

Receitinhas da Vovó é uma plataforma web completa para compartilhamento de receitas culinárias, desenvolvida com Django. O projeto implementa um sistema de gerenciamento de receitas.

### 🌟 O que funcionou

#### Deploy

O site está disponível em https://livialuiza.pythonanywhere.com/

link do vídeo do youtube usado como tutorial para fazer o deploy no pythonanywhere : https://www.youtube.com/watch?v=xtnUwvjOThg

##### Email no terminal
Em deploy, o email é enviado para o terminal e aparece no log em https://www.pythonanywhere.com/user/livialuiza/files/var/log/livialuiza.pythonanywhere.com.server.log (acessado apenas com login)

#### Sistema de Usuários
- ✅ Cadastro de usuários 
- ✅ Sistema de login e logout
- ✅ Perfil personalizado com foto de perfil
- ✅ Edição de dados pessoais
- ✅ Esqueci minha senha com email enviado no terminal
- ✅ Exclusão de conta com confirmação

#### Gerenciamento de Receitas
- ✅ Criação de receitas
- ✅ Controle de visibilidade (público/privado)
- ✅ Edição de receitas
- ✅ Exclusão de receitas com confirmação
- ✅ Visualização detalhada de receitas

#### Interface e Experiência
- ✅ Navegação intuitiva entre páginas (Nav-bar com autenticação)
- ✅ Formulários com validação
- ✅ Feedback visual para ações do usuário

---

## O que não funcionou

- Conforme as especificações do trabalho no enunciado, não houve nenhuma funcionalidade que testamos e não funcionou


## 🚀 Instalação e Configuração Local

### Instalação Automática

```bash
./run.sh
```

### Instalação Manual

- **Crie o ambiente virtual**:

    ```bash
    python -m venv venv
    ```

- **Ative o ambiente virtual**:

    ```bash
    source venv/bin/activate
    ```

- **Instale as dependências**:

    ```bash
    pip install -r requirements.txt
    ```

- **Navegue para o diretório do projeto**:

    ```bash
    cd site_receitas/
    ```

- **Aplique as migrações do banco de dados**:

    ```bash
    python manage.py migrate
    ```

- **Execute o servidor de desenvolvimento**:

    ```bash
    python manage.py runserver
    ```

Após executar este comando, você poderá acessar o site em `http://127.0.0.1:8000/` no seu navegador.

---

## 📚 Manual do Usuário

### 🏠 Página Inicial
A página inicial apresenta todas as receitas públicas disponíveis e botões de homepage, login e cadastro.

### 👤 Sistema de Usuários

#### Cadastro de Novo Usuário
1. Clique em **"Cadastrar"** no menu superior
2. Preencha os campos obrigatórios:
   - Nome de usuário
   - Email
   - Senha
   - Confirmação
3. Opcionalmente, adicione uma foto de perfil
4. Clique em **"Cadastrar"** para criar a conta

#### Login
1. Clique em **"Login"** no menu superior
2. Insira seu email e senha
3. Clique em **"Login"** para acessar sua conta
4. Caso tenha esquecido sua senha ou errado sua senha, clique em **Esqueceu a senha?** (O email de recuperação é enviado para o terminal)
5. Caso não tenha uma conta, clique em **Cadastre-se!** 

#### Gerenciamento de Perfil
- **Perfil**: Acesse através do menu superior após fazer login
- **Editar Dados**: Clique em "Atualizar Perfil" no seu perfil para modificar informações
- **Deletar Conta**: Clique em "Deletar Conta" para deletar sua conta com confirmação
- **Trocar senha**: Clique em "Trocar Senha" para trocar a senha da sua conta
- **Ver receitas**: Clique em "Minhas Receitas" para ver as receitas criadas pelo seu usuário, incluindo as privadas - Você pode clicar em cada receita para vê-la, editar ou excluir
- **Criar receitas**: Clique em "Criar Receita" para criar uma receita
- **Esqueci a senha**: Clique no link na página de perfil, coloque seu email no campo designado e veja a mensagem no terminal. O link gerado no **href** deve ser copiado da seguinte forma no seu navegador: 
Copie o link que aparece a partir de **/password_reset_confirm** (incluso) e cole depois da url da home.

### 🍳 Gerenciamento de Receitas

#### Criar Nova Receita
1. Faça login na sua conta
2. Clique em **"Criar Receita"**
3. Preencha todos os campos obrigatórios:
   - Nome da receita
   - Ingredientes 
   - Modo de preparo 
   - Tempo de preparo (em minutos)
   - Número de porções
   - Categoria
4. Defina a visibilidade (Pública ou Privada)
5. Opcionalmente, adicione uma foto da receita (No momento adicionar a foto não muda a visualização do campo no formulário, mas é possível remover ou trocar a foto depois na edição da receita)
6. Clique em **"Salvar"** para publicar

#### Visualizar Receitas
- **Receitas Próprias**: Acesse através do seu perfil
- **Receitas Públicas**: Disponíveis na página inicial (incluindo as suas públicas)
- **Detalhes**: Clique no nome de qualquer receita para ver informações completas

#### Editar Receitas
1. Acesse sua receita através do perfil ou a partir da homepage clicando em receitas cujo autor é o seu usuário
2. Clique no botão **"Editar"**
3. Modifique os campos desejados
4. Salve as alterações

#### Excluir Receitas
1. Acesse sua receita
2. Clique no botão **"Excluir"**
3. Confirme a exclusão (ação irreversível)

### 🔒 Controle de Privacidade
- **Receitas Públicas**: Visíveis para todos os usuários
- **Receitas Privadas**: Visíveis apenas para o autor

### 🔧 Testes Realizados

#### Testes de Funcionalidade
- ✅ Cadastro de múltiplos usuários com dados válidos e inválidos
- ✅ Login com credenciais corretas e incorretas
- ✅ Criação de receitas com diferentes combinações de campos
- ✅ Upload de imagens
- ✅ Edição e exclusão de receitas próprias
- ✅ Tentativa de acesso a receitas privadas de outros usuários

#### Testes de Interface
- ✅ Validação visual de formulários
- ✅ Carregamento e exibição de imagens

#### Testes de Segurança
- ✅ Prevenção de acesso não autorizado a páginas protegidas
- ✅ Validação de permissões para edição/exclusão

---

## 🔄 Instruções para Manutenção

### Atualizações do Banco de Dados

Quando mudanças que afetam o banco de dados forem realizadas:

```bash
python manage.py makemigrations
python manage.py migrate
```
