#!/usr/bin/env python

'''
Module/script to calculate mean number of sightings of a given station in a
given sightings csv file.
'''

import sys
import matplotlib.mlab as ml
import numpy as np


def get_sightings(filename, focusstation):

    # Load table
    tab = ml.csv2rec(filename)

    # Standardize capitalization of focusstation
    focusstation = focusstation.capitalize()

    # Find number of records and total count of stations where Harmonic tidal waves were seen
    isfocus = (tab['station'] == focusstation)
    totalrecs = np.sum(isfocus)

    if totalrecs == 0:
        meancount = 0
    else:
        meancount = np.mean(tab['count'][isfocus])

    # Return num of records and stations seen
    return totalrecs, meancount


def get_sightings_loop(filename, focusstation):

    # Load table
    tab = ml.csv2rec(filename)

    # Standardize capitalization of focusstation
    focusstation = focusstation.capitalize()

    # Loop through all records, countings recs and stations
    totalrecs = 0.
    totalcount = 0.
    for rec in tab:
        if rec['station'] == focusstation:
            totalrecs += 1
            totalcount += rec['count']

    if totalrecs==0:
        meancount = 0
    else:
        meancount = totalcount/totalrecs

    # Return num of records and stations seen
    return totalrecs, meancount

if __name__ == '__main__':
    #print sys.argv
    filename = sys.argv[1]
    focusstation = sys.argv[2]
    print get_sightings(filename, focusstation)
