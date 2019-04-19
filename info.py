##def myInfo():
##    info = ["name" , "age" , "job" , "Email" , "phone number"]
##    x = 0
##
##    while x < len(info):
##        ask = input("What is your {} : ".format(info[x]))
##        x += 1
##


def myInfo():
    
    info = ["name" , "age" , "job" , "Email" , "phone number"]
    print("Welcome to this Programme, i am a Robot and i'll discuss with you about some personal information"
          "\nAre you ready ?\n")
    
    answer = input("You can answer by 'YES' / 'NO' : ")
    accept = True
    while accept:
        
        if answer == "NO":
            print("Sorry, it seems you are not ok today, try again later, good by")
            break
        
        elif answer != "YES" and answer != "NO":
            answer = input("Please enter a correct answer, you can choose 'YES' / 'NO' : ")
            
        else:
            name = input("\nWhat is your {} please : ".format(info[0]))
            age = input("Hello Mr. {} and What is your {} : ".format(name,info[1]))

            numbers = ['0','1','2','3','4','5','6','7','8','9']
            letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

            play = False
            age.split()
            while play != True:
                
                for item in age:
                    if item not in numbers or item in letters:
                        age = input("Please enter a valid number : ")
                        
                    else:
                        play = True
                         
            job = input("Ok That's good Mr {} and what is you {} please : ".format(name,info[2]))

            email = input("You are a {} that seems very good, What is your {} please : ".format(job,info[3]))

            count = True
            while count:
                mail_list = ["@gmail.com","@yahoo.com","@outlook.com","@yahoo.fr"]
                
                #myEmail = mail_list[x]
                if email.find('@') != -1 and email[email.index('@'):] in mail_list:
                    count = False
                    phone = input("Finally could you give me your {} please : ".format(info[4]))
                    break
                
                else:
                    email = input("Sorry there is an error, please enter a valid email adress : ")

            younger = "<< It seems that your age is less than 40, you are younger than me >>"
            report = ("* Ok thank you Mr. {} for these information. \nI am really happy to meet you"
                  " let me give you the report about your personal information\n\n"
                  "* Your name is >>>>> '{}'\n* You age is >>>>> {} years old\n{}\n* You job is >>>>> {}\n* Your Email adress"
                  " is >>>>> '{}'\n* Your phone number is >>>>> {}.\n\n>>>> If you need more help please contact me"
                  "".format(name,name,age,younger,job,email,phone))

            if int(age) < 40:
                print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>> The Report >>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
                print(report)

            elif int(age) == 40:
                same_age = "<< It seems that you have the same age as me: {} years old >>".format(age)
                report = report.replace(younger,same_age)
                print(report)
                
            else:
                older = "<< It seems that your age is greater than 40, you are older than me >>"
                report = report.replace(younger,older)
                print(report)
            accept = False

myInfo()


















