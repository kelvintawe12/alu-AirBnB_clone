from models.base_model2 import BaseModel


class State(BaseModel):
    name = ""
    city_id = ""
    country_id = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name')
        self.city_id = kwargs.get('city_id')
        self.country_id = kwargs.get('country_id')
        self.save()
        self.save_to_file()
        self.id = self.update_id()
        self.save_to_json_file()

    def save_to_json_file(self):
        BaseModel.save_to_json_file([self])
        return True

    def update_id(self):
        return f"State.{self.id}"
