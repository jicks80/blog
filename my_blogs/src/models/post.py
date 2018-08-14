import uuid

import datetime

from src.common.database import Database

__author__ = 'jslvtr'


class Article(object):

    def __init__(self, ArtId, ArtCategory, ArtTitle, ArtContent, ArtAuthor, ArtViews, ArtLike, ArtComment,
                 ArtCdate=datetime.datetime.utcnow(), _id=None):
        self.ArtId = ArtId
        self.ArtTitle = ArtTitle
        self.ArtCategory = ArtCategory
        self.ArtContent = ArtContent
        self.ArtAuthor = ArtAuthor
        self.ArtCdate = ArtCdate
        self.ArtViews = ArtViews
        self.ArtLike = ArtLike
        self.ArtComment = ArtComment
        self._id = uuid.uuid4().hex if _id is None else _id

    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())

    def json(self):
        return {
            'ArtId': self.ArtId,
            'ArtCategory': self.ArtCategory,
            'ArtContent': self.ArtContent,
            'ArtAuthor': self.ArtAuthor,
            'ArtCdate': self.ArtCdate,
            'ArtViews': self.ArtViews,
            'ArtLike': self.ArtLike,
            'ArtComment': self.ArtComment,
            '_id': self._id
        }

    @classmethod
    def fetch_article(cls, ArtId):
        post_data = Database.find_one(collection='post', query={'ArtId': ArtId})
        return cls(**post_data)

    @classmethod
    def fetch_cat(cls, ArtCategory):
        blogs = Database.find(collection='post', query={'ArtCategory': ArtCategory})
        return [cls(**blog) for blog in blogs]

    @classmethod
    def fetch_all(cls):
        blogs = Database.find(collection='post', query={})
        return [cls(**blog) for blog in blogs]
