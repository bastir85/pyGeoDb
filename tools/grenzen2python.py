#!/usr/bin/env python
# encoding: utf-8
"""
grenzen2python.py - convert OpenStreetMap data to python code

Created by Maximillian Dornseif on 2010-01-17.
Copyright (c) 2010 HUDORA. All rights reserved.
"""

import sys
import os
import unittest
from pprint import pprint

from xml.etree.ElementTree import ElementTree
tree = ElementTree()
tree.parse("data/de_landmasse_osm_relation_62781.gpx")
root = tree.getroot()

tracks = []
for trkseg in root.findall(".//trkseg"):
    track = []
    for trkpt in trkseg.findall('trkpt'):
        track.append((float(trkpt.attrib['lon']), float(trkpt.attrib['lat'])))
    tracks.append(track)

sys.stdout.write("# autogenerated - do not edit\n")
sys.stdout.write("deutschgrenzen = ")
pprint(tracks, sys.stdout)