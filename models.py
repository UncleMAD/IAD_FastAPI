# coding: utf-8
from sqlalchemy import BigInteger, Boolean, Column, DateTime, Integer, Numeric, String, Table, Text, Time, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True, server_default=text("nextval('items_id_seq'::regclass)"))
    name = Column(String, index=True)
    description = Column(String, index=True)


t_weather_data = Table(
    'weather_data', metadata,
    Column('request_type', Text),
    Column('query', Text),
    Column('language', Text),
    Column('unit', Text),
    Column('location_name', Text),
    Column('location_country', Text),
    Column('location_region', Text),
    Column('location_lat', Numeric(5, 3)),
    Column('location_lon', Numeric(5, 3)),
    Column('location_timezone_id', Text),
    Column('location_localtime', DateTime),
    Column('location_localtime_epoch', BigInteger),
    Column('location_utc_offset', Numeric(3, 1)),
    Column('observation_time', Time),
    Column('temperature', Integer),
    Column('weather_code', Integer),
    Column('weather_icon', Text),
    Column('weather_description', Text),
    Column('wind_speed', Integer),
    Column('wind_degree', Integer),
    Column('wind_dir', Text),
    Column('pressure', Integer),
    Column('precip', Numeric(4, 1)),
    Column('humidity', Integer),
    Column('cloudcover', Integer),
    Column('feelslike', Integer),
    Column('uv_index', Integer),
    Column('visibility', Integer),
    Column('is_day', Boolean)
)


class X(Base):
    __tablename__ = 'x'

    id = Column(Integer, primary_key=True, server_default=text("nextval('x_id_seq'::regclass)"))
    number = Column(Integer, nullable=False)


class Y(Base):
    __tablename__ = 'y'

    id = Column(Integer, primary_key=True, server_default=text("nextval('y_id_seq'::regclass)"))
    number = Column(Integer, nullable=False)
    dt = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
