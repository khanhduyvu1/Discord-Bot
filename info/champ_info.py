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
    

def champion_response(champion_name, level):
    champion_data = get_champion_data(champion_name)
 
    id = champion_data['id']
    name = champion_data['name']
    title = champion_data['title']
    lore = champion_data['lore']
    stats = champion_data['stats']
    base_url = f"https://ddragon.leagueoflegends.com/cdn/{version}/img/champion/{id}.png"
    
    level_stats = {
        "hp": round(stats['hp'] + stats['hpperlevel'] * (level - 1), 3),
        "mp": round(stats['mp'] + stats['mpperlevel'] * (level - 1), 3),
        "attackdamage": round(stats['attackdamage'] + stats['attackdamageperlevel'] * (level - 1), 3),
        "armor": round(stats['armor'] + stats['armorperlevel'] * (level - 1), 3),
        "spellblock": round(stats['spellblock'] + stats['spellblockperlevel'] * (level - 1), 3),
        "crit": round(stats['crit'] + stats['critperlevel'] * (level - 1), 3),
        "movespeed": round(stats['movespeed'], 3),
        "attackspeed": round(stats['attackspeed'] * (1 + stats['attackspeedperlevel'] / 100 * (level - 1)), 3),
        "attackrange": round(stats['attackrange'], 3),
        "hpregen": round(stats['hpregen'] + stats['hpregenperlevel'] * (level - 1), 3),
        "mpregen": round(stats['mpregen'] + stats['mpregenperlevel'] * (level - 1), 3)
    }   
    
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
    
    embed = discord.Embed(title=f"Champion: {name} - {title}")  
    embed.set_thumbnail(url=base_url)  
    embed.add_field(name="Lore", value=lore, inline=False)

# Add stats in two columns
    stats_left = (
        f"{hp_emoji} HP: {level_stats['hp']}\n"
        f"{mp_emoji} MP: {level_stats['mp']}\n"
        f"{ad_emoji} Attack Damage: {level_stats['attackdamage']}\n"
        f"{armor_emoji} Armor: {level_stats['armor']}\n"
        f"{mr_emoji} Magic Resist: {level_stats['spellblock']}\n"
        f"{crit_emoji} Crit: {level_stats['crit']}\n"
    )

    stats_right = (
        f"{ms_emoji} Movement Speed: {level_stats['movespeed']}\n"
        f"{as_emoji} Attack Speed: {level_stats['attackspeed']}\n"
        f"{ar_emoji} Attack Range: {level_stats['attackrange']}\n"
        f"{hpregen_emoji} HP Regen: {level_stats['hpregen']}\n"
        f"{mpregen_emoji} MP Regen: {level_stats['mpregen']}\n"
    )

    embed.add_field(name="Stat Assets", value=stats_left, inline=True)
    embed.add_field(name="\u200b", value=stats_right, inline=True)
    
    embed.set_footer(text=f"Level {level}")

    return embed
    
