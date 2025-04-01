# import numpy as np
import torch
from transformers import BertTokenizer, BertModel
from k_means_constrained import KMeansConstrained

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")


def get_embedding(word):
    inputs = tokenizer(word, return_tensors="pt",
                       padding=True, truncation=True)
    with torch.no_grad():
        targets = model(**inputs)
    embedding = targets.last_hidden_state[:, 0, :].squeeze().numpy()
    return embedding


def bert_untrained_model(words):
    model.eval()
    kmeans = KMeansConstrained(n_clusters=4, size_min=4,
                               size_max=4, random_state=42)
    clusters = kmeans.fit_predict(get_embedding(words))
    answers = [[] for _ in range(4)]
    for word, cluster in zip(words, clusters):
        answers[cluster].append(word)

    return answers
