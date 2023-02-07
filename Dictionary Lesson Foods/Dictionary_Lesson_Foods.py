#name_list=['banana','egg','cheese pizza','tamales']
#vegan=[True,False,False,True]
#calories=[105,78, 213, 284]

#vegan_dict={'banana':True, 'egg':False, 'cheese pizza':False, 'tamales':True  }

foods=[{'name':'banana','vegan':True, 'calories':105},
       {'name':'egg','vegan':False, 'calories':78},
       {'name':'cheese pizza','vegan':False, 'calories':213},
       {'name':'tamales','vegan':True, 'calories':284}]

for food in foods:
    if food['vegan']:
        print(f"{food['name']} is vegan and has {food['calories']} calories ")
    else:
        print(f"{food['name']} is not vegan and has {food['calories']} calories ")

