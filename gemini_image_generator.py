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

prompt = sys.argv[1] if len(sys.argv) > 1 else "Hi, can you create a 3d rendered image of a pig with wings and a top hat flying over a happy futuristic scifi city with lots of greenery?"

response = client.models.generate_images(
    model='imagen-3.0-generate-002',
    prompt=prompt,
    config=types.GenerateImagesConfig(
        number_of_images=4,
    )
)
for generated_image in response.generated_images:
  image = Image.open(BytesIO(generated_image.image.image_bytes))
  image.show()
  output_dir = 'output'
  os.makedirs(output_dir, exist_ok=True)
  timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
  filename = f'generated_image_{timestamp}.png'
  filepath = os.path.join(output_dir, filename)
  image.save(filepath)
  print(f'Image saved to: {filepath}')
