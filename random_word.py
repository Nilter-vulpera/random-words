import random
v = ["а","е","ё","и","о","у","ы","э","ю","я"]
k = ["б","в","г","д","ж","з","й","к","л","м","н","п","р","с","т","ф","х","ц","ч","ш","щ"]

h = " "
o=0
u=0

r=random.randint(3,7)
h = (h + str(random.choice(k)))
for i in range(r):


        l = random.randint(1, 2)
        if l==1:
            if o == 2:
                h = (h + str(random.choice(k)))
                o=0
            h=(h+str(random.choice(v)))
            o=o+1

        else:
            if u == 2:
                h = (h + str(random.choice(v)))
                u=0
            h=(h+str(random.choice(k)))
            u=u+1



print(h)








