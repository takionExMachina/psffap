import requests

url = 'https://docs.google.com/<your-google-forms-url>'
form_data = {'<textarea-name>':'<some text>'}
r = requests.post(url, data=form_data)
