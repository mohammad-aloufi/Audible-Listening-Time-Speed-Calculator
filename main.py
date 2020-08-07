#We need sys to show us the way out of this mideval calculator
import sys
#We need timedelta, timedelta we need. We'll use it for converting the time in a bit
from datetime import timedelta

#The main function
def main():
    #the main loop
    while(True):
        #We ask the user for all kinds of data we need for calculating the end result
        hours=input('How many hours is the book')
        minutes=input('Enter the minutes')
        speed=input('Enter the reading speed')
        #if the string for hours and minutes aren't digits we tell the user that something is wrong with their input. Else we convert everything to ints, and the speed to float
        if hours.isdigit() ==False or minutes.isdigit() ==False:
            print('Error, unexpected input')
        else:
            hour=int(hours)
            minute=int(minutes)
            spd=float(speed)
            #We start the calculation by converting the hours into minutes then adding the minute variable to it. The result should be the time the user has entered in minutes.
            time=(hour*60)+minute
            #now we divide that by the speed
            time=time/spd
            #now we convert the minutes to hours and minutes. Result should be in hours and minutes like X:XX
            time=str(timedelta(minutes=time))[:-3]
            #printing the result of our calculation
            print('Your listening time is {} hours'.format(time))
            #Lets see if the user wants to do another calculation and act on that
            question=input('Would you like to do another calculation?')
            if question =='yes':
                break
            else:
                sys.exit()


#Welcome aboard
intro=input('Welcome to Audible Listening Time Calculater.\nType \"help\" for more info, or press enter to continue')
#if the user typed "help" show them the help message
if intro =='help':
    print("This app is designed to help with calculating your listening time to Audible books.\nIt's more helpful if you're not listening to the normal speed.\nI created this app because Audible doesn't update the listening time or the remaining time to the new speed when listening.\nThe app will ask you for some data, such as the hours, the minutes and the reading speed of the narrator.\nAfter then it will calculate the actual time according to the speed you set and show that to you on the screen")
main()

if __name__ =='__main__':
    main()