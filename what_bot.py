import pywhatkit as kit
import pyfiglet
import selenium


banner = pyfiglet.figlet_format('X3-0n')
print(banner)

print('\033[1;32mHello How can I help you today?\033[m')

while True:

    option = input('''\033[1;32m 
1 = Schedule a message
2 = Play videos on youtube
3 = Search something on Google
4 = Info about something
5 = Exit\033[m

write here >>  ''')



    # sending messages to someone
    if option == '1':
        message = input("Type here your message: ")
        number = input('Type or paste here the number: ')
        time_hour = int(input('Hour: '))
        time_min = int(input('Minute: '))
        kit.sendwhatmsg(f'+55{number}', message, time_hour, time_min)




    # play any video on youtube
    elif option == '2':
        video_topic = input("Type the video topic here: ")
        try:
            kit.playonyt(video_topic)
        except:
            print('Sorry, I cannot find your video :(')
        



    # searching topics on the internet(google)
    elif option == '3':
        search = input("Type here: ")
        kit.search(search)



    # showing info about any topic
    elif option == '4':
        topic = input("What topic do you want to know?: ")
        try:
            kit.info(topic, 3)
        except:
            print(f'\033[1;31mSorry cannot find any information about {topic}\033[m')
    

    elif option == '5':
        print('Good bye!')
        exit()
    cont = input('''
Press C: To continue
Press E: To Exit
    
write here >>>  ''').upper()


    if cont == "E":
        print("Good bye ;)")
        break
