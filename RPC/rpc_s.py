import thriftpy2
pingpong_thrift = thriftpy2.load("pingpong.thrift", module_name="pingpong_thrift")
import time
from thriftpy2.rpc import make_server

class Dispatcher(object):
    def ping(self):
        time.sleep(3)
        return "pong"

server = make_server(pingpong_thrift.PingPong, Dispatcher(), '127.0.0.1', 8000)
server.serve()