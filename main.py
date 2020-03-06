from fhir_parser import FHIR

# fhir = FHIR('https://localhost:5001/api/', verify_ssl=False)

class Main:
    def __init__(self):
        self.fhir = FHIR('https://localhost:5001/api/', verify_ssl=False)
        self.patients = self.fhir.get_all_patients()

    def print_patients_in_range(self, lower, upper):
        for patient in self.patients:
            id = patient.uuid
            name = patient.full_name()
            age = patient.age()
            if age >= lower and age < upper:
                msg = "Hi " + name + ",\n" + "Are you a carer? If so, you can download our app for carers here: <Insert Link>"
                print(msg)
                print(id)
                print(name)
                print(age)

main = Main()
main.print_patients_in_range(55, 65)

# patient = fhir.get_patient('8f789d0b-3145-4cf2-8504-13159edaa747')
# name = patient.full_name()
# print(patient)