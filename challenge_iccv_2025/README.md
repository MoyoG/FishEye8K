# 🐳 Docker Setup for AI City ICCV 2025 Track 4

This guide provides a quick start tutorial for container submissions using a fine-tuned YOLOv11n model as a reference.

**You should develop your own implementations of the get_model, preprocess_image, and postprocess_results functions in utils.py for your submission. Prize winners need to place their pretraining data (if applicable) and models in the shared Google Drive and upload training and evaluation containers on Docker Hub. Your training and evaluation scripts inside the container should load models from the mounted /models directory and the data from the /data directory.**

# Evaluation Container Instruction

## 🔹 Pull the Prebuilt Docker Image

Start by pulling the prebuilt Docker image designed for Jetson devices:

```bash
docker pull ganzobtn/aicity_iccv_2025_track4_jetson:latest
```
## 🔹 Build Image Locally (Optional)
If you'd prefer to build the Docker image locally:

```bash
docker build -f Dockerfile.jetson -t ganzobtn/aicity_iccv_2025_track4_jetson:latest .
```

## 🔹 Run the Docker container

```bash
IMAGE="ganzobtn/aicity_iccv_2025_track4_jetson:latest"
DATA_DIR="/path/to/your/data"
```

```bash
docker run -it --ipc=host --runtime=nvidia -v ${DATA_DIR}:/data ${IMAGE}
```

📁 Expected Directory Structure

The `run_evaluation_jetson.py` script inside the container expects the following structure:

- `/data/FishEye1K_eval/` Contains the groundtruth.json file, evaluation images and corresponding annotation files.

- `models/yolo11n_fisheye8k.pt`  
  The fine-tuned YOLOv11n model file used for inference.
  


# Training Container Instruction

This section provides a getting started guide for setting up and running the training Docker container for the challenge, which uses a YOLOv11n model finetuning pipeline.

## 🔹 Pull Prebuilt Docker Image 

You can use the prebuilt Docker image available on Docker Hub:

```bash
docker pull ganzobtn/aicity_iccv_2025_track4_train:latest
```
---

## 🔹 Build the Docker Image Locally (Optional)
If you'd prefer to build the image from the provided Dockerfile:

```bash
docker build -f Dockerfile.train -t ganzobtn/aicity_iccv_2025_track4_train:latest .
```

## 🔹 Run the Docker Container
Set your local paths and run the container:

```bash
IMAGE="ganzobtn/aicity_iccv_2025_track4_train:latest"

DATA_DIR="/path/to/your/data"
MODEL_DIR="/path/to/your/models"

docker run -it --ipc=host --runtime=nvidia \
  -v ${DATA_DIR}:/data \
  -v ${MODEL_DIR}:/models \
  ${IMAGE}
```

📁 Expected Directory Structure
 run_train_yolo.py script inside the container expects the following structure:

 - A dataset folder named Fisheye8K located inside /data.

 - Trained models and output logs will be saved to /models.

