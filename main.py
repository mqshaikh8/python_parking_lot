import random

class ParkingLot:
    def __init__(self, square_footage_size, parking_spot_width=8, parking_spot_length=12):
        self.parking_lot_size = square_footage_size
        self.parking_spot_size = parking_spot_width * parking_spot_length
        self.num_parking_spots = self.parking_lot_size // self.parking_spot_size
        self.parking_spots = [None] * self.num_parking_spots

    def park_car(self, car, spot_number=None):
        if spot_number < 0 or spot_number >= self.num_parking_spots:
            return False

        if self.parking_spots[spot_number] is not None:
            return False

        self.parking_spots[spot_number] = car
        return True

    def is_full(self):
        for spot in self.parking_spots:
            if spot is None:
                return False

        return True

    def get_parking_spots(self):
        return self.parking_spots

class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def __str__(self):
        return self.license_plate

    def park(self, parking_lot, spot_number):
        if not parking_lot.park_car(self, spot_number):
            print(f"Car with license plate {self.license_plate} was not parked successfully.")
            return

        print(f"Car with license plate {self.license_plate} parked successfully in spot {spot_number}.")




def generate_car():
    indian_state_license_plate_codes = [
        "AN",
        "AP",
        "AR",
        "AS",
        "BR",
        "CH",
        "CG",
        "DN",
        "DD",
        "DL",
        "GA",
        "GJ",
        "HR",
        "HP",
        "JK",
        "JH",
        "KA",
        "KL",
        "LD",
        "PY",
        "MP",
        "MH",
        "MN",
        "ML",
        "MZ",
        "NL",
        "OR",
        "PY",
        "PB",
        "RJ",
        "SK",
        "TN",
        "TS",
        "TR",
        "UP",
        "UK",
        "WB",
    ]
    alphabets = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    state_code = random.choice(indian_state_license_plate_codes)
    trasnport_auth_code = random.randint(10, 99)
    registration_series = f"{random.choice(alphabets)}{random.choice(alphabets)}"
    unique_numbers = random.randint(1000, 9999)
    license_plate = f"{state_code}{trasnport_auth_code}{registration_series}{unique_numbers}"
    return Car(license_plate)

def main():
    lot = ParkingLot(2000)
    cars = [generate_car() for _ in range(random.randint(0, lot.num_parking_spots))]


    for car in cars:
        while not lot.is_full():
            spot_number = random.randint(0, lot.num_parking_spots - 1)
            if lot.park_car(car, spot_number):
                print(f"Car with license plate {car.license_plate} parked successfully in spot {spot_number}.")
                break
            else:
                print(f"Car with license plate {car.license_plate} failed to park in spot {spot_number}. Retrying...")

    if lot.is_full():
        print("Parking lot is full.")
    else:
        print("All cars are parked.")

main()