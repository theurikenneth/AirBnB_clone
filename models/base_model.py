#!/usr/bin/python3
"""
module: class BaseModel
creates new instance objects 

"""
import uuid
from datetime import datetime
import models

class BaseModel():
    """
    BaseClass model
    """

    def __init__(self, *args, **kwargs):
        
        """
        initializes all the instances with mapped with the attributes
        attributes:
            id = unique id for every instance
            created_at = the time of instance creation
            updated_at = time of instance edit 
        """
        if kwargs:
            time_format = "%Y-%m-%dT%H:%M:%S.%f"
            crt =  kwargs['created_at']
            updt = kwargs['updated_at']
            self.created_at = datetime.strptime(crt, time_format)
            self.updated_at = datetime.strptime(updt, time_format)

            not_to_list = ["created_at", "__class__", "updated_at"]
            for key, value in kwargs.items():
                if key not in not_to_list:
                    self.__setattr__(key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)


    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        dict = {key: value for key, value in self.__dict__.items()}
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        dict["__class__"] = self.__class__.__name__
        return dict
