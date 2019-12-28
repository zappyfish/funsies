#!/usr/bin/env python

from image_streaming import ImageStreamer
from threading import Thread
from flask import Flask

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello_world():
    return 'Hello, World!'


def main():
    app_thread = Thread(target=app.run())

    image_streamer = ImageStreamer()
    image_streamer.stream_non_blocking()
    image_streamer.end_stream_non_blocking()

    app_thread.join()

if __name__ == '__main__':
    main()
