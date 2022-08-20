class Doctor():
    def __init__(self):
        print("This Is Class Doctor")
        
    def BMI(weight, height):
        bmi = weight/(height*height)
        print("Your BMI Is " + str(bmi))
        
    def heart_rate(heart_rates):
        if(heart_rates > 60 and heart_rates < 100):
            print("Great Your Heart Rate Is Normal")
        
        else:
            print("Your Heart Rate Does Not Seem Normal, Please Visit The Clinic")
            
class Patient(Doctor):
    def __init__(self, name , height, weight, heart_rates):
        self.patient_name = name
        self.patient_height = height
        self.patient_weight = weight
        self.patient_heart_rates = heart_rates
        
    def healthCheck(self):
        print("\n Patient Name : ", self.patient_name)
        Doctor.BMI(self.patient_height, self.patient_weight)
        Doctor.heart_rate(self.patient_heart_rates)
        
patient1 = Patient("Michael", 30, 0.9144, 80)
patient1.healthCheck()

patient2 = Patient("Jessica", 40, 1, 120)
patient2.healthCheck()

