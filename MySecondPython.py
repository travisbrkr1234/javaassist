import sys
sys.path.append("C:\\Users\\carlos.ochoa\\Documents\\Support Dev\\Python\\csvToolbox\\")
import csv
import ISServer_master as ISServer
infusionsoftapp = "as113"
infusionsoftAPIKey = ""

thisserver = ISServer.ISServer(infusionsoftapp, infusionsoftAPIKey)
allrecords = thisserver.getAllRecords("Contact")
for eachrecord in allrecords:
    print "FirstName: %s \t LastName: %s"%(eachrecord["FirstName"], eachrecord["LastName"])
