from wsgiref.simple_server import make_server

HTML = """
<!DOCUTYPE html>
<head>
<title>servidor en python</title>
<body>
<h1>Hola mundo desde el servidor pagina web</h1>
</body>
</head> 
</html>

"""

def application(env, start_response):
    headers = [('Content-Type', 'text/html')]
    
    start_response('200 OK', headers)
    
    return [bytes(HTML,'utf-8')]

server = make_server('localhost', 8000, application)
server.serve_forever()
