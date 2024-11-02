# **discordbot-file-uploader**

discordbotファイルアップローダー

discordbotで投げたファイルをローカルに保存する


https://github.com/user-attachments/assets/3bc00493-a34d-43e9-a939-67e0450b3438

↑NAS（Sambaで構築）と連携もできます。

## つかいかた

### 1. DiscordBotの作成

[https://discord.com/developers/applications](https://discord.com/developers/applications)

からアプリケーションを作成（詳細は省略）

トークンは1度しか表示されないので控えておく

bot, Send Messages, View Channels, Attach FilesをONにする

作成されたGENERATED URLをブラウザ等で入力し、お好みのサーバーへ

（※管理者権限が必要です）

### 2. upload.pyを動かす

```bash
git clone https://github.com/ABfry/discordbot-file-uploader.git
```


.env.example を参考に 

.envを作成し、先程作成したトークンと保存先にしたいディレクトリのパスを入力する

![スクリーンショット 2024-11-02 16 01 31](https://github.com/user-attachments/assets/7f60839e-7f06-4f94-a27d-48e3dc672dd2)

```bash
docker-compose up
```

おわり。
