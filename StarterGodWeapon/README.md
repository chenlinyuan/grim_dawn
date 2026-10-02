# StarterGodWeapon — 开局神话武器 Mod（恐怖黎明 Grim Dawn）

一把 1 级即可佩戴的**神话（Mythical）**双手剑，**攻击敌人时 100% 触发「天击」**（从天空劈下一道雷霆轰击敌人）。

> **获取方式**：恶魔十字（Devil's Crossing）外下城区（Lower Crossing）的**尸体**会掉落这把武器。

## 效果

| 项目 | 值 |
|---|---|
| 武器名 | 天击之刃 / Heaven's Bane |
| 类型 | 双手剑 (WeaponMelee_Sword2h) |
| 品质 | Legendary + 神话前缀 (`tagStyleUniqueTier3`) |
| 物品等级 | 1 |
| 等级需求 | **1** |
| 授予技能 | 天击 (Heaven Strike) — 天降雷霆 |
| 触发方式 | **攻击敌人时 100% 触发** (`AttackEnemy`) |
| 技能冷却 | 1.5 秒 |
| 记录路径 | `records/items/gearweapons/melee2h/b013a_sword2h.dbr`（**覆盖原版**） |

## 获取方式（掉落）

恶魔十字外下城区的**尸体**（`a01_chestcorpse01_lowercrossing`）开出的武器中会出现本武器。

原理：本 Mod **覆盖原版物品** `records/items/gearweapons/melee2h/b013a_sword2h.dbr`
（该物品原本就是下城区尸体掉落表 `tdyn_melee2h_b06_lowercrossing.dbr` 里的物品之一）。
**不修改掉落表本身**，让原版掉落表自然引用被覆盖后的物品。

> ⚠️ **核心限制（务必理解）**：AssetManager 无法编译"掉落表 `lootName` 指向**本 Mod 自己定义/覆盖**的记录"——
> 一旦该路径被本 Mod 覆盖，掉落表里指向它的值就会被**丢弃**。
> 因此**绝不能在 Mod 里同时覆盖掉落表并引用自定义物品**。
> 正确做法：只覆盖**原版物品**（用原版路径），让**原版掉落表**去引用它。

### 备用获取方式（控制台）

启用控制台后按 `~` 输入：
```
game.give "records/items/gearweapons/melee2h/b013a_sword2h.dbr"
```

启用控制台：关闭游戏，编辑 `文档\My Games\Grim Dawn\Settings\options.txt`，加入一行 `console = true`。

> 控制台粘贴乱码时：手打，或试 **Ctrl+V**（不是右键）。

## 目录结构

```
mods/StarterGodWeapon/
├── database/
│   ├── StarterGodWeapon.arz
│   └── Records/
│       ├── Controllers/ItemSkills/cast_@enemyonanyhit_100%.dbr   # triggerType=AttackEnemy
│       ├── Items/GearWeapons/Melee2h/b013a_sword2h.dbr           # 覆盖原版物品
│       └── Skills/ItemSkills/Legendary/item_heavenstrike.dbr     # Skill_AttackRadiusLightning
├── resources/
│   ├── Text_EN.arc / Text_ZH.arc
└── source/
    ├── Text_EN/tags_startergodweapon.txt
    └── Text_ZH/tags_startergodweapon.txt
```

## 实现原理

1. **技能记录** `item_heavenstrike.dbr`
   模板 `skill_attackradiuslightning.tpl`（`Skill_AttackRadiusLightning`）—— 从天而降的雷霆。
   基于原版 `item_lightningbolt.dbr` 修改：开启 `Sword,1`、冷却 1.5s、换名字标签。

2. **自动施法控制器** `cast_@enemyonanyhit_100%.dbr`
   - `chanceToRun,100` — 100% 几率
   - `triggerType,AttackEnemy` — **攻击敌人时触发**（`HitByEnemy` 是"被击中时"，不是这个）
   - `targetType,Enemy`

3. **武器记录** `b013a_sword2h.dbr`（覆盖原版 `records/items/gearweapons/melee2h/b013a_sword2h.dbr`）
   - 以原版 1 级双手剑为底，改品质/等级/伤害，并挂上技能：
   - `itemSkillName,records/skills/itemskills/legendary/item_heavenstrike.dbr`
   - `itemSkillLevelEq,1`
   - `itemSkillAutoController,records/controllers/itemskills/cast_@enemyonanyhit_100%.dbr`
   - ⚠️ 务必**删除原版自带的** `itemSkillName`/`itemSkillAutoController`/`itemSkillLevelEq` 行，否则会冲突。

### 触发类型对照表（triggerType）

| 值 | 含义 |
|---|---|
| `AttackEnemy` | 攻击敌人时（挥击）← **本 mod 使用** |
| `AttackEnemyCrit` | 攻击暴击时 |
| `HitByEnemy` | **被**敌人击中时 |
| `HitByMelee` / `HitByProjectile` | 近战/投射物命中敌人时 |
| `OnKill` | 击杀敌人时 |

## ⚠️ 重新编译（注意顺序）

**第 1 步 — 数据库**（必须用 AssetManager）：
- `AssetManager.exe` → Work Offline → Mod → Select → StarterGodWeapon → Build → Build (F7)
- ⚠️ 改了记录后若 build 不生效，先**删除** `database/StarterGodWeapon.arz` 再 build（有缓存）。

**第 2 步 — 本地化**（必须在数据库 build **之后**做！）：
```powershell
$gd  = "H:\SteamLibrary\steamapps\common\Grim Dawn"
$mod = "$gd\mods\StarterGodWeapon"
Remove-Item "$mod\resources\Text_EN.arc","$mod\resources\Text_ZH.arc" -Force -ErrorAction SilentlyContinue
Push-Location "$mod\source"
& "$gd\ArchiveTool.exe" "$mod\resources\Text_EN.arc" -add "Text_EN" "."
& "$gd\ArchiveTool.exe" "$mod\resources\Text_ZH.arc" -add "Text_ZH" "."
Pop-Location
```

> ⚠️ **关键**：AssetManager 的 Build 会把 `resources\Text_*.arc` **覆盖成空的 2048 字节文件**！
> 所以**每次用 AssetManager build 数据库后，都必须重新用 ArchiveTool 生成本地化 arc**。
> 验证：`Text_*.arc` 应 > 2048 字节（正常约 2.4KB）。

> ⚠️ **安全提示**：AssetManager 的 Build Directory 绝不能指向游戏安装根目录，
> 否则会覆盖游戏本体的 `database\database.arz`。若发生，用 Steam 验证文件完整性恢复。

## 备注

- 原版没有叫「天击」的技能，本 Mod 用 **雷击 (Lightning Bolt)** 作为原型（从天劈雷）并命名「天击」。
- 换技能：改 `itemSkillName` 指向对应记录即可。
- **核心限制**：AssetManager 无法编译"掉落表 `lootName` 指向本 Mod 自己定义/覆盖的记录"——
  值会被丢弃。所以**掉落必须靠覆盖原版物品**（原版路径），让原版掉落表自然引用被覆盖的物品，
  **不能**在 Mod 里新建掉落表去引用自定义物品。
