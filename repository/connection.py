import postgresql

def get_db():
	return postgresql.open('pq://postgres:Gandalf01@127.0.0.1:5432/book_loan')