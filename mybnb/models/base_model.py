#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models
class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
    def save(self):
        """Updates the instance's updated_at with the current datetime and saves to storage."""
        self.updated_at = datetime.now()

        # Save the instance to storage
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance, including class name."""
        # Create a copy of the instance's dict, then update datetime objects to strings
        dict_rep = dict(self.__dict__)
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()
        dict_rep['__class__'] = self.__class__.__name__
        return dict_rep

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        class_name = type(self).__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
