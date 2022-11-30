from math import sin, cos, sqrt, atan2, radians
import re

global coords_path
coords_path = r'G:\My Drive\informatik\coords.csv' #path to the coords file
def dist(lat1, lon1, lat2, lon2):
    r = 6373 # ungefaehr der Radius der Erde

    lat1 = radians(lat1) #python trigonometry functions need radians therefore the conversion
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    distlon = lon2 - lon1
    distlat = lat2 - lat1

    a = sin(distlat / 2)**2 + cos(lat1) * cos(lat2) * sin(distlon / 2)**2 # andwenden er Haversine formel
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = r * c

    return distance

def read_coords(location): # lesen der Koordinaten aus einer CSV datei
    with open(coords_path, 'rt') as f:
        data = f.readlines()
        for line in data:
            if location in line:
                return line


def get_lat_cord(string):
    substring = re.findall(';(.+);', string) #finding he lat cord between 2 semicolons
    string = str(substring) #converting from list to string

    return float(string[+2:-2:])

def get_long_coord(string):
    letter = ";"
    position = len(string) - string.rfind(letter) -1 #finding the chars of lon coords
    return float(string[-position:])

def main():
    while True:
        user_input = ''
        while user_input.count(' ') < 1: #user input has to be more then 1 location
            user_input = input("Enter at least 2 diffrent locations (seperated by spaces): ") #getting user input
        locList = user_input.split(' ') # seperating the strings from userinput
        print(locList)
        print("Distanz: ",dist_from_list(locList))

def dist_from_list(locList):
    dist_list = [] #creating list of distances to add together later
    for elem,next_elem in zip(locList, locList[1:]): # for every location and the next location distance is beeing calculated
        try:
            dist_list.append(dist(get_lat_cord(read_coords(elem)), get_long_coord(read_coords(elem)), get_lat_cord(read_coords(next_elem)),get_long_coord(read_coords(next_elem)))) #geting the distance and adding it to the distance list
        except TypeError: # occurs in case location  is not in database (csv file)
            print("Location not in database. Make sure to add location names in all caps!")
    return sum(dist_list) # getting sum of all distances
if __name__ == '__main__':
    main()