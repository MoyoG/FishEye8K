from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval


coco_gt = COCO('../../../evaluation/Fisheye1K_eval/groundtruth.json')
coco_dt = coco_gt.loadRes(
    '../../../evaluation/Fisheye1K_eval/detection_dgx.json')

print(type(coco_dt))
print(type(coco_gt))

coco_eval = COCOeval(coco_gt, coco_dt, 'bbox')
coco_eval.evaluate()
coco_eval.accumulate()
coco_eval.summarize()
