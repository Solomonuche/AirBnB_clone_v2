#!/usr/bin/python3
"""
responsible for storing our models to the database
"""
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv


load_dotenv()

classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review
        }


class DBStorage:
    """
    defines the dbstorage class methods and attributes
    """
    classes = {
            'User': User,
            'Place': Place, 'State': State, 'City': City,
            'Amenity': Amenity, 'Review': Review
            }
    __engine = None
    __session = None
    username = getenv('HBNB_MYSQL_USER')
    password = getenv('HBNB_MYSQL_PWD')
    db_name = getenv('HBNB_MYSQL_DB')
    host = getenv('HBNB_MYSQL_HOST')

    def __init__(self):
        """ Initializes the instance"""

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            DBStorage.username, DBStorage.password, DBStorage.host,
            DBStorage.db_name
                ), pool_pre_ping=True)
        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ returns all the objects of the class name cls """
        # session = sessionmaker(bind=self.__engine)
        # self.__session = session()
        objects = {}
        if cls:
            if isinstance(cls, str) and cls in DBStorage.classes:
                cls = DBStorage.classes[cls]

            if not isinstance(cls, str):
                # loop through to get key
                for k, v in DBStorage.classes.items():
                    if v == cls:
                        obj_key = k

                query_obj = self.__session.query(cls).all()
                for obj in query_obj:
                    key = f"{obj_key}.{obj.id}"
                    objects[key] = obj

            return objects
        else:
            all_object = {}
            for key in DBStorage.classes.keys():
                obj = self.__session.query(DBStorage.classes[key]).all()
                if obj:
                    for i in obj:
                        obj_key = f"{key}.{i.id}"
                        all_object[obj_key] = i
            return all_object

    def new(self, obj):
        """adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes from current database session obj is not none"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reload data from the databases"""
        Base.metadata.create_all(self.__engine)
        ses_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(ses_factory)
        self.__session = Session

    def close(self):
        """
        call remove() method on the private session attribute (self.__session)
        """

        self.__session.remove()
