import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.ext.declarative
from sqlalchemy import Column, Integer, Unicode, UnicodeText, DateTime
from sqlalchemy.sql import functions

from config import Config

database_config = Config('Database')
ENGINE_URL = database_config['url']

engine = sqlalchemy.create_engine(ENGINE_URL)

Session = sqlalchemy.orm.sessionmaker(bind=engine, autocommit=True)
Base = sqlalchemy.ext.declarative.declarative_base(engine)

class Note(Base):
    __tablename__ = 'note'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), nullable=False, default=functions.now())

    name = Column(Unicode(255), nullable=False)
    description = Column(UnicodeText, nullable=False)

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

