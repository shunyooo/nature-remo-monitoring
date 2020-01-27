# NatureRemo Monitoring

**English** | [日本語](./README-ja.md)

#### SETUP

1. Get Nature Remo access token from https://home.nature.global/.
2. Create or get google service account from https://console.developers.google.com/iam-admin/serviceaccounts, and download credintial json file.
3. Create spread sheet from https://docs.google.com/spreadsheets/create.

set [.env](.env).

```yml
REMO_TOKEN={YOUR_REMO_TOKEN}
GOOGLE_APPLICATION_CREDENTIALS={YOUR_GOOGLE_CREDINTIAL_FILE_PATH}
SHEET_NAME={YOUR_SPREAD_SHEET_NAME}
```



#### Local RUN

```bash
docker-compose up
```



#### Deploy Cloud Functions

1. [(Install Google Cloud SDK)](https://cloud.google.com/sdk/docs/downloads-interactive?hl=ja)
2. `sh deploy.sh`
3. Setting Pub/Sub scheduler.