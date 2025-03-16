# System Patterns: Gemini Image Forge

**System Architecture:**

The project follows a simple, modular architecture with two main components:

1.  **Image Generation Script (`gemini_image_generator.py`):**
    *   Takes a text prompt as input.
    *   Uses the Gemini API to generate an image based on the prompt.
    *   Saves the generated image to the `output` directory.

2.  **Image Transformation Script (`gemini_image_transform.py`):**
    *   Takes an image path and a text prompt as input.
    *   Uses the Gemini API to transform the image based on the prompt.
    *   Saves the transformed image to the `output` directory.

**Key Technical Decisions:**

*   Using the Gemini API for image generation and transformation.
*   Using the PIL library for image manipulation.
*   Using the `gh` command-line tool for GitHub repository management.

**Design Patterns in Use:**

*   **Command-line interface:** Provides a simple and intuitive way for users to interact with the scripts.
*   **Modular design:** Separates the image generation and transformation logic into distinct scripts.

**Component Relationships:**

*   The `gemini_image_generator.py` and `gemini_image_transform.py` scripts are independent of each other.
*   Both scripts rely on the Gemini API and the PIL library.
