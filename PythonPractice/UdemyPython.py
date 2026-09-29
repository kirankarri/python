import random
import string
import data
Alphabets = list(string.ascii_lowercase)
numbers = list(string.digits)
characters = list(string.punctuation)

def day_3():
    print('Welcome to the PyPassworn Generator')
    nr_letters = int(input('How many letters woudl you like in your password?'))
    nr_symbols = int(input('how many symbolw would you like?'))
    nr_numbers = int(input('How many numbers would you like'))
    password = []
    for i in range(0,nr_letters):
        password.append(random.choice(Alphabets))
    for i in range(0,nr_symbols):
        password.append(random.choice(characters))
    for i in range(0, nr_numbers):
        password.append(random.choice(numbers))

    print(password)
    random.shuffle(password)
    print(str(password))
def day_7():
    print('Hello')
    word_list = ['kiran','keerthi','hanuman','a','aa']
    word_shortlisted = word_list[random.randint(0,len(word_list)-1)]
    word_tobefilled = '_'*len(word_shortlisted)
    print(word_shortlisted)
    balance_charac = len(word_shortlisted) 
    lives = 6
    while balance_charac > 0 and lives > 0:
        word_guessed = input('Guess a word')
        tracker = False
        for i in range(len(word_shortlisted)):
            if word_guessed in word_shortlisted[i]:
                balance_charac -= 1
                word_tobefilled = word_tobefilled[:i]+word_guessed+word_tobefilled[i+1:len(word_tobefilled)]
                tracker = True
        if tracker == False:
            lives -= 1
        print(word_tobefilled)
    if lives == 0:
        print('You Loose')
    else:
        print('You Win!')
def day_8():
    greet()
    greet_var('kiran','USA')
    greet_var(location='USA',namee='keerthi')
    love_score('Kiran','Keerthi')
    #ceaser_ciper('encode',3,'kiranyz')
    #ceaser_ciper('decode',3,'nludqbc')
    again = True
    while(again):
      encryptiontype_name = input('Type encode to encrypt or decode for decrypt\n')
      message = input('Type your message\n')
      shiftnumber = int(input('Type in shift number'))
      ceaser_ciper(encryptiontype_name,shiftnumber,message)
      again = input('Type yes if you want to do again. Otherwise type no\n')
      if again == 'yes':
          again = True
      elif again == 'no':
          again = False
          print('Bye!')
def greet():
    print('Hello')
    print('Hello')
def greet_var(namee, location):
    print(f'Hello {namee}')
    print(f'What it is like in {location}')
def love_score(fname,sname):
    combo_string = fname+sname
    Word1 = 'true'
    Word2 = 'love'
    Word1Counter = 0
    Word2Counter = 0
    for i in range(len(Word1)):
        for j in range(len(combo_string)):
            if Word1[i] == combo_string[j]:
                Word1Counter += 1
    for i in range(len(Word2)):
            for j in range(len(combo_string)):
                if Word2[i] == combo_string[j]:
                    Word2Counter += 1            
    print(str(Word1Counter)+str(Word2Counter))
def ceaser_ciper(encryptiontype_name, shiftnumber,message):
    temp_message = ''
    if encryptiontype_name == 'encode':
        for i in range(len(message)):
            new_char = Alphabets[(Alphabets.index(message[i])+shiftnumber)%26]
            temp_message += new_char
    if encryptiontype_name == 'decode':
            for i in range(len(message)):
                new_char = Alphabets[Alphabets.index(message[i])-shiftnumber]
                temp_message += new_char
    print(temp_message)
def day_9():
    more_bidder = True
    bidder_dic = {}
    while(more_bidder):
        name = input('What is your name?\n')
        price = int(input('What is your bid in $?\n'))
        bidder_dic[name] = price
        more_bidder = input('Do you have more bidders yes or no\n')
        if more_bidder == 'yes':
            more_bidder = True
        elif more_bidder == 'no':
            more_bidder = False 
        print('\n'*100)
    max_bidder = ''
    max_amount = 0
    for key in bidder_dic:
        if max_amount <= bidder_dic[key]:
            max_amount = bidder_dic[key]
            max_bidder = key
    print(f'Max bidder is {max_bidder} at price {max_amount}')
    print(max(bidder_dic,key=bidder_dic.get))
def day_10():
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def div(a,b):
        return a/b
    def mul(a,b):
        return a*b
    func_mapping = {
        '+':add,
        '-':sub,
        '*':mul,
        '/':div
        }
    use_old_number = False
    while(True):
        if not(use_old_number):
            first_num = float(input('what is the first number?\n'))
        ope = input('Pick an operation\n')
        sec_num = float(input('what is the next number?\n'))
        print(func_mapping[ope])
        final_output = func_mapping[ope](first_num,sec_num)
        print(f'{first_num} {ope} {sec_num} = {final_output}')
        con_math = input(f'Type y to continue calculating with {first_num} or type n to start new calculation')
        if con_math == 'y':
            use_old_number = True
            first_num = final_output
        elif con_math == 'n':
            use_old_number = False
def best_score(cards):
    running_total = 0
    for i in range(len(cards)):
        if cards[i] == 11:
            temp = running_total + cards[i]
            if temp > 21:
                running_total += 1
            else:
                running_total += cards[i]
        else:
            running_total += cards[i]
    return running_total

def winner(userscore,computerscore):
    if userscore > 21:
        return 0
    if computerscore == userscore:
        return 0
    if (userscore < 21 and computerscore > 21) or userscore > computerscore:
        return 1
    if userscore < computerscore:
        return 0

def day_10():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    print('Welcome to BlackJack!')
    user_cards = random.choices(cards,k=2)
    computer_cards = random.choices(cards,k=2)
    print(f'Your cards:{user_cards}')
    print(f'Computer first card: {computer_cards[0]}')
    con = input('Type y to get another card type n to pass\n')
    while True:
        if con == 'y':
            user_cards.append(random.choice(cards))
            user_best_score = best_score(user_cards)
            print(f'Users New cards {user_cards}')
            if user_best_score > 21:
                print('You loose')
                break
            else:
                con = input('Type y to get another card type n to pass\n')

        elif con == 'n':
            print(f'Your final hand:{user_cards}')
            user_best_score = best_score(sorted(user_cards))
            computer_best_score = best_score(sorted(computer_cards))
            if user_best_score > 21:
                print('You loose')
                break
            if computer_best_score < 17:
                computer_cards.append(random.choice(cards))
                computer_best_score = best_score(sorted(computer_cards))
            print(f'Computer final hand {computer_cards}')

            final_winner = winner(user_best_score,computer_best_score)
            if final_winner == 1:
                print('You Win!')
                break
            else:
                print('You loose')
                break
def day_11_number_guessing_game():
    ###Number Guessing game###
    print('Welcome to the Number Guessing game')
    print('I am thinking of a number between 1 and 100')
    final_number = random.choice(range(1,100))
    diff_level = input('Choose a difficulty. Type easy or hard: ')
    if diff_level == 'easy':
        num_of_tries = 10
    elif diff_level == 'hard':
        num_of_tries = 5
    while num_of_tries >0:
        print(f'You have {num_of_tries} attempts remaining to guess the number')
        guessed_number = int(input('Make a guess:'))
        if guessed_number > final_number:
            print('Too high')
            num_of_tries -= 1
            if num_of_tries > 0:
                print('Guess again')
            else:
                print(f'You ran out of guesses. You loose. Actual Number is {final_number}')
        elif guessed_number < final_number:
            print('Too Low')
            num_of_tries -= 1
            if num_of_tries > 0:
                print('Guess again')
            else:
                print(f'You ran out of guesses. You loose. Actual Number is {final_number}')
        elif guessed_number == final_number:
            print(f'You Won!!! The answer is {final_number}')
            break
def day_12_Higger_Lower():
    temp_list = random.choices(data.data,k=2)
    correct_answer = True
    Score = 0
    while correct_answer:
        if Score > 0 :
            print('\n'*100)
            print(f'Your are correct! Current Score {Score}')
        print(f'Compare A: {temp_list[0]['name']}, a {temp_list[0]['description']}, from {temp_list[0]['country']}')
        print('VS')
        print(f'Compare B: {temp_list[1]['name']}, a {temp_list[1]['description']}, from {temp_list[1]['country']}')
        option_selected = input('Who had more followers? Type A or B:')
        if option_selected == 'A' and temp_list[0]['follower_count'] >= temp_list[1]['follower_count']:
            correct_answer = True
            del temp_list[1]
            temp_list.append(random.choice(data.data))
            Score += 1
        elif option_selected == 'B' and temp_list[0]['follower_count'] <= temp_list[1]['follower_count']:
            correct_answer = True
            del temp_list[0]
            temp_list.append(random.choice(data.data))
            Score += 1
        else:
            correct_answer = False
            print('\n'*100)
            print(f'Wrong answer and You score is {Score}')
            print(f'{temp_list[0]['name']} has {temp_list[0]['follower_count']} compared to {temp_list[1]['name']} which has {temp_list[1]['follower_count']} ')




day_12_Higger_Lower()


