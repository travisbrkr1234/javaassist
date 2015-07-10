import sys
sys.path.append("C:\\Users\\carlos.ochoa\\Documents\\Support Dev\\Python\\csvToolbox\\")
import csv
import ISServer_master as ISServer
infusionsoftapp = "as113"
infusionsoftAPIKey = ""

thisserver = ISServer.ISServer(infusionsoftapp, infusionsoftAPIKey)
allrecords = thisserver.getAllRecords("OrderItem")
for eachrecord in allrecords:
    for eachkey in eachrecord:
        print eachkey, eachrecord[eachkey]
