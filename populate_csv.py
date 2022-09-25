import csv
import random
#import numpy as np

c=10
with open("radio.csv", "w") as f:
    for i in range(99):
        id = "U0443S95K" + str(c)
        c+=1

        q1 = random.randint(1,5)
        if q1 == 1 or q1 == 2:
            q1 = random.randint(1,5)
        f.write("RR2o,"+id+",How are you today? :woozy_face:,"+str(q1)+"\n")

        q2 = random.randint(1,5)
        if q2 == 4 or q2 == 5:
            q2 = random.randint(1,5)
        f.write("ntL,"+id+",How well supported do you feel at work? :face_with_thermometer:,"+str(q2)+"\n")

        q3 = random.randint(1,5)
        if q3 == 3:
            q3 = random.randint(1,5)
        f.write("qwKw,"+id+",How diverse and inclusive do you feel the company is? :stuck_out_tongue_winking_eye:,"+str(q3)+"\n")

        q4 = random.randint(1,5)
        if q4 == 1 or q4 == 2 or q4 == 3:
            q4 = random.randint(1,5)
        f.write("s/o,"+id+",How satisfied are you with the company's leadership? :disguised_face:,"+str(q4)+"\n")

        q5 = random.randint(1,5)
        f.write("ij5Y,"+id+",How connected to your co-workers do you feel? :smiling_face_with_3_hearts:,"+str(q5)+"\n")