#!/usr/bin/python3
"""
This is a file storage that has FileStorage class, it serializes instances to JSON format and deserializes JSON back to instances
"""
import json
import os.path
import models
import datetime


class FileStorage:

    """
    Defination of FileStorage class that serializes instances to JSON and deserializing JSON back to instances.
    """

    __file_path = "file.json"
    __objects = {}

#    def __init__(self):
#        super().__init__()

   # @property
    def all(self):
        """ Returns the dictionary in __objects """
        return (FileStorage.__objects)
    
   # @new.setter
    def new(self, obj):
        """
              Puts a new object instance in the '__objects' dictonary with <obj class name >.is as the instance key.
        Attributes:
              obj (object): object to be set in the _-objects dictionary.
    
        """
        FileStorage.__objects[obj.id] = obj

    def save(self):
        """
            Serializes oobjects in __objects to JSON and into the Json file in __file_path.
        """
        context_obj = {}
#        list1 = ["created_at", "updated_at"]
        for key in FileStorage.__objects.keys():
#            if key not in list1:
            context_obj[key] = FileStorage.__objects[key].to_dict()
#            else:
#                context_obj[key] = value.isoformat() 
            
        with open(FileStorage.__file_path, "w") as f:
            json.dump(context_obj, f)
                
    def reload(self):
        """
            Deserializes the JSON file to __objects if __file_path exists.
            Otherwise does nothing.
        """
        try:
#        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='UTF-8') as f:
                context2 = json.load(f)
            
                for key in context2.keys():
                    new_value = context2[key]
                    clss = new_value['__class__']
#                    self.new(eval(clss)(**value))

        except Exception as e:
            pass
