import random

print('Генератор ников\nПрограмма берет случайное существительное и прилагательное и делает из них ник')

nouns = [
        "Wolf", "Dragon", "Tiger", "Eagle", "Lion", "Fox", "Raven", "Shark", "Bear", "Hawk",
    "Panther", "Cobra", "Falcon", "Viper", "Ghost", "Ninja", "Samurai", "Viking", "Knight", "Wizard",
    "Hunter", "Warrior", "Master", "King", "Queen", "Lord", "Blade", "Sword", "Arrow", "Storm",
    "Thunder", "Lightning", "Fire", "Ice", "Shadow", "Star", "Moon", "Sun", "Sky", "Cloud",
    "Wind", "Stone", "Rock", "Steel", "Flame", "Void", "Phantom", "Spirit", "Demon", "Angel",
    "Phoenix", "Griffin", "Hydra", "Kraken", "Wyvern", "Golem", "Reaper", "Ranger", "Sniper", "Assassin",
    "Berserker", "Paladin", "Druid", "Rogue", "Bard", "Monk", "Chieftain", "Emperor", "Baron", "Duke",
    "Sage", "Oracle", "Nomad", "Drifter", "Wanderer", "Sentinel", "Guardian", "Avenger", "Titan", "Colossus",
    "Specter", "Wraith", "Banshee", "Valkyrie", "Fury", "Comet", "Nova", "Eclipse", "Mirage", "Echo"
]

adjectives = [        "Swift", "Dark", "Iron", "Golden", "Shadow", "Frozen", "Crimson", "Silent", "Wild", "Epic",
    "Cosmic", "Neon", "Phantom", "Turbo", "Mystic", "Electric", "Savage", "Lucky", "Mad", "Crystal",
    "Black", "White", "Red", "Blue", "Silver", "Steel", "Fire", "Storm", "Night", "Ghost",
    "Cyber", "Hyper", "Mega", "Ultra", "Prime", "Alpha", "Omega", "Ancient", "Royal", "Fierce",
    "Deadly", "Sneaky", "Crazy", "Bold", "Bright", "Cold", "Hot", "Sharp", "Smooth", "Rough",
    "Rapid", "Vicious", "Lunar", "Solar", "Astral", "Blazing", "Freezing", "Thunder", "Venom", "Granite",
    "Titan", "Obsidian", "Mythic", "Sacred", "Cursed", "Rebel", "Rogue", "Noble", "Grim", "Sly",
    "Brave", "Cruel", "Fatal", "Giant", "Hidden", "Immortal", "Infernal", "Jade", "Keen", "Lost",
    "Nimble", "Onyx", "Pale", "Quiet", "Rusty", "Scarlet", "Slick", "Stern", "Void", "Wicked"]

print(f'Ваш ник - {random.choice(adjectives)}_{random.choice(nouns)}')
