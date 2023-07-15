import requests
from datetime import datetime
now = datetime.now().isoformat()[:-3] + "Z"

url = "https://fiu-uat.setu.co/consents"

payload = {
	"Detail": {
		"consentStart": now,
		"consentExpiry": "2025-04-23T05:44:53.822Z",
		"Customer": {"id": "9500057910@onemoney"},
		"FIDataRange": {
			"from": "2020-04-01T00:00:00Z",
			"to": "2023-01-01T00:00:00Z"
		},
		"consentMode": "STORE",
		"consentTypes": ["TRANSACTIONS", "PROFILE", "SUMMARY"],
		"fetchType": "PERIODIC",
		"Frequency": {
			"value": 30,
			"unit": "MONTH"
		},
		"DataFilter": [
			{
				"type": "TRANSACTIONAMOUNT",
				"value": "5000",
				"operator": ">="
			}
		],
		"DataLife": {
			"value": 1,
			"unit": "MONTH"
		},
		"DataConsumer": {"id": "setu-fiu-id"},
		"Purpose": {
			"Category": {"type": "string"},
			"code": "101",
			"text": "Loan underwriting",
			"refUri": "https://api.rebit.org.in/aa/purpose/101.xml"
		},
		"fiTypes": ["DEPOSIT", "EQUITIES"]
	},
	"redirectUrl": "https://setu.co",
	"context": [
		{
			"key": "accounttype",
			"value": "somevalue"
		}
	]
}
headers = {
	"x-client-id": "255d0b6c-492d-44cf-8581-e9494c7b0914",
	"x-client-secret": "9c2fc756-3d17-46d6-b28d-be4d71953e83"
}

response = requests.request("post", url, json=payload, headers=headers)

print(response.text)