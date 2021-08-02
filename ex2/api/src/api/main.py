import cherrypy

from .root import ApiRoot

def main():
    cherrypy.config.update({
        'server.socket_host': '0.0.0.0'
        })

    api = ApiRoot()

    cherrypy.tree.mount(api, '/v1', {})
    
    cherrypy.engine.start()
    cherrypy.engine.block()    