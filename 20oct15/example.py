#!/usr/bin/env python3

import sys

pdbfilename=sys.argv[1]

f=open(pdbfilename)
lines=f.readlines()
f.close()

records=[]
massdict={"H":1.01, "C":12.01,"N":14.01,"O":16.0, "P":30.97, "S":32.07,"MG":24.30}
for line in lines:
	x=float(line[30:38])
	element=line[76:78].strip()
	mass=massdict[element]
	records.append([x,element,mass])

summass=0
sumx_mass=0
for record in records:
	summass+=record[2]
	sumx_mass+=record[2]*record[0]

weightedx=summass/sumx_mass
print (summass,sumx_mass,weightedx)

#for record in records:
#	print ("The mass for %s is %.3f" % (record[1], record[2]))
