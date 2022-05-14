from logger import logger
from flask import Flask


app = Flask(__name__)


@app.route("/1")
def index_1():
    logger.critical("1")
    print(id(logger))
    return "1"


@app.route("/2")
def index_2():
    logger.critical("2")
    print(id(logger))
    return "2"


app.run()
