# Debugging task

## Task

Debug a nameko service which compute the sum of current month, minute and second every 5 second.

Example:

```
Current time: 2021-06-23 10:43:35.885372
Sum: 84

Current time: 2021-06-23 10:45:37.885372
Sum: 88
```


## Steps to run the solution

### 1. Start redis docker-compose

```
cd ./docker
docker-compose up -d
```

### 2. Setup Python 3.9 (tested on 3.9.19) environment using requirement.txt.

### 3. Run Nameko service

```
 nameko run --config config.yaml service
```
