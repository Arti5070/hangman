import random
 
def hangman():
    list_of_word=['peace','sin','cold','demon','breath','butterfly','trust','bang','high','ride']  
    word= random.choice(list_of_word) 
    # print(word)
    '''secret word'''
    
    chances=10
    guess_made=''
    '''casually for candition'''
    
    valid_word=set('abcdefghijklmnopqrstuvwxyz')
    # print(valid_word)
    
    while len(word)>0:
        main_word= " "
        
        for letter in word:
            if letter in guess_made:
                main_word +=letter
            else:
                main_word += '_'
                
        if  main_word == word:
            print(main_word)
            print("you won !")
            break
        
        print("guess the word",  main_word)
        guess=input("enter the guess letter")
        
        if guess in valid_word:
            guess_made +=guess
            
        else:
            print("invalid character")
        if  guess not in word:
            chances  -= 1
            
            if chances ==9:
                print("9  chances left")
                print("-----------")
                
            if  chances  == 8:
                print("8 chances left")
                print("-----------")
                print('    0      ')
                 
            if  chances  ==7:
                print("-----------")
                print('     0      ')
                print("      |     ")
                
            if  chances == 6:
                print("6 chances left")
                print("----------")
                print('    0     ')
                print('     0    ')
                print("     |    ")
                print('    /     ')
                
            if  chances  ==5:
                print("5 chances left")
                print("----------")
                print('     0 "   ')
                print("     |    ")
                print('    / \   ')
                
            if  chances  ==4:
                print("4  chances left")
                print("-----------")
                print('     \0   ')
                print("      |   ")
                print('     / \  ')
                
            if  chances  ==3:
                print("3  chances  left")
                print("----------")
                print('     \0/  ')
                print("      |  ")
                print('     / \ ')
                
                
            if  chances == 2:
                print("2  chances left")
                print("---------")
                print('       \0/   |  ')
                print("        |     ")
                print('       / \    ')
                
            if  chances  == 1:
                print("1  chance left !! hangman on his last breath")
                print("--------")
                print('      \0/_|  ')
                print("       |     ")
                print('      / \    ')
                
            if  chances  ==0:
                print("you  loose")
                print("you  let  a good man die")
                print("--------")
                print('   0_|   ')
                print("  /|\    ")
                print('  / \     ')
                break
            
            
            
name =input("ENTER PLAYER NAME  -->  ")
print('********')
print("welcome",name, '!')
print("you have 10 chances to the  words")

hangman()

def again():
   while True:
       play_again = input("do you to play enter again enter y if yes or anything if no")
       if play_again =="y":
           hangman()
again()