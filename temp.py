import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import face_recognition

# Load the jpg file into a numpy array
image = mpimg.imread("image/1691383186dRJmSJCCv2.JPG")

face_locations = face_recognition.face_locations(img=image, model="hog")
print(f"found {len(face_locations)} face(s) in this photograph.")

# Display the image with rectangles around the faces
plt.imshow(image)

for face_location in face_locations:
    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print(f"A face is located at pixel location Top: {top}, Left: {left}, Bottom: {bottom}, Right: {right}")

    # Draw a rectangle around the face
    rect = plt.Rectangle((left, top), right - left, bottom - top, 
                         linewidth=1, edgecolor='r', facecolor='none')
    plt.gca().add_patch(rect)

# Show the image with rectangles
plt.show()
