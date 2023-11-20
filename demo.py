"""
A SIMPLE SHODAN SEARCH OF EXISTING + PUBLIC DATA THAT RETURNS INFO ABOUT DOMAINS THAT ARE INTERNET FACING:
"""

import shodan
from config import SHODAN_API_KEY

api = shodan.Shodan(SHODAN_API_KEY)


"""

THIS IS A PROGRAM THAT WILL OFFER GEOGRAPHICAL INFORMATION OF OPEN PORTS OF STORED SHODAN ENTITIES

"""

def user_search(query):
    results = api.search(query)
    return results

def total(results):
    return results['total']

def create_ip_dict(results):
    
    # Create a dictionary to store information
    ip_dict = {}
    list_domain = []

    # Iterate through each search result
    for result in results['matches']:

        # Assign k to each result's IP address
        k = result['ip_str']
        domain = result['domains']

        # If k is not in the dictionary, then add it and the corresponding city
        if k not in ip_dict:
            ip_dict[k] = result['location']['city'], domain

    return ip_dict

# print(create_ip_dict(user_search('Wayfair')))

def get_non_webservers(ip_dict):

    nonweb_list = []

    for k, v in ip_dict.items():
        if v[-1][:] == []:
            nonweb_list.append((k, v[0]))

    return nonweb_list

print(get_non_webservers(create_ip_dict(user_search('Wayfair'))))

def get_ip_list(query):
    results = user_search(query)
    ip_dict = create_ip_dict(results)
    ip_list = list(ip_dict.keys())

    return ip_list

def get_ip_coords(query):
    ip = get_ip_list(query)
    first_ip = ip[2]

    host = api.host(first_ip)
    latitude = host['data'][1]['location']['latitude']
    longitude = host['data'][1]['location']['longitude']
    coords = latitude, longitude

    return coords

# print(get_ip_coords('babson'))


# def see_ips(query):
#     results = user_search(query)
#     ip_dict = create_ip_dict(results)
#     print(get_ip_list(ip_dict))
# see_ips('babson')

# def get_ip_info(ip_list):
    
#     ip = ip_list[0]

#     host = api.host(ip)

#     print(host)

# except shodan.APIError as e:
#     print(f'Error: {format(e)}.')
    


# host = api.host()


