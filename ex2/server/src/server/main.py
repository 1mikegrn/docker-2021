import cherrypy

from .root import ServerRoot

def main():
    cherrypy.config.update({
        'server.socket_host': '0.0.0.0'
        })

    server = ServerRoot()

    cherrypy.tree.mount(server, '/', {})
    
    cherrypy.engine.start()
    cherrypy.engine.block() 