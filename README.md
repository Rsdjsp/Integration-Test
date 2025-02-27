# Integration-Test

Nexton Integration Test

## Requirements

- Docker
- Docker Compose

## Instructions to Run the Project

1. Clone the repository:
   ```sh
   git clone <REPOSITORY_URL>
   cd Integration-Test

2. run command:
    ```sh
    docker-compose up --build
3. Make a postman request:
    ```sh
    curl --location 'http://127.0.0.1:5000/calculate' \
    --header 'Content-Type: application/json' \
    --data '{
    "expression": "2 + 2 * 2"
    }'
4. Validate Response on logs


