## GitHub Troll
/n
# FaceEmotionRecognition
https://github.com/SomyaRanjanSahu/FaceEmotionRecognition/blob/master/.ipynb_checkpoints/Image_recognition-checkpoint.ipynb
- By SomyaRanjanSahu
- Utilizing the Deep Face Library
- This code is for a facial emotion recognition software.
- Each emotion is separated into different data sets
- The first in was the happy face FaceEmotionRecognition
- It seems that they are coding something into an existing software, as their code seems to be missing a lot of information and referencing different pre existing information
- In each data set, there is a prediction of "dominant emotion"
- Im not really sure what i am looking at.

predictions["dominant_emotion"]
'happy'

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #print(faceCascade.empty())
faces = faceCascade.detectMultiScale(gray,1.1,4)

    #Draw a rectangle around the faces
for(x, y, w, h) in faces:
    cv2.rectangle(img[:, :, ::-1], (x,y), (x+w, y+h), (255, 0, 0), 5)

- What are the colors referencing??
- I think it is the way the computer analyzes the color of the picture. Maybe it takes less computational power to grayscale the pic before analysis.
- Last they insert a picture.
- Then they move onto the next data set with is the next emotion of sad Face
- The last three commits were Disgust, Fear, and Surprise, which are all formatted the same way as happy
- I think this is only a partial picture and i am going to explore the other folders in this repository.
- Going through each of the folders in the repository, There is one that has 85 lines. This one just has to do with the opening and closing of the app. it says that if videocapture, the adjacent software, is not working or open, to display "cannot open webcam"
- it also gives instructions on what to do if it is open. It puts the camera in Grayscale - which answers my question from earlier.
-  https://github.com/SomyaRanjanSahu/FaceEmotionRecognition/blob/master/Realtime_recognition.ipynb
- Opening up the folder i find that most of the content inside is a sub version of the emotion data sets stated above
- the last sub folder is 2615 lines of HTML and now im very confused
- https://github.com/SomyaRanjanSahu/FaceEmotionRecognition/blob/master/haarcascade_frontalface_default.xml
- I think this is a reference to text and formatting. I have zero clue how to approach this.
