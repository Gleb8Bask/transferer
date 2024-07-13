1. Initiation message prints bot commands and help
2. Bot commands:
- /start - initiation message
- /summarize - prints ML aggregated news of the day
- /statistics - prints statistics
- /send - sends news of the day to database where Kafka reads with CDC, then SPARK puts to S3
https://www.notion.so/blog/building-and-scaling-notions-data-lake

TELEGRAM_BOT_TOKEN=7490241795:AAEjpT-1pX9K8SoKQ7nH-kavTpmN4AvwjCA python bot.py