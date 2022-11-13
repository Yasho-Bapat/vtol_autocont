import dronekit
from dronekit import connect, VehicleMode
import time

vehicle = connect('tcp:127.0.0.1:5760', wait_ready=True)

def goSomewhere(target_altitude):
    print("pre arming checks")
    while not vehicle.is_armable:
        print("waiting for vehicle to initialise")
        time.sleep(1)

    print("arming motors")
    vehicle.mode = VehicleMode("GUIDED")
    while not vehicle.armed:
        vehicle.armed = True  # commands to change a value are NOT GUARANTEED TO SUCCEED therefore put in a loop
        print("arming...")
        time.sleep(1)
        if (vehicle.armed):
            print("armed")

    vehicle.simple_takeoff(target_altitude)
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)

        # Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt >= target_altitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)

goSomewhere(30)
