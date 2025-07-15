AI-Powered Textile Carbon Emission Estimator
An AI-powered pipeline that estimates textile carbon emissions from natural language input using OpenAI's GPT models, n8n automation, and a Flask-based CO₂e calculator. Automatically extracts structured data, computes emissions, and returns a human-friendly interpretation of environmental impact.

🔍 Overview
This project enables users to input plain English descriptions like:

"1kg of recycled polyester from China, assembled, shipped by road 800km"

And get:

✅ Structured data (material, origin, transport, etc.)

✅ Carbon emission estimation in kg CO₂e

✅ A clear and relatable explanation

⚙️ Tech Stack
Tool	Purpose
🧠 OpenAI GPT (gpt-4.1-mini)	Converts text → structured JSON
🧪 Flask	Calculates CO₂e emissions
🔁 n8n	Manages webhooks and automation logic
🧵 Custom Dataset	Textile carbon factors (materials, origin, transport)

💡 Features
🌐 Accepts human-like input (via API or webhook)

🔎 Extracts accurate data using LLMs

📦 Calculates CO₂e using emission multipliers

💬 Translates output into natural language interpretation

🔄 Fully automated using n8n orchestration

🚀 Quickstart
1. Clone the repo
bash
Copy
Edit
git clone https://github.com/your-username/AI-Powered-Textile-Carbon-Emission-Estimator.git
cd AI-Powered-Textile-Carbon-Emission-Estimator
2. Start the Flask API
bash
Copy
Edit
pip install flask
python app.py
3. Set up n8n Workflow
Add a Webhook Trigger node (to accept input like 1kg of cotton from India, dyed and assembled, shipped by sea 500km)

Connect to HTTP Request node (OpenAI API)

Pass result to HTTP Request node (Flask CO₂e API)

Connect final result to HTTP Request node (OpenAI for human-readable interpretation)

Send final result to Respond to Webhook

🧠 Example JSON Flow
Input Prompt:

1kg of recycled polyester from China, assembled, shipped by road 800km

LLM Extracted JSON:

json
Copy
Edit
{
  "material": "Polyester (mechanically recycled)",
  "manufacturing_processes": ["Garment Assembly"],
  "origin": "China",
  "transport_mode": "Road",
  "weight": 1.0,
  "distance": 800
}
Flask API Response:

json
Copy
Edit
{
  "total_co2e_kg": 74.0608
}
Final Interpretation:

A carbon emission of 74.06 kg CO₂e is moderate, roughly equivalent to driving a typical car for about 200 miles. It's higher than the average daily electricity use for a household.

🛠️ Emission Factors Used
Materials: Cotton, Polyester (virgin & recycled), Wool, Silk, etc.

Processes: Dyeing, Assembly, Tanning, etc.

Transport: Road, Rail, Sea, Air

Origin Multipliers: Based on region-specific energy footprints

📘 Use Cases
🏷️ E-commerce sustainability labels

📊 Environmental impact reports

🧾 Eco-footprint calculators

👚 Green fashion product analysis

🧑‍💻 Contributing
Pull requests are welcome! For major changes, open an issue first to discuss the proposal.

📄 License
This project is licensed under the Apache License 2.0.
See the LICENSE file for details.
