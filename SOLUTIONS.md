There have been created 3 solutions to this problem in three different branches:

### 1. Asyncio

This solution makes use of Asyncio library to achieve asynchronous running of the task. Although the task does run asynchronously, it still blocks the main request and the server or the client may still fail due to timeout issues.

This solution can be found under [this github branch](https://github.com/HarithJ/fastapi-async-tasks/tree/asyncio).

### 2. FastAPI Backgroud Tasks

This solution uses the FastAPI's inbuilt Background Tasks Class to put the task in the background. Although this does the trick, its still not very performant for large scale systems because it will be taking up lots of CPU resources. 

This solution can be found under [this github branch](https://github.com/HarithJ/fastapi-async-tasks/tree/background-tasks).

### 🔥 3. Celery Implementation

This Solution uses Celery and Redis to run the task asynchronously. When the user hits the `normalize_merchant` endpoint, s/he gets immediate feedback and the task gets put in a queue and then it is handled by the celery worker. This solution is the BEST.

This solution can be found under [this github branch](https://github.com/HarithJ/fastapi-async-tasks/tree/celery-implementation).
