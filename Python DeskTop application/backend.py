import psycopg2

class Database:
	def __init__(self,db):
		#self.conn=sqlite3.connect(db)
		self.conn=psycopg2.connect(host="localhost",user="postgres",database="database_name",password="yourpassword")
		self.cur=self.conn.cursor()
		self.cur.execute("CREATE TABLE IF NOT EXISTS assets(id SERIAL  PRIMARY KEY,description text,tag_number text UNIQUE ,serial_number text,category text,location text,cost integer)")
		self.conn.commit()

	def insert(self,description,tag_number,serial_number,category,location,cost):
		self.cur.execute("INSERT INTO assets(description,tag_number,serial_number,category,location,cost) VALUES(%s,%s,%s,%s,%s,%s)",(description,tag_number,serial_number,category,location,cost))
		self.conn.commit()

	def view(self):
		self.cur.execute("SELECT * FROM assets")
		rows=self.cur.fetchall()
		return rows

	def update(self,description,tag_number,serial_number,category,location,cost):
		self.cur.execute("UPDATE assets SET description=?,tag_number=?,serial_number=?category=?,location=?,cost=?) WHERE id=?",(description,tag_number,serial_number,category,location,cost,id))
		self.conn.commit()

	def search(self):
		self.cur.execute("SELECT *FROM assets WHERE description=? OR tag_number=? OR serial_number=? OR category=? OR location=? OR cost=?")
		rows=self.cur.fetchall()		
		self.conn.commit()

	def delete(self):
		self.cur.execute("DELETE FROM assets WHERE id=?",(id))
		self.conn.commit

	def __del__(self):
		self.conn.close()

