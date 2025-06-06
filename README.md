# Aurora Observation Support System

低緯度オーロラの観測を支援するWebアプリです。気象情報、地磁気、雲量、光害などをもとに観測可能性を評価します。

## 構成

- フロントエンド：React + Vite
- バックエンド：Node.js + Express
- データベース：PostgreSQL
- インフラ：Docker / docker-compose

## セットアップ

```bash
git clone https://github.com/jm8psy/aurora-app.git
cd aurora-app
docker compose up --build
```

- フロントエンド： http://localhost:3000  
- バックエンド： http://localhost:5000

## ディレクトリ構成

```
aurora-app/
├── backend/         # Node.js API
│   └── Dockerfile
├── frontend/        # Reactアプリ
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## ライセンス

MIT
