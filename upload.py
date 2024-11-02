import discord
from discord import app_commands
import os

# ボットのトークン
TOKEN = os.getenv("TOKEN")

# ファイルを保存するディレクトリ
SAVE_DIRECTORY = "/app/data"

# Botをインスタンス化
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# ディレクトリが存在しない場合は作成
if not os.path.exists(SAVE_DIRECTORY):
    os.makedirs(SAVE_DIRECTORY)


@client.event
async def on_ready() -> None:
    # アクティビティを設定
    new_activity = f"ふんふんふん"
    await client.change_presence(activity=discord.CustomActivity(new_activity))
    await tree.sync()


@tree.command(name="upload", description="ファイルアップロードするよ")
@app_commands.describe(file="アップロードするファイル")
async def upload(interaction: discord.Interaction, file: discord.Attachment) -> None:

    await interaction.response.send_message("アップしますちょいまち")
    # ファイルの保存パスを作成
    file_path = os.path.join(SAVE_DIRECTORY, file.filename)

    try:
        # 既に同名のファイルまたはディレクトリが存在するか確認
        if os.path.exists(file_path):
            await interaction.edit_original_response(
                content=f"エラー: {file.filename} は既にあるみたい"
            )
            return

        # ファイルを保存
        await file.save(file_path)
        # ユーザーに通知
        await interaction.edit_original_response(
            content=f"{file.filename} を保存したよ！ファイルサイズ: {file.size} bytes"
        )
    except Exception as e:
        await interaction.edit_original_response(
            content=f"ファイルの保存に失敗したみたい：{e}", ephemeral=True
        )


client.run(TOKEN)
