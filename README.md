## ▶️ How to run

Before you run the application, make sure you have installed the following:
- Docker
- Docker Compose

### Step 1: Build and run

```
docker-compose up --build
```

### Step 2: test

Use the below command to test out the API endpoint:
```
curl -X 'POST' \
  'http://127.0.0.1:9898/normalize_merchant' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "date": "2021-04-01",
  "description": "Payment Netflix APRIL***",
  "amount": 12.99
}'
```

Head over to `localhost:5556` to see the status of the above query.

