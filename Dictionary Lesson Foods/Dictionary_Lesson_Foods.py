name_list=['banana','egg','cheese pizza','tamales']
#vegan=[True,False,False,True]
#calories=[105,78, 213, 284]

vegan_dict={'banana':True, 'egg':False, 'cheese pizza':False, 'tamales':True  }

for name in name_list:
    if vegan_dict[name]:
        print(f"{name} is vegan")
    else:
        print(f"{name} is not vegan")

