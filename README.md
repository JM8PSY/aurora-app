````markdown
# Aurora Observation Support System

このプロジェクトは、低緯度オーロラ観測支援システムです。FastAPI（バックエンド）、React + Vite（フロントエンド）、PostgreSQL（DB）をDocker Composeで統合し、ホットリロード対応の開発環境を構築しています。

---

## 動作環境

- Docker
- Docker Compose

---

## 起動方法

```bash
git clone https://github.com/your-repo/aurora-app.git
cd aurora-app
docker-compose up --build
````

* バックエンドAPI: [http://localhost:5000](http://localhost:5000)
* フロントエンド: [http://localhost:3000](http://localhost:3000)

---

## 開発のポイント

* ソースコードはコンテナにマウントされているため編集即反映
* FastAPIは `uvicorn --reload` でホットリロード対応
* Viteの開発サーバーもホットリロード対応済み

---

## ディレクトリ構成例

```
aurora-app/
├─ backend/
│  ├─ app/
│  │  └─ main.py
│  ├─ Dockerfile
│  └─ requirements.txt
├─ frontend/
│  ├─ src/
│  ├─ Dockerfile
│  ├─ package.json
│  └─ vite.config.js
└─ docker-compose.yml
```

---

## 技術スタック

* バックエンド: Python, FastAPI, Uvicorn
* フロントエンド: React, Vite
* データベース: PostgreSQL
* コンテナ管理: Docker, Docker Compose

---

## 注意事項

* PostgreSQLデータはボリュームで永続化
* WindowsのDockerでのマウント設定に注意

---

## 問い合わせ

ご質問はIssueかPRでお気軽にどうぞ。

```
