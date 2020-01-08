#!/usr/bin/env python
# -*- coding:utf-8 -*-
import logging
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.websocket import WebSocketHandler
import os.path
import asyncio
from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/chat", ChatHandler),
        ]
        settings = dict(
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("home.html")


class ChatHandler(WebSocketHandler):
    # 存储每一个人的信息
    users = []

    # 判断源origin，对于符合条件的请求源允许链接
    def check_origin(self, origin):
        return True

    def allow_draft76(self):
        # for iOS 5.0 Safari
        return True

    # 连接建立后被调用，客户端建立链接后调用open。
    def open(self):
        print("new client opened===>")
        # 链接上后再进行存储用户信息，self 为每个连接服务器的客户端的对象
        self.users.append(self)
        print(id(self))
        print(self.users)
        for user in self.users:
            print(self.request.remote_ip)
            # 主动向客户端发送message消息，message可以是字符串或者字典。
            user.write_message('u[{}]登陆了'.format(self.request.remote_ip))

    # 客户端发送消息过来时服务器调用on_message
    async def on_message(self, message):
        # 如果前端发的数据是字典，需要转一下
        # parsed = tornado.escape.json_decode(message)
        await asyncio.sleep(5)
        for user in self.users:
            # write_message的消息会被前端ws.onmessage方法接收
            user.write_message(u'{}说：{}'.format(self.request.remote_ip, message))

    # 客户端断开链接调用on_close
    def on_close(self):
        print("new client closed===>")
        self.users.remove(self)
        for user in self.users:
            user.write_message('u[{}]退出登陆了'.format(self.request.remote_ip))


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()