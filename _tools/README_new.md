# StarterGodWeapon — 开局神话武器 Mod（恐怖黎明 Grim Dawn）

一把 1 级即可佩戴的**神话（Mythical）**单手剑，**攻击敌人时 100% 触发「天击」**（从天空劈下一道雷霆轰击敌人）。

**获取方式**：恶魔十字外下城区（Lower Crossing）的尸体掉落。

## 效果

| 项目 | 值 |
|---|---|
| 武器名 | 天击之刃 / Heaven's Bane |
| 类型 | 单手剑 (WeaponMelee_Sword) |
| 品质 | Legendary（神话，`tagStyleUniqueTier3`）|
| 物品等级 / 需求 | 1 / 1 |
| 基础物理伤害 | 60–90（固定）|
| 闪电伤害 | 40–70（固定）|
| 物理伤害加成 | +50% |
| 闪电伤害加成 | +50% |
| 物理→闪电转化 | 15% |
| 攻击速度 | +20% |
| 移动速度 | +20% |
| 攻击能力 | +30 |
| 防御能力 | +20 |
| 生命恢复 | +5% |
| 全部抗性 | +10 |
| 武器特效 | 闪电拖尾 + 发光模型 |
| 授予技能 | 天击（攻击时 100% 触发，4 米范围，冷却 1.5 秒）|

> 所有属性均为**固定数值**（`attributeScalePercent=0`，无随机浮动）。

## ⚠️ 重要：修改 mod 后必须让游戏重新加载

Grim Dawn 会**缓存 mod 数据库**。重新编译 mod 后，如果直接进自定义游戏，游戏可能加载**旧版本**。

**强制重载方法**：
1. 启动游戏
2. 先进**主线战役**（Play / Campaign）随便玩一下
3. 退回主菜单
4. 再进 **Custom Game → StarterGodWeapon**

这样游戏才会重新读取最新的 `StarterGodWeapon.arz`。

## 目录结构

```
mods/StarterGodWeapon/
├── database/
│   ├── StarterGodWeapon.arz
│   ├── templates.arc
│   └── Records/
│       ├── Controllers/ItemSkills/cast_@enemyonanyhit_100%.dbr   # triggerType=AttackEnemy
│       ├── Items/GearWeapons/Swords1h/item_startergodsword.dbr
│       ├── Items/LootChests/ChestLootTables/chestloot_all_a01_lowercrossinga01.dbr   # 尸体掉落
│       ├── Items/LootChests/ChestLootTables/chestloot_all_a01_lowercrossingmelee.dbr
│       ├── Items/LootChests/ChestLootTables/chestloot_rackweapon_b01.dbr
│       ├── Items/LootChests/QuestChests/QuestChestLootTables/chestloot_intropotions.dbr
│       ├── Items/LootTables/MasterTables/mt_gearweapons_a01.dbr
│       └── Skills/ItemSkills/Legendary/item_heavenstrike.dbr     # Skill_AttackRadiusLightning
├── resources/
│   └── Text_EN.arc / Text_ZH.arc
└── source/
    ├── Text_EN/tags_startergodweapon.txt
    └── Text_ZH/tags_startergodweapon.txt
```

## 实现原理

1. **技能记录** `item_heavenstrike.dbr`
   模板 `skill_attackradiuslightning.tpl`（`Skill_AttackRadiusLightning`）—— 从天而降的雷霆。
   `skillTargetRadius=4.0`（4 米目标区域）、冷却 1.5s。

2. **自动施法控制器** `cast_@enemyonanyhit_100%.dbr`
   - `chanceToRun,100`、`triggerType,AttackEnemy`、`targetType,Enemy`

3. **武器记录** `item_startergodsword.dbr`
   - `itemSkillName` / `itemSkillAutoController` / `itemSkillLevelEq`
   - `attributeScalePercent,0`（固定数值）
   - `glowTexture`（发光）+ `weaponTrail`（闪电拖尾）

## ⚠️ 重新编译（注意顺序）

**第 1 步 — 数据库**（必须用 AssetManager）：
- `AssetManager.exe` → Work Offline → Mod → Select → StarterGodWeapon → Build → Build (F7)
- 改了记录后若 build 不生效，先**删除** `database/StarterGodWeapon.arz` 再 build。

**第 2 步 — 本地化**（必须在数据库 build **之后**做）：
```powershell
$gd  = "H:\SteamLibrary\steamapps\common\Grim Dawn"
$mod = "$gd\mods\StarterGodWeapon"
Push-Location "$mod\source"
& "$gd\ArchiveTool.exe" "$mod\resources\Text_EN.arc" -add "Text_EN" "."
& "$gd\ArchiveTool.exe" "$mod\resources\Text_ZH.arc" -add "Text_ZH" "."
Pop-Location
```

> ⚠️ AssetManager 的 Build 会把 `resources\Text_*.arc` 覆盖成空的 2048 字节文件，
> 所以每次 build 数据库后都必须重新用 ArchiveTool 生成本地化 arc（应 > 2048 字节）。

> ⚠️ **安全提示**：AssetManager 的 Build Directory 绝不能指向游戏安装根目录。

## 关键经验（踩坑记录）

- **`.dbr` 文件必须用 LF 换行**（Unix 风格）。用 CRLF 会导致 AssetManager 解析字段错乱。
- **字段顺序要符合模板定义**（如 `itemCostName` 应在 `attributeScalePercent` 之后）。
- **AssetManager 无法编译"掉落表引用本 Mod 自定义物品"** —— 值会被丢弃。
  解决：让掉落表引用**原版物品路径**，或直接覆盖原版物品。
- **游戏会缓存 mod 数据库** —— 改完 mod 后必须"切主线→回主菜单→进自定义游戏"强制重载。
