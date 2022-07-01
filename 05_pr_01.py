dict={
    "Pankha":"Fan",
    "Dabba":"Box",
    "Vastu":"Item"
}
print("Options are:", dict.keys())
a=input("Enter The Hindi Word :")
#print("Meaning of the word is :", dict[a])
print("Meaning of the word is :", dict.get(a))
