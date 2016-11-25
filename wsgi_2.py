from pprint import pformat
from cgi import parse_qsl, escape

def wsgi_application(environ, start_response):
    output = '<p>Hello, world!</p>'

    output += 'Post:'
    output += '<form method="post">'
    output += '<input type="text" name = "post">'
    output += '<input type="submit" value="Send">'
    output += '</form>'

    d = parse_qsl(environ['QUERY_STRING'])
    if environ['REQUEST_METHOD'] == 'POST':
        output += '<h1>Post  data:</h1>'
        output += pformat(environ['wsgi.input'].read())

    if environ['REQUEST_METHOD'] == 'GET':
        if environ['QUERY_STRING'] != '':
            output += '<h1>Get data:</h1>'
            for ch in d:
                output += ' = '.join(ch)
                output += '<br>'

    start_response('200 OK', [('Content-type', 'text/html'), ('Content-Length', str(len(output)))])
    return [ output ]
