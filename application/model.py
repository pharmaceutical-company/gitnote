import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.ext.declarative
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, and_
from sqlalchemy import Column, Integer, String, Unicode, orm, DateTime
from sqlalchemy.orm import sessionmaker

ENGINE_URL = 'sqlite:///drug.db'
engine = create_engine(ENGINE_URL, echo=True)

Base = declarative_base(engine)

class Repository(Base):
	__tablename__ = 'repository'
	phys_name = Column(String(50), nullable=False, primary_key=True)
	repr_name = Column(String(50), nullable=False)
	def __init__(self, phys_name, repr_name):
		self.phys_name = phys_name
		self.repr_name = repr_name
	def __repr__(self):
		return "<Repository('%s','%s')>" % (self.phys_name, self.repr_name)
"""
class Files(Base):
	__tablename__ = 'files'
	repository = Column(String(45), ForeignKey("repository.repository"), nullable=False, primary_key=True)
	files = Column(String(50), nullable=False)
	def __init__(self, repository, files):
		self.repository = repository
		self.files = files
	def __repr__(self):
		return "<Files('%s','%s')>" % (self.repository, self.files)
"""
Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker(bind=engine, autocommit=True)
session = Session()
