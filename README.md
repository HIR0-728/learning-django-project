# learning-django-project

## 概要
- Django学習用リポジトリ

## 開発環境構築
Dockerコンテナを使って開発する。

### 依存パッケージ
- Dockerimage:python3.11.1-slim-bullseye
- パッケージについては[pyproject.toml](./pyproject.toml)を参照

### ローカルでの動作確認
#### Dockerコンテナを使用する
```sh
$ cd learning-django-project

$ make local-container-build
$ make local-container-up

$ make log

$ make container-down
```

#### 仮想環境を用意する
- poetry動作環境を想定

```sh
$ cd learning-django-project

$ poetry install
$ poetry shell

$ make local-run
```