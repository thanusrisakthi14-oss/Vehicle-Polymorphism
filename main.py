class BMW:
    def fuel_type(self):
        print("Diesel")

    def max_speed(self):
        print("250 km/h")


class Ferrari:
    def fuel_type(self):
        print("Petrol")

    def max_speed(self):
        print("340 km/h")

b = BMW()
f = Ferrari()

b.fuel_type()
b.max_speed()

f.fuel_type()
f.max_speed()