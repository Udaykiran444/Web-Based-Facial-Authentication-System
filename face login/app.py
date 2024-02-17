from flask import Flask, render_template, Response, request
import cv2
import face_recognition

app = Flask(__name__, template_folder='templates')

# Load the known face image and encoding
known_image_path = "known_face.png"
known_image = face_recognition.load_image_file(known_image_path)
known_encoding = face_recognition.face_encodings(known_image)[0]

def gen_frames():
    video_capture = cv2.VideoCapture(0)

    while True:
        success, frame = video_capture.read()
        if not success:
            break
        else:
            unknown_encoding = face_recognition.face_encodings(frame)

            if unknown_encoding:
                results = face_recognition.compare_faces([known_encoding], unknown_encoding[0])

                if results[0]:
                    yield (b'--frame\r\n'
                           b'Content-Type: image/jpeg\r\n\r\n' + cv2.imencode('.jpg', frame)[1].tobytes() + b'\r\n\r\n')
                else:
                    cv2.putText(frame, "Login Failed. Face does not match.", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                    ret, jpeg = cv2.imencode('.jpg', frame)
                    frame = jpeg.tobytes()
                    yield (b'--frame\r\n'
                           b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

            else:
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + cv2.imencode('.jpg', frame)[1].tobytes() + b'\r\n\r\n')

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if check_user_authentication():
            return render_template("success.html")
        else:
            return render_template("login_failed.html")
    else:
        return render_template("index_with_camera.html")

@app.route("/video_feed")
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

def check_user_authentication():
    # Implement your user authentication logic here
    # For simplicity, let's assume user is authenticated if the face matches
    return face_matches()

def face_matches():
    # Load the current frame and find face encodings
    video_capture = cv2.VideoCapture(0)
    _, frame = video_capture.read()
    unknown_encoding = face_recognition.face_encodings(frame)

    # Check if the face matches the known face
    if unknown_encoding:
        results = face_recognition.compare_faces([known_encoding], unknown_encoding[0])
        return results[0]
    else:
        return False

if __name__ == "__main__":
    app.run(debug=True)
