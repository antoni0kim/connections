# Connections

![GitHub Actions Status](https://github.com/antoni0kim/connections/actions/workflows/main.yml/badge.svg)

This is a simple machine-learning app solving New York Times' Connections. To install the app, it is highly recommended that the app is installed in
virtual environment. Once virtual environment is set up, you should have both torch and transformers installed:

```bash
pip install torch transformers
```

Then the rest of dependencies can be installed via following command:

```bash
pip install -e .
```

The installation of dependencies is due to testing environment being large storage on the pipeline. Thus, it is recommended to install them separately
(see below for explanation). Once all the dependencies are installed, you can now use the following commands to run the app:

| Commands | Description |
| --- | --- |
| **version** | Output current version of the app |
| **status** | Returns the status of the app |
| **solve** | Solves 16 words entered by the user. There must be 16 words after the command in order for app to solve |

## Explanation of the App

The app uses pre-trained BERT encoder from Hugging Face's transformers library. The tokenizer is also pre-trained from BERT encoder. It is highly recommended to use same tokenizer and the model for the app to work properly. The algorithm uses constrained K-mean clustering with k=4 to set four categorization like the puzzle. The model then sets the word to the categories based on cosine-proximity based on the their tensor values. While training the model to fit the solution is possible, upon examination the model would not suffice to meet the baseline, let alone close the gap between the baseline and validation sets for the current implementation. See the following paper that describes the gap between human and large LLM (<https://arxiv.org/abs/2412.01621>). Thus, the app has been shelf for now.

## Recommendation for future implementation

If transformer models are still being considered, encoder-based transformers are recommended for classification problem like this. The dataset are available in Kaggle (<https://www.kaggle.com/datasets/tm21cy/nyt-connections>).

There are few other possibilities to solve this issue: first, while encoder-based transformers are recommended for classification, it could also be possible to implement the full-transformers to complete the model. The output of the puzzle are dynamic, and thus having LLM to do create categories itself and then have the words to meet their categories would be possible. Second, while LLM would be the first choice to implement this, it is not the only choice either. Deep Q-Network (DQN) is another method that can be implemented here, but the author currently lacks deep (pun intended) knowledge of this area. Hence, the author recommends using this approach if an individual would like to try implementing a beter model
