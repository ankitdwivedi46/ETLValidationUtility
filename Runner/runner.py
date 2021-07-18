from Scripts.CountsCheck import CountsCheck
from Scripts.DuplicatesCheck import DuplicatesCheck
from Scripts.UniqueCheck import UniqueCheck
from Scripts.NotNullCheck import NotNullCheck


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
    elif(check=="1"):
        source_count_query = input("Enter Source Count Query")
        target_count_query = input("Enter Target Count Query")
        cc = CountsCheck(source_count_query, target_count_query)
        cc.count_validation()
    elif(check == "2"):
        source_dup_query = input("Enter Source Dup Query")
        target_dup_query = input("Enter Target Dup Query")
        dc = DuplicatesCheck(source_dup_query, target_dup_query)
        dc.duplicate_validation()
    elif(check == "3"):
        source_uniq_query = input("Enter Source Unique Query")
        target_uniq_query = input("Enter Target Unique3 Query")
        uc = UniqueCheck(source_uniq_query, target_uniq_query)
        uc.unique_validation()
    elif (check == "4"):
        source_notnull_query = input("Enter Source Unique Query")
        target_notnull_query = input("Enter Target Unique3 Query")
        nc = NotNullCheck(source_notnull_query, target_notnull_query)
        nc.notnull_validation()







