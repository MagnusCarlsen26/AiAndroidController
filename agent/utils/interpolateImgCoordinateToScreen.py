from utils.readConfig import readConfig

def interpolateImgCoordinateToScreen(
    targetCoordinate : dict,
    imgResolution : dict
):

    config = readConfig()

    top_left_x = config["topLeftCorner"]["coordinates"][0]
    top_left_y = config["topLeftCorner"]["coordinates"][1]
    bottom_right_x = config["bottomRightCorner"]["coordinates"][0]
    bottom_right_y = config["bottomRightCorner"]["coordinates"][1]

    # Calculate actual screen width and height from corner coordinates
    actual_screen_width = bottom_right_x - top_left_x
    actual_screen_height = bottom_right_y - top_left_y

    img_width = imgResolution["width"]
    img_height = imgResolution["height"]

    target_horizontal = targetCoordinate["horizontal"]
    target_vertical = targetCoordinate["vertical"]

    # Perform linear interpolation using calculated screen dimensions
    interpolated_x = (target_horizontal / img_width) * actual_screen_width
    interpolated_y = (target_vertical / img_height) * actual_screen_height

    # Adjust for top-left corner offset
    actual_x = top_left_x + interpolated_x
    actual_y = top_left_y + interpolated_y

    return actual_x, actual_y
