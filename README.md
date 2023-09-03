# YOLOv5 People Counter with InfluxDB Integration

This repository contains the code for an object detection project using YOLO.

## Prerequisites

- Docker
- Python 3.x
- InfluxDB
- An available RTSP camera

## Configuration

### Changes in `database.py`

You need to modify the InfluxDB configuration in order to work properly. Open the `database.py` file and make the following change:

```python
client = InfluxDBClient(url="http://your_ip:your_port/", token="your_token", org="your_org")
```

### Changes in `count_people.py`

To set up the RTSP camera source and the weights for YOLO, you need to modify the `count_people.py` file as follows:

```python
subprocess.Popen(['python3', 'detect.py', '--source', 'rtsp://you_ip:your_port/cam', '--weights', 'yolov5s.pt','--save-txt'])
```

## Usage

### Clone the Repository

```bash
git clone https://github.com/DianaChica/influxdb-yolov5.git
cd influxdb-yolov5
```

### Build and Run the Docker Container

Once you're in the directory of the cloned repository, run the following commands:

```bash
docker build -t detection-yolo .
docker run --memory=3072m --name=detection-yolo-container -d detection-yolo
```
### Acknowledgments
This project utilizes the YOLOv5 object detection framework developed by Ultralytics. Special thanks to their team for their valuable contribution.