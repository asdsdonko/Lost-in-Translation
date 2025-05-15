import os
import subprocess

def train_model(model_dir):
    print(f"Training model in {model_dir}...")
    subprocess.run([
        "onmt_train", 
        "-config", os.path.join(model_dir, "config.yaml")
    ])

if __name__ == "__main__":
    for model in ["scaled_dot_model", "multi_head_model", "cross_attention_model", "no_attention_model"]:
        train_model(os.path.join("models", model))