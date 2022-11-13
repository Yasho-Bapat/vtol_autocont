import time
import dronekit_sitl, sys
from dronekit import connect, VehicleMode

vehicle = connect('tcp:127.0.0.1:5760', wait_ready=True)

def arm_and_takeoff(target_altitude):
    print("pre arming checks")
    while not vehicle.is_armable:
        print("waiting for vehicle to initialise")
        time.sleep(1)

    print("arming motors")
    vehicle.mode = VehicleMode("GUIDED")
    while not vehicle.armed:
        vehicle.armed = True #commands to change a value are NOT GUARANTEED TO SUCCEED therefore put in a loop
        print("arming...")
        time.sleep(1)


    print("autopilot firmware version: " + str(vehicle.version))
    print("global location: " + str(vehicle.location.global_frame))
    print("global location (relative altitude): " + str(vehicle.location.global_relative_frame))
    print("local location: " + str(vehicle.location.local_frame))
    print("is armable: " + str(vehicle.is_armable))
    print("vehicle armed: " + str(vehicle.armed))
    print("heading: " + str(vehicle.heading))

arm_and_takeoff(20)