#!/usr/bin/env python

from image_streaming import ImageStreamer
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

image_streamer = ImageStreamer()

@app.route('/hello', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/click', methods=['POST'])
def image_click():
    content = request.json
    x = int(content['x'])
    y = int(content['y'])
    image_streamer.add_red_circle(x, y)
    response = jsonify({})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


def main():

    image_streamer.stream_non_blocking()
    # image_streamer.add_red_circle(50, 50)
    app.run(host='0.0.0.0')

    image_streamer.end_stream_non_blocking()


if __name__ == '__main__':
    main()
