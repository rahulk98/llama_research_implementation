import pandas as pd
from transformers import pipeline
import os

path = os.getcwd()
file_path = path + '\llama_research_implementation\expenses.xlsx'

try:
    if os.path.exists(file_path):
        os.chmod(file_path, 0o666)
except PermissionError:
    print(1)

# Load the Excel file
df = pd.read_excel('expenses.xlsx')

# Convert the data to a string format suitable for LLaMA
data_str = df.to_string()

# Initialize the LLaMA model for text generation
pipe = pipeline("text-generation", model="meta-llama/Llama-3.2-1B")

# Generate insights
result = pipe(f"Analyze the following expense data and provide insights:\n{data_str}")

# Print the result
print(result[0]['generated_text'])