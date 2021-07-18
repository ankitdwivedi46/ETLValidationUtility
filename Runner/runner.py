from Scripts.CountsCheck import CountsCheck


print("---------------------------ETL VALIDATION UTILITY---------------------------")

print("Available Validations")

print("1.Count Check")
print("2.Duplicate Check")
print("3.Unique Check")
print("4.Not Null Check")
print("5.Data Check")
while(1):
    check = input("Enter Type of Check(1 for Counts, 2 for Duplicates, 3 for Unique, 4 for Not Null, 5 for Data and E for Exit)")
    if(check=="E"):
        break
    if(check=="1"):
        source_count_query = input("Enter Source Count Query")
        target_count_query = input("Enter Target Count Query")
        cc = CountsCheck(source_count_query, target_count_query)
        cc.count_validation()








