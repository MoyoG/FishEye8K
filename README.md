# FishEye8K: A Benchmark and Dataset for Fisheye Camera Object Detection

**Authors:**
[Munkhjargal Gochoo](https://github.com/moyog/), [Munkh-Erdene Otgonbold](https://github.com/omunkhuush/), Erkhembayar Ganbold, Ming-Ching Chang, [Ping-Yang Chen](https://github.com/pingyang1117), Byambaa Dorj, Hamad Al Jassmi, [Ganzorig Batnasan](https://github.com/ganzob/), Fady Alnajjar, Mohammed Abduljabbar, Fang-Pang Lin, Jun-Wei Hsieh

<p align="center" width="100%">
    <img width="100%" src="https://github.com/MoyoG/FishEye8K/assets/10125947/5e53c3bb-3bde-48fe-a287-327c05da08ce">
</p>

We provide detailed information on the new FishEye8K road object detection dataset. The dataset consists of 8,000 annotated images with 157K bounding boxes of five object classes. The figure displays sample images from each of the 18 cameras with wide-angle fisheye views. These cameras offer new possibilities for extensive coverage.

**Results of YOLOv7-E6E model on the input size 1280x1280.**

https://github.com/MoyoG/FishEye8K/assets/73123564/f7dd27db-7613-4e2c-b5f0-ec33c44deba4


                         
**Classes (Color)**
- ![#FF3333](https://placehold.co/15x15/FF3333/FF3333.png) - Bus 
- ![#3358FF](https://placehold.co/15x15/3358FF/3358FF.png) - Bike
- ![#33FF33](https://placehold.co/15x15/33FF33/33FF33.png) - Car
- ![#F6FF33](https://placehold.co/15x15/F6FF33/F6FF33.png) - Pedestrian
- ![#9F33FF](https://placehold.co/15x15/9F33FF/9F33FF.png) - Truck


# Dataset
- [Click to download the Fisheye8K dataset](https://scidm.nchc.org.tw/en/dataset/fisheye8k)
- If you want to download whole dataset at once, choose **Fisheye8K_all_including_train_test.zip**
- Click on "**Explore**" and "**Go to resource**"

<p align="center" width="100%">
    <img src="https://github.com/MoyoG/FishEye8K/assets/73123564/847fca10-d970-4ccc-96cf-dd1de68df624">
</p>

# Paper
- [Click to download the paper](https://openaccess.thecvf.com/content/CVPR2023W/AICity/html/Gochoo_FishEye8K_A_Benchmark_and_Dataset_for_Fisheye_Camera_Object_Detection_CVPRW_2023_paper.html?fbclid=IwAR2UCUtrPydcCFxRjN67d7RyAyX-dNJAEi7mWPJjWhX3kTUA_SQ4AJyaFWc)

# Train and Test 

<p align="center" width="100%">
    <img src="https://github.com/MoyoG/FishEye8K/assets/10125947/0a291e9e-43e2-41a1-89ff-e29630a57cab">
</p>

# Experimental results 

We evaluated using default yolo test.py 

- conf_thres=0.5  
- iou_thres=0.5

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
```
@InProceedings{Gochoo_2023_CVPR,
    author    = {Gochoo, Munkhjargal and Otgonbold, Munkh-Erdene and Ganbold, Erkhembayar and Hsieh, Jun-Wei and Chang, Ming-Ching and Chen, Ping-Yang and Dorj, Byambaa and Al Jassmi, Hamad and Batnasan, Ganzorig and Alnajjar, Fady and Abduljabbar, Mohammed and Lin, Fang-Pang},
    title     = {FishEye8K: A Benchmark and Dataset for Fisheye Camera Object Detection},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Workshops},
    month     = {June},
    year      = {2023},
    pages     = {5304-5312}
}

