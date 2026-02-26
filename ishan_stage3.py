name = input('Enter Your Name: ')

sub1= float(input('Enter Marks For Subject 1:'))
sub2= float(input('Enter Marks For Subject 2:'))
sub3= float(input('Enter Marks For Subject 3:'))

total = sub1 + sub2 + sub3
percentage = (total / 300) * 100

# Grade logic
if percentage >= 75:
    grade = 'A' 
elif percentage >=60:
    grade = 'B'
elif percentage >= 50:
    grade = 'C'
else:
    grade = 'F'

print(f'\nName: {name}')
print(f'Total Marks: {total}')
print(f'Percentage: {percentage}%')
print(f'Grade: {grade}')