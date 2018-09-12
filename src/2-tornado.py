import time

import tornado.web
from tornado.ioloop import IOLoop
from tornado import gen


class AsyncHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def post(self, *args, **kwargs):
        json_input = tornado.escape.json_decode(self.request.body)
        print (f'Got the following input: {json_input}')
        yield self.perform_long_task(*args, **json_input)

    @gen.coroutine
    def perform_long_task(self, **params):
        yield gen.sleep(10)
        self.write(str(params))


if __name__ == '__main__':
    application = tornado.web.Application([
        (r"/", AsyncHandler),
    ])

    application.listen(8888)
    IOLoop.instance().start()
