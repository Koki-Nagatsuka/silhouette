# シルエットメーカー

## Pipenv のインストール

`Pipenv` をまだインストールしていない場合は、以下のコマンドでインストールする。

```bash
pip install pipenv
```

## 仮想環境のセットアップ

1. ルートディレクトリに移動する。

```bash
cd path/to/your/dir
```

2. 仮想環境を起動し、必要な依存関係を同時にインストールする。

```bash
pipenv shell
pipenv install --dev
```

## 使用方法

シルエットに加工したい画像を`images`ディレクトリに保存する。

```bash
python app.py
```
