import discord
import requests

from info.champ_info import get_champion_data

def get_skill_data(champion_name):
    champion_data = get_champion_data(champion_name)
    champion_name = champion_data['id']
    
    skill_url_info = f'https://cdn.merakianalytics.com/riot/lol/resources/latest/en-US/champions/{champion_name}.json'
    response = requests.get(skill_url_info)
    data = response.json()
    id = data['id']
    if id < 100:
        link_id = f'00{id}'
    else:
        link_id = f'0{id}'
    embeds =[]
    
    #embed = discord.Embed(title=f"{champion_name} Abilities")
    
    for ability_key in ['P', 'Q', 'W', 'E', 'R']:
        ability_data = data['abilities'][ability_key][0]
        skill_url_video = f'https://d28xe8vt774jo5.cloudfront.net/champion-abilities/{link_id}/ability_{link_id}_{ability_key}1.mp4'
        name = ability_data['name']
        ability_image = ability_data['icon']
        descriptions = get_first_two_descriptions(ability_data)
        description_text = '\n\n'.join(descriptions)  # Joining the first two descriptions with a newline
        
        embed = discord.Embed()
        embed.add_field(name=f'{name}', value="", inline=True)
        embed.add_field(name="", value=description_text, inline=False)
        embed.add_field(name="", value=skill_url_video, inline=False)
        embed.set_thumbnail(url=ability_image)
        
        embeds.append(embed)

    return embeds

def get_first_two_descriptions(ability_data):
    descriptions = [effect['description'] for effect in ability_data['effects'][:2]]
    return descriptions