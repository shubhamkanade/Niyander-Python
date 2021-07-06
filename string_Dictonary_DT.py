#Python's dictionaries are kind of hash table type. They work like associative arrays
#or hashes found in Perl and consist of key-value pairs. A dictionary key can be almost
#any Python type, but are usually numbers or strings. Values, on the other hand, can
#be any arbitrary Python object.
#Dictionaries are enclosed by curly braces ({ }) and values can be assigned and
#accessed using square braces ([]). For example:



dict={}
dict["one"]="This is one"

tinydict={"name":"john","age":40,"address":"pune"}
#print ["one"]

print tinydict["name"]

print tinydict.keys()

print tinydict.values()

#Dictionaries have no concept of order among elements. It is incorrect to say that the
#elements are "out of order"; they are simply unordered.


