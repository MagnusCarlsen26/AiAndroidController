from PIL import Image, ImageDraw, ImageFont

def addCoordinateGrid(
    img,
    marks=None,
    save=False,
    grid_spacing=25,
    output_path="proccessedImg.png",
    x_offset=0,
    y_offset=0
):
    width, height = img.size

    # Create a drawing context
    draw = ImageDraw.Draw(img)
    
    font = ImageFont.load_default()
    
    grid_color = (255, 0, 0)

    # Calculate starting points for labels to align with absolute multiples of grid_spacing
    start_x_for_labels = (grid_spacing - (x_offset % grid_spacing)) % grid_spacing
    start_y_for_labels = (grid_spacing - (y_offset % grid_spacing)) % grid_spacing

    # Draw vertical lines and X coordinates
    last_x = 0
    for x in range(0, width, grid_spacing):
        # draw.line([(x, 0), (x, height)], fill=grid_color, width=1)
        last_x = x
    
    for x_label_pos in range(start_x_for_labels, width, grid_spacing):
        absolute_x = x_label_pos + x_offset
        _draw_label(draw, font, x_label_pos, str(absolute_x), True)
 
    # Draw horizontal lines and Y coordinates
    last_y = 0
    for y_draw_pos in range(start_y_for_labels, height, grid_spacing):
        # Draw horizontal line
        # draw.line([(0, y_draw_pos), (width, y_draw_pos)], fill=grid_color, width=1)
        last_y = y_draw_pos

    for y_label_pos in range(start_y_for_labels, height, grid_spacing):
        absolute_y = y_label_pos + y_offset
        _draw_label(draw, font, y_label_pos, str(absolute_y), False)
    _draw_marks(draw, marks)

    if save:
        img.save(output_path)
    
    print("saved img to ", output_path)

    return {
        "screenshot" : img,
        "imageMeta" : {
            "width" : last_x,
            "height" : last_y
        }
    }

def _draw_label(
    draw,
    font,
    label_value,
    label_text,
    is_x_axis
):
    bbox = draw.textbbox((0, 0), label_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    if is_x_axis:
        # X coordinate label
        draw.rectangle(
            [label_value - text_width // 2 - 2, 2, label_value + text_width // 2 + 2, text_height + 4],
            fill=(255, 255, 255)
        )
        draw.text((label_value - text_width // 2, 2), label_text, fill=(0, 0, 0), font=font)
    else:
        # Y coordinate label
        # Adjust x-position for label to prevent overlap
        x_pos_text = 5 # Small padding from the left edge
        draw.rectangle(
            [x_pos_text - 2, label_value - text_height // 2 - 2, x_pos_text + text_width + 2, label_value + text_height // 2 + 2],
            fill=(255, 255, 255)
        )
        draw.text((x_pos_text, label_value - text_height // 2), label_text, fill=(0, 0, 0), font=font)

def _draw_marks(draw, marks):
    if marks is not None:
        for mark_x, mark_y in marks:
            # Draw a red circle at the marked coordinate
            mark_radius = 5
            draw.ellipse(
                [(mark_x - mark_radius, mark_y - mark_radius),
                 (mark_x + mark_radius, mark_y + mark_radius)],
                fill=(0, 255, 0, 128),
                outline=(0, 255, 0)
            )
