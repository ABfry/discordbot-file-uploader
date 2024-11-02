# ベースイメージ
FROM python:3.9-slim

# 作業ディレクトリ
WORKDIR /app

# ライブラリ
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

# 実行
CMD ["python", "upload.py"]
