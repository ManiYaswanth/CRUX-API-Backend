import os

class CRUXAPIConfig:
    API_KEY = os.getenv("CRUX_API_KEY")
    url = "https://chromeuxreport.googleapis.com/v1/records:queryRecord?"

