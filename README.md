This tool will aggregate core financial indicators of companies for convenient comparison.
Example:
![](demo.jpg)

Enable Google Sheets API - https://developers.google.com/sheets/api/quickstart/python
Also helful links (if the first one did not help):
https://medium.com/@a.marenkov/how-to-get-credentials-for-google-sheets-456b7e88c430
https://stackoverflow.com/questions/56445257/valueerror-client-secrets-must-be-for-a-web-or-installed-app

Place `credentials.json` file into project's root.

Install dependencies with:
```
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib yfinance --no-cache-dir
```

Run `python3 start.py` to create stock analysis spreadsheet
