from app import db, Email

print(Email.query.all())

print(Email.query.first())

#print(Email.query.filter_by(name='salah').all())

#email5 = Email.query.filter_by(name='jeff').first()
#print(email5.id, email5.name, email5.message)


# clear database
db.drop_all()
db.create_all()
db.session.commit()
