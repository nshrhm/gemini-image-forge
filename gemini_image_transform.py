from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
from datetime import datetime
import os
import sys

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Missing GEMINI_API_KEY environment variable")
client = genai.Client(api_key=api_key)

def transform_image(image_path, prompt):
    try:
        # Load the image
        img = Image.open(image_path)
        
        # Prepare the content for Gemini
        contents = [
            f"Stylize this image: {prompt}",
            img
        ]

        for i in range(4):
            response = client.models.generate_content(
                model="models/gemini-2.0-flash-exp",
                contents=[
                    f"Stylize this image: {prompt} (variation {i+1})",
                    img
                ],
                config=types.GenerateContentConfig(response_modalities=['Text', 'Image'])
            )

            if response.candidates[0].content:
                for part in response.candidates[0].content.parts:
                    if part.text is not None:
                        print(part.text)
                    elif part.inline_data is not None:
                        transformed_image = Image.open(BytesIO(part.inline_data.data))

                        # Save the transformed image
                        output_dir = 'output'
                        os.makedirs(output_dir, exist_ok=True)
                        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                        filename = f'transformed_image_{timestamp}_variation_{i+1}.png'
                        filepath = os.path.join(output_dir, filename)
                        transformed_image.save(filepath)
                        print(f'Transformed image saved to: {filepath}')
            else:
                print(f"No content in response for variation {i+1}.")

        return None

    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python gemini_image_transform.py <image_path> <prompt>")
        sys.exit(1)

    image_path = sys.argv[1]
    prompt = sys.argv[2]

    filepath = transform_image(image_path, prompt)
    if filepath:
        print(f"Image transformation complete. Saved to: {filepath}")
    else:
        print("Image transformation failed.")
