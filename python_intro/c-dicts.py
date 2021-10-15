mydict = {"key": "value", "secondkey": "secondvalue"}

print(mydict)

mydict["intkey"] = 123
mydict["floatkey"] = 456.789
mydict["listkey"] = [1, 2, 3]

print(mydict)

print(mydict["intkey"])
print(mydict["key"])

print(mydict["listkey"][1])

nested_list = mydict["listkey"]
print(nested_list)

print(id(nested_list), id(mydict["listkey"]))

mydict["dictkey"] = {"nestedkey": "nestedvalue", "nesteddictkey": {"nestednestedkey": "racecar"}, "nestedlistkey": [4, 5, 6]}
print(mydict)

print(mydict["dictkey"]["nestedlistkey"][2])
print(mydict["dictkey"]["nesteddictkey"]["nestednestedkey"])

mydict2 = {
    "key": "value",
    "somelist": [100, 200, 300],
    "somedict": {
        "blah": {
            "tacocat": {
                "racecar": [555, 999, 0]
            },
            "somethingelse": "averylongandboringstring"
        },
        "potato": "potatoagain"
    }
}

for index, char in enumerate(mydict2["somedict"]["blah"]["somethingelse"]):
    print(index, char)

print(mydict2["somedict"]["blah"]["tacocat"]["racecar"][1])

print(mydict2.keys())

print(mydict2.values())

print(mydict2.items())

for item in mydict2.items():
    print(item)

for key, value in mydict2.items():
    print(key, value)

# print(mydict2["tacocat"])

print(mydict2.get("tacocat"))

