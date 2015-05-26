from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Category(Base):
    __tablename__ = 'category'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'id'               : self.id,
           'name'             : self.name,
           'user_id'          : self.user_id,
       }
 
class CatalogItem(Base):
    __tablename__ = 'catalog_item'

    id = Column(Integer, primary_key = True)
    title = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    item_picture = Column(String(250))
    category_id = Column(Integer,ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)



    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'id'           : self.id,
           'title'        : self.title,
           'description'  : self.description,
           'price'        : self.price,
           'item_picture' : self.item_picture,

       }



engine = create_engine('sqlite:///catalogwithusers.db')
 

Base.metadata.create_all(engine)
