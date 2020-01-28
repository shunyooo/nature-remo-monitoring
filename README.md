# NatureRemo Monitoring

**English** | [日本語](./README-ja.md)

A Python script that monitors room temperature, humidity, illuminance, and motion every minute with the [Nature Remo Cloud API](https://developer.nature.global/) and saves it in GoogleSpreadSheet. Deployable to Cloud Functions.



#### SETUP

1. Get Nature Remo access token from https://home.nature.global/.
2. Create or get google service account from https://console.developers.google.com/iam-admin/serviceaccounts, and download credintial json file.
3. Create spread sheet from https://docs.google.com/spreadsheets/create. (Set to 10 columns and 500000 rows)

4. set [.env](.env).

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

1. [(Install Google Cloud SDK)](https://cloud.google.com/sdk/docs/downloads-interactive)
2. `sh deploy.sh`
3. Setting Pub/Sub scheduler.