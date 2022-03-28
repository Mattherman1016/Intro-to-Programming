##Final Project Proposal

Many prospective music students don’t know where to apply for college or what school would be right for them. I am solving this problem with a program that tells the student where they would thrive the most, based on their most listened to genres in Spotify.

For my final project, I would like to make a program that tells perspective music students what music school would be best for them based on their liked songs on Spotify. For this, I have to connect the Spotify API to the Python program. This will be based on genres of music and the frequency of the genre. If their Spotify account shows that they listen the most to jazz, my python program will give them a few results for possible schools that are more jazz based. This will take non programming research on the strengths and weaknesses of different schools. I could take this a step further and make it about genre AND specific artists but that seems like there would be too much data to enter into my program.

#Choosing schools
I will choose 20-30 of the most renowned music schools in the USA. I will categorize them based on their primary focus regarding genre. Examples include but are not limited to…

#Contemporary/pop	Jazz	Classical	  Bluegrass/country
Berklee	          NEC	  Julliard	  Berklee
USC            N.Texas	Curtis 	    Kentucky School of BG
Frost	            NYU	   MSM	      Musicians Institute

The student would get 10 options based on the frequency of genre. So, say if I was taking the test and the program saw that I had 50% Classical, 30% jazz and 20% Pop, out of the 10 schools that it will present, I will have 5 classical schools, 3 jazz schools and 2 contemporary schools. Of course, the numbers will not work out as cleanly as this so we will have to make an estimate using elif statements that would say, if the percentage is is between j and k, allow for this conversion to %. This is certainly something that I will need further guidance on.

Each school will come with a description, also depicting the school’s strengths and weaknesses. For this research, I must go to both the school’s website and to reviews of students to find the strengths and weaknesses. One of my first steps should be gathering this information, putting it into python as variables to be printed under the correct conditions.

#Connecting with the Spotify API
https://medium.com/@maxtingle/getting-started-with-spotifys-api-spotipy-197c3dc6353b

https://github.com/TheComeUpCode/SpotifyGeneratePlaylist

https://betterprogramming.pub/how-to-extract-any-artists-data-using-spotify-s-api-python-and-spotipy-4c079401bc37

https://vsupalov.com/analyze-spotify-music-library-with-jupyter-pandas/

https://towardsdatascience.com/extracting-song-data-from-the-spotify-api-using-python-b1e79388d50

https://towardsdatascience.com/get-your-spotify-streaming-history-with-python-d5a208bbcbd3


The steps to do this are located in the link above.

I have to install SPOTIPY – all of the steps needed to do this are in the link as well. It seems that what I will have to do is locate the data points that I need to take my information from. What I will be looking for is top genres played yearly (or maybe quarterly) by the user. Spotify should present at least 5 of them.

#Pandas
-	Python data analysis – open source tool built on python to analyze data. I need to learn more about this but I think this is the key component to gather and analyze Spotify user data.

#What should be easy
-	Setting up Spotify developer account
-	Doing the school research and writing descriptions/creating categories

#What should be moderately difficult
-	Creating subcategories for the categories – “if this person has 10% jazz, recommend school X, if this person has 50% recommend School y, if this person has 100% jazz, recommend school Z”
-	Creating all of the Elif statements in python

#What should be difficult
-	Seamlessly linking the program to a specific Spotify user
-	Connecting to the correct variables in Spotify to get the info I need

#Timeline

Steps
1.	Create developer account
2.	Locate the variables needed from the API
3.	Link those variables to a mock python program
4.	Make a simple version of this for proof of concept
5.	Create the answers to print (The school names and the descriptions)
6.	Link those to Elif statements with percentages that can read Spotify user’s statistics
7.	Make sure the program works!

Due – May 2

March 28-April 3
-	Steps 1,2 and 3

April 4-April 10
-	Step 4

April 11-April 18
-	Step 5

April 18-April 25
-	Step 6 and 7

April 25-May 2
-	Step 7


#Assessment 

Although I would love to be graded on how hard I tried, I know that this program has to work. I should rightfully be assessed based on the program working, even if the program is a simplified version of what is stated above. This class has been particularly hard for my brain to comprehend so it is very likely that the final project that I submit will be a simplified version of what is described above.
