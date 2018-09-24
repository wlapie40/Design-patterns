import sqlite3

class Singleton(type):
    def __call__(cls, *args, **kw):
        if not hasattr(cls,'instance'):
            cls.instance = super(Singleton, cls).__call__(*args, **kw)
        return cls.instance

class MetaSingleton(metaclass = Singleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj

db1 = MetaSingleton().connect()
print(db1)

db2 = MetaSingleton().connect()
print(db2)