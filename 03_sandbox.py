import os ;import sys ;import subprocess
def calculateGrade():
    try:
        val = float(input("Enter your marks: "))
        if val == 100:
            print("wow")
        elif val >= 90 and val <= 100:
            print("Outstanding")
        elif val >= 80 and val < 90:
            print("Excellent")
        elif val >= 70 and val < 80:
            print("Very Good")
        elif val>= 60 and val < 70:
            print("Needs Improvement")
        elif val>=30 and val <60:
            print("Work hard")
        elif val>=0 and val<30:
            print("Poor")
        
        else:
            raise ValueError("Enter a valid score, i.e., between 0 and 100")
    except Exception as err:
        print("ERROR:", err)
        print("Restarting the program")
        print("------------------------")
        subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:]) #restart the program
calculateGrade()