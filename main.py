from ultralytics import YOLO
from multiprocessing import freeze_support

def main():
    model = YOLO('yolov8m.pt')

    results = model.train(data= "C:\\Users\\dell\\Desktop\\ML\\MlPro\\object detection\\config.yml", imgsz=640, lr0=0.01)
    metrics = model.val(data="C:\\Users\\dell\\Desktop\\ML\\MlPro\\object detection\\config.yml")


if __name__ == '__main__':
    freeze_support()
    main()