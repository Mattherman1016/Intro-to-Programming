##Final Project Markdown File
#Matthew Herman

This final project is for my personal website. It is written in HTML and was originally derived from a w3School template. The template has embedded CSS which I can not edit. I knew that going into the project, however, I liked the formatting of the template a lot. With that being said, there were aspects of the projected that I wish I could have changed. I tried getting in touch with W3School support but my efforts were futile.

Templates:
https://www.w3schools.com/w3css/w3css_templates.asp
 

The Website is 2 pages - The home page is extended with the sections:
- Home (bio)
- Teaching (Pedagogy)
- My Music/Bands (ensembles, small combos and Funk Machine)
- Contact

The second page can be found in links both in the teaching section and "more"-> "Pedagogical Articles"
This page houses my articles that I have written in the realm of music education. There are 9 papers housed on this site. Each paper has a title and short description.

There were two websites that I pulled code from;
Cory Wongs personal website
- Pulled the bootstrap code
https://www.corywongmusic.com/

My current personal website
- Pulled the code for the embedded videos, FM picture link and audio players.
- I also pulled some of the text from this site
https://www.matthermanmusic.com/


##Home Page

#Nav Bar
- Inserted nav from template
- Changed the names of the tabs
- Got rid of the search bar
- HARD PART - Tried to figure out how to get the nav to line up with the sections that i created. The href is connected not to the sections but to specific places on the screen by % of screen. This is embedded in the CSS

 <a href="#band" class="w3-bar-item w3-button w3-padding-large w3-hide-small">TEACHING</a>
    <a href="#tour" class="w3-bar-item w3-button w3-padding-large w3-hide-small">MY MUSIC/BANDS</a>
    <a href="#contact" class="w3-bar-item w3-button w3-padding-large w3-hide-small">CONTACT</a>
    <div class="w3-dropdown-hover w3-hide-small">
    
- The href = the areas on the site. the areas are called #band, #tour and #contact
- I tried inputting the different names of the new sections into these instead but it didn't work
- I tried putting html links instead but again didn't work
- I contemplated just getting rid of the scrolling site and doing them all on separate pages but i think this layout looks professional.
- At this point, i went into the CSS but i sadly couldn't change anything in it. This is the downside of having to use a template. Luckily, this is the only thing on the website that doesn't work. 
- Went on to the more section
- Got rid of what was there and put a link to 1. Funk Machine site and 2. i made a new page meant to house my papers that i have written.

##Page Content 
#Home page
- I had to edit the template a lot in this section.
- I deleted the band members thing that was originally there
- Simplified the page by just having paragraphs and an h2
- I put in paragraphs, added paragraph breaks and adjusted the margins on the top
- I then added a picture of myself.
- I adjusted the size of the picture.
- Aligned the text to the left to go with the theme that i created in the nav bar
- Kept the white and black layout for professionalism 

#Pedagogy
- I copied and pasted everything from the previos section
- changed the background color to black
- Adjusted the margins to 800PX  - - Kept everything else from the layout
- The next step was a challenge - i had to create the testimonials section
- For this, i knew i had to change the class to "w3-third" to separate each testimonial into 3 equal columns
- from there, I had to adjust the padding on the sides to keep in in line with the rest of the paragraphs
- This was all using Div tags

##My Music/Bands
- For this section, I needed to copy and paste code from my previous website. 
- I transfered over the list for small combos
- Also transfered the embedded video links 
- I had to add the audio player for the two songs
- I used the previous "w3-third" thing to separate the linked album art (also copied from previous site), and the two audio players
- I changed the fortmat of the audio as i wanted new songs
- Using ADAPTOR, i created 1 MP3 and 1 OGG for each song.
- Once all of that information was in there, i created the opening paragraph
- This paragraph included ample links to different performance videos that i have in various places (Vimeo, youtube, instagram)

#Contact 
- The only thing that i really changed about the contact page was the information. I left most of that the same, as it was exactly what i wanted.

#Footer
- The footer just consists of social media links that i created. 
- The icons were a part of the template and embedded CSS
- No matter how hard i tried, i couldn't get them to link (eventually i did)
- I first put the link around the icon - didn't work
- I then tried to create separate links with embedded icons that i created - this didn't work either
- Finally i looked up the solution via W3school
https://www.w3schools.com/icons/tryit.asp?filename=tryicons_fa-linkedin-square
- IT WORKED!

#Bootstrap
- I took the bootstrap info from a few different places
- First, i went on WeSchool to learn more about the functionality of it
- Then i went to my own personal site to see how it was used - I didn't see too much of it - It seemed to be linked to another program that was housing the bootstrap
- Finally i went to Cory wongs site - it was created by square space
- I saw they had inline bootstrap in the header and the footer
- I copied what was there into my own program.
- I havent been able to check it ob my phone but the site is more responsive now so i assume it worked.

#Pedagogical articles
- I utilized the Pedagogy section of the site for this. 
- I centered my paragraphs, as it looked a bit better for this
- I pretty much plugged and played, inputting all the new information
- I had to link PDFs, which i wasn't sure how to do at first
- Eventually i figured out that it worked the same way as pictures or videos.
- I got all of the PDFs into the folder that everything was housed on.
- One problem that I had regarded the spacing of the paragraphs. I had to manually put breaks in the sentences to make them look good in relation to the other columns of text.

##WHAT IS LEFT TO DO?
- Fix the top nav bar situation
- Host site on Bluehost  - Why? affordable, complimentary with GitHub, working contact page, Association with wordpress