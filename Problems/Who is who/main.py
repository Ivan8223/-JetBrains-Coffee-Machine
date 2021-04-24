class Angel:
    color = "white"
    feature = "wings"
    home = "Heaven"


class Demon:
    color = "red"
    feature = "horns"
    home = "Hell"


my_angel, my_demon = Angel(), Demon()

for creature in [my_angel, my_demon]:
    print(creature.color, creature.feature, creature.home, sep="\n")
