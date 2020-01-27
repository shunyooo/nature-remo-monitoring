cp .env .env.yml
sed -i '' -e "s/=/: /g" .env.yml
gcloud functions deploy nature-remo-spread-sheet --runtime python37 --trigger-topic=nature-remo-monitoring --entry-point run --env-vars-file .env.yml
rm .env.yml