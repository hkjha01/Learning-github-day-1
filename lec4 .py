#dictionary-they are mutable  stor data in form of key:("val1","val2")

a={"name":"ab",
   "id" : "12",
   "per":{"sc":"90.9",  #nested-key in a key
          "pq":"98.9",
          "ar":"80.9"}}

print(type(a))
print(a["name"])
print(a)

a["name"]="bc" #muting
print(a)
a["name"]="" #can be empty
print(a)

# mydict.keys() -shows all keys
print(a.keys())

#printing total no. of  keys
print(len(a))

#mydict.values() -returns all values
print(a.values())

#mydict.items()  - returns all key as tuples
print(a.items())

#mydict.get("xyz")  -returns the key according to value asked
print(a.get("id"))

#mydict.update({newdict}) - can insert new items
a.update({"name":"1aw","name":"tp"})
print(a)


