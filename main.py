import os
import google.generativeai as genai

# Configure the API key from environment variable
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set up generation configuration
generationConfig = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 100000000
}

model = genai.GenerativeModel("gemini-pro", generation_config=generationConfig)

def get_google_gen_ai_response(prompt):
    response = model.generate_content([prompt])
    return response.text

def main():
    input_file = 'input.txt'
    output_file = 'output.md'
    
    try:
        with open(input_file, 'r') as file:
            content = file.read()
            prompts = content.split('----')
            
        with open(output_file, 'w') as outfile:
            for i, prompt in enumerate(prompts):
                if prompt.strip():
                    question_name = f"### User Prompt {i+1} ###"
                    response = get_google_gen_ai_response(prompt.strip())
                    print(f"User Prompt {i+1} processed.")
                    outfile.write(f"{question_name}\n\n")
                    outfile.write(f"{prompt.strip()}\n\n")
                    outfile.write(f"**AI Response:**\n\n{response}\n\n")
                    outfile.write("---\n\n")

    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
