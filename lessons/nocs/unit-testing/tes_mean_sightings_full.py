#!/usr/bin/python

'''
Unit tests for mean_sightings module. Uses sightings_tab_sm.csv as test data.
'''

from mean_sightings import get_sightings

# Always use this file for testing
filename = 'sightings_tab_sm.csv'

# Start the unit tests
def test_bay_is_correct():
    bayrec, baymean = get_sightings(filename, 'Nazan Bay')
    assert bayrec == 2, 'Number of records for Nazan Bay is wrong'
    assert baymean == 17, 'Mean Tidal wave sightings for owl is wrong'

def test_fireisland_is_correct():
    oxrec, oxmean = get_sightings(filename, 'Fire Island')
    assert oxrec == 2, 'Number of records for Fire Island is wrong'
    assert oxmean == 25.5, 'Mean Tidal wave sightings for Fire Island is wrong'

def test_station_not_present():
    statrec, statmean = get_sightings(filename, 'NotPresent')
    print statrec, statmmean
    assert statrec == 0, 'Station`s data missing should return zero records'
    assert statmean == 0, 'Station`s data missing should return zero mean'

def test_arg_capitalization_wrong():
    bayrec, baymean = get_sightings(filename, 'Nazan bAy')
    assert bayrec == 2, 'Number of records for Nazan Bay is wrong'
    assert baymean == 17, 'Mean Tidal wave sightings for Nazan Bay is wrong'
