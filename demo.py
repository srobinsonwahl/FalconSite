"""
A SIMPLE SHODAN SEARCH OF EXISTING + PUBLIC DATA THAT RETURNS INFO ABOUT DOMAINS THAT ARE INTERNET FACING:
"""

import shodan
from config import SHODAN_API_KEY

import pprint as p

api = shodan.Shodan(SHODAN_API_KEY)


"""

THIS IS A PROGRAM THAT WILL OFFER GEOGRAPHICAL INFORMATION OF OPEN PORTS OF STORED SHODAN ENTITIES

"""

def user_search(query):
    results = api.search(query)
    return results

# print(user_search("Dell EMC"))

def total(results):
    return results['total']

def create_ip_dict(results):
    
    # Create a dictionary to store information
    ip_dict = {}

    # Iterate through each search result
    for result in results['matches']:

        # Assign k to each result's IP address
        k = result['ip_str']
        domain = result['domains']
        port = result['port']

        # If k is not in the dictionary, then add it and the corresponding city
        if k not in ip_dict:
            ip_dict[k] = result['location']['city'], [domain, port]

    return ip_dict

# print(create_ip_dict(user_search('Dell EMC')))

def get_ip_list(query):
    results = user_search(query)
    ip_dict = create_ip_dict(results)
    ip_list = list(ip_dict.keys())

    return ip_list

# print(get_ip_list('McDonalds'))

def get_ip_coords(query):
    ip = get_ip_list(query)
    ip_coords_list = []

    for i in ip:
        host = api.host(i)
        if len(host['data']) > 1:
            latitude = host['data'][1]['location']['latitude']
            longitude = host['data'][1]['location']['longitude']
            coords = latitude, longitude
            ip_coords_list.append(coords)
        else:
            coords = 0, 0
            ip_coords_list.append(coords)
    
    return ip_coords_list

# print(get_ip_coords('McDonalds'))

from reverse_geocode import make_mapbox_url, get_json, get_address, address_from_coords

def get_addresses(ip_coords_list):
    address_list = []

    for i in ip_coords_list:
        if i != (0, 0):
            address_list.append(address_from_coords(i))
        else:
            address_list.append(None)
    
    return address_list

# print(get_addresses(get_ip_coords('Dell EMC')))


import folium

def create_map(ip_coords_list):

    coordinates = ip_coords_list
    if coordinates:
        map_center = [sum(x[0] for x in coordinates) / len(coordinates), sum(x[1] for x in coordinates) / len(coordinates)]

        my_map = folium.Map(location=map_center, zoom_start=2)

        for coord in coordinates:
            if coord != (0, 0):
                folium.Marker(location=coord, popup=address_from_coords(coord)).add_to(my_map)

        output_path = 'templates/coordinate_map.html'
        my_map.save(output_path)
    else:
        print("No IP Info found")

create_map(get_ip_coords("Deftones"))