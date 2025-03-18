# NiceGUI Chat with OpenAI Agent SDK

NiceGUIを使用したチャットアプリケーションです。OpenAI Agent SDKを統合して、インターネット検索機能などを備えたAIチャットを実現しています。

## 機能

- カウンターページ: シンプルなカウンター機能
- AIチャットページ: OpenAI Agent SDKを使用した高度なチャット機能
  - インターネット検索機能
  - 自然な会話体験

## セットアップ

1. 必要なパッケージをインストール:

```bash
uv pip install -e .
```

2. 環境変数を設定:

`.env.example`ファイルをコピーして`.env`を作成し、APIキーを設定:

```bash
cp .env.example .env
```

`.env`ファイルを編集してAPIキーを設定:
```
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here  # オプション
```

## 実行方法

```bash
python run.py
```

または:

```bash
python -m src.main
```

ブラウザで http://localhost:8081 にアクセスしてアプリケーションを使用できます。

## 注意事項

- OpenAI APIキーが必要です
- インターネット検索機能を使用する場合はTavily APIキーも必要です
