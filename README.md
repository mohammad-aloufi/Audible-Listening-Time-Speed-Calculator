# What's this
Audible Listening Time Calculator is an app that helps you calculate your listening time to the books that are in the Audible app.
# What is Audible?
[Audible][www.audible.com] is an audio books company owned by Amazon. In Audible, you can find all sorts of books in an audio format.
From what I know, they offer a lot of stuff, not just books. However, my experience with them personally is just with listening to books.
The books they have are actually are in high quality, although a bit expensive. Sometimes, they do book sales and you can buy books at a discounted price, or even you can buy the audio book at a discounted price if you buy the kindle version of the same book first.
# Why did I create this?
The audible app allows you to speed up the reading speed of the narrator, so you can set it at say 1.5 times the normal reading speed.
Usually people speed up the thing because they find the normal speed too slow for their liking.
However, the problem in the audible app is that when you speed it up, it won't update the listening remaining time according to the new set speed.
Example:
If you're listening to a book, and say you have 5 hours and 30 minutes remaining left to finish the book, and at that point you decided to set the speed to 1.5.
The remaining time won't update itself to the actual remaining time according to the new speed, in this case it should be 2 hours and 40 minutes.
However, when you speed up the listening time, say to 1.5, the way it works in audible is that it passes 1.5 seconds for every 1 actual second in the timer you see on your screen, that's why it doesn't think that it doesn't need to update the time remaining to the new speed.
I hope that makes sense.
# How to use
When you open the app, you will be presented by a welcome message, either type "help" or press enter to continue.
After then, it'll ask you for the hours, then the minutes, then the speed.
It will calculate everything and show the result for you on the screen.
It will ask you if you want to do another calculation, answer with yes or no.
# Known issues
The app will print a traceback if you enter anything that's not a float for speed.
If you look at the code, after I took the user's input, I checked if the hours and minutes aren't digits, if they aren't then the app will tell the user about it.
If they are, then we convert the hours and minutes to integers and the speed to float.
I did the checking because converting the strings without checking them first will print a traceback that says "ValueError: invalid literal for int() with base 10: '". So much for trusting user input.
It prints this error if I try to convert a string that has letters in it to an integer. So I found a way around it by checking if the strings aren't digits and give the user a message then return them back to the start where they can input everything all over again.
The problem here is with speed, I can't do the same with it, since "1.5" will not count as a digit only string, and the string object doesn't have a method for checking if the string is a float just like the method I used for checking for digits.
So for now, unexpected speed input will traceback "ValueError: could not convert string to float: '".
That's in case of the user has typed something that's not a float in the speed field.