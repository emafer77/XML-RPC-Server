from xmlrpc.server import SimpleXMLRPCServer
def add_numbers(a, b):
    return a + b
def res_numbers(a,b):
    return a - b
def mul_numbers(a, b):
    return a * b 
def div_numbers(a,b):
    return a/b

server = SimpleXMLRPCServer(('localhost', 9000))
print("Listening on port 9000...")
server.register_function(add_numbers, 'add')
server.register_function(res_numbers, 'res')
server.register_function(mul_numbers, 'mul')
server.register_function(div_numbers, 'div')
server.serve_forever()