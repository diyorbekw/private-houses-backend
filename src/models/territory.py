from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from src.core.db import Base


class Country(Base):
    __tablename__ = "country"
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)

    regions = relationship("Region", back_populates="country")


class Region(Base):
    __tablename__ = "region"
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    country_id = Column(Integer, ForeignKey("country.id"))

    country = relationship("Country", back_populates="regions")
    cities = relationship("City", back_populates="region")


class City(Base):
    __tablename__ = "city"
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    region_id = Column(Integer, ForeignKey("region.id"))

    region = relationship("Region", back_populates="cities")
    districts = relationship("District", back_populates="city")


class District(Base):
    __tablename__ = "district"
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    city_id = Column(Integer, ForeignKey("city.id"))

    city = relationship("City", back_populates="districts")
    microdistricts = relationship("MicroDistrict", back_populates="district")


class MicroDistrict(Base):
    __tablename__ = "microdistrict"
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    district_id = Column(Integer, ForeignKey("district.id"))

    district = relationship("District", back_populates="microdistricts")
    streets = relationship("Street", back_populates="microdistrict")


class Street(Base):
    __tablename__ = "street"
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    microdistrict_id = Column(Integer, ForeignKey("microdistrict.id"))

    microdistrict = relationship("MicroDistrict", back_populates="streets")
