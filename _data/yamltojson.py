from yaml import load, dump, Loader, Dumper
import json

yamlfile=open('conf_papers.yaml','r')
entries=load(yamlfile, Loader=Loader)
jsonfile=open('conf_papers.json','w')

entrlist=[]
for entry,v in entries.items():
    tempdict={}
    for value in v:
        for k,e in value.items():
            tempdict[k]=e
    entrlist.append(tempdict)
print(entrlist)
json.dump(entrlist,jsonfile,indent=3)

yamlfile.close()
jsonfile.close()
