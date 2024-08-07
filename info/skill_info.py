import discord
import requests

from info.champ_info import get_champion_data

def get_skill_data(champion_name):
    champion_data = get_champion_data(champion_name)
    champion_id = champion_data['id']
    champion_key = champion_data['key']
    champion_key = int(champion_key)
    if champion_key < 100:
        champion_key = str(f"00{champion_key}")
    else:
        champion_key = str(f"0{champion_key}")
    
    skill_url_info = f'https://cdn.merakianalytics.com/riot/lol/resources/latest/en-US/champions/{champion_id}.json'
    response = requests.get(skill_url_info)
    data = response.json()
    
    embeds =[]
    
    #embed = discord.Embed(title=f"{champion_id} Abilities")
    
    for ability_key in ['P', 'Q', 'W', 'E', 'R']:
        ability_data = data['abilities'][ability_key][0]
        name = ability_data['name']
        ability_image = ability_data['icon']
        ability_video = f"https://d28xe8vt774jo5.cloudfront.net/champion-abilities/{champion_key}/ability_{champion_key}_{ability_key}1.mp4"
        descriptions = get_first_two_descriptions(ability_data)
        description_text = '\n\n'.join(descriptions)  # Joining the first two descriptions with a newline
        
        embed = discord.Embed()
        embed.add_field(name=f'{name}', value="", inline=True)
        embed.add_field(name="", value=description_text, inline=False)
        embed.add_field(name="", value=ability_video, inline=False)
        embed.set_thumbnail(url=ability_image)
        
        embeds.append(embed)
        
        

    return embeds

def get_first_two_descriptions(ability_data):
    descriptions = [effect['description'] for effect in ability_data['effects'][:2]]
    return descriptions