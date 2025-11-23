import time
import random  
PARAGRAPHS = [
     "Infinite riches are all around you if you will open your mental eyes and behold the treasure house of infinity within you",
     "There is a gold mine within you from which you can extract everything you need to live life gloriously, joyously, and abun-dantly.",
     " Many are sound asleep because they do not know about this gold mine of infinite intelligence and boundless love within themselves.",
     "You can bring into your life more power, more wealth, more health, more happiness, and more joy by learning to con-tact and release the hidden power of your subconscious mind.",
     "An excellent way to get acquainted with the two functions of your mind is to look upon your own mind as a garden. You are a gardener,and you are planting seeds (thoughts) in your subconscious mind all day long, based on your habitual think-ing. As you sow in your subconscious mind, so shall you reap in your body and environment."
]

totalwords = 0  
border = '-+-' * 10
def createbox():
    """Prints the decorative border and instructions."""
    print(border)
    print()
    print('Enter the phrase as fast as possible and with accuracy')
    print()
while 1:  
    string = random.choice(PARAGRAPHS)
    totalwords = len(string.split())  
    t0 = time.time()
    createbox()
    print('Type the following:\n')
    print(string, '\n')
    inputText = str(input())
    t1 = time.time()
    lengthOfInput = len(inputText.split())
    accuracy = len(set(inputText.split()) & set(string.split()))
    accuracy = (accuracy / totalwords)
    timeTaken = (t1 - t0)  
    if timeTaken > 0:
        wordsperminute = (lengthOfInput / timeTaken) * 60 
    else:
        wordsperminute = 0

    print('\n' + border)
    print('Total words \t :' ,lengthOfInput)
    print('Time used \t :',round(timeTaken, 2),'seconds')
    print('Your accuracy \t :',round(accuracy, 3)*100,'%')
    print('Speed is \t :' , round(wordsperminute, 2),'words per minute')
    print(border)
    
    print("\nDo you want to retry? (Type 'yes' to continue, 'no' to exit): ", end='')
    retry_input = input().lower()  
    
    if retry_input == 'yes':
        print('Continuing with a new paragraph...')
        time.sleep(1)
        continue
    else:
        print('Thank you, bye bye.')
        time.sleep(1.5)
        break