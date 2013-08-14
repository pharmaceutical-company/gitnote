import sqlalchemy.orm
import sqlalchemy.ext.declarative

#: SQLAlchemy session class.
#:
#: .. seealso:: SQLAlchemy --- :ref:`session_toplevel`
Session = sqlalchemy.orm.sessionmaker(autocommit=True)

#: SQLAlchemy declarative base class.
#:
#: .. seealso:: SQLAlchemy --- :ref:`declarative_toplevel`
Base = sqlalchemy.ext.declarative.declarative_base()


class User(Base):
	__tablename__ = 'users'
	userid = Column(Integer, primary_key=True)

	login = Column(Unicode(45), nullable=False, unique=True)

	password_hash = orm.deferred(Column(String(32), nllable=False))

    name = Column(Unicode(45), nullable=False, index=True)

    created_at = orm.deferred(Column(DateTime(timezone=True), nullable=False,
                                     default=functions.now(), index=True),
                              group='profile')
