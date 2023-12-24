from flask import Blueprint, request, jsonify
from views import logics
from http import HTTPStatus
from exception_handlers.Exceptions import InvalidRequestException, APIConnectionException

mod = Blueprint("routes", __name__, template_folder="templates")

@mod.route('/report', methods=['POST'])
def get_crux_report():
    '''
    Endpoint that receives POST request with urls and filters
    fetches the API responses for received urls, formats them.
        request: 
            { urls - str, filterMetric - List[str], thresholdFilter - str }
        returns:
            400 -  Invalid Request
            404 -  API Connection error
            500 -  Internal server Error
            200 -  Formatted API responses
    '''
    data = None
    if logics.validate_request(request.json) == "invalid":
        raise InvalidRequestException
    try:
        urls = request.json["urls"]
        urls = urls.split(',')
        metric_filter = request.json["filterMetric"]
        threshold_filter = request.json["thresholdFilter"]
        print(f"{request.json = }")
        data = logics.get_crux_data_report(urls, metric_filter, threshold_filter)
        if not data:
            raise APIConnectionException
    except InvalidRequestException as e:
        return jsonify(message = e.description), e.code
    except APIConnectionException as e:
        return jsonify(message = e.description), e.code
    except:
        return jsonify(message="Internal Server Error"), HTTPStatus.INTERNAL_SERVER_ERROR
    return data