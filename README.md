# Random Shapes Generator

## Overview

This Python script generates random images with various shapes (circles, hexagons, rectangles, triangles, and letters) on a black background. The shapes are positioned randomly within the image, and their colors and transparency are also randomly assigned. The generated images can be used for creative purposes, testing, or any other application that requires random shape patterns.

## Features

- Generates images with random shapes, colors, and transparency.
- Supports different types of shapes, including circles, hexagons, rectangles, triangles, and letters.
- Avoids fully overlapping shapes to ensure clear and distinct patterns.
- Configurable settings for the number of images, image dimensions, number of shapes per image, and maximum transparent shapes.

## Examples

Here are some examples of images generated using the script:

![Example 1](https://raw.githubusercontent.com/Dreamink-Official/random_shape_generator/main/examples/random_shapes_a4_2.png)
![Example 2](https://raw.githubusercontent.com/Dreamink-Official/random_shape_generator/main/examples/random_shapes_a4_28.png)
![Example 3](https://raw.githubusercontent.com/Dreamink-Official/random_shape_generator/main/examples/random_shapes_a4_3.png)
![Example 4](https://raw.githubusercontent.com/Dreamink-Official/random_shape_generator/main/examples/random_shapes_a4_43.png)

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/random-shapes-generator.git
    ```

2. Navigate to the project directory:

    ```bash
    cd random-shapes-generator
    ```

3. Install the required dependencies (Pillow library):

    ```bash
    pip install pillow
    ```

## Usage

1. Open the script (`random_shapes_generator.py`) in your preferred Python environment.
2. Configure the script by adjusting the settings in the "__main__" block:

    ```python
    num_images = 50  # Adjust the number of images as needed
    output_base_path = "random_shapes_a4_"
    width, height = 700, 700
    num_shapes = 3  # Adjust the number of shapes per image as needed
    max_transparent_shapes = 1  # Adjust the maximum number of transparent shapes as needed
    ```

3. Run the script:

    ```bash
    python random_shapes_generator.py
    ```

4. The generated images will be saved in the current directory with filenames like `random_shapes_a4_1.png`, `random_shapes_a4_2.png`, etc.


