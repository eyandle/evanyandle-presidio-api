from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from DatabaseModels.base import Base
from DatabaseModels import Organization
from main import database

meta = MetaData()
engine = create_engine(database)


Base.metadata.create_all(engine)