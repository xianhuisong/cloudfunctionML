from predictor import predict


def hello_http(request):
    """entry point of cloud function
        :param request: the http request parameters
        :return predicting result
    """
    request_json = request.get_json(silent=True)
    request_args = request.args
    print(request_args)
    print(request_json)
    if request_json and 'features' in request_json:
        features = request_json['features']
    elif request_args and 'features' in request_args:
        features = request_args['features']
    else:
        features = "1,2,3"
    """construct a two dimensions array
    """
    params = [[int(i) for i in features.split(',')]]
    print(params)
    res = predict(params)
    return str(res)
