import httpx

with httpx.Client() as client:
    r = client.get(url="http://172.17.0.2:8000/healthcheck/")
    print(r.json())
