from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)

@app.route("/")
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dicionario = json.loads(data)

    return render_template("characters.html", characters=dicionario["results"])

@app.route("/profile/<id>")
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dicionario = json.loads(data)

    return render_template("profile.html", profile=dicionario)

@app.route('/lista')
def get_list_characters():
    
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    characters_data = response.read()
    characters_dict = json.loads(characters_data)
    
    characters = []
    
    for character in characters_dict["results"]:
        character_info = {
            "name": character["name"],
            "status": character["status"],
            "species": character["species"],
        }
        characters.append(character_info)  

    return {"characters": characters}


if __name__ == "__main__":
    app.run(debug=True)
