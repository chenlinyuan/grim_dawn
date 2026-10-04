import os

mod = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon'

zh = os.path.join(mod, 'source', 'Text_ZH', 'tags_startergodweapon.txt')
open(zh, 'w', encoding='utf-8', newline='\n').write(
    'tagStarterGodSword=天击之刃\n'
    'tagStarterGodSwordDesc=锻造于凯恩黎明之时的利刃，蕴含天穹的怒火。以持有者为中心爆发出雷电新星，粉碎周围的敌人。\n'
    'tagItemSkillHeavenStrikeName=天击·雷电新星\n'
    'tagItemSkillHeavenStrikeDesc=以自身为中心爆发一圈雷电新星，轰击周围所有敌人。\n'
)

en = os.path.join(mod, 'source', 'Text_EN', 'tags_startergodweapon.txt')
open(en, 'w', encoding='utf-8', newline='\n').write(
    "tagStarterGodSword=Heaven's Bane\n"
    'tagStarterGodSwordDesc=A blade forged at the dawn of Cairn. Unleashes a nova of lightning around the wielder, shattering nearby foes.\n'
    'tagItemSkillHeavenStrikeName=Heaven Strike (Lightning Nova)\n'
    'tagItemSkillHeavenStrikeDesc=Detonate a ring of lightning around yourself, striking all nearby enemies.\n'
)
print('updated localization source')
print(open(zh, encoding='utf-8').read())
