from flask.ext.script import Manager

from myapp import app
from views import test
import os

manager = Manager(app)

@manager.command
def komut():
    test()

if __name__ == "__main__":
    manager.run()
