# NatureRemo Monitoring

[English](./README.md) | **日本語**

[Nature Remo Cloud API](https://developer.nature.global/) から室温, 湿度, 照度, 動きを毎分監視し、GoogleSpreadSheet に保存する Pythonスクリプト。Cloud Functions にデプロイ可能。



#### 初期設定

1. https://home.nature.global/ から Nature Remo のアクセストークンを取得してください
2.  https://console.developers.google.com/iam-admin/serviceaccounts からGoogleサービスアカウントを作成か選択して認証ファイル.jsonを取得してください
3. https://docs.google.com/spreadsheets/create からスプレッドシートを作成してください

4. 以下の [.env](.env) ファイルを設定します

```yml
REMO_TOKEN={NatureRemoのアクセストークン}
GOOGLE_APPLICATION_CREDENTIALS={Googleの認証ファイルパス}
SHEET_NAME={スプレッドシート名}
```



#### ローカル実行

```bash
docker-compose up
```



#### Cloud Functionにデプロイ

1. [(Google Cloud SDK をインストール)](https://cloud.google.com/sdk/docs/downloads-interactive?hl=ja)
2. `sh deploy.sh`
3. Pub/Sub scheduler を設定