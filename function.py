def percent(marks):
    p= ((sum(marks))/400)*100
    return p
marks1=[45,78,88,98]
percentage1=percent(marks1)

marks2=[45,77,85,97]
percentage2=percent(marks2)
print(percentage1,percentage2)