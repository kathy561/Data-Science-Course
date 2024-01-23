'''
[Case Study Story] --> Imagine the first day of university for a freshman named Alex. 
Alex is excited but also overwhelmed by the vast campus, numerous courses, and the sea of new faces. 
To aid new students like Alex, the university's IT department has developed a personalised chatbot. 
This chatbot, named "UniBuddy", is designed to make the transition smoother for freshmen.
Upon accessing the chatbot, Alex is prompted to enter their name, favourite colour, and age. 
Based on this input, UniBuddy offers a personalised greeting.
For instance, if Alex's favourite colour is blue,
    UniBuddy might suggest joining the university's "Blue Art Club".
If Alex is 18, the chatbot might provide information about freshman-specific events.
The chatbot also offers a feature where Alex can input specific queries, like "Where is the library?"
    or "How do I join the debate club?", 
        and UniBuddy responds with relevant information, all while adhering to a friendly tone,
        using string transformation methods to ensure the responses feel personalised and engaging.
'''

# Initialise message, for first time start
print('''
Welcome to UniBuddy! Your all-in-one app that makes your freshman journey a bit
easier to navigate!

Please enter your credentials to get started! :
''')

user_name = input("Please enter your student name : ").capitalize()
user_age = int(input("Please enter your age : "))
fav_colour = input("Please enter your favourite colour : ").capitalize()

print(f"""
Welcome {user_name}! I see that your favourite colour is {fav_colour}.
I have a few suggestions based on your choice!
""")

other_colours = ["Orange", "Yellow", "Green", "Purple", "White", "Black", "Grey", "Pink", "Brown"]

while True:
    if fav_colour == 'Red':

        print("If you like the colour RED, I have the following for you! Check out : ")

        print("""
    1. Our red colour themed football club.
    2. Our red themed art club.
    3. Our twilight themed club
    """)
        break
        
    elif fav_colour == 'Blue':

        print("If you like the colour BLUE, I have the following for you! Check out : ")

        print("""
    1. Our swimming club which include activites such as : aqua aerobics, rowing etc.
    3. Our blue themed art club.
    4. Our deep sea exploration club.
    5. Our bird watching society.
    """)
        break

    elif fav_colour == 'Yellow':

        print("If you like the colour YELLOW, I have the following for you! Check out : ")

        print("""
    1. Our happy society
    2. Our hiking club
    3. Our mountain climbing club
    4. Our dance club
    5. Our suntan society.
    """)
        break

    elif fav_colour in other_colours:
        print(f"Sorry, we dont have any recommends for {fav_colour}.")
        break
    
    elif fav_colour == "S":
        break

    else:
        print("I'm not sure if that was a colour you have entered, please try again or skip (s)")
        fav_colour = input("Please enter your favourite colour : ").capitalize()

#age input

if user_age <= 20:
    print("Here are some freshman specific events!")
    print("""
- Freshers fare 
- Campus tour
- Bar Crawl
- Mentorship program
- Academic Meet and Greet
         """)
else:
    print("I can see you are over the age of 20,")
    freshmen = input("Are you a freshman?  y/n: ")
    if freshmen == "y":
        print("Here are some freshman specific events!")
        print("""
- Freshers fare 
- Campus tour
- Bar Crawl
- Mentorship program
- Academic Meet and Greet
            """)
    else: 
        print("Here are some events you might like:")
        print("""
- Careers fare
- Food truck festival
- Smart Spending
- Academic Meet and Greet
- Welcome Back BBQ
            """)
    

# FAQ ; frequently asked questions
    

question = input("Is there anything you would like to ask me? (type in q to quit) : ").lower()


while True:
    if question == 'How is your day':
        print("I exist, so my day is going rather well!")
        break

    elif "where" in question:
        print("I can see you are looking for a location, please refer to the university map on the university website.")
        break

    elif "club" in question:
        print("I can see you are interested in joining a club, we have the following clubs and societies at the university:")
        print(""" 
- Debate Club
- Investment Society 
- Science Club
- Musical Theatre Club
- Drama Club 
- Rowing Club
              
To join any club, please visit the societies page on the university website!

            """
            )
        break

    elif question == "q":
        print("Quiting....")
        break

    else:
        print("Sorry I don't think I understood your question, please try again.")
        question = input("Is there anything you would like to ask me? (type in q to quit) : ")