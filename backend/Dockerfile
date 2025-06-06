# ベースイメージ
FROM node:20

# 作業ディレクトリ
WORKDIR /app

# 依存関係インストール
COPY package*.json ./
RUN npm install

# アプリケーションのソースコードをコピー
COPY . .

# アプリケーション起動
CMD ["node", "app.js"]

# 必要なポート
EXPOSE 5000
