# Data Management Agent by ADK + Toolbox

## Abstract
- ADK と MCP Toolbox for Database を使ってデータマネジメントするエージェントのデモ
- サンプルとして企業マスタをメンテナンスするのを手伝うエージェントを作成

## Getting Started
```sh
$ cd /path/to/adk-data-management-agent/

# GOOGLE_CLOUD_PROJECT を自分のプロジェクトに置き換える
$ cp .env.sample .env
$ vim .env

# {YOUR_PROJECT_ID} を自分のプロジェクトに置き換える
$ cp toolbox/tools.yml.sample toolbox/tools.yml
$ vim toolbox/tools.yml

# もしまだ Google Cloud の認証情報を取得していなかったら以下を実行
$ gcloud auth application-default login

# Docker で起動
$ docker compose build
$ docker compose up -d
```

`http://localhost:8000` へアクセス

## Tools
- `list-companies`: すべての企業データを取得します。
- `search-companies-by-name`: 企業名で企業データを検索します。
- `add-company`: 新しい企業データを追加します。
- `delete-company`: 企業データを削除します。
- `init-company-master`: company_masterテーブルを初期化します（テスト用）。
- `update-corporate-number`: 企業の法人番号を更新します。
- `update-company-name`: 企業名を更新します。
