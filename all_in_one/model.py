from mongoengine import *
import datetime

connect('yn_history', host='db')


class News(Document):
    title = StringField()
    url = StringField()
    date = DateTimeField(default=datetime.datetime.now)
