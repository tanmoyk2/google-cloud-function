def hello_world(request):
    request_args=request.args
    request_json=request.get_json(silent=True)
    if request_args and 'name' in request_args and 'lname' in request_args:
        name=request_args['name']
        lname=request_args['lname']
    elif request_json and 'name' in request_json and 'lname' in request_json:
        name=request_json['name']
        lname=request_json['lname']
    else:
        name='world'
        lname=''
    return 'Hello {} {}'.format(name,lname)

