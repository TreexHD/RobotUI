import flask

"""
this is the main file
"""

class UI:

    app = flask.Flask(__name__)

    @app.route('/startseite')
    def startseite(self):
        return "Startseiten Test!"
    pass