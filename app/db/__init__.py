import psycopg2 as psb
from dotenv import load_dotenv

import os
from hashlib import sha256 as sha
import sys

sys.path.append("..")
from model import UserRegistration

class DB:
    def __init__(self):
        self.url = os.getenv("DATABASE_NAME")
        self.name = os.getenv("ROOT_NAME")
        self.password = os.getenv("DATABASE_PASSWORD")
        print(self.url, self.name, self.password, 1)
        self.conn = psb.connect(dbname=self.url, user=self.name, password=self.password, host="localhost")
        #self.conn = psb.connect("dbname=XDrive user=postgres")
        self.cur = self.conn.cursor()

    def _promt(self, a: str, returnable: bool = True):
        self.cur.execute(a)
        self.conn.commit()
        if returnable:
            return self.cur.fetchall()

    def reg_user(self, user: UserRegistration):
        self._promt(f"INSERT INTO {self.url} (email, JWT) VALUES ('{user.email}', '{self.get_hash(user.email, user.password)}');", returnable=False)

    def get_users(self):
        return self._promt(f"SELECT * FROM {self.url};")

    @staticmethod
    def get_hash(a: str, b: str) -> str:
        a_pass, b_pass = [str(sha(x.encode('utf-8')).hexdigest()) for x in (a, b)]
        return a_pass + b_pass

    def close(self):
        self.cur.close()
        self.conn.close()

    def create_table(self):
        self._promt(f"""CREATE TABLE {self.url} 
              (id serial PRIMARY KEY,
              email varchar,
              JWT varchar(128));""", returnable=False)


if __name__ == "__main__":
    load_dotenv()
    #db = DB()
    print("connected")
    #db._promt(f"DROP TABLE None", returnable=False)
    print(db.url)
    db._promt(f"""CREATE TABLE {db.url} 
              (id serial PRIMARY KEY,
              email varchar,
              JWT varchar(128));""", returnable=False)
    db._promt(f"INSERT INTO {db.url} (email, JWT) VALUES ('artsadert@gmail.com', '{db.get_hash('artsadert@gmmail.com', '12341234')}');", returnable=False)
    res = db._promt(f"SELECT * FROM {db.url}") 
    print(res)
    #db._promt(f"INSERT INTO {db.name};")
    db.close()
