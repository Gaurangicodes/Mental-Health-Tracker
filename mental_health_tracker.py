import mysql.connector 
import pymysql 
import random 
from datetime import datetime 
 
#connecting to the mysql server and our created database mental_health_tracker 
mycon=mysql.connector.connect(host='localhost', 
                              user='root', 
                              password='1234', 
                              database='mental_health_tracker') 
cursor=mycon.cursor() 
cursor.execute('use mental_health_tracker') 
 
#Function to create a new user 
def create_user(name,email): 
    query = """ 
        INSERT INTO users (name, email) 
        VALUES (%s, %s) 
    """ 
    try: 
        # Executing the query 
        cursor.execute(query, (name, email)) 
        mycon.commit()  # Committing the transaction 
 
        print(f"User '{name}' with email '{email}' has been added successfully!") 
    except mysql.connector.Error as err: 
        print(f"User already exists or {err}") 
    finally: 
        # Closing the cursor and the connection after the operation 
        cursor.close() 
        mycon.close() 
 
#Function to write a letter to yourself  
def write_a_letter(user_id, to_self, letter_text): 
    # Get the current date and time when the letter is written 
    date_written = datetime.now() 
    query = """ 
        INSERT INTO letters (user_id, to_self, letter_text, date_written)  
        VALUES (%s, %s, %s, %s) 
    """ 
    try: 
        mycon=mysql.connector.connect(host='localhost', 
                              user='root', 
                              password='1234', 
                              database='mental_health_tracker') 
        cursor=mycon.cursor() 
        cursor.execute(query, (user_id, to_self, letter_text, date_written)) 
        mycon.commit() 
 
        print(f"Letter to your {to_self} self has been added successfully!") 
 
    except mysql.connector.Error as err: 
        print(f"Error inserting letter into database: {err}") 
 
    finally: 
        cursor.close() 
        mycon.close() 
 
#Function for gratitude journal feature 
def grat_journal(user_id, gratitude_entry): 
    # Get the current date and time when the gratitude entry is added 
    date_added = datetime.now() 
    query = """ 
            INSERT INTO gratitude_journal (user_id, gratitude_entry, date_added)  
            VALUES (%s, %s, %s) 
        """ 
    try: 
        mycon=mysql.connector.connect(host='localhost', 
                              user='root', 
                              password='1234', 
                              database='mental_health_tracker') 
        cursor=mycon.cursor() 
        cursor.execute(query, (user_id, gratitude_entry, date_added)) 
        mycon.commit() 
        print(f"Gratitude entry has been added successfully!") 
 
    except mysql.connector.Error as err: 
        print(f"Error inserting gratitude entry into database: {err}") 
 
    finally: 
        cursor.close() 
        mycon.close() 
 
#Function for mood tracking 
def mood_track(user_id, mood): 
    date_recorded = datetime.now() 
    query = """ 
            INSERT INTO mood_tracker (user_id, mood, date_recorded)  
            VALUES (%s, %s, %s) 
        """ 
    try: 
        mycon=mysql.connector.connect(host='localhost', 
                              user='root', 
                              password='1234', 
                              database='mental_health_tracker') 
        cursor=mycon.cursor() 
        cursor.execute(query, (user_id, mood, date_recorded)) 
        mycon.commit()   
        print(f"Mood entry has been recorded successfully!") 
 
    except mysql.connector.Error as err: 
        print(f"Error inserting mood data into database: {err}") 
 
    finally: 
        cursor.close() 
        mycon.close() 
 
#Function for creating a bucket list 
def bucket_list(user_id, item): 
    date_added = datetime.now() 
    query = """ 
            INSERT INTO bucket_list (user_id, item, date_added)  
            VALUES (%s, %s, %s) 
        """ 
    try: 
        mycon=mysql.connector.connect(host='localhost', 
                              user='root', 
                              password='1234', 
                              database='mental_health_tracker') 
        cursor=mycon.cursor() 
        cursor.execute(query, (user_id, item, date_added)) 
        mycon.commit() 
        print(f"Bucket list item has been added successfully!") 
 
    except mysql.connector.Error as err: 
        print(f"Error inserting bucket list item into database: {err}") 
 
    finally: 
        cursor.close() 
        mycon.close() 
         
#Function for creating a worry box 
def worrybox(user_id, worry_text): 
    date_added = datetime.now() 
    query = """ 
            INSERT INTO worry_box (user_id, worry_text, date_added)  
            VALUES (%s, %s, %s) 
        """ 
    try: 
        mycon=mysql.connector.connect(host='localhost', 
                              user='root', 
                              password='1234', 
                              database='mental_health_tracker') 
        cursor=mycon.cursor() 
        cursor.execute(query, (user_id, worry_text, date_added)) 
        mycon.commit() 
        print(f"Your worry has been added to the worry box successfully!") 
 
    except mysql.connector.Error as err: 
        print(f"Error inserting worry into the database: {err}") 
 
    finally: 
        cursor.close() 
        mycon.close() 
 
#Function to get an affirmation quote 
def affirmation(): 
    try: 
        query = "SELECT quote FROM affirmations" 
        mycon=mysql.connector.connect(host='localhost', 
                              user='root', 
                              password='1234', 
                              database='mental_health_tracker') 
        cursor=mycon.cursor() 
        cursor.execute(query) 
        quotes = cursor.fetchall() 
 
        if quotes: 
            # Randomly select one quote from the list of fetched quotes 
            random_quote = random.choice(quotes)[0]  # 'quotes' is a list of tuples, so we get the first item 
            print("Your daily affirmation is:") 
            print(random_quote) 
        else: 
            print("I believe in you.") 
 
    except mysql.connector.Error as err: 
        print(f"Error fetching affirmation from the database: {err}") 
 
    finally: 
        cursor.close() 
        mycon.close() 
     
 
# Main function to run the program and get user input 
def main(): 
    print("Welcome to the Mental Health & Mood Tracker!") 
    print("Please enter the following details to get started with us.") 
     
    # Get user input for the new user 
    name = input("Enter your name: ") 
    email = input("Enter your email: ") 
    # Call the create_user function to add the user to the database 
    create_user(name, email) 
 
    print('''Which self-care activity would you like to choose? 
             1. Write a letter to yourself 
             2. View my letters 
             3. Fill in the gratitude journal 
             4. View my gratitude journal 
             5. Track your mood 
             6. View my mood record 
             7. Bucket List 
             8. View my bucket list 
             9. Insert a worry into the worry box 
             10. Open worry box 
             11. Get daily affirmation quotes 
             12. Exit''') 
    choice=int(input("Enter your choice[1-7]:")) 
     
    while choice!=12: 
        if choice==1: 
            #get the user's id 
            mycon=mysql.connector.connect(host='localhost', 
                              user='root', 
                              password='1234', 
                              database='mental_health_tracker') 
            cursor=mycon.cursor() 
            user_id=cursor.execute('SELECT user_id from users') 
            # Get the recipient (past, present, or future) 
            to_self = input("Who are you writing this letter to? (past/present/future): ").lower() 
            # Ensure recipient is valid 
            if to_self not in ['past', 'present', 'future']: 
                print("Invalid recipient. Please choose from 'past', 'present', or 'future'.") 
                return 
            # Get the content of the letter 
            letter_text = input("Write your letter: ") 
            # Call the write_a_letter function to save the letter to the database 
            write_a_letter(user_id, to_self, letter_text) 
            print('''Which self-care activity would you like to choose? 
             1. Write a letter to yourself 
             2. View my letters 
             3. Fill in the gratitude journal 
             4. View my gratitude journal 
             5. Track your mood 
             6. View my mood record 
             7. Bucket List 
             8. View my bucket list 
             9. Insert a worry into the worry box 
             10. Open worry box 
             11. Get daily affirmation quotes 
             12. Exit''') 
            choice=int(input("Enter your choice[1-7]:")) 
 
        if choice==2: 
            mycon=mysql.connector.connect(host='localhost', 
                              user='root', 
                              password='1234', 
                              database='mental_health_tracker') 
            cursor=mycon.cursor() 
            cursor.execute('SELECT * FROM letters') 
            tup1= cursor.fetchall() 
            print(tup1) 
            print('''Which self-care activity would you like to choose? 
             1. Write a letter to yourself 
             2. View my letters 
             3. Fill in the gratitude journal 
             4. View my gratitude journal 
             5. Track your mood 
             6. View my mood record 
             7. Bucket List 
             8. View my bucket list 
             9. Insert a worry into the worry box 
             10. Open worry box 
             11. Get daily affirmation quotes 
             12. Exit''') 
            choice=int(input("Enter your choice[1-7]:")) 
 
        if choice==3: 
            #get the user's id 
            mycon=mysql.connector.connect(host='localhost', 
                              user='root', 
                              password='1234', 
                              database='mental_health_tracker') 
            cursor=mycon.cursor() 
            user_id=cursor.execute('SELECT user_id from users') 
            # Get the gratitude entry 
            gratitude_entry = input("Write your entry. (Hint: What you're grateful for today?): ") 
            # Call the grat_journal function to save the gratitude entry to the database 
            grat_journal(user_id, gratitude_entry) 
            print('''Which self-care activity would you like to choose? 
             1. Write a letter to yourself 
             2. View my letters 
             3. Fill in the gratitude journal 
             4. View my gratitude journal 
             5. Track your mood 
             6. View my mood record 
             7. Bucket List 
             8. View my bucket list 
             9. Insert a worry into the worry box 
             10. Open worry box 
             11. Get daily affirmation quotes 
             12. Exit''') 
            choice=int(input("Enter your choice[1-7]:")) 
 
        if choice==4: 
            mycon=mysql.connector.connect(host='localhost', 
                              user='root', 
                              password='1234', 
                              database='mental_health_tracker') 
            cursor=mycon.cursor() 
            cursor.execute('SELECT * FROM gratitude_journal') 
            tup2= cursor.fetchall() 
            print(tup2) 
            print('''Which self-care activity would you like to choose? 
             1. Write a letter to yourself 
             2. View my letters 
             3. Fill in the gratitude journal 
             4. View my gratitude journal 
             5. Track your mood 
             6. View my mood record 
             7. Bucket List 
             8. View my bucket list 
             9. Insert a worry into the worry box 
             10. Open worry box 
             11. Get daily affirmation quotes 
             12. Exit''') 
            choice=int(input("Enter your choice[1-7]:")) 
 
        if choice==5: 
            #get the user's id 
            mycon=mysql.connector.connect(host='localhost', 
                              user='root', 
                              password='1234', 
                              database='mental_health_tracker') 
            cursor=mycon.cursor() 
            user_id=cursor.execute('SELECT user_id from users') 
            # Get the mood from the user (e.g., Happy, Sad, Anxious) 
            mood = input("How are you feeling today? (e.g., Happy, Sad, Anxious): ").capitalize() 
            # Call the mood_track function to save the mood data to the database 
            mood_track(user_id, mood) 
            print('''Which self-care activity would you like to choose? 
             1. Write a letter to yourself 
             2. View my letters 
             3. Fill in the gratitude journal 
             4. View my gratitude journal 
             5. Track your mood 
             6. View my mood record 
             7. Bucket List 
             8. View my bucket list 
             9. Insert a worry into the worry box 
             10. Open worry box 
             11. Get daily affirmation quotes 
             12. Exit''') 
            choice=int(input("Enter your choice[1-7]:")) 
 
        if choice==6: 
            mycon=mysql.connector.connect(host='localhost', 
                              user='root', 
                              password='1234', 
                              database='mental_health_tracker') 
            cursor=mycon.cursor() 
            cursor.execute('SELECT * FROM mood_tracker') 
            tup3= cursor.fetchall() 
            print(tup3) 
            print('''Which self-care activity would you like to choose? 
             1. Write a letter to yourself 
             2. View my letters 
             3. Fill in the gratitude journal 
             4. View my gratitude journal 
             5. Track your mood 
             6. View my mood record 
             7. Bucket List 
             8. View my bucket list 
             9. Insert a worry into the worry box 
             10. Open worry box 
             11. Get daily affirmation quotes 
             12. Exit''') 
            choice=int(input("Enter your choice[1-7]:")) 
 
        if choice==7: 
            #get the user's id 
            mycon=mysql.connector.connect(host='localhost', 
                              user='root', 
                              password='1234', 
                              database='mental_health_tracker') 
            cursor=mycon.cursor() 
            user_id=cursor.execute('SELECT user_id from users') 
            # Get the bucket list item from the user 
            item = input("Enter an item you want to add to your bucket list: ") 
            # Call the bucket_list function to save the item to the database 
            bucket_list(user_id, item) 
            print('''Which self-care activity would you like to choose? 
             1. Write a letter to yourself 
             2. View my letters 
             3. Fill in the gratitude journal 
             4. View my gratitude journal 
             5. Track your mood 
             6. View my mood record 
             7. Bucket List 
             8. View my bucket list 
             9. Insert a worry into the worry box 
             10. Open worry box 
             11. Get daily affirmation quotes 
             12. Exit''') 
            choice=int(input("Enter your choice[1-7]:")) 
 
        if choice==8: 
            mycon=mysql.connector.connect(host='localhost', 
                              user='root', 
                              password='1234', 
                              database='mental_health_tracker') 
            cursor=mycon.cursor() 
            cursor.execute('SELECT * FROM bucket_list') 
            tup4= cursor.fetchall() 
            print(tup4) 
            print('''Which self-care activity would you like to choose? 
             1. Write a letter to yourself 
             2. View my letters 
             3. Fill in the gratitude journal 
             4. View my gratitude journal 
             5. Track your mood 
             6. View my mood record 
             7. Bucket List 
             8. View my bucket list 
             9. Insert a worry into the worry box 
             10. Open worry box 
             11. Get daily affirmation quotes 
             12. Exit''') 
            choice=int(input("Enter your choice[1-7]:")) 
 
        if choice==9: 
            #get the user's id 
            mycon=mysql.connector.connect(host='localhost', 
                              user='root', 
                              password='1234', 
                              database='mental_health_tracker') 
            cursor=mycon.cursor() 
            user_id=cursor.execute('SELECT user_id from users') 
            # Get the user's worry from input 
            worry_text = input("What's worrying you today?: ") 
            # Call the worrybox function to save the worry to the database 
            worrybox(user_id, worry_text) 
            print('''Which self-care activity would you like to choose? 
             1. Write a letter to yourself 
             2. View my letters 
             3. Fill in the gratitude journal 
             4. View my gratitude journal 
             5. Track your mood 
             6. View my mood record 
             7. Bucket List 
             8. View my bucket list 
             9. Insert a worry into the worry box 
             10. Open worry box 
             11. Get daily affirmation quotes 
             12. Exit''') 
            choice=int(input("Enter your choice[1-7]:")) 
 
        if choice==10: 
            mycon=mysql.connector.connect(host='localhost', 
                              user='root', 
                              password='1234', 
                              database='mental_health_tracker') 
            cursor=mycon.cursor() 
            cursor.execute('SELECT * FROM worry_box') 
            tup5= cursor.fetchall() 
            print(tup5) 
            print('''Which self-care activity would you like to choose? 
             1. Write a letter to yourself 
             2. View my letters 
             3. Fill in the gratitude journal 
             4. View my gratitude journal 
             5. Track your mood 
             6. View my mood record 
             7. Bucket List 
             8. View my bucket list 
             9. Insert a worry into the worry box 
             10. Open worry box 
             11. Get daily affirmation quotes 
             12. Exit''') 
            choice=int(input("Enter your choice[1-7]:")) 
 
        if choice==11: 
            affirmation() 
            print('''Which self-care activity would you like to choose? 
             1. Write a letter to yourself 
             2. View my letters 
             3. Fill in the gratitude journal 
             4. View my gratitude journal 
             5. Track your mood 
             6. View my mood record 
             7. Bucket List 
             8. View my bucket list 
             9. Insert a worry into the worry box 
             10. Open worry box 
             11. Get daily affirmation quotes 
             12. Exit''') 
            choice=int(input("Enter your choice[1-7]:")) 
     
    print("You chose to exit. Hope you have a nice day!") 
 
if __name__ == "__main__": 
    main() 