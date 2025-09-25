class BankDetails:
    def __init__(person):
        person.information = [ ]
    def add_info(person_name, deposits, withdraws, loans):
        info = (person_name, deposits,withdraws)
        person.information.append(info)
    def remove_info(loans):
        for info in person.information:
            if info[0] == person_name:
                person.information.remove(info)
                break
        def calculate_total(person):
            total=0
            for item in person.information:
                total += info[1]
            return total
b = BankDetails()
b.add_info("varshitha",1000,400)
b.add_info("kavys",2000,800)
b.add_info("sarvani",3000,900)
print("Current information in  BankDetails: ")
for info in b.information:
    print(info[0], "_", info[1])
total_withdraws = b.calculate_total()
print("total withdraws: ",total_withdraws)
