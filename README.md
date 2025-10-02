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

## 📖 Escopo do Projeto

**Receitinhas da Vovó** é uma plataforma web completa para compartilhamento de receitas culinárias, desenvolvida com Django. O projeto implementa um sistema de gerenciamento de receitas.

### 🌟 O que funcionou

#### Sistema de Usuários
- ✅ Cadastro de usuários com campos personalizados
- ✅ Sistema de login e logout
- ✅ Perfil personalizado com foto de perfil
- ✅ Edição de dados pessoais
- ✅ Exclusão de conta com confirmação

#### Gerenciamento de Receitas
- ✅ Criação de receitas com campos estruturados
- ✅ Upload de imagens para receitas
- ✅ Controle de visibilidade (público/privado)
- ✅ Edição completa de receitas existentes
- ✅ Exclusão de receitas com confirmação
- ✅ Visualização detalhada de receitas

#### Interface e Experiência
- ✅ Design responsivo e moderno
- ✅ Tema escuro com elementos visuais atraentes
- ✅ Navegação intuitiva entre páginas
- ✅ Formulários com validação
- ✅ Feedback visual para ações do usuário

---

## O que não funcionou

- Conforme as especificações do trabalho no enunciado, não houve nenhuma funcionalidade que testamos e não funcionou


## 🚀 Instalação e Configuração

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
A página inicial apresenta todas as receitas públicas disponíveis na plataforma. Os usuários podem:
- Visualizar receitas em cards organizados
- Navegar entre receitas sem necessidade de login
- Acessar detalhes completos de cada receita

### 👤 Sistema de Usuários

#### Cadastro de Novo Usuário
1. Clique em **"Cadastrar"** no menu superior
2. Preencha os campos obrigatórios:
   - Nome de usuário (único)
   - Email
   - Senha e confirmação
3. Opcionalmente, adicione uma foto de perfil
4. Clique em **"Cadastrar"** para criar a conta

#### Login
1. Clique em **"Entrar"** no menu superior
2. Insira seu nome de usuário e senha
3. Clique em **"Entrar"** para acessar sua conta

#### Gerenciamento de Perfil
- **Visualizar Perfil**: Acesse através do menu superior após fazer login
- **Editar Dados**: Clique em "Editar" no seu perfil para modificar informações
- **Alterar Foto**: Faça upload de uma nova imagem de perfil
- **Excluir Conta**: Opção disponível nas configurações do perfil

### 🍳 Gerenciamento de Receitas

#### Criar Nova Receita
1. Faça login na sua conta
2. Clique em **"Criar Receita"**
3. Preencha todos os campos obrigatórios:
   - Nome da receita
   - Ingredientes (um por linha)
   - Modo de preparo (um passo por linha)
   - Tempo de preparo
   - Número de porções
   - Categoria
4. Defina a visibilidade (Pública ou Privada)
5. Opcionalmente, adicione uma foto da receita
6. Clique em **"Salvar"** para publicar

#### Visualizar Receitas
- **Receitas Próprias**: Acesse através do seu perfil
- **Receitas Públicas**: Disponíveis na página inicial
- **Detalhes**: Clique em qualquer receita para ver informações completas

#### Editar Receitas
1. Acesse sua receita através do perfil
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
- ✅ Upload de imagens em formatos diversos (JPG, PNG)
- ✅ Edição e exclusão de receitas próprias
- ✅ Tentativa de acesso a receitas privadas de outros usuários

#### Testes de Interface
- ✅ Navegação em diferentes dispositivos e resoluções
- ✅ Validação visual de formulários
- ✅ Responsividade em mobile e desktop
- ✅ Carregamento e exibição de imagens

#### Testes de Segurança
- ✅ Prevenção de acesso não autorizado a páginas protegidas
- ✅ Validação de permissões para edição/exclusão
- ✅ Sanitização básica de dados de entrada

---

## 🔄 Instruções para Manutenção

### Atualizações do Banco de Dados

Quando mudanças que afetam o banco de dados forem realizadas:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Backup dos Dados

```bash
python manage.py dumpdata > backup.json
```

### Restauração dos Dados

```bash
python manage.py loaddata backup.json
```
