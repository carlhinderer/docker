from flask import Flask
from flask import jsonify
import logging

app = Flask(__name__)

# Create logger
logger = logging.getLogger("Sample App")
logger.setLevel(logging.WARN)

# Create a console handler (StreamHandler outputs to STDOUT)
ch = logging.StreamHandler()

# Create a formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


@app.route('/')
def hello():
    logger.info("Accessing endpoint '/'")
    return 'Hello World'

@app.route('/colors')
def colors():
    logger.warning("Warning, you are accessing '/colors'")
    return jsonify(['red', 'green', 'blue'])

if __name__ == '__main__':
    app.run()