import requests
import discord
import os
import re

version = os.getenv("LEAGUE_VERSION")

def validate_input(s):
    return re.sub(r'[^a-zA-Z]', '', s).lower()

def get_champion_data(champion_name):
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
         # Replace the emoji names with the correct ones you uploaded
        hp_emoji = os.getenv("HP_EMOJI")
        mp_emoji = os.getenv("MP_EMOJI")
        ad_emoji = os.getenv("AD_EMOJI")
        armor_emoji = os.getenv("ARMOR_EMOJI")
        mr_emoji = os.getenv("MR_EMOJI")
        crit_emoji = os.getenv("CRIT_EMOJI")
        ms_emoji = os.getenv("MS_EMOJI")
        as_emoji = os.getenv("AS_EMOJI")
        ar_emoji = os.getenv("AR_EMOJI")
        hpregen_emoji = os.getenv("HPREGEN_EMOJI")
        mpregen_emoji = os.getenv("MPREGEN_EMOJI")
        
        response = (f"**Lore:** {lore}\n\n"
            #f"```\n"
            f"Stat Assets       | Info\n"
            f"----------------|------------------------\n"
            f"{hp_emoji} HP              | {stats['hp']} (+{stats['hpperlevel']}/lv)\n"
            f"{mp_emoji} MP              | {stats['mp']} (+{stats['mpperlevel']}/lv)\n"
            f"{ad_emoji} Attack Damage   | {stats['attackdamage']} (+{stats['attackdamageperlevel']}/lv)\n"
            f"{armor_emoji} Armor           | {stats['armor']} (+{stats['armorperlevel']}/lv)\n"
            f"{mr_emoji} Magic Resist    | {stats['spellblock']} (+{stats['spellblockperlevel']}/lv)\n"
            f"{crit_emoji} Crit            | {stats['crit']} (+{stats['critperlevel']}/lv)\n"
            f"{ms_emoji} Movement Speed  | {stats['movespeed']}\n"
            f"{as_emoji} Attack Speed    | {stats['attackspeed']} (+{stats['attackspeedperlevel']}/lv)\n"
            f"{ar_emoji} Attack Range    | {stats['attackrange']}\n"
            f"{hpregen_emoji} HP Regen        | {stats['hpregen']} (+{stats['hpregenperlevel']}/lv)\n"
            f"{mpregen_emoji} MP Regen        | {stats['mpregen']} (+{stats['mpregenperlevel']}/lv)\n"
            #f"```"
            )
        embed = discord.Embed(description=response)
        return embed
    
