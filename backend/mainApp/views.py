from django.shortcuts import render

# Create your views here.

def getWord(request): #Generate and send a randow valid word, also append that word to the logs of the user for checking the number of attempts and generating corresponding points.
    pass

def checkWord(request): #To check if the word entered by the user is valid or not
    pass

def matchWord(request): #If the word is valid then check if the word matches with the word in logs
    pass

def winGame(request): #If the word is correct the add the corresponding points to user's data
    pass

def endGame(request): #If user clicks on the exit game button, then erase all the logs
    pass