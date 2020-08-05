


contacts = [
    ('Joe', 56, 'green'),
    ('Jane', 32, 'blue'),
    ('Joanna', 3, 'red')
]
for contact in contacts:
    print(f'{contact[0]}\'s favorite color is {contact[2]}')


contact = ('Joe', 56, 'green')
print(contact[0]) # Joe
print(contact[1]) # 56
print(contact[2]) # green

# contact.append(5) # crash

for i in range(len(contact)):
    print(contact[i])

for element in contact:
    print(element)




