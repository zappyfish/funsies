#!/usr/bin/env python

from image_streaming import ImageStreamer
from flask import Flask, request

app = Flask(__name__)
image_streamer = ImageStreamer()

@app.route('/hello', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/click', methods=['POST'])
def image_click():
    content = request.json
    x = content['x']
    y = content['y']
    image_streamer.add_red_circle(x, y)
    return "OK"


def main():

    image_streamer.stream_non_blocking()

    app.run()

if __name__ == '__main__':
    main()
