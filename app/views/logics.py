from flask import Blueprint
import requests
from config.constants import CRUXAPIConfig
import traceback

CRUX_API_KEY = CRUXAPIConfig.API_KEY
CRUX_URL = CRUXAPIConfig.url
mod = Blueprint("logics", __name__, template_folder="templates")

def validate_request(data):
    '''
    Validates the received request
        args: request object
        returns: valid or invalid string
    '''
    if not data or not data.get("urls"):
        return "invalid"
    urls = data["urls"].split(",")
    for url in urls:
        if "www." in url:
            return "invalid"
    return "valid"

def get_crux_data_report(urls: list, metric_filter: list, threshold_filter: str):
    '''
    Receives data from CRUX API for the urls received from request
        args:
            urls - List of urls from request received
            metric_filter - List of metrics to be filtered out
            threshold_filter - string value to be filtered out
        return:
            List of responses from the API.
    '''
    formatted_response = []
    for url in urls:
        crux_api_url = f'{CRUX_URL}key={CRUX_API_KEY}'
        response = requests.post(crux_api_url, json={"origin": url})
        if response:
            response = response.json()
            formatted_response.extend(format_crux_api_response(response, url, metric_filter, threshold_filter))
        else:
            return "error"
    return formatted_response

def format_crux_api_response(data: dict, url: str, metric_filter: str, threshold_filter: str):
    '''
    formats and filteres the response receievd from API into 
    table structure to display on the frontend 
        args:
            data - Json data received from API
            url - str url for which the data is received from API
            metric_filter - List of metrics to be filtered out
            threshold_filter - string value to be filtered out
        return:
            List of filtered responses
    '''
    formatted_response = []
    try:
        for metric, metric_data in data["record"]["metrics"].items():
            p75 = metric_data["percentiles"]["p75"]
            threshold = metric_data["histogram"][0]["end"]
            passes = p75 < threshold
            if ((not metric_filter or metric in metric_filter) and
                ((not threshold_filter or threshold_filter == 'None') or (threshold_filter == "Pass" and passes) or
                (threshold_filter == "Fail" and not passes))):
                    
                for histogram_data in metric_data["histogram"]:
                    formatted_response.append(
                        {"origin": url,
                        "metric": metric,
                        "start": histogram_data.get("start", "-"),
                        "end": histogram_data.get("end", "-") , 
                        "density": histogram_data.get("density", "-")}
                        ) 
        return formatted_response
    except:
        print(traceback.format_exc())


    