# FishEye8K
FishEye8K: A Benchmark and Dataset for Fisheye Camera Object Detection

<p align="center" width="100%">
    <img width="100%" src="https://github.com/MoyoG/FishEye8K/assets/10125947/5e53c3bb-3bde-48fe-a287-327c05da08ce">
</p>

We provide detailed information on the new FishEye8K road object detection dataset. The dataset consists of 8,000 annotated images with 157K bounding boxes of five object classes. The figure displays sample images from each of the 18 cameras with wide-angle fisheye views. These cameras offer new possibilities for extensive coverage.

**Results of YOLOv7-E6E model on the input size 1280x1280.**

https://github.com/MoyoG/FishEye8K/assets/10125947/89b1f6d4-624a-4822-bd3a-890cd0600e91

                         
**Classes (Color)**
- Bus (Red)
- Bike (Blue)
- Car (Green)
- Pedestrian (Yellow)
- Truck (Purple)


# Dataset
- [Click to download the Fisheye8k dataset](https://scidm.nchc.org.tw/dataset/fisheye8k?fbclid=IwAR1BEkiuq4TVOrkvainiteDTtx75mKRS__UrEoxZQP3MBCN8D5qtsYTgw0g)
- [Click to download the paper]()

# Train and Test 

<p align="center" width="100%">
    <img src="https://github.com/MoyoG/FishEye8K/assets/10125947/0a291e9e-43e2-41a1-89ff-e29630a57cab">
</p>

# Experimental results 

| Model      | Version   | Input Size | Precision | Recall | mAP0.5 | mAP.5-.95 | f1\-score | APS    | APM    | APL    | Inference[ms] |
| ---------- | --------- | ---------- | --------- | ------ | ------ | --------- | --------- | ------ | ------ | ------ | ------------- |
| YOLOv5     | YOLOv5l6  | 1280       | 0.7929    | 0.4076 | 0.6139 | 0.4098    | 0.535     | 0.1299 | 0.434  | 0.6665 | 22.7          |
|            | YOLOv5x6  | 1280       | 0.8224    | 0.4313 | 0.6387 | 0.4268    | 0.5588    | 0.133  | 0.452  | 0.6925 | 43.9          |
| YOLOR      | YOLOR-W6  | 1280       | 0.7871    | 0.4718 | 0.6466 | 0.4442    | 0.5899    | 0.1325 | 0.4707 | 0.6901 | 16.4          |
|            | YOLOR-P6  | 1280       | 0.8019    | 0.4937 | 0.6632 | 0.4406    | 0.6111    | 0.1419 | 0.4805 | 0.7216 | 13.4          |
| YOLOv7     | YOLOv7-D6 | 1280       | 0.7803    | 0.4111 | 0.3977 | 0.2633    | 0.5197    | 0.1261 | 0.4462 | 0.6777 | 26.4          |
|            | YOLOv7-E6E| 1280       | 0.8005    | 0.5252 | 0.5081 | 0.3265    | 0.6294    | 0.1684 | 0.5019 | 0.6927 | 29.8          |
| YOLOv7     | YOLOv7    | 640        | 0.7917    | 0.4373 | 0.4235 | 0.2473    | 0.5453    | 0.1108 | 0.4438 | 0.6804 | 4.3           |
|            | YOLOv7-X  | 640        | 0.7402    | 0.4888 | 0.4674 | 0.2919    | 0.5794    | 0.1332 | 0.4605 | 0.7212 | 6.7           |
| YOLOv8     | YOLOv8l   | 640        | 0.7835    | 0.3877 | 0.612  | 0.4012    | 0.5187    | 0.1038 | 0.4043 | 0.6577 | 8.5           |
|            | YOLOv8x   | 640        | 0.8418    | 0.3665 | 0.6146 | 0.4029    | 0.5106    | 0.0997 | 0.4147 | 0.7083 | 13.4          |

# Citation
hello
