#Declaring a class Phonebook which inherits from list class

class Phonebook(list):

    #Constructor for initiating an empty list to store records    
    def __init__(self):
        self=[]

    #To add contacts to phonebook
    def add_contact(self,name,phone_no,email):
        self.append([name,phone_no,email])

    #To format the records in phonebook in organized form for printing
    def __str__(self):
        a=0
        formatted='Name                PhoneNumber         Email'
        for item in self:
            formatted+=f'\n{item[0]:20}{item[1]:20}{item[2]:20}'
            a+=1
        if a>0:return formatted
        else:return 'No Record Found!'

    #For sorting the records according to name
    def sort(self):
        sorted_list=sorted(self)
        self.clear()
        for item in sorted_list:
            self.append([item[0],item[1],item[2]])
        return self

    #For searching a record with any desired parameter        
    def search(self):
        print('''Select a parameter to search:
        1. First Name
        2. Last Name
        3. Phone Number
        4. Email''')
        choice=int(input('Enter your choice: '))
        contact_found=Phonebook()

        if choice==1:
            parameter=input('Enter first name: ')
            for item in self:
                name=item[0].split()
                if name[0]==parameter:
                    contact_found.add_contact(item[0],item[1],item[2])
            return contact_found

        if choice==2:
            parameter=input('Enter last name: ')
            for item in self:
                name=item[0].split()
                if name[1]==parameter:
                    contact_found.add_contact(item[0],item[1],item[2])
            return contact_found

        if choice==3:
            parameter=input('Enter phone number: ')
            for item in self:
                if item[1]==parameter:
                    contact_found.add_contact(item[0],item[1],item[2])
            return contact_found

        if choice==4:
            parameter=input('Enter email: ')
            for item in self:
                if item[2]==parameter:
                    contact_found.add_contact(item[0],item[1],item[2])
            return contact_found

#Declaring a class ProtectedPhonebook which inherits from Phonebook

class ProtectedPhonebook(Phonebook):
    #For disabling pop method to prevent deletion from Phonebook records
    def pop(self):
        print('Pop functionality not supported')
        return 'Invalid Method'
    
    #For disabling remove method to prevent deletion from Phonebook records
    def remove(self,item):
        print('Remove functionality not supported')
        return 'Invalid Method'

#Driver Program 

p1=ProtectedPhonebook()
p1.add_contact('Faizan Sheikh','0313417','is@loser.com')
p1.add_contact('Umer Khalil','0214295','has@std.com')
p1.add_contact('Andrew Carnegie','0316839','andrew@book.com')
print(p1)
p1.pop()
