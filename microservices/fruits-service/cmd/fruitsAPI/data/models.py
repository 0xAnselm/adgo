class Fruit:
    def __init__(self, _id, name, color, weight):
        self._id = _id
        self.name = name
        self.color = color
        self.weight = weight

    def to_json(self):
        return {
            'name': self.name,
            'color': self.color,
            'weight': self.weight
        }

    def to_bson(self):
        data = self.dict(by_alias=True, exclude_none=True)
        if data["_id"] is None:
            data.pop("_id")
        return data
