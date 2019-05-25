from app import db
from app.models import User, Post

def initializedb():
	db.create_all()

	# making the users
	user_1 = User(username='cap', email='c@demo.com', password='pass')
	db.session.add(user_1)
	user_2 = User(username='raf', email='r@demo.com', password='pass')
	db.session.add(user_2)

	# commit the chagnes to the db
	db.session.commit()

	'''
	Queries for retrieving the users in the User table
	'''
	User.query.all()
	User.query.first()
	User.query.filter_by(username='cap').all()
	User.query.filter_by(username='cap').first()
	user = User.query.filter_by(username='cap').first()
	print(user.id)
	user = User.query.get(1) # gets the user with the id of 1

	post_1 = Post(title='News', content='First Post News!', user_id=user.id)
	post_2 = Post(title='News 2', content='Second Post News!', user_id=user.id)
	db.session.add(post_1)
	db.session.add(post_2)
	db.session.commit()

	print(user.posts)

	'''
	Making some queries with the Post table
	'''
	post = Post.query.first()
	print(post.user_id)
	print(post.author)

def dropdb():
	db.drop_all()