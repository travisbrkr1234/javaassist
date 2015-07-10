import sys
sys.path.append("C:\\Users\\carlos.ochoa\\Documents\\Support Dev\\Python\\csvToolbox\\")
import csv
import ISServer_master as ISServer
infusionsoftapp = "as113"
infusionsoftAPIKey = ""

thisserver = ISServer.ISServer(infusionsoftapp, infusionsoftAPIKey)
with open("C:\\Users\\carlos.ochoa\\Documents\\Support Dev\\Python\\export_1.csv", 'rb') as infile:
    thisreader = csv.DictReader(infile)
    for eachrow in thisreader:
        thisserver.dupeCreate(eachrow)
