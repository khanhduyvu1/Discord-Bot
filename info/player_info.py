import requests
import os

api_key = os.getenv("API_KEY")

def get_player_url(gameName, tagLine):
    gameName = gameName.replace(" ", "%20")
    tagLine = tagLine.replace(" ", "%20")
    player_url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}?api_key={api_key}"
    response = requests.get(player_url)
    data = response.json()
    puuid = data['puuid']
    return puuid
def get_player_data():
    pass
