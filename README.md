# gemini-image-forge

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

`gemini-image-forge` は、Google の Gemini API を使って、テキストプロンプトから画像を生成したり、既存の画像にスタイルを適用したりできる Python スクリプトです。

## 使い方

### 1. 必要なもの

*   Python 3.7 以上
*   Google Cloud Platform (GCP) のアカウント
*   Gemini API キー

### 2. API キーの取得

Gemini API を利用するには、API キーが必要です。以下の手順で取得してください。

1.  Google AI Studio にアクセスします: [https://ai.google.dev/](https://ai.google.dev/)
2.  画面の指示に従って、API キーを取得します。
3.  取得した API キーを環境変数 `GEMINI_API_KEY` に設定します。

### 3. スクリプトの実行

#### 画像生成

```bash
python gemini_image_generator.py "生成したい画像のプロンプト"
```

例:

```bash
python gemini_image_generator.py "翼のある豚が、緑豊かな未来的なSF都市の上空を飛んでいる3Dレンダリング画像"
```

生成された画像は `output` ディレクトリに保存されます。

#### 画像変換

```bash
python gemini_image_transform.py <画像パス> "適用したいスタイルのプロンプト"
```

例:

```bash
python gemini_image_transform.py input.jpg "水彩画風"
```

変換された画像は `output` ディレクトリに保存されます。

## ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。詳細は [LICENSE](LICENSE) ファイルをご覧ください。
