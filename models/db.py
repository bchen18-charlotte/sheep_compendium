from models.models import Sheep

class FakeDB:
    def __init__(self):
        self.data = {
            1: Sheep(id=1, name="Spice", breed="Gotland", sex="ewe")
        }

    def get_sheep(self, id):
        return self.data.get(id)

    def add_sheep(self, sheep):
        if sheep.id in self.data:
            raise ValueError("Sheep with this ID already exists")
        self.data[sheep.id] = sheep
        return sheep

    def update_sheep(self, id, sheep):
        if id not in self.data:
            return None
        self.data[id] = sheep
        return sheep

db = FakeDB()