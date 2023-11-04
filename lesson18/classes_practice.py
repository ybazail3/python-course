# Classes are blueprints for objects
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("Moves along...")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")


my_car = Vehicle("Tesla", "Model 3")

my_car.get_make_model()
# print(my_car.make)
# print(my_car.model)
# Using dot notation
my_car.moves()

your_car = Vehicle("Honda", "Civic")
your_car.get_make_model()
your_car.moves()


class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        # super will allow us to inherit the make and model from the Vehicle class
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print("Flies along...")


class Truck(Vehicle):
    def moves(self):
        print("Rumbles along...")


class GolfCart(Vehicle):
    #  with pass this class will inherit from the Vehicle class
    pass


cessna = Airplane("Cessna", "Skyhawk", "N-12345")
toyota = Truck("Toyota", "Tundra")
yamaha = GolfCart("Yamaha", "SGC100")

cessna.get_make_model()
cessna.moves()
toyota.get_make_model()
toyota.moves()
yamaha.get_make_model()
yamaha.moves()

print("\n\n")

# polymorphism

for v in (my_car, your_car, cessna, toyota, yamaha):
    v.get_make_model()
    v.moves()
