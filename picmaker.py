f = open("image.ppm","w+")
f.write("P3\n")
f.write("50 50\n")
f.write("255\n")
for i in range(50):
    for w in range(50):
        f.write("255 ")
    


f.close()
