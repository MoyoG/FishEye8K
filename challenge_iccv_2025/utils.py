from ultralytics import YOLO
import os
import cv2
import numpy as np
from pycocotools.coco import COCO
from pycocotools.cocoeval_modified import COCOeval
import json

def f1_score(predictions_path, ground_truths_path):
    coco_gt = COCO(ground_truths_path)

    gt_image_ids = coco_gt.getImgIds()

    with open(predictions_path, 'r') as f:
        detection_data = json.load(f)
    filtered_detection_data = [
        item for item in detection_data if item['image_id'] in gt_image_ids]
    with open('./temp.json', 'w') as f:
        json.dump(filtered_detection_data, f)
    coco_dt = coco_gt.loadRes('./temp.json')
    coco_eval = COCOeval(coco_gt, coco_dt, 'bbox')
    coco_eval.evaluate()
    coco_eval.accumulate()
    coco_eval.summarize()
    
    # Assuming the F1 score is at index 20 in the stats array
    return coco_eval.stats[20]  # Return the F1 score from the evaluation stats
    # return 0.85  # Simulated constant value for demo purposes

def get_model(model_path):
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file {model_path} does not exist.")
    # You need to implement your model here
    model = YOLO(model_path)
    return model
def preprocess_image(image):
    if image is None:
        raise ValueError("Input image is None.")
    # Preprocess the image for your own model

    return image
def postprocess_result(results):
    if not results or len(results) == 0:
        return []
    boxes = results[0].boxes.xyxy.cpu().numpy().tolist()        # shape: (N, 4)
    scores = results[0].boxes.conf.cpu().numpy().tolist()       # shape: (N,)
    classes = results[0].boxes.cls.cpu().numpy().tolist()       # shape: (N,)

    return [boxes, scores, classes] 
def changeId(id):
    sceneList = ['M', 'A', 'E', 'N']
    cameraId = int(id.split('_')[0].split('camera')[1])
    sceneId = sceneList.index(id.split('_')[1])
    frameId = int(id.split('_')[2])
    imageId = int(str(cameraId)+str(sceneId)+str(frameId))
    return imageId
