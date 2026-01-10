from control_server.services.vehicle_control import controls as controls
from control_server.models.vehicle_model import Vehicle
import json
import jwt

def add_vehicle(data):

    vehicle_type = data.get("type")

    try:
        vehicle = Vehicle(vehicle_type=vehicle_type, name=data.get("name"))
        vehicle.save()
    except vehicle_type != "utility" and vehicle_type != "charge":
        return {"status": "error", "message": "Invalid vehicle type."}
    
    return {"status": "ok", "message": f"Vehicle {vehicle_type} added."}

def fetch_vehicles(vehicle_id = None, vehicle_type = None):
    vehicles = Vehicle.objects.all()
    
    if vehicle_type:
        vehicles = vehicles.filter(vehicle_type=vehicle_type)
    
    if vehicle_id:
        vehicles = vehicles.filter(id=vehicle_id)

    return vehicles.order_by('id')

def initiate_vehicle_control():
    # controls.func()
    return "Vehicle control initiated"

def login(vehicle_id, password):
    
    vehicle_raw_id = int(vehicle_id.split("_")[1])
    vehicle_type = "utility" if vehicle_id.split("_")[0] == "u" else "charge"

    print("data", vehicle_raw_id, vehicle_type)

   
    vehicle = Vehicle.objects.filter(id = vehicle_raw_id, vehicle_type = vehicle_type)[0]
    passwords_match = vehicle.compare_password(password)
    print('passwords match', passwords_match)
    
    if passwords_match == False:
        return {"status":"error", "message":"passwords don't match"}

    key = 'secret'
    token = jwt.encode({"id":vehicle_raw_id}, key, algorithm="HS256")
    return {"status":"ok", "message":"succesfully logged into vehicle", "token":token}

def update_vehicle(request):
    data = json.loads(request.body)
    vehicle = Vehicle.objects.filter(id=data.get("id"))[0]
    vehicle.generate_password(data.get("password"))
    vehicle.save()
    print("vehicle", vehicle)

    return {"status": "ok", "message": "ok"} 