# NitiAI-Backend-AA-API
To run the project:
- Create a consent by running the program '1_create_consent.py' in the terminal (POST request):
```
python 1_create_consent.py
```
- Click on the consent manager URL in the response obtained as part of the first step, webview the same, login to oneMoney to verify the bank accounts and approve data sharing.
- Get the consent status by running the program '2_get_consent.py' (GET request):
```
python 1_get_consent.py
```
- If the status is "ACTIVE", create a data session by running the program '3_create_datasession.py' in the terminal (POST request):
```
python 3_create_datasession.py
```
- Finally, we try to fetch the data by running the program '4_fetch_data.py' in the terminal (GET request):
```
python 4_fetch_data.py
```
