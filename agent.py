from google import genai
import json

def analyze_company_data(raw_text, api_key):
    """Feeds raw scraped text to Gemini and demands a structured JSON response."""
    print("🧠 Agent is analyzing the data...")
    
    try:
        client = genai.Client(api_key=api_key)
        
        # The System Prompt: This is where the magic happens. 
        # We give the AI strict rules on how it must format its answer.
        prompt = f"""
        You are a highly skilled B2B market research agent. 
        Analyze the following scraped website text and extract the core business details.
        
        You MUST return your answer as a raw, valid JSON object with EXACTLY these three keys:
        - "Value_Proposition": A one-sentence summary of what the company does.
        - "Target_Audience": Who their ideal customer is.
        - "Pricing_Model": How they charge (e.g., Subscription, Freemium, Custom Enterprise). If not found, write "Not publicly listed".
        
        Do not include markdown blocks, do not say "Here is the JSON". ONLY output the JSON bracket string.
        
        Scraped Text:
        {raw_text}
        """
        
        # Call the Gemini 3.5 Flash model
        response = client.models.generate_content(
            model="gemini-3.5-flash", 
            contents=prompt
        )
        
        # Convert the AI's text string back into a real Python dictionary
        structured_data = json.loads(response.text.strip())
        return structured_data
        
    except json.JSONDecodeError:
        return {"Error": "The AI failed to format the response as JSON. Try again."}
    except Exception as e:
        return {"Error": f"API Connection failed: {e}"}

# --- Testing Block ---
if __name__ == "__main__":
    # To test this standalone, paste your key below
    test_key = ""
    
    # We pass in a fake messy string to see if the AI cleans it up
    fake_scraped_text = "Welcome to CloudFlow! We help enterprise marketing teams automate their email campaigns. Contact sales for pricing."
    
    result = analyze_company_data(fake_scraped_text, test_key)
    print("\n--- AGENT OUTPUT ---\n")
    print(json.dumps(result, indent=4))
