from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BigInteger, String, Sequence, Boolean, DateTime, Integer, desc
from sqlalchemy import create_engine, Table, MetaData, ForeignKey, text, bindparam, TIMESTAMP
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

Base = declarative_base()
engine = create_engine('sqlite:///mapping.db')
Session = sessionmaker(bind=engine)

class Mapper(Base):
    __tablename__ = "mapper"

    tgid = Column(String(64), primary_key=True)
    ethaddress = Column(String(128), nullable=False)

    @staticmethod
    def delete():
        s = Session()
        s.query(Mapper).delete()
        s.commit()
        s.close()
        return True

    @staticmethod
    def get(tgid):
        s = Session()
        try:
            return s.query(Mapper).filter(Mapper.tgid == tgid).first()
        finally:
            s.close()

    @staticmethod
    def add(tgid, ethaddress):
        s = Session()
        s.add(Mapper(
            tgid=tgid,
            ethaddress=ethaddress
        ))
        try:
            s.commit()
            return True
        except IntegrityError:
            return False
        finally:
            s.close()

if __name__ == '__main__':
    Base.metadata.create_all(engine)