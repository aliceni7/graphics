f = open("image.ppm","w+")
f.write("P3\n")
f.write("500 500\n")
f.write("255\n")
for i in range(500):
    for j in range(500):
        for k in range(3):
            f.write(str(j - 150 * k)+" ")
    f.write("143\n")
    
f.close()
