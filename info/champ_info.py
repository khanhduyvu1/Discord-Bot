import requests



def get_champion_data(champion_name):
    url = f"https://ddragon.leagueoflegends.com/cdn/11.24.1/data/en_US/champion/{champion_name}.json"
    response = requests.get(url)
    if response.status_code == 200:
        champion_data = response.json()
        return champion_data['data'][champion_name]
    else:
        return None

def get_response(message: str) -> str:
    if message.startswith(''):
        champion_name = message[len(''):].capitalize()
        champion_data = get_champion_data(champion_name)

        if champion_data:
            title = champion_data['title']
            lore = champion_data['lore']
            stats = champion_data['stats']
            response = (f"**{champion_name} - {title}**\n\n"
                        f"**Lore:** {lore}\n\n"
                        f"**Stats:**\n"
                        f"HP: {stats['hp']}\n"
                        f"Attack Damage: {stats['attackdamage']}\n"
                        f"Armor: {stats['armor']}\n"
                        f"Magic Resist: {stats['spellblock']}\n"
                        f"Movement Speed: {stats['movespeed']}")
            return response
        else:
            return f"Champion '{champion_name}' not found."
    return "Please use the format '[ChampionName]', with Capitalize first letter to get information about a League of Legends champion."