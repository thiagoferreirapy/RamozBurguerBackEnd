


<h1 align="center">💻 BACKEND RAMOZZ BURGUERS:</h1>
<p align="center">
  endpoints para interagir com os dados dos clientes, pedidos e produtos, permitindo que o próprio framework Django controle o fluxo de dados do usuário. Com essa integração, os desenvolvedores podem criar aplicativos web e móveis dinâmicos e responsivos, proporcionando uma experiência de usuário fluida ao solicitar produtos da Ramos Burguers. Esta API é desenvolvida com Django, um framework robusto e escalável para desenvolvimento web em Python, e é projetada para facilitar a integração e a manutenção de aplicativos baseados em Django.
</p>
<br/>
<h3 align="center">TECNÓLOGIAS QUE USEI</h2>
<div align="center">

 ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)  ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white) 
</div>
   

<br/>
<h3>O QUE FOI FEITO ATÉ AGORA</h2>
<ul>
  
- Endpoints para criar e listar produtos
- Endpoints para criar e listar categorias
- Endpoints para criar e adicionais
- Endpoints para criar e listar produtos na sacola
- Integração com o Front-end
</ul>


<br/>
<h3>NOVAS METAS</h2>
<ul>
  
  - Migrar para um banco de dados mais robusto
  - Cadastro de usuário
  - Criar pedidos referente a cada usuário
  - Endpoints para atualizar pedido
  - Endpoints para deletar pedido
  - Integração com metódo de pagamento
  - Envio de e-mail/sms para usuários
</ul>


<h2 align="center">COMO UTILIZAR O PROJETO</h2>

### Pré-requisitos

Antes de começar, certifique-se de ter os seguintes pré-requisitos instalados em seu sistema:

1. [Python](https://www.python.org/downloads/) (Python3++).
2. Importante ter o ambiente virtual no seu projeto VirtualEnv 
 ```bash
   # No seu terminal / powershell digite o seguinte comando para baixar a virtualenv
   
     pip install virtualenv
   
   ```
3. Antes de ativar o ambiente virtual é importante configurar o powershell
 ```bash
   # No seu powershell digite o seguinte comando
   
     Set-ExecutionPolicy Unrestricted -Scope Process -Force
   
   ```
### ⚙️🖥️ Configurando o Projeto em sua máquina

1. Clone este repositório em uma pasta na sua máquina localmente:
   ```bash
   # Na pasta selecionada abra com o git bash e cole este código!
   
     https://github.com/thiagoferreirapy/RamozzBurguerFrontEnd.git
   
   ```
2. Certifique-se que deu certo e entre na pasta do projeto:
    ```bash
    # 1- Verifique se o projeto foi clonado corretamente:
    # Resultado esperado ( Ramoz-Burguer-BackEnd/ )
    
      ls

    # 2- Entre na pasta do projeto
    
      cd Ramoz-Burguer-BackEnd/

    #3- Aproveite e já entra usando o Vscode

      code .

    
   ```
3. Com o projeto aberto você pode ativar/criar o ambiente virtual:
   - Para Windons:
Entre na pasta do projeto e rode os seguintes códigos no terminal:
    ```bash
    #Pelo Prompt de comando
    
    #Criar a VENV
    python -m venv venv
    
    #Ativar a VENV
    .\venv\Scripts\activate.bat
    
    #Atualizar o pip
    python -m pip install --upgrade pip

    #Pelo PowerShell

    #Criar a VENV
    python -m venv venv

    #Ativar a VENV
    .\venv\Scripts\activate ou .\venv\Scripts\activate.ps1

    #Atualizar o pip
    python -m pip install --upgrade pip
    
   ```
   - Para linux:
Entre na pasta do projeto e rode os seguintes códigos no terminal:
    ```bash
    #Criar a VENV 
    python3 -m venv venv

    #Ativar a VENV
    .\venv/bin/activate

    #Atualizar o pip
    python -m pip install --upgrade pip
    
   ```
   - Para Mac:
Entre na pasta do projeto (cd Morse) e rode os seguintes códigos no terminal:
    ```bash

    #Criar a VENV
    python -m venv venv

    #Ativar a VENV
    .\venv/bin/activate

    #Atualizar o pip
    python -m pip install --upgrade pip
        
   ```
    
### 🚩 Iniciando o Servidor local
1. No terminal do projeto execute o comando para baixar todas as dependências do projeto:
   ```text
   
   pip install -r requirements.txt
   
   ```
2. Baixe as migrações do banco de dados:
   ```bash
   # Certificar-se de que está no diretório do projeto Django onde o arquivo manage.py está localizado
   
   python manage.py migrate
   
   ```
3. Você poderá criar um Super Usuário:
   ```bash
      # Essa é uma parte opcional mas é impoirtante criar para ter acesso a parte de admin do django
     
      python manage.py createsuperuser
  
      # logo após esse comando vai ser preciso colocar um nome de usuario, email(opcional) e senha.
  
   ```
3. Você poderá iniciar o servidor:
   ```bash
      # Essa é uma parte opcional mas é impoirtante criar para ter acesso a parte de admin do django
     
      python manage.py runserver 800
  
   ```
  O servidor estará acessível em: [http://localhost:800/](http://localhost:800/) 
  
  #### 🚩💻 Endpoints
  <ul> 
  
  - Criar ou listar produtos: [http://localhost:800/api/v1/product/](http://localhost:800/api/v1/product/) 
  - Criar ou listar categorias: [http://localhost:800/api/v1/category/](http://localhost:800/api/v1/category/)
  - Criar ou listar sacolas: [http://localhost:800/api/v1/bag/](http://localhost:800/api/v1/bag/)
  - Listar produtos por tipo de categoria: [http://localhost:800/api/v1/products/<str:pk>/](http://localhost:800/api/v1/products/<str:pk>/)
  - Listar adicionais por tipo de categoria: [http://localhost:800/api/v1/additional/<str:pk>/](http://localhost:800/api/v1/additional/<str:pk>/)
  </ul>

<br/>
<br/>

3. Você poderá iniciar o servidor:
    ```bash
        # METODO POST para criar uma categoria (http://localhost:800/api/v1/category/)
        {
            "name": string
        }
        {
            "name": "Burguer",
        } 
    ```
    ```bash
        # METODO POST para criar um produto (http://localhost:800/api/v1/product/)
        {
            "name": string,
            "description": string,
            "ingredients": string,
            "value": float,
            "image": string,
            "category": string
        } 
        {
            "name": "Hamburguer do bom",
            "description": "Hamburguer muito bom",
            "ingredients": "1 hamburguer e pão",
            "value": 20.00,
            "image": "imagemdohamburguer.jpg",
            "category": "id_da_categoria"
        } 
    ```
    ```bash
        # METODO POST para criar uma sacola (http://localhost:800/api/v1/bag/)
        {
            "quantity": integer,
            "observation": string,
            "value": float,
            "finished": false,
            "product_id": string,
            "additional_meat": string,
            "additional_sauce": string
        }
        {
            "quantity": 1,
            "observation": "Sem cebola",
            "value": 10.00,
            "finished": false,
            "product_id": "id_do_produto",
            "additional_meat": "id_do_adicional_meat",
            "additional_sauce": "id_do_adicional_sauce"
        }
    ```
    
<br/>



<h1 align="center">MUITO OBRIGADO PELA VISITA!</h1>

