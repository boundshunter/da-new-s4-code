#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'
import tornado
import tornado.web
import tornado.ioloop
class MainHandler(tornado.web.RequestHandler):

    def get(self):
        print(111)
        u = self.get_argument('user')
        e = self.get_argument('email')
        p = self.get_argument('pwd')
        if u == 'jfsu' and p == '123' and e =='76686094@qq.com':
            self.write("OK")
        else:
            self.write("Input error,try again.")

    def post(self,*args,**kwargs):
        u = self.get_argument('user')
        e = self.get_argument('email')
        p = self.get_argument('pwd')
        print(u,e,p)
        self.write("POST")

application = tornado.web.Application([
    (r"/index",MainHandler)
])

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()