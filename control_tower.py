
# THIS PROGRAM ALLOWS TOWER'S COMPUTER TO RECEIVE AIRCRAFT DATA

# **NOTE: Tasks that use a "re-ping" module will require "speed" & "distance" as additional arguments**

class Airplane:

    def __init__(self, flight_number, altitude):
        self.__flight_number = flight_number
        self.__altitude = altitude

    def plane_arrival(self):
        return '{} at {}, you are cleared to land'.format(self.__flight_number, self.__altitude)

    def plane_departure(self):
        return '{}, you are cleared for takeoff'.format(self.__flight_number)


aircraft_fn = input("CONFIRM FLIGHT NUMBER: ")
aircraft_alt = input("CONFIRM CURRENT ALTITUDE: ")
aircraft_intention = input("CONFIRM YOUR INTENTIONS: Arrival or Departure? ")
airplanes = [Airplane(aircraft_fn, aircraft_alt)]

if aircraft_intention == "Arrival":
    print("**YOU REQUESTED CLEARANCE TO LAND**")
    print(Airplane.plane_arrival(airplanes[0]))
    # From here, an aircraft status module will "re-ping" the control tower with positioning status.
    # If the airplane has reached an x speed below 60 kts, the system will pass the aircraft's flight
    # information onto ground controlled operations.
elif aircraft_intention == "Departure":
    print("**YOU REQUESTED CLEARANCE FOR TAKEOFF**")
    print(Airplane.plane_departure(airplanes[0]))
    # From here, an aircraft status module will "re-ping" the control tower with positioning status.
    # If the airplane has reached an x-distance from control tower at x-altitude, the system will pass
    # the aircraft's flight information onto center controlled operations.
