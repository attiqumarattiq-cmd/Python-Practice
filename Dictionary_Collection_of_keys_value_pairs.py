
#==========================================================
#  SYNTEX 
a = {
        "Artificial" : "Intelligence",
        "Ahmad" : "Coding", 
        "marks" : "100",
        "list" : [1,2,9,0]
}
   
print(a["Artificial"])    # Output: Intelligence
print(a["Ahmad"])         # Output: coding
print(a["marks"])         # Output: 100
print(a["list"])          # Output: [1,2,9,0]

#===================================================
# items(): Gives the list of data in dictionary
print(a.items())

#===================================================
# keys(): Returns the list of keys
print(a.keys())

#====================================================
# update({"friends"}): Used to update the data.
d = {'X': 10}
d.update(Y=20, z=30)
print(d)

#=====================================================
