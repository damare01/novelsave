from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ..model import Model


class NovelUrl(Model):
    __tablename__ = 'novel_urls'

    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)

    novel_id = Column(Integer, ForeignKey('novels.id'))
    novel = relationship('Novel', back_populates='urls')
