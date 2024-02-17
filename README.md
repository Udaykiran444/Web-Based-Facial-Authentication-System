**Face Recognition Flask Application**
This Flask application provides real-time face recognition using the OpenCV and face_recognition libraries. It captures video from the webcam, detects faces, compares them with a known face, and authenticates users based on face matches.

**Description**
The Face Recognition Flask Application allows users to authenticate themselves using their face. It captures video frames from the webcam, detects faces in each frame, and compares them with a known face image to determine authentication. If the face matches the known face, the user is authenticated; otherwise, authentication fails.

**Features**
Real-time face recognition: The application captures video from the webcam and performs face recognition in real-time.
User authentication: Users can authenticate themselves using their face. If the face matches the known face image, authentication is successful.
Authentication feedback: The application provides feedback on authentication status, indicating whether the login was successful or not.
Dependencies
This project relies on the following libraries:

Flask: For building the web application framework.
OpenCV: For capturing video frames from the webcam and image processing.
face_recognition: For face detection and recognition.
Getting Started
**To run the application, follow these steps:**

Ensure you have Python installed on your system.
Install the required dependencies using pip:
Copy code
pip install flask opencv-python-headless face_recognition
Clone or download the repository to your local machine.
Navigate to the project directory and run the app.py file using Python:
Copy code
python app.py
Open a web browser and navigate to http://localhost:5000 to access the application.
**Usage**
On the homepage, the application starts capturing video from the webcam.
If the face matches the known face, the application displays a success message and grants access.
If the face does not match, the application displays a login failed message.
**Customization**
You can customize the known face image and authentication logic according to your requirements. Update the known_image_path variable in the app.py file to specify the path to the known face image.

**Contributions**
Contributions to this project are welcome. Feel free to submit issues or pull requests.
