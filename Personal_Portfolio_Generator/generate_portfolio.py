import json
from jinja2 import Template
import os

# Step 1: Load data from JSON
with open('data.json', 'r') as f:
    data = json.load(f)

# Step 2: Load HTML template
with open('template.html', 'r') as f:
    template = Template(f.read())

# Step 3: Render HTML with data
output_html = template.render(**data)

# Step 4: Save output
os.makedirs("output", exist_ok=True)
with open('output/index.html', 'w') as f:
    f.write(output_html)

print("✅ Portfolio website generated: output/index.html")
