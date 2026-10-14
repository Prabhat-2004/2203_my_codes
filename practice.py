# s1 = "Prabhat"
# s2 = "Kumar"

# print("Adress os s1",id(s1))
# print("Adress os s2",id(s2))
# print("Adress of 'a' from s1:",id(s1[2]))
# print("Adress of 'a' from s1:",id(s1[5]))
# print("Adress of 'a' from s2:",id(s2[3]))
 

full_name = "Prabhat Kumar Dakua"
name_parts = full_name.split()
initials_name = f"{name_parts[0]}" + " ".join([f"{name_parts[0]}." for name in name_parts[1:]])
print("Name Parts: ", name_parts)
print("Formated name with initials:", initials_name)