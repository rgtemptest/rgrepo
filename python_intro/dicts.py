mydict = {
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

for index,value in enumerate(mydict["somedict"]["blah"]["somethingelse"]):
    print(index, value)	

print("\n\nnow\n\n")
print(mydict["somedict"]["blah"]["tacocat"]["racecar"][1])
print(mydict.items())

for key,value in mydict.items():
    print(key, '--', value)
