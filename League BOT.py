import discord
from discord import app_commands
from discord.ext import commands
import os
from os.path import join , dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__),".env")
load_dotenv(verbose=True ,dotenv_path=dotenv_path)

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()#適当に。
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print("起動完了")
    await tree.sync()#スラッシュコマンドを同期

champions_list = [
    "Aatrox (エイトロックス)",
    "Ahri (アーリ)",
    "Akali (アカリ)",
    "Akshan (アクシャン)",
    "Alistar (アリスター)",
    "Amumu (アムム)",
    "Anivia (アニビア)",
    "Annie (アニー)",
    "Aphelios (アフェリオス)",
    "Ashe (アッシュ)",
    "Aurelion Sol (オレリオンソル)",
    "Aurora (オーロラ)",
    "Azir (アジール)",
    "Bard (バード)",
    "Bel'Veth (ベルヴェス)",
    "Blitzcrank (ブリッツクランク)",
    "Brand (ブランド)",
    "Braum (ブラウム)",
    "Briar (ブライア)",
    "Caitlyn (ケイトリン)",
    "Camille (カミール)",
    "Cassiopeia (カシオペア)",
    "Cho'Gath (チョガス)",
    "Corki (コーキ)",
    "Darius (ダリウス)",
    "Diana (ダイアナ)",
    "Dr. Mundo (ドクタームンド)",
    "Draven (ドレイブン)",
    "Ekko (エコー)",
    "Elise (エリス)",
    "Evelynn (イブリン)",
    "Ezreal (エズリアル)",
    "Fiddlesticks (フィドルスティックス)",
    "Fiora (フィオラ)",
    "Fizz (フィズ)",
    "Galio (ガリオ)",
    "Gangplank (ガングプランク)",
    "Garen (ガレン)", 
    "Gnar (ナー)",
    "Gragas (グラガス)",
    "Graves (グレイブス)",
    "Gwen (グウェン)",
    "Hecarim (へカリム)",
    "Heimerdinger (ハイマーディンガー)",
    "Hwei (フェイ)",
    "Illaoi (イラオイ)",
    "Irelia (イレリア)",
    "Ivern (アイバーン)",
    "Janna (ジャンナ)",
    "Jarvan IV (ジャーヴァン IV世)",
    "Jax (ジャックス)",
    "Jayce (ジェイス)",
    "Jhin (ジン)",
    "Jinx (ジンクス)",
    "K'Sante (カサンテ)",
    "Kai'Sa (カイサ)",
    "Kalista (カリスタ)",
    "Karma (カルマ)",
    "Karthus (カーサス)",
    "Kassadin (カサディン)",
    "Katarina (カタリナ)",
    "Kayle (ケイル)",
    "Kayn (ケイン)",
    "Kennen (ケネン)",
    "Kha'Zix (カジックス)",
    "Kindred (キンドレッド)",
    "Kled (クレッド)",
    "Kog'Maw (コグマウ)",
    "LeBlanc (ルブラン)",
    "Lee Sin (リーシン)",
    "Leona (レオナ)",
    "Lillia (リリア)",
    "Lissandra (リサンドラ)",
    "Lucian (ルシアン)",
    "Lulu (ルル)",
    "Lux (ラックス)",
    "Malphite (マルファイト)",
    "Malzahar (マルザハール)",
    "Maokai (マオカイ)",
    "Master Yi (マスターイー)",
    "Milio (ミリオ)",
    "Miss Fortune (ミス・フォーチューン)",
    "Mordekaiser (モルデカイザー)",
    "Morgana (モルガナ)",
    "Naafiri (ナフィーリ)",
    "Nami (ナミ)",
    "Nasus (ナサス)",
    "Nautilus (ノーチラス)",
    "Neeko (ニーコ)",
    "Nidalee (ニダリー)",
    "Nilah (ニーラ)",
    "Nocturne (ノクターン)",
    "Olaf (オラフ)",
    "Orianna (オリアナ)",
    "Ornn (オーン)",
    "Pantheon (パンテオン)",
    "Poppy (ポッピー)",
    "Pyke (パイク)",
    "Qiyana (キヤナ)",
    "Quinn (クイン)",
    "Rakan (ラカン)",
    "Rammus (ラムス)",
    "Rek'Sai (レクサイ)",
    "Rell (レル)",
    "Renata Glasc (レナータ・グラスク)",
    "Renekton (レネクトン)",
    "Rengar (レンガー)",
    "Riven (リヴェン)",
    "Rumble (ランブル)",
    "Ryze (ライズ)",
    "Sejuani (セジュアニ)",
    "Senna (セナ)",
    "Seraphine (セラフィーン)",
    "Sett (セト)",
    "Shen (シェン)",
    "Shyvana (シヴァーナ)",
    "Singed (シンジド)",
    "Sion (サイオン)",
    "Sivir (シヴィア)",
    "Skarner (スカーナー)",
    "Smolder (スモルダー)",
    "Sona (ソナ)",
    "Soraka (ソラカ)",
    "Swain (スウェイン)",
    "Sylas (サイラス)",
    "Tahm Kench (タムケンチ)",
    "Taliyah (タリヤ)",
    "Talon (タロン)",
    "Taric (タリック)",
    "Teemo (ティーモ)",
    "Thresh (スレッシュ)",
    "Tristana (トリスターナ)",
    "Trundle (トランドル)",
    "Tryndamere (トリンダメア)",
    "Twisted Fate (ツイステッドフェイト)",
    "Twitch (トゥイッチ)",
    "Udyr (ウディア)",
    "Urgot (アーゴット)",
    "Varus (ヴァルス)",
    "Veigar (ヴェイガー)",
    "Vel'Koz (ヴェルコズ)",
    "Vex (ヴェックス)",
    "Vi (ヴァイ)",
    "Viego (ヴィエゴ)",
    "Viktor (ヴィクター)",
    "Vladimir (ブラッドミア)",
    "Volibear (ボリベア)",
    "Warwick (ワーウィック)",
    "Wukong (ウーコン)",
    "Xayah (ザヤ)",
    "Xerath (ゼラス)",
    "Xin Zhao (シンジャオ)",
    "Yasuo (ヤスオ)",
    "Yone (ヨネ)",
    "Yorick (ヨリック)",
    "Yuumi (ユーミ)",
    "Zac (ザック)",
    "Zed (ゼド)",
    "Zeri (ゼリ)",
    "Ziggs (ジグス)",
    "Zilean (ジリアン)",
    "Zoe (ゾーイ)",
    "Zyra (ザイラ)"
]

async def ChampionChoice(interaction:discord.Interaction, text: str,) -> list[app_commands.Choice[str]]: #これはなんのためにやっているの
    result_champions = []   #最終的に結果が入る
    for i in champions_list:   #チャンピオンごとに実行
        if text == i[:len(text)]:   #もし今打ってる文字とチャンピオン名の最初が同じなら
            result_champions.append(discord.app_commands.Choice(name=i,value=i))   #候補に追加していくよ
            if len(result_champions) >= 25:   #追加してて25個以上になってるなら
                return result_champions   #もう終わりってことでreturnするよ
    return result_champions   #ループが終了したので完成品をreturnするよ
    
@tree.command(name="build",description="選択したチャンピオンのビルドを表示します")
@discord.app_commands.describe(text="チャンピオンの名前を入力してください 参照: Aatrox, Ahri, Akali...") # 引数名=説明

@discord.app_commands.rename(text="champion") # 引数名=名前
# あとでチャンピオンの英語訳と韓国訳かこうかね

@discord.app_commands.autocomplete(text=ChampionChoice)
async def build(ctx:discord.Interaction,text:str):
    if text == "Aatrox (エイトロックス)" or text == "Aatrox":
        embed=discord.Embed(title="Aatrox Build",color=000000,url="https://u.gg",description="エイトロックスのビルドを表示しています")
        embed.set_image(url="https://lol-skin.weblog.vc/img/wallpaper/splash/Aatrox_8.jpg")
        embed.set_author(name="U.gg", 
                         url="https://u.gg",
                         icon_url="https://media.discordapp.net/attachments/1062457619274547222/1284223357671313409/image.png")
        embed.set_thumbnail(url="https://www.enthusiastgaming.com/wp-content/uploads/2022/04/UGG_Logo_White.png") 

        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="TopLane",url="https://u.gg/lol/champions/aatrox/build/top?rank=overall",style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="MidLane",url="https://u.gg/lol/champions/aatrox/build/mid?rank=overall",style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="ARAM",url="https://u.gg/lol/champions/aram/aatrox-aram",style=discord.ButtonStyle.primary))
        view.add_item(discord.ui.Button(label="Arena",url="https://u.gg/lol/champions/arena/aatrox-arena-build",style=discord.ButtonStyle.danger))
        await ctx.response.send_message(embed=embed ,view=view,ephemeral=True)

    elif text == "Ahri (アーリ)" or text == "Ahri":
        embed=discord.Embed(title="Ahri Build",color=000000,url="https://u.gg",description="アーリのビルドを表示しています")
        embed.set_image(url="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ahri_86.jpg")
        embed.set_author(name="U.gg", 
                         url="https://u.gg",
                         icon_url="https://media.discordapp.net/attachments/1062457619274547222/1284223357671313409/image.png")
        embed.set_thumbnail(url="https://www.enthusiastgaming.com/wp-content/uploads/2022/04/UGG_Logo_White.png") 

        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="TopLane",url="https://u.gg/lol/champions/ahri/build/top?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="MidLane",url="https://u.gg/lol/champions/ahri/build/mid?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="ARAM",url="https://u.gg/lol/champions/aram/ahri-aram" ,style=discord.ButtonStyle.primary))
        view.add_item(discord.ui.Button(label="Arena",url="https://u.gg/lol/champions/arena/ahri-arena-build" ,style=discord.ButtonStyle.danger))
        await ctx.response.send_message(embed=embed ,view=view,ephemeral=True)

    elif text == "Akali (アカリ)" or text == "Akali":
        embed=discord.Embed(title="Akali Build",color=000000,url="https://u.gg",description="アカリのビルドを表示しています")
        embed.set_image(url="https://www.riotgames.com/darkroom/1440/8bbf8ba11c0eb0209c7b158c3737d5c1:1a5740da15f2d3fb286a0a07ef598c7e/072622-star-guardian-akali-splash.png")
        embed.set_author(name="U.gg", 
                         url="https://u.gg",
                         icon_url="https://media.discordapp.net/attachments/1062457619274547222/1284223357671313409/image.png")
        embed.set_thumbnail(url="https://www.enthusiastgaming.com/wp-content/uploads/2022/04/UGG_Logo_White.png") 

        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="TopLane",url="https://u.gg/lol/champions/akali/build/top?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="MidLane",url="https://u.gg/lol/champions/akali/build/mid?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="ARAM",url="https://u.gg/lol/champions/aram/akali-aram" ,style=discord.ButtonStyle.primary))
        view.add_item(discord.ui.Button(label="Arena",url="https://u.gg/lol/champions/arena/akali-arena-build" ,style=discord.ButtonStyle.danger))
        await ctx.response.send_message(embed=embed ,view=view,ephemeral=True)

    elif text == "Akshan (アクシャン)" or text == "Akshan":
        embed=discord.Embed(title="Akshan Build",color=000000,url="https://u.gg",description="アクシャンのビルドを表示しています")
        embed.set_image(url="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Akshan_0.jpg")
        embed.set_author(name="U.gg", 
                         url="https://u.gg",
                         icon_url="https://media.discordapp.net/attachments/1062457619274547222/1284223357671313409/image.png")
        embed.set_thumbnail(url="https://www.enthusiastgaming.com/wp-content/uploads/2022/04/UGG_Logo_White.png") 

        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="TopLane",url="https://u.gg/lol/champions/akshan/build/top?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="MidLane",url="https://u.gg/lol/champions/akshan/build/mid?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="ARAM",url="https://u.gg/lol/champions/aram/akshan-aram" ,style=discord.ButtonStyle.primary))
        view.add_item(discord.ui.Button(label="Arena",url="https://u.gg/lol/champions/arena/akshan-arena-build" ,style=discord.ButtonStyle.danger))
        await ctx.response.send_message(embed=embed ,view=view,ephemeral=True)

    elif text == "Alistar (アリスター)" or text == "Alistar":
        embed=discord.Embed(title="Alistar Build",color=000000,url="https://u.gg",description="アリスターのビルドを表示しています")
        embed.set_image(url="https://www.mobafire.com/images/champion/skins/landscape/alistar-blackfrost-762x.jpg")
        embed.set_author(name="U.gg", 
                         url="https://u.gg",
                         icon_url="https://media.discordapp.net/attachments/1062457619274547222/1284223357671313409/image.png")
        embed.set_thumbnail(url="https://www.enthusiastgaming.com/wp-content/uploads/2022/04/UGG_Logo_White.png") 

        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="Support",url="https://u.gg/lol/champions/alistar/build/support?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="ARAM",url="https://u.gg/lol/champions/aram/alistar-aram" ,style=discord.ButtonStyle.primary))
        view.add_item(discord.ui.Button(label="Arena",url="https://u.gg/lol/champions/arena/alistar-arena-build" ,style=discord.ButtonStyle.danger))
        await ctx.response.send_message(embed=embed ,view=view,ephemeral=True)

    elif text == "Amumu (アムム)" or text == "Amumu":
        embed=discord.Embed(title="Amumu Build",color=000000,url="https://u.gg",description="アムムのビルドを表示しています")
        embed.set_image(url="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Amumu_24.jpg")
        embed.set_author(name="U.gg", 
                         url="https://u.gg",
                         icon_url="https://media.discordapp.net/attachments/1062457619274547222/1284223357671313409/image.png")
        embed.set_thumbnail(url="https://www.enthusiastgaming.com/wp-content/uploads/2022/04/UGG_Logo_White.png") 

        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="Jungle",url="https://u.gg/lol/champions/amumu/build/jungle?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="Support",url="https://u.gg/lol/champions/amumu/build/mid?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="ARAM",url="https://u.gg/lol/champions/aram/amumu-aram" ,style=discord.ButtonStyle.primary))
        view.add_item(discord.ui.Button(label="Arena",url="https://u.gg/lol/champions/arena/amumu-arena-build" ,style=discord.ButtonStyle.danger))
        await ctx.response.send_message(embed=embed ,view=view,ephemeral=True)

    elif text == "Anivia (アニビア)" or text == "Anivia":
        embed=discord.Embed(title="Anivia Build",color=000000,url="https://u.gg",description="アニビアのビルドを表示しています")
        embed.set_image(url="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Anivia_46.jpg")
        embed.set_author(name="U.gg", 
                         url="https://u.gg",
                         icon_url="https://media.discordapp.net/attachments/1062457619274547222/1284223357671313409/image.png")
        embed.set_thumbnail(url="https://www.enthusiastgaming.com/wp-content/uploads/2022/04/UGG_Logo_White.png") 

        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="MidLane",url="https://u.gg/lol/champions/anivia/build/mid?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="Support",url="https://u.gg/lol/champions/anivia/build/support?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="ARAM",url="https://u.gg/lol/champions/aram/anivia-aram" ,style=discord.ButtonStyle.primary))
        view.add_item(discord.ui.Button(label="Arena",url="https://u.gg/lol/champions/arena/anivia-arena-build" ,style=discord.ButtonStyle.danger))
        await ctx.response.send_message(embed=embed ,view=view,ephemeral=True)

    elif text == "Annie (アニー)" or text == "Annie":
        embed=discord.Embed(title="Annie Build",color=000000,url="https://u.gg",description="アニーのビルドを表示しています")
        embed.set_image(url="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Annie_22.jpg")
        embed.set_author(name="U.gg", 
                         url="https://u.gg",
                         icon_url="https://media.discordapp.net/attachments/1062457619274547222/1284223357671313409/image.png")
        embed.set_thumbnail(url="https://www.enthusiastgaming.com/wp-content/uploads/2022/04/UGG_Logo_White.png") 

        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="MidLane",url="https://u.gg/lol/champions/annie/build/mid?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="Support",url="https://u.gg/lol/champions/annie/build/support?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="ARAM",url="https://u.gg/lol/champions/aram/annie-aram" ,style=discord.ButtonStyle.primary))
        view.add_item(discord.ui.Button(label="Arena",url="https://u.gg/lol/champions/arena/annie-arena-build" ,style=discord.ButtonStyle.danger))
        await ctx.response.send_message(embed=embed ,view=view,ephemeral=True)

    elif text == "Aphelios (アフェリオス)" or text == "Aphelios":
        embed=discord.Embed(title="Aphelios Build",color=000000,url="https://u.gg",description="アフェリオスのビルドを表示しています")
        embed.set_image(url="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Aphelios_9.jpg")
        embed.set_author(name="U.gg", 
                         url="https://u.gg",
                         icon_url="https://media.discordapp.net/attachments/1062457619274547222/1284223357671313409/image.png")
        embed.set_thumbnail(url="https://www.enthusiastgaming.com/wp-content/uploads/2022/04/UGG_Logo_White.png") 

        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="AD Carry",url="https://u.gg/lol/champions/aphelios/build/adc?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="ARAM",url="https://u.gg/lol/champions/aram/aphelios-aram" ,style=discord.ButtonStyle.primary))
        view.add_item(discord.ui.Button(label="Arena",url="https://u.gg/lol/champions/arena/aphelios-arena-build" ,style=discord.ButtonStyle.danger))
        await ctx.response.send_message(embed=embed ,view=view,ephemeral=True)

    elif text == "Ashe (アッシュ)" or text == "Ashe":
        embed=discord.Embed(title="Ashe Build",color=000000,url="https://u.gg",description="アッシュのビルドを表示しています")
        embed.set_image(url="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ashe_17.jpg")
        embed.set_author(name="U.gg", 
                         url="https://u.gg",
                         icon_url="https://media.discordapp.net/attachments/1062457619274547222/1284223357671313409/image.png")
        embed.set_thumbnail(url="https://www.enthusiastgaming.com/wp-content/uploads/2022/04/UGG_Logo_White.png") 

        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="AD Carry",url="https://u.gg/lol/champions/ashe/build/adc?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="Support",url="https://u.gg/lol/champions/ashe/build/support?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="ARAM",url="https://u.gg/lol/champions/ashe/ahri-aram" ,style=discord.ButtonStyle.primary))
        view.add_item(discord.ui.Button(label="Arena",url="https://u.gg/lol/champions/arena/ashe-arena-build" ,style=discord.ButtonStyle.danger))
        await ctx.response.send_message(embed=embed ,view=view,ephemeral=True)

    elif text == "Aurelion Sol (オレリオンソル)" or text == "Aurelion Sol":
        embed=discord.Embed(title="Aurelion Sol Build",color=000000,url="https://u.gg",description="オレリオンソルのビルドを表示しています")
        embed.set_image(url="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/AurelionSol_31.jpg")
        embed.set_author(name="U.gg", 
                         url="https://u.gg",
                         icon_url="https://media.discordapp.net/attachments/1062457619274547222/1284223357671313409/image.png")
        embed.set_thumbnail(url="https://www.enthusiastgaming.com/wp-content/uploads/2022/04/UGG_Logo_White.png") 

        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="MidLane",url="https://u.gg/lol/champions/aurelionsol/build/mid?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="AP Carry",url="https://u.gg/lol/champions/aurelionsol/build/adc?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="ARAM",url="https://u.gg/lol/champions/aram/aurelionsol-aram" ,style=discord.ButtonStyle.primary))
        view.add_item(discord.ui.Button(label="Arena",url="https://u.gg/lol/champions/arena/aurelionsol-arena-build" ,style=discord.ButtonStyle.danger))
        await ctx.response.send_message(embed=embed ,view=view,ephemeral=True)

    elif text == "Aurora(オーロラ)" or text == "Aurora":
        embed=discord.Embed(title="Aurora Build",color=000000,url="https://u.gg",description="オーロラのビルドを表示しています")
        embed.set_image(url="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Aurora_0.jpg")
        embed.set_author(name="U.gg", 
                         url="https://u.gg",
                         icon_url="https://media.discordapp.net/attachments/1062457619274547222/1284223357671313409/image.png")
        embed.set_thumbnail(url="https://www.enthusiastgaming.com/wp-content/uploads/2022/04/UGG_Logo_White.png") 

        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="TopLane",url="https://u.gg/lol/champions/aurora/build/top?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="MidLane",url="https://u.gg/lol/champions/aurora/build/mid?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="ARAM",url="https://u.gg/lol/champions/aurora/ahri-aram" ,style=discord.ButtonStyle.primary))
        view.add_item(discord.ui.Button(label="Arena",url="https://u.gg/lol/champions/arena/aurora-arena-build" ,style=discord.ButtonStyle.danger))
        await ctx.response.send_message(embed=embed ,view=view,ephemeral=True)

    elif text == "Azir (アジール)" or text == "Azir":
        embed=discord.Embed(title="Azir Build",color=000000,url="https://u.gg",description="アジールのビルドを表示しています")
        embed.set_image(url="https://i.redd.it/4b3ivxdtvom91.jpg")
        embed.set_author(name="U.gg", 
                         url="https://u.gg",
                         icon_url="https://media.discordapp.net/attachments/1062457619274547222/1284223357671313409/image.png")
        embed.set_thumbnail(url="https://www.enthusiastgaming.com/wp-content/uploads/2022/04/UGG_Logo_White.png") 

        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="TopLane",url="https://u.gg/lol/champions/azir/build/top?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="MidLane",url="https://u.gg/lol/champions/azir/build/mid?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="ARAM",url="https://u.gg/lol/champions/azir/ahri-aram" ,style=discord.ButtonStyle.primary))
        view.add_item(discord.ui.Button(label="Arena",url="https://u.gg/lol/champions/arena/azir-arena-build" ,style=discord.ButtonStyle.danger))
        await ctx.response.send_message(embed=embed ,view=view,ephemeral=True)

    elif text == "Bard (バード)" or text == "Bard":
        embed=discord.Embed(title="Bard Build",color=000000,url="https://u.gg",description="バードのビルドを表示しています")
        embed.set_image(url="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Bard_26.jpg")
        embed.set_author(name="U.gg", 
                         url="https://u.gg",
                         icon_url="https://media.discordapp.net/attachments/1062457619274547222/1284223357671313409/image.png")
        embed.set_thumbnail(url="https://www.enthusiastgaming.com/wp-content/uploads/2022/04/UGG_Logo_White.png") 

        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="Support",url="https://u.gg/lol/champions/bard/build/top?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="ARAM",url="https://u.gg/lol/champions/aram/bard-aram" ,style=discord.ButtonStyle.primary))
        view.add_item(discord.ui.Button(label="Arena",url="https://u.gg/lol/champions/arena/bard-arena-build" ,style=discord.ButtonStyle.danger))
        await ctx.response.send_message(embed=embed ,view=view,ephemeral=True)

    elif text == "Bel'Veth (ベルヴェス)" or text == "Belveth":
        embed=discord.Embed(title="Bel'Veth Build",color=000000,url="https://u.gg",description="ベルヴェスのビルドを表示しています")
        embed.set_image(url="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Belveth_1.jpg")
        embed.set_author(name="U.gg", 
                         url="https://u.gg",
                         icon_url="https://media.discordapp.net/attachments/1062457619274547222/1284223357671313409/image.png")
        embed.set_thumbnail(url="https://www.enthusiastgaming.com/wp-content/uploads/2022/04/UGG_Logo_White.png") 

        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="TopLane",url="https://u.gg/lol/champions/belveth/build/top?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="Jungle",url="https://u.gg/lol/champions/belveth/build/jungle?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="ARAM",url="https://u.gg/lol/champions/aram/belveth-aram" ,style=discord.ButtonStyle.primary))
        view.add_item(discord.ui.Button(label="Arena",url="https://u.gg/lol/champions/arena/belveth-arena-build" ,style=discord.ButtonStyle.danger))
        await ctx.response.send_message(embed=embed ,view=view,ephemeral=True)
 
    elif text == "Blitzcrank (ブリッツクランク)" or text == "Blitzcrank":
        embed=discord.Embed(title="Blitzcrank Build",color=000000,url="https://u.gg",description="ブリッツクランクのビルドを表示しています")
        embed.set_image(url="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Blitzcrank_29.jpg")
        embed.set_author(name="U.gg", 
                         url="https://u.gg",
                         icon_url="https://media.discordapp.net/attachments/1062457619274547222/1284223357671313409/image.png")
        embed.set_thumbnail(url="https://www.enthusiastgaming.com/wp-content/uploads/2022/04/UGG_Logo_White.png") 

        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="Support",url="https://u.gg/lol/champions/blitzcrank/build/support?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="ARAM",url="https://u.gg/lol/champions/aram/blitzcrank-aram" ,style=discord.ButtonStyle.primary))
        view.add_item(discord.ui.Button(label="Arena",url="https://u.gg/lol/champions/arena/blitzcrank-arena-build" ,style=discord.ButtonStyle.danger))
        await ctx.response.send_message(embed=embed ,view=view,ephemeral=True)

    elif text == "Brand (ブランド)" or text == "Brand":
        embed=discord.Embed(title="Brand Build",color=000000,url="https://u.gg",description="ブランドのビルドを表示しています")
        embed.set_image(url="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Brand_21.jpg")
        embed.set_author(name="U.gg", 
                         url="https://u.gg",
                         icon_url="https://media.discordapp.net/attachments/1062457619274547222/1284223357671313409/image.png")
        embed.set_thumbnail(url="https://www.enthusiastgaming.com/wp-content/uploads/2022/04/UGG_Logo_White.png") 

        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="Jungle",url="https://u.gg/lol/champions/brand/build/jungle?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="MidLane",url="https://u.gg/lol/champions/brand/build/mid?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="AP Carry",url="https://u.gg/lol/champions/brand/build/adc?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="Support",url="https://u.gg/lol/champions/brand/build/support?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="ARAM",url="https://u.gg/lol/champions/aram/brand-aram" ,style=discord.ButtonStyle.primary))
        view.add_item(discord.ui.Button(label="Arena",url="https://u.gg/lol/champions/arena/brand-arena-build" ,style=discord.ButtonStyle.danger))
        await ctx.response.send_message(embed=embed ,view=view,ephemeral=True)
 
    elif text == "Braum (ブラウム)" or text == "Braum":
        embed=discord.Embed(title="Braum Build",color=000000,url="https://u.gg",description="ブラウムのビルドを表示しています")
        embed.set_image(url="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Braum_11.jpg")
        embed.set_author(name="U.gg", 
                         url="https://u.gg",
                         icon_url="https://media.discordapp.net/attachments/1062457619274547222/1284223357671313409/image.png")
        embed.set_thumbnail(url="https://www.enthusiastgaming.com/wp-content/uploads/2022/04/UGG_Logo_White.png") 

        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="Support",url="https://u.gg/lol/champions/braum/build/support?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="ARAM",url="https://u.gg/lol/champions/aram/braum-aram" ,style=discord.ButtonStyle.primary))
        view.add_item(discord.ui.Button(label="Arena",url="https://u.gg/lol/champions/arena/braum-arena-build" ,style=discord.ButtonStyle.danger))
        await ctx.response.send_message(embed=embed ,view=view,ephemeral=True)

    elif text == "Briar (ブライアー)" or text == "Briar":
        embed=discord.Embed(title="Briar Build",color=000000,url="https://u.gg",description="ブライアーのビルドを表示しています")
        embed.set_image(url="https://static.wikia.nocookie.net/leagueoflegends/images/5/52/Briar_PrimordianSkin.jpg")
        embed.set_author(name="U.gg", 
                         url="https://u.gg",
                         icon_url="https://media.discordapp.net/attachments/1062457619274547222/1284223357671313409/image.png")
        embed.set_thumbnail(url="https://www.enthusiastgaming.com/wp-content/uploads/2022/04/UGG_Logo_White.png") 

        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="Jungle",url="https://u.gg/lol/champions/briar/build/jungle?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="ARAM",url="https://u.gg/lol/champions/aram/briar-aram" ,style=discord.ButtonStyle.primary))
        view.add_item(discord.ui.Button(label="Arena",url="https://u.gg/lol/champions/arena/briar-arena-build" ,style=discord.ButtonStyle.danger))
        await ctx.response.send_message(embed=embed ,view=view,ephemeral=True)

    elif text == "Caitlyn (ケイトリン)" or text == "Caitlyn":
        embed=discord.Embed(title="Caitlyn Build",color=000000,url="https://u.gg",description="ケイトリンのビルドを表示しています")
        embed.set_image(url="https://lolninja.net/wp-content/uploads/2021/11/Caitlyn_SheriffSkin-1024x604.jpg")
        embed.set_author(name="U.gg", 
                         url="https://u.gg",
                         icon_url="https://media.discordapp.net/attachments/1062457619274547222/1284223357671313409/image.png")
        embed.set_thumbnail(url="https://www.enthusiastgaming.com/wp-content/uploads/2022/04/UGG_Logo_White.png") 

        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="AD Carry",url="https://u.gg/lol/champions/caitlyn/build/adc?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="ARAM",url="https://u.gg/lol/champions/aram/caitlyn-aram" ,style=discord.ButtonStyle.primary))
        view.add_item(discord.ui.Button(label="Arena",url="https://u.gg/lol/champions/arena/caitlyn-arena-build" ,style=discord.ButtonStyle.danger))
        await ctx.response.send_message(embed=embed ,view=view,ephemeral=True)

    elif text == "Camille (カミール)" or text == "Camille":
        embed=discord.Embed(title="Camille Build",color=000000,url="https://u.gg",description="カミールのビルドを表示しています")
        embed.set_image(url="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Camille_2.jpg")
        embed.set_author(name="U.gg", 
                         url="https://u.gg",
                         icon_url="https://media.discordapp.net/attachments/1062457619274547222/1284223357671313409/image.png")
        embed.set_thumbnail(url="https://www.enthusiastgaming.com/wp-content/uploads/2022/04/UGG_Logo_White.png") 

        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="TopLane",url="https://u.gg/lol/champions/camille/build/top?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="Support",url="https://u.gg/lol/champions/camille/build/support?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="ARAM",url="https://u.gg/lol/champions/aram/camille-aram" ,style=discord.ButtonStyle.primary))
        view.add_item(discord.ui.Button(label="Arena",url="https://u.gg/lol/champions/arena/camille-arena-build" ,style=discord.ButtonStyle.danger))
        await ctx.response.send_message(embed=embed ,view=view,ephemeral=True)

    elif text == "Cassiopeia (カシオペア)" or text == "Cassiopeia":
        embed=discord.Embed(title="Cassiopeia Build",color=000000,url="https://u.gg",description="カシオペアのビルドを表示しています")
        embed.set_image(url="https://i.pinimg.com/originals/55/85/e1/5585e1604b3bc97df16576260e617d3a.jpg")
        embed.set_author(name="U.gg", 
                         url="https://u.gg",
                         icon_url="https://media.discordapp.net/attachments/1062457619274547222/1284223357671313409/image.png")
        embed.set_thumbnail(url="https://www.enthusiastgaming.com/wp-content/uploads/2022/04/UGG_Logo_White.png") 

        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="TopLane",url="https://u.gg/lol/champions/cassiopeia/build/top?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="MidLane",url="https://u.gg/lol/champions/cassiopeia/build/mid?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="ARAM",url="https://u.gg/lol/champions/aram/cassiopeia-aram" ,style=discord.ButtonStyle.primary))
        view.add_item(discord.ui.Button(label="Arena",url="https://u.gg/lol/champions/arena/cassiopeia-arena-build" ,style=discord.ButtonStyle.danger))
        await ctx.response.send_message(embed=embed ,view=view,ephemeral=True)

    elif text == "Cho'Gath (チョガス)" or text == "Chogath":
        embed=discord.Embed(title="Cho'Gath Build",color=000000,url="https://u.gg",description="チョガスのビルドを表示しています")
        embed.set_image(url="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ahri_86.jpg")
        embed.set_author(name="U.gg", 
                         url="https://u.gg",
                         icon_url="https://media.discordapp.net/attachments/1062457619274547222/1284223357671313409/image.png")
        embed.set_thumbnail(url="https://www.enthusiastgaming.com/wp-content/uploads/2022/04/UGG_Logo_White.png") 

        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="TopLane",url="https://u.gg/lol/champions/chogath/build/top?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="Jungle",url="https://u.gg/lol/champions/chogath/build/jungle?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="MidLane",url="https://u.gg/lol/champions/chogath/build/mid?rank=overall" ,style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="ARAM",url="https://u.gg/lol/champions/aram/chogath-aram" ,style=discord.ButtonStyle.primary))
        view.add_item(discord.ui.Button(label="Arena",url="https://u.gg/lol/champions/arena/chogath-arena-build" ,style=discord.ButtonStyle.danger))
        await ctx.response.send_message(embed=embed ,view=view,ephemeral=True)


    else:
        await ctx.response.send_message("そのチャンピオンは存在しません",ephemeral=True)

# @tree.command(name="skins",description="チャンピオンのスキンの一覧を表示します")
# @discord.app_commands.autocomplete(text=ChampionChoice)
# @discord.app_commands.describe(text="チャンピオンの名前を入力してください 参照: Aatrox, Ahri, Akali...") # 引数名=説明
# @discord.app_commands.rename(text="champion") # 引数名=名前
# async def champions(inetraction:discord.Interaction,text:str):
#     await inetraction.response.send_message("https://u.gg", ephemeral=True)

@tree.command(name="quiz",description="チャンピオンのスキルアイコンでクイズができます。")
async def champions(inetraction:discord.Interaction,):
    await inetraction.response.send_message("https://u.gg", ephemeral=True)

# 今日はファイルを参照したクイズの作り方を学ぶ random.choiceを使う ↑


client.run(TOKEN)