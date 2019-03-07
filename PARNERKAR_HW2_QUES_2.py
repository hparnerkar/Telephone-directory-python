#HARSHPARNERKAR
import sys
import os
import fileinput

def main():
    condition='y'
    while(condition=='y' or condition=='Y'):    
        os.system('cls')
        print("CONTACT LIST---------------------")
        print("1) ADD CONTACT")
        print("2) SHOW CONTACTS")
        print("3) MODIFY CONTACTS")
        print("4) DELETE CONTACT")
        print("5) SEARCH CONTACT")
        print("6) QUIT")
        choice=int(input("\nEnter your Choice: "))
        if(choice==1):
            add()
        elif(choice==2):
            show()
        elif(choice==3):
            modify()
        elif(choice==4):
            delete()
        elif(choice==5):
            search()
        elif(choice==6):
            end()
        condition=input("\nDo you want to continue Y or N: ")

def end():
    sys.exit()




def add():
    file=open('contact.txt','a')
    condition='y'
    while(condition=='y' or condition=='Y'):
        name=input("Enter your name")
        num=input("Enter you number")
        email=input("Enter your email")
        file.write( name + '\n')
        file.write( num + '\n')
        file.write( email + '\n')
        file.write("------------------------------------" + '\n')
        condition=input("Do you want to enter another contact")
    file.close()

def modify():
    file2=open('contact.txt','r')
    temp=open('tempfile.txt','w')
    name=input("Enter the name to update detail: ")
    contactnew=input("Enter new contact number: ")
    emailnew=input("Enter new email id: ")
    descr=file2.readline()
    found=False
    while(descr != ''):
        contact=file2.readline()
        email=file2.readline()
        dash=file2.readline()
        if(name in descr):
            temp.write(descr)
            temp.write(contactnew+'\n')
            temp.write(emailnew+'\n')
            temp.write(dash)
            found=True
        else:
            temp.write(descr)
            temp.write(contact)
            temp.write(email)
            temp.write(dash)
        descr=file2.readline()
            
    temp.close()
    file2.close()
    if found:
        print("found and changed")
    else:
        print("not found")
    os.remove('contact.txt')
    os.rename('tempfile.txt','contact.txt')
    

def show():
    file3=open('contact.txt','r')
    for line in file3:
        print (line)
            
def search():
    file4=open('contact.txt','r')
    flag=1
    name=input("Enter the name you want to search:")
    for line in file4:
        if(name in line):
            contact=file4.readline()
            emailid=file4.readline()
            print ('NAME : ' + name + '\n')
            print ('CONTACT NO : ' + contact + '\n')
            print ('EMAIL : ' + emailid + '\n')
            flag=0
    if(flag==1):
        print("Name not found.")

def delete():
    file2=open('contact.txt','r')
    temp=open('tempfile.txt','w')
    name=input("Enter the name to delete its details: ")
    descr=file2.readline()
    found=False
    while(descr != ''):
        contact=file2.readline()
        email=file2.readline()
        dash=file2.readline()
        if(name in descr):
            found=True
        else:
            temp.write(descr)
            temp.write(contact)
            temp.write(email)
            temp.write(dash)
        descr=file2.readline()
            
    temp.close()
    file2.close()
    if found:
        print("\nFound and Deleted")
    else:
        print("Contact Not Found")
    os.remove('contact.txt')
    os.rename('tempfile.txt','contact.txt')

    

main()
    
                

    
