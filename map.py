#!/bin/python3
import sys
import csv
import json
import yaml

i = 0
for arg in sys.argv:
    print('args[' + str(i) + ']->`' + arg + "'" )
    i = i + 1

# load iepcd.json
file_iepcd_json = 'iepcd.json'
with open(file_iepcd_json) as fp_iepcd_json:
    iepcd = json.load(fp_iepcd_json)

# load manifest.yaml
file_manifest_yaml = 'manifest.yaml'
with open(file_manifest_yaml, 'r') as fp_manifest_yaml:
    manifest = yaml.safe_load(fp_manifest_yaml)
    dump = yaml.dump(manifest)
    print( 'manifest before:' )
    print( dump )

# load map.csv

file_map_csv  = 'map.csv'
with open(file_map_csv, newline='') as f:
    reader = csv.reader(f)
    print('mapping iepcd keys to iep cloud keys')
    # for each mapping, map it
    for row in reader: 
        print(row)
        iepcdKey = row[0]
        cloudKey = row[1]
        try:
            iepcdValue = iepcd[iepcdKey]
        except:
            # magic behavior:
            # if the key is not in iepcd
            # then the key is the value
            iepcdValue = iepcdKey
        manifest[cloudKey] = iepcdValue
        

dump = yaml.dump(manifest)
print( 'manifest after :' )
print( dump )

