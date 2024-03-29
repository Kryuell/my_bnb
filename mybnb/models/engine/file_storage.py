#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel

class FileStorage:
    """
    FileStorage class for storing, serializing and deserializing data
    """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
        Sets an object in the __objects dictionary with a key of 
        <obj class name>.id.
        """
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """
        Returns the __objects dictionary. 
        It provides access to all the stored objects.
        """
        return FileStorage.__objects

    def save(self):
        """
        Serializes the __objects dictionary into 
        JSON format and saves it to the file specified by __file_path.
        """
        all_objs = FileStorage.__objects
        obj_dict = {obj: all_objs[obj].to_dict() for obj in all_objs.keys()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects dictionary if file exists.
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)
                    for key, value in obj_dict.items():
                        class_name = key.split('.')[0]
                        cls = globals()[class_name]
                        instance = cls(**value)
                        self.__objects[key] = instance
                except Exception:
                    pass