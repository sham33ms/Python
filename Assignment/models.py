from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from db import Base

class Subscriber(Base):
    __tablename__ = "subscribers"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    joined_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="active")  # active/unsubscribed

    engagements = relationship("Engagement", back_populates="subscriber")


class Newsletter(Base):
    __tablename__ = "newsletters"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    sent_at = Column(DateTime, default=datetime.utcnow)

    engagements = relationship("Engagement", back_populates="newsletter")


class Engagement(Base):
    __tablename__ = "engagements"
    id = Column(Integer, primary_key=True)
    subscriber_id = Column(Integer, ForeignKey("subscribers.id"))
    newsletter_id = Column(Integer, ForeignKey("newsletters.id"))
    opened = Column(Boolean, default=False)
    clicked = Column(Boolean, default=False)

    subscriber = relationship("Subscriber", back_populates="engagements")
    newsletter = relationship("Newsletter", back_populates="engagements")
