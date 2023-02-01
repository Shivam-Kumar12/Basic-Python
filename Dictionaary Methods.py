mydict={    
          #keys      #values
         "fast" :"IN A quick manner",
         "harry"  : "A coder",
         "shivam" : "is a good cooder",
         "marks" :  [1,2,5] ,
         "another" :{'shivam': 'player'} # nested dictionay
      }
    
    
print(list(mydict.keys())) #prints the keys of the dictionary
print(list(mydict.values())) #prints the vaallues of the dictionary
print(list(mydict.items()))  # print  the (keys , valueess ) for all content of the dictionary
print(mydict)
updatedict={
    " freinds" : "shivam"       # this is used to update aor asdd the item in the dictionary with key and values
}
mydict.update(updatedict)
print(mydict)
print(mydict.get("shivam"))  # prints value associated wih key shivam in the dictionary
print(mydict['shivam'])    #  prints value associated wih key shivam in the dictionary
  # diffrence between .gt and [] syntax in dictinaries 
print(mydict.get("shivam2"))  #Retun None as shivam 2 is not present in the dictionary
print(mydict['shivam2'])    # throws an Error as shivam2 is not present in the dictionary