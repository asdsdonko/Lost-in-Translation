import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("--model", required=True)
parser.add_argument("--src", required=True)
args = parser.parse_args()

output_path = "results/output.txt"

subprocess.run([
    "onmt_translate",
    "-model", f"{args.model}/model_step_500.pt",
    "-src", args.src,
    "-output", output_path,
    "-replace_unk",
    "-verbose"
])