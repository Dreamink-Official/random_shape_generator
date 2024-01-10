from PIL import Image, ImageDraw, ImageFont
from math import cos, sin, radians
import random
import string

def generate_random_color(max_transparent_shapes=1):
    if max_transparent_shapes > 0 and random.choice([True, False]):
        max_transparent_shapes -= 1
        return (0, 0, 0, 0)  # Fully transparent
    else:
        grey_tones = [
            # (0, 0, 0),       # Black
            (100, 100, 100),  # Medium grey
            (200, 200, 200)   # Very light grey
        ]
        random.shuffle(grey_tones)  # Shuffle the list to improve randomness
        return random.choice(grey_tones)

def generate_random_shape(draw, width, height, max_transparent_shapes):
    shape_type = random.choice(['letter', 'circle', 'hexagon', 'rectangle', 'triangle'])
    color = generate_random_color(max_transparent_shapes)

    # Ensure the shape is fully contained within the image
    min_size = 100
    max_size = 300

    size = random.randint(min_size, max_size)

    # Center coordinates within a margin from the image border
    margin = 10
    center_x = random.randint(size + margin, width - size - margin)
    center_y = random.randint(size + margin, height - size - margin)

    letter = random.choice(string.ascii_uppercase)  # Choose a random letter

    border_color = tuple(255 - component for component in color)  # Opposite color for the border

    # Function to check if a new shape overlaps with existing shapes
    def overlaps_existing_shapes(new_shape_bbox, existing_shapes_bboxes):
        for existing_bbox in existing_shapes_bboxes:
            # Check if the bounding boxes intersect
            if (
                new_shape_bbox[0] < existing_bbox[2] and
                new_shape_bbox[2] > existing_bbox[0] and
                new_shape_bbox[1] < existing_bbox[3] and
                new_shape_bbox[3] > existing_bbox[1]
            ):
                return True
        return False

    # Get bounding boxes of existing shapes
    existing_shapes_bboxes = []

    for _ in range(100):  # Limit the number of attempts to find a non-overlapping position
        if shape_type == 'circle':
            # Check if the circle overlaps with existing shapes
            new_shape_bbox = (center_x - size, center_y - size, center_x + size, center_y + size)
            if not overlaps_existing_shapes(new_shape_bbox, existing_shapes_bboxes):
                # Draw the circle
                draw.ellipse(new_shape_bbox, fill=color)

                # Draw the border with a thicker width
                border_width = 10  # Adjust the thickness as needed
                draw.ellipse((center_x - size - border_width, center_y - size - border_width,
                              center_x + size + border_width, center_y + size + border_width), outline=border_color, width=border_width)

                existing_shapes_bboxes.append(new_shape_bbox)
                break

        elif shape_type == 'hexagon':
            # Check if the hexagon overlaps with existing shapes
            hexagon_size = size  # Set the size of the hexagon
            hexagon_points = [
                (center_x + hexagon_size * cos(radians(angle)), center_y + hexagon_size * sin(radians(angle)))
                for angle in range(0, 360, 60)
            ]
            new_shape_bbox = (min(p[0] for p in hexagon_points), min(p[1] for p in hexagon_points),
                              max(p[0] for p in hexagon_points), max(p[1] for p in hexagon_points))

            if not overlaps_existing_shapes(new_shape_bbox, existing_shapes_bboxes):
                # Draw the hexagon
                draw.polygon(hexagon_points, fill=color)

                # Draw the border with a thicker width
                border_width = 10  # Adjust the thickness as needed
                hexagon_border_points = [
                    (point[0] + border_width * cos(radians(angle)), point[1] + border_width * sin(radians(angle)))
                    for point, angle in zip(hexagon_points, range(0, 360, 60))
                ]
                draw.polygon(hexagon_border_points, outline=border_color, width=border_width)

                existing_shapes_bboxes.append(new_shape_bbox)
                break

        elif shape_type == 'letter':
            letter_size = random.randint(400, 500)  # Adjust size range for letters
            letter_angle = random.uniform(0, 360)
            font_size = int(letter_size)  # Adjust the multiplier based on your preference
            font = ImageFont.truetype("arial.ttf", font_size)  # Use a suitable font file path

            # Create a transparent image for the rotated letter with border
            rotated_letter_with_border = Image.new("RGBA", (letter_size + 2 * margin, letter_size + 2 * margin), (0, 0, 0, 0))
            draw_letter = ImageDraw.Draw(rotated_letter_with_border)

            # Draw the rotated letter on the transparent image with stroke (border)
            draw_letter.text((margin, margin), letter, fill=color, font=font, stroke_width=5, stroke_fill=border_color)

            # Calculate the new position after rotation, considering the border offset and margin
            rotated_letter_with_border = rotated_letter_with_border.rotate(letter_angle, resample=Image.BICUBIC, expand=True)

            # Calculate the valid range for the center coordinates after rotation
            valid_center_x_range = min(rotated_letter_with_border.width // 2, (width - margin) // 2)
            valid_center_y_range = min(rotated_letter_with_border.height // 2, (height - margin) // 2)

            # Generate center coordinates within the valid range
            center_x = random.randint(valid_center_x_range, width - valid_center_x_range)
            center_y = random.randint(valid_center_y_range, height - valid_center_y_range)

            # Calculate the new position after rotation
            rotated_position = (
                center_x - rotated_letter_with_border.width // 2,
                center_y - rotated_letter_with_border.height // 2
            )

            # Paste the rotated letter with border onto the main image
            image.paste(rotated_letter_with_border, rotated_position, rotated_letter_with_border)

            break

        elif shape_type == 'rectangle':
            # Check if the rectangle overlaps with existing shapes
            new_shape_bbox = (center_x - size, center_y - size, center_x + size, center_y + size)

            if not overlaps_existing_shapes(new_shape_bbox, existing_shapes_bboxes):
                # Draw the rectangle
                draw.rectangle(new_shape_bbox, fill=color)

                # Draw the border with a thicker width
                border_width = 10  # Adjust the thickness as needed
                draw.rectangle((center_x - size - border_width, center_y - size - border_width,
                                center_x + size + border_width, center_y + size + border_width), outline=border_color, width=border_width)

                existing_shapes_bboxes.append(new_shape_bbox)
                break
        elif shape_type == 'triangle':
            # Check if the triangle overlaps with existing shapes
            # Define the triangle vertices (adjust as needed)
            triangle_vertices = [
                (center_x, center_y - size),  # Top vertex
                (center_x - size, center_y + size),  # Bottom left vertex
                (center_x + size, center_y + size),  # Bottom right vertex
            ]
            new_shape_bbox = (
                min(p[0] for p in triangle_vertices), min(p[1] for p in triangle_vertices),
                max(p[0] for p in triangle_vertices), max(p[1] for p in triangle_vertices)
            )

            if not overlaps_existing_shapes(new_shape_bbox, existing_shapes_bboxes):
                # Draw the triangle
                draw.polygon(triangle_vertices, fill=color)

                # Draw the border with a thicker width
                border_width = 10  # Adjust the thickness as needed
                triangle_border_vertices = [
                    (center_x, center_y - size - border_width),  # Top border vertex
                    (center_x - size - border_width, center_y + size),  # Bottom left border vertex
                    (center_x + size + border_width, center_y + size),  # Bottom right border vertex
                ]
                draw.polygon(triangle_border_vertices, outline=border_color, width=border_width)

                existing_shapes_bboxes.append(new_shape_bbox)
                break


if __name__ == "__main__":
    num_images = 50  # Adjust the number of images as needed
    output_base_path = "random_shapes_a4_"
    width, height = 700, 700

    for i in range(num_images):
        output_path = f"{output_base_path}{i+1}.png"
        image = Image.new("RGB", (width, height), (0, 0, 0))
        draw = ImageDraw.Draw(image)

        num_shapes = 3 # Adjust as needed
        max_transparent_shapes = 1  # Adjust as needed

        for _ in range(num_shapes):
            generate_random_shape(draw, width, height, max_transparent_shapes)

        image.save(output_path)
        # image.show()  # Commented out to avoid opening multiple windows
