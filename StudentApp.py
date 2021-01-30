import csv

def write_into_csv(info_list):
     with open('stInf.csv', 'a',  newline='') as csv_file:
         writer = csv.writer(csv_file)
         if csv_file.tell() == 0 :
             writer.writerow(["Name", "Age", "Contact Number", "E-Mail ID"])
         writer.writerow(info_list)


if __name__ == '__main__' :
    condition = True
    stNum = 1

    while(condition):
        stInf = input("Enter information of student number {}  in formate as follow (Name Age Contact_Number E-Mail ID): ".format(stNum) )
        # print("Entered information: " + stInf)

        # split
        stInf_list = stInf.split(' ')
        print('\nThe entered information is :\nName : {}\nAge : {}\nContact Number : {}\nEmail id : {} '.format(stInf_list[0], stInf_list[1], stInf_list[2], stInf_list[3]) )
        stCheck1 = True
        while stCheck1 :   #if user mistakenly something else than yes or no
            check = input('Is entered information is correct? (yes/no) : ')
            if check == 'yes' :
                stCheck1 = False
                write_into_csv(stInf_list)
                stCheck2 = True
                while stCheck2 :   #if user mistakenly something else than yes or no
                    condition_check = input("Do you want to enter another student's information (yes/no) : ")
                    if condition_check == "yes":
                        stCheck2 = False
                        stNum += 1
                    elif condition_check == "no":
                        stCheck2 = False
                        condition = False
                    else :
                        print('\nPlease write either \'yes\' or \'no\' (You wrote {}) '.format(condition_check))
            elif check == 'no' :
                stCheck1 = False
                print('\nPlease re-enter the information.')
            else :
                print('\nPlease write either \'yes\' or \'no\' (You wrote {})'.format(check))
