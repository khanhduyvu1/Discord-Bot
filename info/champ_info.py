import requests
import discord
import os
import re

version = os.getenv("LEAGUE_VERSION")

def validate_input(s):
    return re.sub(r'[^a-zA-Z]', '', s).lower()

def get_champion_data(champion_name):
    version = os.getenv("LEAGUE_VERSION")
    champ_url = os.getenv("CHAMP_URL")
    response = requests.get(champ_url)
    data = response.json()
    cc = data['data'].keys()
    champion_name = validate_input(champion_name)
    validated_champions = {validate_input(c): c for c in cc}
    if champion_name not in validated_champions:
        return None
    champion_name = validated_champions[champion_name]
    champ_url_info = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion/{champion_name}.json"
    response_info = requests.get(champ_url_info)
    data_info = response_info.json()
    champion_data = data_info['data'].get(champion_name)    
    return champion_data
    
def champion_image(champion_name):
    champion_data = get_champion_data(champion_name)
    id = champion_data['id']
    name = champion_data['name']
    title = champion_data['title']
    base_url = f"https://ddragon.leagueoflegends.com/cdn/{version}/img/champion/{id}.png"
    embed = discord.Embed(title=f"Champion: {name} - {title}")
    embed.set_thumbnail(url=base_url)
    return embed


def champion_response(champion_name):
    champion_data = get_champion_data(champion_name)
        
    if champion_data:
        
        lore = champion_data['lore']
        stats = champion_data['stats']
        response = (f"**Lore:** {lore}\n\n"
                    f"**Stats:**\n"
                    f"HP: {stats['hp']} (+{stats['hpperlevel']}/lv)\n"
                    f"Attack Damage: {stats['attackdamage']} (+{stats['attackdamageperlevel']}/lv)\n"
                    f"Armor: {stats['armor']} (+{stats['armorperlevel']}/lv)\n"
                    f"Magic Resist: {stats['spellblock']} (+{stats['spellblockperlevel']}/lv)\n"
                    f"Movement Speed: {stats['movespeed']}\n\n")
        embed = discord.Embed(description=response)
        return embed
    
