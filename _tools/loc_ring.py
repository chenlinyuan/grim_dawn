import os

mod = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon'

zh = os.path.join(mod, 'source', 'Text_ZH', 'tags_startergodweapon.txt')
open(zh, 'w', encoding='utf-8', newline='\n').write(
    'tagSoulRing=灵魂暗戒\n'
    'tagSoulRingDesc=以灵魂之力锻造的暗金戒指。佩戴者身轻如燕，汲取天地灵气，攻击时爆发雷电新星。\n'
    'tagSoulRingSetName=灵魂暗戒\n'
    'tagSoulRingSetDesc=灵魂暗戒（唯一）\n'
    'tagItemSkillHeavenStrikeName=天击·雷电新星\n'
    'tagItemSkillHeavenStrikeDesc=以自身为中心爆发一圈雷电新星，轰击周围所有敌人。\n'
)

en = os.path.join(mod, 'source', 'Text_EN', 'tags_startergodweapon.txt')
open(en, 'w', encoding='utf-8', newline='\n').write(
    'tagSoulRing=Soul Ring\n'
    'tagSoulRingDesc=A legendary ring forged from soul essence. Swift as the wind, it draws on the world\'s energy and erupts a lightning nova on attack.\n'
    'tagSoulRingSetName=Soul Ring\n'
    'tagSoulRingSetDesc=Soul Ring (Unique)\n'
    'tagItemSkillHeavenStrikeName=Heaven Strike (Lightning Nova)\n'
    'tagItemSkillHeavenStrikeDesc=Detonate a ring of lightning around yourself, striking all nearby enemies.\n'
)
print('localization updated')
print(open(zh, encoding='utf-8').read())
