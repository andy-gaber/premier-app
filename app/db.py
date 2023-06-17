import sqlite3
from app import app, SQLITE_DATABASE_URI


def _connect_db():
	# creates db file if doesn't exist
	conn = sqlite3.connect(SQLITE_DATABASE_URI)
	return conn


def _close_db(conn):
	conn.close()


def create_tables():

	conn = _connect_db()

	cur = conn.cursor()
	cur.execute("DROP TABLE IF EXISTS Customer_Order")
	cur.execute("DROP TABLE IF EXISTS Item")


	order_table = """
		CREATE TABLE Customer_Order (
			id INTEGER PRIMARY KEY,
			store TEXT,
			order_number TEXT,
			iso_datetime TEXT,
			order_datetime TEXT,
			customer TEXT
		);
	"""

	item_table = """
		CREATE TABLE Item (
			id INTEGER PRIMARY KEY,
			sku TEXT,
			quantity INTEGER,
			order_number TEXT,
			FOREIGN KEY (order_number) 
			REFERENCES Customer_Order (order_number) 
				ON DELETE CASCADE
		);
	"""

	cur.execute(order_table)
	cur.execute(item_table)

	# create_table = """
	# 	CREATE TABLE Item (
	# 		id INTEGER PRIMARY KEY,
	# 		store TEXT,
	# 		order_num TEXT,
	# 		iso_datetime TEXT,
	# 		order_datetime TEXT,
	# 		customer TEXT,
	# 		sku TEXT
	# 	);
	# """
	# cur.execute(create_table)

	store_idx = """
		CREATE INDEX store_idx
		ON Customer_Order (store);
	"""

	iso_dt_idx = """
		CREATE INDEX iso_dt_idx
		ON Customer_Order (iso_datetime);
	"""
	cur.execute(store_idx)
	cur.execute(iso_dt_idx)

	_close_db(conn)


# def create_tables():
# 	with app.app_context():
# 		db.drop_all()
# 		db.create_all()


# class Item(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	store = db.Column(db.String(64), index=True)
# 	order_num = db.Column(db.String(64))
# 	order_datetime = db.Column(db.String(64), index=True)
# 	customer = db.Column(db.String(128))
# 	sku = db.Column(db.String(128))
	#description = db.Column(db.String(128))
	#quantity = db.Column(db.Integer)

	# def __repr__(self):
	# 	return '<Item>\n' + \
	# 			'Order number:  ' + self.order_num + '\n' + \
	# 			'Order date:    ' + self.order_date + '\n' + \
	# 			'Store:         ' + self.store + '\n' + \
	# 			'Customer:      ' + self.customer + '\n' + \
	# 			'SKU:           ' + self.sku + '\n' + \
	# 			'Description:   ' + self.description + '\n' + \
	# 			'Quantity:      ' + str(self.quantity)
		

# class Note(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	note = db.Column(db.String(320))

# 	def __repr__(self):
# 		return 	'<Note>\n' + \
# 				'Note: ' + self.note
