from pycocotools.coco import COCO
from pycocotools.cocoeval_modified import COCOeval
import json

coco_gt = COCO('groundtruth.json')

gt_image_ids = coco_gt.getImgIds()

print("Total images ", len(gt_image_ids))


with open('detections.json', 'r') as f:
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
print('----------------------------------------')
print('AP_0.5-0.95', coco_eval.stats[0])
print('AP_0.5', coco_eval.stats[1])
print('AP_S', coco_eval.stats[3])
print('AP_M', coco_eval.stats[4])
print('AP_L', coco_eval.stats[5])
print('f1_score: ', coco_eval.stats[20])
print('----------------------------------------')
