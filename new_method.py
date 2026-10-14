sentence = "This is the air fiber. This is not giving air it is only fiber.".replace("."," ").split()
print(sentence)
di = {}
for i in sentence:
    if i in di:
        di[i] += 1
    
    else:
        di[i] = 1
print(di)
for key in di:
    print(f"{key}: {di[key]}")