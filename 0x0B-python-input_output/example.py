class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            json_dict = {}
            for key in attrs:
                if hasattr(self, key):
                    json_dict[key] = getattr(self, key)

            return json_dict

