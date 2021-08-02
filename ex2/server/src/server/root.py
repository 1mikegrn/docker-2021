import cherrypy


class ServerRoot:
    @cherrypy.expose
    def index(self):
        return "<h1>Hello Crunchies!<h1>"