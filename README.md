<h1>
    <a href="challengerickymorty.vercel.app" target="_blank">
     <img align="center" width="40px" src="./static/favicon.ico"></a>
    <span>Desafio Rick and Morty com Flask e Tailwind CSS</span>
</h1>


Este é um projeto para consumir a API pública de Rick and Morty, que fornece informações sobre os personagens, localizações e episódios da série. O aplicativo é desenvolvido usando Flask, um microframework em Python, e estilizado com Tailwind CSS para um design moderno e responsivo.

## Link para a API Rick and Morty

A API pública de Rick and Morty pode ser acessada através do seguinte link: [Rick and Morty API Documentation](https://rickandmortyapi.com/documentation/#rest).

## Funcionalidades

- **Listagem de Personagens**: Visualize uma lista de personagens da série com suas informações detalhadas.
- **Listagem de Localizações**: Explore diferentes localizações do universo Rick and Morty.
- **Listagem de Episódios**: Navegue pelos episódios e descubra quais personagens aparecem em cada um.
- **Perfis Detalhados**: Visualize perfis detalhados de personagens, localizações e episódios, com links para explorar mais informações.

## Requisitos do Sistema

- Python 3.x
- Node.js e npm (para Tailwind CSS)
- Vercel CLI (opcional, para implantação na Vercel)

## Instalação e Configuração

Siga os passos abaixo para configurar o ambiente de desenvolvimento e executar o projeto localmente.

### 1. Criar e Ativar um Ambiente Virtual

Primeiro, crie um ambiente virtual para isolar as dependências do projeto:

```bash
python3 -m venv .venv
```

## Ative o ambiente virtual:

- Linux/macOS:
```
source .venv/bin/activate
```
- Windows:
```
.venv\Scripts\activate
```
### 2. Instalar o Flask
Com o ambiente virtual ativado, instale o Flask:
```
pip install Flask
```
### 3. Instalar Tailwind CSS
Instale Tailwind CSS para adicionar estilos modernos ao seu aplicativo Flask.
- Passo 1: Inicializar o NPM
```
npm init -y
```
- Passo 2: Instalar o Tailwind CSS
```
npm install -D tailwindcss
npx tailwindcss init
```
- Passo 3: Configurar o Tailwind CSS

Edite o arquivo tailwind.config.js gerado para incluir seus templates:
```
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html"],
  theme: {
    extend: {},
  },
  plugins: [],
}
```
- Passo 4: Criar o arquivo de entrada do Tailwind CSS

Crie um arquivo static/styles.css e adicione:
```
@tailwind base;
@tailwind components;
@tailwind utilities;
```
- Passo 5: Compilar o Tailwind CSS

Use o comando abaixo para compilar o Tailwind CSS:
```
npx tailwindcss -i ./static/styles.css -o ./static/styles.css --watch
```

### 4. Configuração do Flask
Crie um arquivo app.py com a lógica do seu aplicativo Flask.

### 5. Executar o Servidor Flask
Para iniciar o servidor Flask, execute o comando:
```
flask --app app run
```
Acesse o aplicativo no navegador em http://127.0.0.1:5000/

### 6. Implantação na Vercel
Para implantar seu projeto na Vercel, siga os passos abaixo:

- Passo 1: Instalar a Vercel CLI
```
npm install -g vercel
```
- Passo 2: Configurar o vercel.json
Crie um arquivo vercel.json na raiz do seu projeto com o seguinte conteúdo:
```
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```
- Passo 3: Implantar na Vercel

Execute o comando para fazer deploy na Vercel:
```
vercel --prod
```

<div align="center">

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br>

##### Desenvolvido por <span>Elizabete Fabri</span> ❤️ 2024

</div>