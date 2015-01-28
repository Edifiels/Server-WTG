from sqlalchemy import create_engine
import tornado.ioloop
import tornado.web
import json


class SQLHandler(tornado.web.RequestHandler):
    def get(self, value=None):
        count = self.get_argument("count", None, True)
        start = self.get_argument("start", None, True)

        engine = create_engine("mysql+pymysql://root:root@localhost:3306/wtg?charset=utf8", echo=True)

        lim = str(start) + "," + str(count)
        connection = engine.connect()
        result = connection.execute("SELECT * FROM point LIMIT " + lim)

        json_products = []

        for row in result:
            json_prod = {'id': row.id, 'title': row.title, 'phone': row.phone, 'adds': row.adds,
                         'url': row.url, 'times_mon': row.times_mon.replace('&ndash;', ' - '), 'lat': row.lat,
                         'lng': row.lng}
            json_products.append(json_prod)

        self.write(json.dumps(
            {
                "result":
                    json_products
            }, indent=5, ensure_ascii=False, sort_keys=True
        ))

        connection.close()