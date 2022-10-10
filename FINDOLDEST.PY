#Take input of age from 3 people determine the oldest and youngest
siddhi = int(input("Age of a first person"))

vidhi = int(input("Age of a second person"))
sky = int(input("Age of a third person"))

if siddhi > vidhi:
    print("vidhi is youngest")

if siddhi < sky:
    print("siddhi is youngest")

if vidhi < sky:
    print("sky is oldest")
    