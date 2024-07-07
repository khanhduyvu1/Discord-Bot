import requests
import discord

def get_champion_data(champion_name):
    champ_url = f"https://ddragon.leagueoflegends.com/cdn/14.13.1/data/en_US/champion/{champion_name}.json"
    response = requests.get(champ_url)
    data = response.json()
    # Extracting champion names
    champion_data = data['data'].get(champion_name)
    return champion_data
    
def champion_image(champion_name):
    champion_data = get_champion_data(champion_name)
    name = champion_data['name']
    title = champion_data['title']
    base_url = "https://ddragon.leagueoflegends.com/cdn/img/champion/tiles/"
    image_url = f"{base_url}{champion_name}_0.jpg"
    embed = discord.Embed(title=f"Champion: {name} - {title}")
    embed.set_thumbnail(url=image_url)
    return embed

def champion_response(champion_name):
    champion_data = get_champion_data(champion_name)
        
    if champion_data:
        
        lore = champion_data['lore']
        stats = champion_data['stats']
        response = (f"**Lore:** {lore}\n\n"
                    f"**Stats:**\n"
                    f"HP: {stats['hp']}\n"
                    f"Attack Damage: {stats['attackdamage']}\n"
                    f"Armor: {stats['armor']}\n"
                    f"Magic Resist: {stats['spellblock']}\n"
                    f"Movement Speed: {stats['movespeed']}\n")
        embed = discord.Embed(description=response)
        return embed
    
