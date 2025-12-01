from PIL import Image
from agent.utils.addCoordinateGrid import addCoordinateGrid
from agent.utils.splitImage import split_image_into_quadrants

def merge_quadrants(quadrants):
    q1 = quadrants["quadrant1"]
    q2 = quadrants["quadrant2"]
    q3 = quadrants["quadrant3"]
    q4 = quadrants["quadrant4"]

    width = q1.width + q2.width
    height = q1.height + q3.height

    merged_image = Image.new('RGB', (width, height))
    merged_image.paste(q1, (0, 0))
    merged_image.paste(q2, (q1.width, 0))
    merged_image.paste(q3, (0, q1.height))
    merged_image.paste(q4, (q1.width, q1.height))

    return merged_image

def test_split_and_merge_image():
    # Create a dummy image for testing
    # For simplicity, create a white image with known dimensions
    try:
        test_image = Image.open("proccessedImg.png")
    except FileNotFoundError:
        print("proccessedImg.png not found. Creating a dummy image for testing.")
        test_image = Image.new('RGB', (200, 100), color = 'white')
    
    # Optionally, add a coordinate grid for visual verification
    # gridded_image_data = addCoordinateGrid(test_image.copy(), save=False)
    # gridded_image = gridded_image_data["screenshot"]
    gridded_image = test_image.copy()

    # Split the image into quadrants
    quadrants = split_image_into_quadrants(gridded_image)

    width, height = gridded_image.size
    half_width = width // 2
    half_height = height // 2

    gridded_quadrants = {}
    gridded_quadrants["quadrant1"] = addCoordinateGrid(quadrants["quadrant1"].copy(), x_offset=0, y_offset=0)["screenshot"]
    gridded_quadrants["quadrant2"] = addCoordinateGrid(quadrants["quadrant2"].copy(), x_offset=half_width, y_offset=0)["screenshot"]
    gridded_quadrants["quadrant3"] = addCoordinateGrid(quadrants["quadrant3"].copy(), x_offset=0, y_offset=half_height)["screenshot"]
    gridded_quadrants["quadrant4"] = addCoordinateGrid(quadrants["quadrant4"].copy(), x_offset=half_width, y_offset=half_height)["screenshot"]

    # Save each quadrant to verify visually
    for name, img in gridded_quadrants.items():
        img.save(f"test_{name}.png")
        print(f"Saved {name} to test_{name}.png with size {img.size}")

    print("Image splitting test complete. Check 'test_quadrantX.png' files in the root directory.")

    # Merge the quadrants back and save for verification
    merged_image = merge_quadrants(gridded_quadrants)
    merged_image.save("test_merged_image.png")
    print("Merged image saved to test_merged_image.png")

if __name__ == "__main__":
    test_split_and_merge_image()
