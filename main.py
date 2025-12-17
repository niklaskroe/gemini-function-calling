from dotenv import load_dotenv
from google import genai
from google.genai import types
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set!")

system_prompt="You are a school teacher and you explain math answers to students at the age of 7. An example: Q: What is 2+2? A: 2+2 is 4 because when you have 2 apples and you get 2 more apples, you count them all together to get 4 apples."
user_prompt = "What is 10+11?"

# Define the function declaration for the model
sum_numbers_function = [
    {
        "name": "sum_numbers",
        "description": "Returns the sum of two given integer numbers.",
        "parameters": {
            "type": "object",
            "properties": {
                "number1": {
                    "type": "integer",
                    "description": "The first integer number to sum.",
                },
                "number2": {
                    "type": "integer",
                    "description": "The second integer number to sum.",
                }
            },
            "required": ["number1", "number2"],
        }
    }
]

# Configure the client and tools
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
tools = types.Tool(function_declarations=sum_numbers_function)
config = types.GenerateContentConfig(
    tools=[tools],
    system_instruction=system_prompt
)

# Send request with function declarations
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=user_prompt,
    config=config,
)

# Check for a function call
if response.candidates[0].content.parts[0].function_call:
    function_call = response.candidates[0].content.parts[0].function_call
    print(f"Function to call: {function_call.name}")
    print(f"Arguments: {function_call.args}")


    # Implement the function logic

    def sum_numbers(number1, number2):
        """
        Returns the sum of the two given integer numbers.
        """
        return {"number1": number1, "number2": number2, "sum": number1 + number2}


    # Call the function with the arguments provided by the model
    result = sum_numbers(**function_call.args)
    print(f"Function result: {result}")

    # Send the function result back to the model for final response
    final_response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            types.Content(parts=[types.Part(text=user_prompt)]),
            response.candidates[0].content,
            types.Part(
                function_response=types.FunctionResponse(
                    name=function_call.name,
                    response=result,
                )
            ),
        ],
        config=config,
    )
    print(final_response.text)
else:
    print("No function call found in the response.")
    print(response.text)
