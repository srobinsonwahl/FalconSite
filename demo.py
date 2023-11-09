"""
A SIMPLE SHODAN SEARCH OF EXISTING + PUBLIC DATA THAT RETURNS INFO ABOUT DOMAINS THAT ARE INTERNET FACING:
"""

import shodan
from config import API_KEY

api = shodan.Shodan(API_KEY)


"""

THIS IS A PROGRAM THAT WILL OFFER GEOGRAPHICAL INFORMATION OF OPEN PORTS OF STORED SHODAN ENTITIES

"""

try:

    # Initial user input that is stored as query
    query = input('Enter an entity to learn more about their security posture:')

    # Use api and query to store results
    results = api.search(query)

    # Print total number of results found
    print(f"Results found: {results['total']}")

    # Create a dictionary to store information
    ip_dict = {}

    # Iterate through each search result
    for result in results['matches']:

        # Assign k to each result's IP address
        k = result['ip_str']

        # If k is not in the dictionary, then add it and the corresponding city
        if k not in ip_dict:
            ip_dict[k] = result['location']['city']

    # Print the dictionary of IP and city
    print(ip_dict)

except shodan.APIError as e:
    print(f'Error: {format(e)}.')

# ipinfo = api.host('8.8.8.8')
# print(ipinfo)

# for banner in api.search_cursor('http.title:"hacked by"'):
#     print(banner)

