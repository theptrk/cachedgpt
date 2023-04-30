# cachedgpt

Q: Are you tired of wasting tokens on OpenAI calls with THE SAME TOKENS?

A: Cache your responses!

## How to setup
step: create, activate your virtual env
`$ python -m venv env`
`$ source env/bin/activate`

step: install requirements
`$ pip install -r requirements.txt`

step: set up your env variables
`echo "YOUR_OPENAI_API_KEY" > .env`

step: run server
`$ uvicorn main:app --reload --port 8001`

## How to use

Example curl to request a completion
```
curl -X POST "http://localhost:8001/chatCompletion" \
    -H "accept: application/json" \
    -H "Content-Type: application/json" \
    -d '{"messages": [{"role": "user", "content": "hi"}]}'
```

Example curl to get all completions
```
curl "http://localhost:8001/chatCompletions"
```
