__author__ = 'Ramya'

###
# External packages used: googlemaps, pygeocoder
# Sources:
# https://pypi.python.org/pypi/googlemaps/
# https://pypi.python.org/pypi/pygeocoder
#
# Installation:
# From the terminal, install the 2 packages using commands below.
# pip install googlemaps
# pip install pygeocoder
#
# Steps to Execute:
# The program takes 2 command line arguments: valid source and destination addresses
# Example:
# python StateLister.py "2221 Broadway St Redwood City, CA 94063" "1600 Pennsylvania Ave NW  Washington, DC 20500"
###

###
# TODO: What if the API response bypasses one or more states on the path?
# We could have information regarding the immediate neighbours of each state. Whenever we move from one state to another,
# we could check the heuristic information to verify that we have not skipped any state along the path.
###


import optparse
from pygeocoder import Geocoder
from googlemaps import GoogleMaps


def listStates(source, destination):
    gmaps = GoogleMaps()
    stateList = []
    # Finding a route from the source to the destination address
    route = gmaps.directions(source, destination)
    for step in route['Directions']['Routes'][0]['Steps']:
        # For each step in the route, find the latitude-longitude coordinates
        latlong = Geocoder.reverse_geocode(step['Point']['coordinates'][1],step['Point']['coordinates'][0])
        # Finding the state corresponding to the lat-long coordinates
        state = latlong.state
        # Checking to avoid duplicates
        if state not in stateList:
            stateList.append(state)
            print state


if __name__ == "__main__":
    parser = optparse.OptionParser("usage: %prog arguments")
    parser.add_option("-s", "--source", type = "string", help = "Source address", dest = "source")
    parser.add_option("-d", "--destination", type = "string", help = "Destination address", dest = "destination")
    (opts, args) = parser.parse_args()
    # Ensure two arguments (source and destination addresses) are passed
    if len(args) < 2:
        parser.error('Insufficient number of arguments! Please provide a source address and a destination address.')
    elif len(args) > 2:
        parser.error('Too many arguments! Please specify only 2 street addresses.')
    # Checking for a valid address
    if Geocoder.geocode(args[0]).valid_address and Geocoder.geocode(args[1]).valid_address:
        listStates(args[0], args[1])
    else:
        parser.error('Incorrect source or destination address! Please verify.')
