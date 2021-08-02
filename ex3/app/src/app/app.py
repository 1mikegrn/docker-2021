import requests

def main():
    resp = requests.get("http://localhost:8081/v1")
    print(resp.json())
