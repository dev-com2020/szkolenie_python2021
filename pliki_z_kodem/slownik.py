slownik3 = {"cztery": 4,"pięć": 5}
slownik = dict([("jeden", 1), ("dwa", 2), ("trzy", 3)])
slownik2 = dict(jeden=1, dwa=2, trzy=3)



print("jeden" in slownik3)
print(slownik2.values())
slownik2["cztery"] = 4
print(slownik2.keys())

