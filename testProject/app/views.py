from flask import render_template, request
from app import app, mail
from flask.ext.mail import Message
from config import ADMINS
import sys
import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

@app.route('/')
@app.route('/index')
def index():
        return render_template('index.html', title='Home')

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        url = request.form['url']
        email = request.form['email']
        s = Screenshot()
        s.capture(url, 'website.png')
        print url
        print email
        msg = Message("Test",
                sender=ADMINS[0],
                recipients=[email])
        msg.body=url
        with app.open_resource("../website.png") as fp:
                msg.attach("../website.png", "image/png", fp.read())
        mail.send(msg)
    return render_template('index.html', title='Home');

class Screenshot(QWebView):
    def __init__(self):
        self.app = QApplication(sys.argv)
        QWebView.__init__(self)
        self._loaded = False
        self.loadFinished.connect(self._loadFinished)

    def capture(self, url, output_file):
        self.load(QUrl(url))
        self.wait_load()
        # set to webpage size
        frame = self.page().mainFrame()
        self.page().setViewportSize(frame.contentsSize())
        # render image
        image = QImage(self.page().viewportSize(), QImage.Format_ARGB32)
        painter = QPainter(image)
        frame.render(painter)
        painter.end()
        print 'saving', output_file
        image.save(output_file)

    def wait_load(self, delay=0):
        # process app events until page loaded
        while not self._loaded:
            self.app.processEvents()
            time.sleep(delay)
        self._loaded = False

    def _loadFinished(self, result):
        self._loaded = True
