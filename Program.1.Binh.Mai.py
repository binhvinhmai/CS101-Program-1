#CS101
#Program 1, Binh Mai
#Program 1
#Binh Mai
#bvmvw5@mail.umkc.edu
#Creation date: September 4, 2014
#Due date: September 7, 2014
#Problem: Create a program that will prompt the user for their desired
#   number of upper, lower, and corner cabinets. Then the program is
#   expected to calculate the total number of cutting, sanding, and
#   finishing required of the project. Finally, it should give a
#   calculation of the total amount of hours required for the project
#Algorithm:
#   1. Prompt for the number of upper cabinets from user
#   2. Prompt for the number of lower cabinets from user
#   3. Prompt for the number of corner cabinets from user
#   4. Calculate the amount of cutting hours from data collected
#   5. Calculate the amount of sanding hours from data collected
#   6. Calculate the amount of finishing hours from data collected
#   7. Calculate the total amount of labor hours
#Error Handling: None

upper_cabinets_str=input("Enter the amount of upper cabinets desired:")
upper_cabinets_int = int(upper_cabinets_str)
#Asking user for number of upper cabinets
#   and then converting the string into an integer

lower_cabinets_str=input("Enter the amount of lower cabinets desired:")
lower_cabinets_int = int(lower_cabinets_str)
#Asking user for number of lower cabinets
#   and then converting the string into an integer

corner_cabinets_str=input("Enter the amount of corner cabinets desired:")
corner_cabinets_int = int(corner_cabinets_str)
#Asking user for number of corner cabinets
#   and then converting the string into an integer

total_cutting_hours=(1.1*upper_cabinets_int)+(1.4*lower_cabinets_int)+(2.0*corner_cabinets_int)

total_sanding_hours=(2.3*upper_cabinets_int)+(1.7*lower_cabinets_int)+(1.3*corner_cabinets_int)

total_finishing_hours=(3.3*upper_cabinets_int)+(2.6*lower_cabinets_int)+(1.6*corner_cabinets_int)

total_labor_hours=total_cutting_hours+total_sanding_hours+total_finishing_hours

print(total_cutting_hours)

print(total_sanding_hours)

print(total_finishing_hours)

print(total_labor_hours)
