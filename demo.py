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
    """
    Returns results from a query using shodan api and module
    """
    results = api.search(query)
    return results


def total(results):
    """
    Returns total number of search results from a user search
    """
    return results['total']


def create_ip_dict(results):
    """
    Returns a dictionary of IP Information based on a user query, stores data in the following convention: "IP":[[City], Port #]
    """
    
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


def get_ip_list(query):
    """
    Returns a list of the IPs within the dictionary based on user search
    """
    results = user_search(query)
    ip_dict = create_ip_dict(results)
    ip_list = list(ip_dict.keys())

    return ip_list


def get_ip_coords(query):
    """
    Returns a list of coordinates based on IP address by navigating Shodan query of each IP and pulling longitude and latitude, if not in query returns 0, 0
    """

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


from reverse_geocode import make_mapbox_url, get_json, get_address, address_from_coords

def get_addresses(ip_coords_list):
    """
    Returns addresses for each IP address by reverse geocoding each coordinate from ip coords list
    """
    address_list = []

    for i in ip_coords_list:
        if i != (0, 0):
            address_list.append(address_from_coords(i))
        else:
            address_list.append(None)
    
    return address_list


import folium

def create_map(ip_coords_list):
    """
    Creates a map using folium module by assessing # of coordinates within ip coords list, and plots each coord with it's respective address from get address, if no coordinates, returns an error message 999
    """

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
        return 999