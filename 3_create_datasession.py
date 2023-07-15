import requests

url = "https://fiu-uat.setu.co/sessions"

payload = {
	"consentId": "7f867706-fb7c-4a45-a34f-8a59d4380ffc",
	"DataRange": {
		"from": "2020-04-01T00:00:00Z",
		"to": "2023-01-01T00:00:00Z"
	},
	"format": "json"
}
headers = {
	"x-client-id": "255d0b6c-492d-44cf-8581-e9494c7b0914",
	"x-client-secret": "9c2fc756-3d17-46d6-b28d-be4d71953e83"
}

response = requests.request("post", url, json=payload, headers=headers)

print(response.text)