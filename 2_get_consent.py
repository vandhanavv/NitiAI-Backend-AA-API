import requests

url = "https://fiu-uat.setu.co/consents/webview/e7b4bca6-4a09-4d0f-ac24-4a8a28e3b8db"

headers = {
	"x-client-id": "255d0b6c-492d-44cf-8581-e9494c7b0914",
	"x-client-secret": "9c2fc756-3d17-46d6-b28d-be4d71953e83"
}

response = requests.request("get", url, headers=headers)

print(response.text)