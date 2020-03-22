from fhir_parser import FHIR

# fhir = FHIR('https://localhost:5001/api/', verify_ssl=False)

class Main:
    def __init__(self):
        self.fhir = FHIR('https://localhost:5001/api/', verify_ssl=False)
        self.patients = self.fhir.get_all_patients()

    def print_patients_in_range(self, limit, lower, upper, sender_name, sender_ref, app_url):
        i = 0
        patients_list = []
        for patient in self.patients:
            dict = {}
            if not i < limit:
                # print(patients_list)
                return patients_list
            id = patient.uuid
            name = patient.full_name()
            age = patient.age()
            if age >= lower and age < upper:
                telecoms = patient.telecoms
                phone = telecoms[len(telecoms) - 1].number
                # print(phone)
                msg = "Hi " + name + ",\n" + "Are you a carer? If so, we've built an app just for you! You can download our app for carers here: " + app_url + "\nUse this reference code to set up your app: " + sender_ref + "\nTake Care,\n" + sender_name
                # print(msg)
                # print(id)
                # print(name)
                # print(age)
                # print()
                dict["phone"] = phone
                dict["msg"] = msg
                patients_list.append(dict)
                i += 1

# main = Main()
# list = main.print_patients_in_range(3, 55, 65, "Paul", "UCL-FHIR-Hack", "appdownload.com")

# patient = fhir.get_patient('8f789d0b-3145-4cf2-8504-13159edaa747')
# name = patient.full_name()
# print(patient)
# list = fhir.get_all_patients()