from ultralytics import YOLO
import cv2

# Load pretrained YOLO model
model = YOLO("yolov8n.pt")  # or 'yolov8s.pt' for better accuracy

# Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)

# Set resolution (optional)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ Unable to access camera")
        break

    # Run YOLO detection
    results = model(frame)

    # Render bounding boxes on frame
    annotated_frame = results[0].plot()

    # Display the result
    cv2.imshow("YOLO Live Detection", annotated_frame)

    # Press ESC or 'q' to quit
    if cv2.waitKey(1) & 0xFF in [27, ord('q')]:
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
