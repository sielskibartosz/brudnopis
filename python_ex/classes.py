class Car:
    wheels = 4  # Class variable
    def __init__(self, model):
        self._model = model

    @classmethod
    def car_info(cls):
        return f"A car has {cls.wheels} wheels."

    # @property
    # def model(self):
    #     return self._model
    #
    # @model.setter
    # def model(self, value):
    #     if value not in  ["Tesla","Opel"]:
    #         raise ValueError("Model must be 'Tesla'")
    #     self._model = value

print(Car.car_info())

print(Car.wheels)

