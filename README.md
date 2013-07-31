StateLister
===========

My solution to an interview question I faced recently. 


Challenge
==========

Given two arbitrary street addresses in the continental US, calculate the list of states that the direct path between 
the two addresses passes through (with a reasonable tolerance for error of several miles)


Sources
========

External packages used: googlemaps, pygeocoder

https://pypi.python.org/pypi/googlemaps/

https://pypi.python.org/pypi/pygeocoder


Installation
=============

From the terminal, install the 2 packages using commands below.

pip install googlemaps

pip install pygeocoder


Steps to Execute
=================

The program takes 2 command line arguments: valid source and destination addresses


Example
=======

python StateLister.py "2221 Broadway St Redwood City, CA 94063" "1600 Pennsylvania Ave NW  Washington, DC 20500"
