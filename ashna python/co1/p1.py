start_year=int(input("enter the starting year:"))
end_year=int(input("enter the ending year:"))
print("the first year is:",start_year,"the last year is:",end_year)
print("list of leap yers are:")
for i in range(start_year,end_year):
    if(i%4==0)and(i%100!=0)or(i%400==0)and(i%100==0):
        print(i,"is a leap year")
