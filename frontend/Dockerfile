# ベースイメージ
FROM node:20

# 作業ディレクトリ
WORKDIR /app

# 依存関係インストール
COPY package*.json ./
RUN npm install

# ソースコードをコピー
COPY . .

# Vite 開発サーバー起動
CMD ["npm", "run", "dev"]

# Viteのデフォルトポート
EXPOSE 5173
