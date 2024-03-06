"""Testing file: Contains playground"""

from transformers import pipeline

classifier = pipeline(
    task="sentiment-analysis",
    )

res = classifier("Depresso Espresso")

print(res)
