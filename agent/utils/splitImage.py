from PIL import Image

def split_image_into_quadrants(image):
    width, height = image.size
    half_width = width // 2
    half_height = height // 2

    quadrant_data = {
        "quadrant1": image.crop((0, 0, half_width, half_height)),
        "quadrant2": image.crop((half_width, 0, width, half_height)),
        "quadrant3": image.crop((0, half_height, half_width, height)),
        "quadrant4": image.crop((half_width, half_height, width, height))
    }
    return quadrant_data
