import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_price_estimate(location,rooms,sqm,bathrooms,yob,heating,elevator):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = rooms
    x[1] = sqm
    x[2] = bathrooms
    x[3] = yob
    x[4] = heating
    x[5] = elevator
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],2)

def get_location_names():
    load_artifacts()
    return __locations

def load_artifacts():
    print("Loading artifacts")
    global __data_columns
    global __locations
    global __model

    with open("./artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[6:]

    with open("./artifacts/mhpp_lr_model.pkl", 'rb') as f:
        __model = pickle.load(f)

    print("Loading artifacts complete")

if __name__ == "__main__":
    load_artifacts()
    print(get_location_names())
    print(get_price_estimate('baggio', 3, 120, 1, 2000, 1, 1))
    print(get_price_estimate('baggio', 2, 60, 1, 1960, 1, 1))
    print(get_price_estimate('città studi', 3, 90, 3, 2000, 1, 1))
    print(get_price_estimate('city life', 3, 90, 3, 2000, 1, 1))
