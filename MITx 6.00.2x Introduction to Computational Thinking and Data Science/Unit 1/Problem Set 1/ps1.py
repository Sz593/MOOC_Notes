###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    trips = []
    cows_available = []
    used_cows = []
    
    for k, v in cows.items():
        cows_available.append((k, v))

    cows_available.sort(key=lambda x: x[1], reverse=True)
    
    while len(cows_available) != len(used_cows):
        current_trip_limit = limit
        current_trip_cows = []
        
        for cow in cows_available:
            if cow not in used_cows:
                if cow[1] <= current_trip_limit:
                    current_trip_cows.append(cow[0])
                    used_cows.append(cow)
                    current_trip_limit -= cow[1]
            
        trips.append(current_trip_cows)

    return trips

    


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    
    # small_cows = {'Betsy':9, 'Florence':2, 'Herman':7, 'Maggie':3}
    # cows_2 = {'Miss Bella': 25, 'Milkshake': 40, 'MooMoo': 50, 'Horns': 25, 'Lotus': 40, 'Boo': 20}
    cow_list = list(cows.keys())
    trip_results = {'min num trips':100, 'list of trips':[]}
    
    for trip_list in get_partitions(cow_list):
        
        trip_weight_list = []
        for trip in trip_list:
            trip_weight = 0
            for passenger_cow in trip:
                trip_weight += cows[passenger_cow]
            trip_weight_list.append(trip_weight)

        if max(trip_weight_list) > limit:
            continue
        
        if len(trip_list) < trip_results['min num trips']:
            trip_results['min num trips'] = len(trip_list)
            trip_results['list of trips'] = trip_list
    
    return trip_results['list of trips']
    

        
# Problem 3
def compare_cow_transport_algorithms(cows, limit):
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """

    greedy_t0 = time.time()
    greedy_cow_transport(cows, limit)
    greedy_t1 = time.time()
    
    print('The greedy algorithm runs in {:.5f} seconds.'.format(greedy_t1 - greedy_t0))
    
    brute_t0 = time.time()
    brute_force_cow_transport(cows, limit=10)
    brute_t1 = time.time()
    print('The brute force algorithm runs in {:.5f} seconds.'.format(brute_t1 - brute_t0))
    


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))

print(compare_cow_transport_algorithms(cows, limit=10))