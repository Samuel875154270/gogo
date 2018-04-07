import tornado.web, tornado.ioloop, os, logging, config, error, sys
from config.tornado_routers import routers
from tornado.options import define

app_path = sys.path[0]
define("app_path", default=app_path)

LOGLEV = logging.INFO
logging.basicConfig(level=LOGLEV,
                    format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='access.log')
# peewee 日志
logger = logging.getLogger('peewee')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())


console = logging.StreamHandler()
console.setLevel(LOGLEV)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
application = tornado.web.Application(routers)

if __name__ == "__main__":
    try:
        port = config.listen
        logging.info("Running on {}".format(port))
        application.listen(port)
        tornado.ioloop.IOLoop.instance().start()
    except error.RequestData as e:
        print(e.code)
        print(e.message)
