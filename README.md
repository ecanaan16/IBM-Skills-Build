# Healthcare Benefits Q&A Assistant  
A Proof-of-Concept AI Assistant using IBM watsonx.ai

## Overview  
Understanding health insurance can be confusing for employees, from eligibility rules to copays, coverage levels, deductibles, and claims procedures. This project gives a simple prototype of an **AI-powered healthcare benefits assistant** that can answer employee questions using the information from a benefits policy document.

The assistant uses:
- A **benefits.txt** document as its knowledge base  
- A **keyword-based context retrieval system**  
- IBM **watsonx.ai Granite models** through the IBM Cloud API  
- Python code to tie everything together

This solution demonstrates how organizations can build helpful, policy-grounded assistants using lightweight retrieval techniques and IBM’s foundation models.

---

## Problem Statement  
Employees frequently struggle to understand health insurance details related to eligibility, copays, dependent coverage, deductibles, and covered services. HR teams often receive repeated questions that could be automated. A fast, accurate, policy-grounded assistant would help reduce confusion and support employees directly.

---

## Solution  
This project implements a **Healthcare Benefits Q&A Assistant**. Users can type questions in plain English, and the assistant:

1. **Searches** the benefits policy text to find relevant sections  
2. **Extracts a context window** around the match  
3. **Sends the context + question** to an IBM watsonx.ai Granite model using the text generation API  
4. **Generates a short, accurate answer** based solely on the policy text  
5. **Avoids hallucination** by explicitly instructing the model to answer only from the document  

The result is a simple but effective HR benefits assistant that can be expanded or integrated into a larger workflow.

---

## Technologies Used  
- **IBM Cloud IAM** for programmatic token generation  
- **IBM watsonx.ai** (Granite 3 8B Instruct model)  
- **Text Generation API endpoint**  
- **Python 3.10+**  
- **requests** library for API calls  
- **dotenv** for environment variable management  

## How to Run the Assistant

### 1. Install dependencies
```bash
pip install requests python-dotenv

```
- ### 2. Create a .env file with:
``` bash 
WATSONX_API_KEY=your_ibm_cloud_api_key_here
PROJECT_ID=your_project_id_here
```
- ### 3. Add your benefits dataset

- ### 4. Run the program

- ### 5. Ask questions such as:
"Am I eligible to add my spouse to my insurance?"

"What is the copay for a specialist visit?"

"How are X-rays covered?"

"What happens when I reach my out-of-pocket maximum?"


