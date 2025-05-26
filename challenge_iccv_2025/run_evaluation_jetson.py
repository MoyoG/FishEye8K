import os
import time
import argparse
import cv2
import json
import numpy as np
from ultralytics import YOLO

from utils import f1_score

from utils import get_model , preprocess_image , postprocess_result, changeId
import json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_folder', type=str, default='/data/Fisheye1K_eval/images', help='Path to image folder')
    parser.add_argument('--model_path', type=str, default='models/yolo11n_fisheye8k.pt', help='Path to the model')
    parser.add_argument('--max_fps', type=float, default=25.0, help='Maximum FPS for evaluation')
    parser.add_argument('--output_json', type=str, default='predictions.json', help='Output JSON file for predictions')
    parser.add_argument('--ground_truths_path', type=str, default='/data/Fisheye1K_eval/groundtruth.json', help='Path to ground truths JSON file')
    args = parser.parse_args()

    image_folder = args.image_folder
    model_path = args.model_path

    model = get_model(model_path)

    image_files = sorted([
        os.path.join(image_folder, f)
        for f in os.listdir(image_folder)
        if f.lower().endswith(('.jpg', '.jpeg', '.png'))
    ])

    print(f"Found {len(image_files)} images.")

    predictions = []
    start_time = time.time()

    for image_path in image_files:
        img = cv2.imread(image_path)
        if img is None:
            print(f"Warning: Could not load {image_path}, skipping.")
            continue
        img = preprocess_image(img)
        results = model(img, verbose=False)
        results = postprocess_result(results) # [boxes, scores, classes]
        predictions.append((image_path,results))
        print(f"Processed {os.path.basename(image_path)}: {len(results[0])} objects detected.")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Processed {len(image_files)} images in {elapsed_time:.2f} seconds.")

    predictions_json = []
    # Convert predictions to JSON format
    for image_path, pred in predictions: #iterate over each image's predictions
        if not pred:
            continue
        #iterate over each prediction in the image
        for i in range(len(pred[0])):
            x1, y1, x2, y2 = pred[0][i]
            image_id = changeId(os.path.basename(image_path).split('.')[0])
            predictions_json.append({
                'image_id': image_id,
                'bbox': [x1, y1, x2 - x1, y2 - y1],
                'score': pred[1][i],
                'category_id': int(pred[2][i])
            })
    # Save predictions to JSON
    with open(args.output_json, 'w') as f:
        json.dump(predictions_json, f, indent=2)

    fps = len(image_files) / elapsed_time
    normfps = min(fps, args.max_fps)/args.max_fps

    f1 = f1_score(args.output_json, args.ground_truths_path)
    harmonic_mean = 2 * f1 * normfps / (f1 + normfps)

    print(f"\n--- Evaluation Complete ---")
    print(f"Total inference time: {elapsed_time:.2f} seconds")
    print(f"FPS: {fps:.2f}")
    print(f"Normalized FPS: {normfps:.4f}")
    print(f"F1-score: {f1:.4f}")
    print(f"Metric (harmonic mean of F1-score and NormalizedFPS): {harmonic_mean:.4f}")

if __name__ == "__main__":
    main()