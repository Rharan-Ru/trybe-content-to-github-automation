# Trybe Github Selenium Automation
Script destinado a organizar seu repositório de exercícios da Trybe.

Este Script funciona com [Selenium](https://www.selenium.dev/) o qual é um automatizador de navegador.

Para usar siga os passos a seguir:


## Quickly setup to start
Este projeto contém 2 drivers padrão (Google Chrome e Firefox), porém para se certificar de estar usando o driver certo siga os passos do próprio site [Selenium Webdrivers](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/)

Primeiramente vamos configurar nosso ambiente virtual, é bem rápido, ele cria um ambiente para nossas dependências:
````
python3 -m venv venv
source venv/bin/activate
````

Para instalar todas dependências do projeto utilize o comando:
````
pip install -r requirements.txt
````

Então você está pronto para utilizar o script, apenas rode o comando:
````
python3 main.py
````

Para apagar as branchs e os arquivos da própria, execute o comando:

````
python3 clear_git_branchs.py
````

### Obs: Para modificar o caminho dos arquivos e da pasta em que será feito o git init do repositório vá para main_functions/send_git.py, e modifique a variável PATH.
