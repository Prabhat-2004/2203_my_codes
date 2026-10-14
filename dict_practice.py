contacts = {}

while True:
    entry = input("Enter name and phone number (or type 'done' to finish): ")
    if entry.lower() == 'done':
        break
    if ',' in entry:
        name, phone = entry.split(',', 1)
        contacts[name.strip()] = phone.strip()
    else:
        print("Invalid format. Please enter in 'Name, PhoneNumber' format.")

# Print the contacts
for name, phone in contacts.items():
    print(f"{name}: {phone}")


#Counting Words
sentence = list(input().replace("."," ").split())
print(sentence)
di = {}
# for i in set(sentence):
#     print(f"{i}: {sentence.count(i)}",end=" ")
for i in sentence:
    if i in di:
        di[i]= di[i]+1
    else:
        di[i]=1
print(di)
for i in di.keys():
    print(f"{i} : {di[i]}")