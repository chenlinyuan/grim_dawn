import os

mod = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon'

zh = os.path.join(mod, 'source', 'Text_ZH', 'tags_startergodweapon.txt')
open(zh, 'w', encoding='utf-8', newline='\n').write(
    'tagSoulRing=灵魂暗戒\n'
    'tagSoulRingDesc=以灵魂之力锻造的暗金戒指。佩戴者身轻如燕，汲取天地灵气，攻击时召唤天击雷霆。\n'
    'tagSoulRingSetName=灵魂暗戒\n'
    'tagSoulRingSetDesc=灵魂暗戒（唯一）\n'
    'tagItemSkillHeavenStrikeName=天击\n'
    'tagItemSkillHeavenStrikeDesc=召唤一道雷霆轰击目标，对周围敌人造成武器伤害（受力量加成）。\n'
)

en = os.path.join(mod, 'source', 'Text_EN', 'tags_startergodweapon.txt')
open(en, 'w', encoding='utf-8', newline='\n').write(
    'tagSoulRing=Soul Ring\n'
    'tagSoulRingDesc=A legendary ring forged from soul essence. Swift as the wind, it calls down Heaven Strike on attack.\n'
    'tagSoulRingSetName=Soul Ring\n'
    'tagSoulRingSetDesc=Soul Ring (Unique)\n'
    'tagItemSkillHeavenStrikeName=Heaven Strike\n'
    'tagItemSkillHeavenStrikeDesc=Call down a thunderbolt, dealing weapon damage (scaled by Strength) to nearby enemies.\n'
)
print('localization updated')
print(open(zh, encoding='utf-8').read())
