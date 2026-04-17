#'''
#testing https://raider.io/api/v1/mythic-plus/runs? api call to get all top 100 runs in each season
#parameters:
#-season itterate over all
#-region always "world"
#-dungeon always "all"
#-page iterate from "0" to "4"
#'''
import json
import csv
from collections import Counter
from raiderio import RaiderIO

#baseURL="https://raider.io/api/v1/mythic-plus/runs?"
#region="region=world"
#dungeon="dungeon=all"
#page="page=0"(,1,2,3,4)
i=0
all_seasons=[#legion seasons
         "season-7.2.0", "season-7.2.5", "season-7.3.0", "season-7.3.5", "season-post-legion", "season-pre-bfa", 
         #bfa seasons
         "season-bfa-1", "season-bfa-2", "season-bfa-2-post", "season-bfa-3", "season-bfa-3-post", "season-bfa-4", "season-bfa-4-post", 
         #expansion that will not be named seasons
         "season-sl-1", "season-sl-1-post", "season-sl-2-legion-timewalking", "season-sl-2-post-915", "season-sl-2-post", "season-sl-2", 
         "season-sl-3-legion-timewalking", "season-sl-3-post-925", "season-sl-3", "season-sl-4-break-the-meta", "season-sl-4-legion-timewalking",
         "season-sl-4", "season-sl-4-patch-10-0", "season-sl-4-post", 
         #dragonflight seasons
         "season-df-1-break-the-meta", "season-df-1-post", "season-df-1", "season-df-2-break-the-meta", "season-df-2-post-1015",
         "season-df-2-post-1017", "season-df-2-post", "season-df-2", "season-df-3-break-the-meta", "season-df-3-meta-vs-meta", "season-df-3", 
         "season-df-4-break-the-meta", "season-df-4-post", "season-df-4", "season-df-4-cutoffs", 
         #tww seasons
         "season-tww-1-break-the-meta", "season-tww-1-post", "season-tww-1", "season-tww-2-meta-vs-meta", "season-tww-2-break-the-meta", 
         "season-tww-2", "season-tww-3-break-the-meta", "season-tww-3", "season-tww-3-cutoff", 
         #midnight seasons
         "season-mn-1" 
         ]
seasons=[#legion seasons
         "season-7.2.0", "season-7.2.5", "season-7.3.0", "season-7.3.5", "season-post-legion", "season-pre-bfa", 
         #bfa seasons
         "season-bfa-1", "season-bfa-2", "season-bfa-2-post", "season-bfa-3", "season-bfa-3-post", "season-bfa-4", "season-bfa-4-post", 
         #expansion that will not be named seasons
         "season-sl-1", "season-sl-1-post", "season-sl-2-post-915", "season-sl-2-post", "season-sl-2", 
         "season-sl-3-post-925", "season-sl-3",
         "season-sl-4", "season-sl-4-patch-10-0", "season-sl-4-post", 
         #dragonflight seasons
         "season-df-1-post", "season-df-1", "season-df-2-post-1015",
         "season-df-2-post-1017", "season-df-2-post", "season-df-2", "season-df-3", 
         "season-df-4-post", "season-df-4", "season-df-4-cutoffs", 
         #tww seasons
         "season-tww-1-post", "season-tww-1",
         "season-tww-2", "season-tww-3", "season-tww-3-cutoffs", 
         #midnight seasons
         "season-mn-1" 
         ]
error_seasons=[]
write_to_sheet=[["Class","Pop","%"]]
#gotta get class and/or spec from character 
with RaiderIO() as rio:
    #total_classes=[]
    #for s in seasons:
        #s="season-tww-1"
        s="season-7.3.0"
        p=0
        season_classes=[]
        while p < 5:
            #print(top20[i].get('run').get('roster')[n].get('character').get('class').get('slug'))
            try:
                top20 = rio.get_mythic_plus_runs(region="world", season=s, dungeon="all", affixes="all", page=p).get('rankings')
                p+=1
                #i=0
                temp_roster=[run.get('run').get('roster')[0] for run in top20]
                temp_class=[player.get('character').get('class').get('slug') for player in temp_roster]
                season_classes.extend(temp_class)
            except:
                 print("an error has occurred on: "+s)
        print(season_classes)
        classes_dict=Counter(season_classes)
        player_pop=classes_dict.total()
        print("Class | Pop | %")
        for player in classes_dict.keys():
             value=classes_dict[player]
             percent=(value/player_pop)*100
             print(player+" | "+str(value)+" | "+str((round(percent)))+"%")
             temp_array=[player, value, round(percent)]
             write_to_sheet.append(temp_array)
        #print(classes_dict.keys())
        #print(classes_dict.values())
        #print("total players: "+str(sum(classes_dict.values())))
with open('test.csv','w',newline='') as sheet:
     writer=csv.writer(sheet)
     writer.writerows(write_to_sheet)
            
                