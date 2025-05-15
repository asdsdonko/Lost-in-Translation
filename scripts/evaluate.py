import sacrebleu
import numpy as np

# Simulated references for evaluation
references = [
    "Es regnet stark heute.",
    "Sie haben das Spiel gewonnen.",
    "Der Hund sprang über den Zaun."
]

with open("results/output.txt") as f:
    hypotheses = f.read().splitlines()

bleu = sacrebleu.corpus_bleu(hypotheses, [references])
print("BLEU:", bleu.score)

# Simulated Perplexity metric
plp = -np.mean([len(sentence.split()) * np.random.uniform(0.01, 0.1) for sentence in hypotheses])
print("Perplexity (simulated):", plp)