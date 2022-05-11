import os

path = os.chdir("videodataset/")

i=1
for file in os.listdir(path):
    new = "user.2.{}.jpg".format(i)
    os.rename(file,new)

    i=i+1