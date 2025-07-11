# Leopard Detection with YOLOv8 🐆

A Python project for real-time leopard detection using a custom YOLOv8 model and OpenCV. This application processes video input from a webcam or video file to detect leopards with high accuracy.

## 🚀 Features
- Real-time leopard detection using a pre-trained YOLOv8 model
- Customizable confidence threshold (default: 0.7)
- Visualizes bounding boxes and labels on detected leopards
- Supports webcam or image/video file input

## 📋 Requirements
- Python 3.8+
- `opencv-python`
- `ultralytics`
- Custom YOLOv8 model (`NTLeopard1.pt`)

Install dependencies:
```bash
pip install opencv-python ultralytics
```

## 🛠️ Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/leopard-detection-yolov8.git
   ```
2. Place your `NTLeopard1.pt` model file in the project directory.
3. Install the required dependencies (see above).

## ▶️ Usage
Run the detection script:
```bash
python main.py
```
- Press `q` to quit the application.
- The script processes video input and displays detected leopards with bounding boxes and labels.

## 📸 Screenshots
<img width="926" height="424" alt="Screenshot 2025-07-11 at 3 29 29 PM" src="https://github.com/user-attachments/assets/d2ec0415-0d14-45d9-8038-979e2276e681" />

<img width="834" height="334" alt="Screenshot 2025-07-11 at 3 29 58 PM" src="https://github.com/user-attachments/assets/892617d1-110f-4a5c-bbe3-fff787f7e03f" />


## 📝 Notes
- Ensure the `NTLeopard1.pt` model is trained for leopard detection.
- Adjust `conf_threshold` in the script for sensitivity tuning.
- Webcam input is set to device `0`; modify `cv2.VideoCapture(0)` for other inputs.

## 🤝 Contributing
Contributions are welcome! Please open an issue or submit a pull request.
