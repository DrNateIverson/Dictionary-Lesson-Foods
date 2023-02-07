name=['banana','egg','cheese pizza','tamales']
vegan=[True,False,False,True]
#calories=[105,78, 213, 284]

for k in range(len(name)):
    if vegan[k]==True:
        print(f"{name[k]} is vegan")
    else:
        print(f"{name[k]} is not vegan")

