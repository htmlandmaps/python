# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# feat_2_shape.py
# Created on: 2013-10-09 14:05:43.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy, os
from arcpy import env

# Set environment settings to location of where first mxd is saved
env.workspace = 'T:\\03Comprehensive_Planning\\Environmental\\Sustainability\\Disaster Preparedness and Planning Project (DP3)\\DP3 Charts and Maps\\moguam\\HAZUS\\ken\\scripts\\ken101013'
datapath = 'T:\\03Comprehensive_Planning\\Environmental\\Sustainability\\Disaster Preparedness and Planning Project (DP3)\\DP3 Charts and Maps\\moguam\\HAZUS\\ken'


#folder where current mxd is saved
mappath = datapath + '\\scripts\\ken101013\\'


# Set local variables
#inFeatures = ["climate.shp", "majorrds.shp"]

# Local variables:
#geodata_EGISDATA_eoc = "geodata.EGISDATA.eoc"
#geodata_EGISDATA_employer_major = "geodata.EGISDATA.employer_major"

#egispath ONLY point files in STRUCTURE
egispath = 'Database Connections\\Connection to BALT-GISWB1-SRV.sde\\geodata.EGISDATA.Structure\\'

#folder where new shapefiles will be saved
outspace = "T:\\03Comprehensive_Planning\\Environmental\\Sustainability\\Disaster Preparedness and Planning Project (DP3)\\DP3 Charts and Maps\\moguam\\HAZUS\\ken\\scripts\\ken101013\\new\\"

#new mxd file where shapefiles will be saved? 
newmxd = outspace + 'hazuslayers_mbtest.mxd'


for mxdfile in arcpy.ListFiles("*.mxd"):   #linked to where workspace is set # keep 1 mxd in folder
   print mappath + mxdfile   #set to maps/copy   hazusegislayers

   #Set mxd file, df, and list layers
   mxd = arcpy.mapping.MapDocument(mappath + mxdfile)
   #df = arcpy.mapping.ListDataFrames(mxd)
   #lyr = arcpy.mapping.ListLayers(mxd)
   #targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Structure", df)[0]
   #print "Target New Group Layer: " + targetGroupLayer.name
   print '\n'

   #LOOP STUCK HERE; not making out to for mxd***************************
   #it's looping through every layer for dataFrame1
   for dataFrame1 in arcpy.mapping.ListDataFrames(mxd):          #loop dataframes  #why is dataframe1 structure? *****************
     #mxd.activeView=dataFrame1
     #targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Structure", df)[0]
     #print targetGroupLayer
     lyr = arcpy.mapping.ListLayers(mxd)
     targetGroupLayer = arcpy.mapping.ListLayers(mxd, "Structure", dataFrame1)[0] ##MUST INCLUDE 0 here or won't work

     #print "Dataframe name: " + df.name
     print "Dataframe1: " + dataFrame1.name
     print '\n'
     for mapLayers1 in lyr:      #loop through layers
         print "mapLayers1: " + mapLayers1.name  #print lists of all layers (groups and non-groups) until reach old structure?
         #it will also print the egis structure layers created in old structures group
         print '\n'
         #if layer is a group layer named Old Structure
         if mapLayers1.isGroupLayer and mapLayers1.name == "Old Structure": #a layer can be a group layer
               print 'Group Old Layer name: ' + mapLayers1.name
               print '\n'
               print 'Start going through layers in above old group layer:'
               print '\n'
               for glyr1 in arcpy.mapping.ListLayers(mapLayers1):  #for layers in oldstructures
                       print "glyr1: " + glyr1.name  #print list of layers in oldstructures including oldstructures
                       print '\n'
                       if glyr1 != mapLayers1:   #when grouplayer doesnt equal Oldstructures
                           slyr1 = arcpy.mapping.ListLayers(glyr1) #list layer under oldstructures (not oldstructure)
                           
                           for slyr1 in arcpy.mapping.ListLayers(glyr1):
                              #for each layer in old structure
                              print "layer name in old structure: " + slyr1.name
                              print '\n'


                               #feat_class = egispath + slyr1.name + '.shp' #create shapefile of egis path
                               #print 'Feature class: ' + feat_class    #print shapefile name
                               #shpshort = feat_class.rstrip('.shp')    
                               #print 'just shapefile: ' + shpshort
                               #print '\n'
                              
                               #copy features from shapefiles in old structures and save in new folder
                              arcpy.FeatureClassToShapefile_conversion(egispath + slyr1.name, outspace)
                              print "shapefile copied"


                               
                           del slyr1 #no more layers to create in old structures
                           print "*********end of slyr1"
                           print '\n'
               del glyr1  #no more layers to loop through in oldstructures 
               print "*********end of glyr1"
               print '\n'
               
     del mapLayers1   #no more layers in the df
     print "*********end of mapLayers1"
     print '\n'

   del dataFrame1
   print "*********end of dataFrames1"
   print '\n'

del mxdfile, mxd
print '\n Done'