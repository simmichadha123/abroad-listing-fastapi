from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from cnext_backend.settings.base import Base



class Country(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    college_obj = relationship('College', back_populates='country_obj')

class College(Base):
    __tablename__ = 'colleges'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(250), nullable=False)
    country_id = Column(Integer, ForeignKey('countries.id'))

    country_obj = relationship('Country', back_populates='college_obj')