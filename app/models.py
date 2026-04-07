from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# Category Table
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    pois = relationship("POI", back_populates="category")


# Location Table
class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    poi = relationship("POI", back_populates="location", uselist=False)


# POI Table
class POI(Base):
    __tablename__ = "pois"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))
    location_id = Column(Integer, ForeignKey("locations.id"))
    category = relationship("Category", back_populates="pois")
    location = relationship("Location", back_populates="poi")