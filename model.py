from sqlalchemy import Column, Integer, String, DateTime, MetaData, func
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class Request(Base):
    __tablename__ = 'medication_request'

    ID = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    mobile = Column(String(15), nullable=False)
    city = Column(String, nullable=False)
    requirement = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())


class Offer(Base):
    __tablename__ = 'medication_offer'

    ID = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    mobile = Column(String(15), nullable=False)
    city = Column(String, nullable=False)
    offer = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
