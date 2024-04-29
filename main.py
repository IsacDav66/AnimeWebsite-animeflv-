from flask import Flask, render_template, request
import requests
import re

app = Flask(__name__)
api_base_url = "https://animeflv-api-1ius.onrender.com"

@app.route('/')
def index():
    print("Index route called.")
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    print(f"Search route called with query: {query}")
    response = requests.get(f"{api_base_url}/search", params={'query': query})
    results = response.json()
    print(f"Search results: {results}")
    return render_template('results.html', results=results)

@app.route('/anime/<anime>/<id>/episodes')
def episodes(anime,id):
    print(f"Episodes route called with ID: {id}")
    print({anime})
    # Obtener información del anime para obtener la cantidad total de episodios
    response = requests.get(f"{api_base_url}/anime/{anime}/episodes/{id}")
    anime_info = response.json()
    print(anime_info)
    # Obtener los enlaces de descarga de todos los episodios
    #all_links = []
    #for episode_info in anime_info['episodes']:
    #    episode_id = episode_info['id']
    #    links_response = requests.get(f"{api_base_url}/anime/{id}/episodes/{episode_id}")
    #    links = links_response.json()
     #   all_links.extend(links)
    
    # Renderizar la plantilla con los datos
    #print(f"All links: {all_links}")
    return render_template('episodes.html', anime_info= anime_info)

@app.route('/anime/<id>/info')

def info(id):
    print(f"Info route called with ID: {id}")
    response = requests.get(f"{api_base_url}/anime/{id}")
    anime_info = response.json()
    print(f"Anime info: {anime_info}")
    return render_template('info.html', anime_info=anime_info)

@app.route('/play_episode', methods=['POST'])
def play_episode():
    url = request.form['url']
    print(f"Play episode route called with URL: {url}")
    
    # Verificar si la URL comienza con "https://mega.nz/"
    if url.startswith("https://mega.nz/"):
        # Eliminar "!z" de la URL
        url = url.replace("#!", "embed/")
        # Reemplazar "!" con "#"
        url = url.replace("!", "#", 1)
    
    if url.startswith("https://streamtape.com/"):
        url = url.replace("v", "e")
        
    return render_template('play_episode.html', url=url)

if __name__ == '__main__':
    app.run(debug=True)
