# Sistema de Login com Python, MVC, SQLite e SQLAlchemy

Este é um simples sistema de login desenvolvido em Python, utilizando o padrão de arquitetura MVC (Model-View-Controller) e integrando um banco de dados SQLite com ORM SQLAlchemy.

## Requisitos

- Python 3.x instalado.
- Bibliotecas: SQLAlchemy (instalável via pip).

## Instalação e Configuração

1. Clone ou faça o download deste repositório.
2. Certifique-se de ter o Python 3.x instalado em seu sistema.
3. Crie um ambiente virtual para este projeto executando o seguinte comando no terminal:

   ```
   python -m venv myenv
   ```

   Isso criará um ambiente virtual chamado `myenv` no diretório atual.

4. Ative o ambiente virtual. No Windows, execute:

   ```
   myenv\Scripts\activate
   ```

   No Linux/Mac, execute:

   ```
   source myenv/bin/activate
   ```

5. Instale as dependências listadas no arquivo `requirements.txt` utilizando o pip:

   ```
   pip install -r requirements.txt
   ```

## Uso

1. Abra o terminal e navegue até o diretório onde os arquivos estão localizados.
2. Execute o arquivo `View.py` digitando o seguinte comando:

   ```
   python View.py
   ```

3. Você será apresentado com um menu:

   ```
   ========== [MENU] ==========
   Digite 1 para cadastrar
   Digite 2 para Logar
   Digite 3 para sair
   ```

4. Escolha a opção desejada digitando o número correspondente:
   - Digite `1` para cadastrar um novo usuário.
   - Digite `2` para fazer login.
   - Digite `3` para sair do programa.

### Cadastro de Usuário

Ao selecionar a opção de cadastrar um novo usuário, siga as instruções exibidas no terminal. Você será solicitado a fornecer seu nome, email e senha. Após o cadastro bem-sucedido, uma mensagem será exibida confirmando o sucesso ou indicando um erro, se aplicável.

### Login

Para fazer login, selecione a opção correspondente no menu e forneça seu email e senha quando solicitado. Se as credenciais estiverem corretas, você será autenticado com sucesso e seu ID será exibido. Caso contrário, uma mensagem de erro será exibida.

## Observações

- Este sistema armazena os dados dos usuários em um banco de dados SQLite (`login.db`).
- A senha é armazenada de forma criptografada (hash SHA-256) para segurança.
- Certifique-se de não compartilhar suas credenciais com outras pessoas.
