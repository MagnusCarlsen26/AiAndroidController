from PIL import Image, ImageDraw, ImageFont

def addCoordinateGrid(
    img,
    marks=None,
    save=False,
    grid_spacing=25,
    output_path="proccessedImg.png"
):
    width, height = img.size

    # Create a drawing context
    draw = ImageDraw.Draw(img)
    
    font = ImageFont.load_default()
    
    grid_color = (255, 0, 0)

    # Draw vertical lines and X coordinates
    last_x = 0
    for x in range(0, width, grid_spacing):
        # Draw vertical line
        draw.line([(x, 0), (x, height)], fill=grid_color, width=1)
        _draw_label(draw, font, x, str(x), True)
        last_x = x
 
    # Draw horizontal lines and Y coordinates
    last_y = 0
    for y in range(0, height, grid_spacing):
        # Draw horizontal line
        draw.line([(0, y), (width, y)], fill=grid_color, width=1)
        _draw_label(draw, font, y, str(y), False)
        last_y = y
    _draw_marks(draw, marks)

    if save:
        img.save(output_path)
    
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
    position,
    label,
    is_x_axis
):
    bbox = draw.textbbox((0, 0), label, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    if is_x_axis:
        # X coordinate label at top
        draw.rectangle(
            [position - text_width // 2 - 2, 2, position + text_width // 2 + 2, text_height + 4],
            fill=(255, 255, 255)
        )
        draw.text((position - text_width // 2, 2), label, fill=(0, 0, 0), font=font)
    else:
        # Y coordinate label at left
        draw.rectangle(
            [2, position - text_height // 2 - 2, text_width + 4, position + text_height // 2 + 2],
            fill=(255, 255, 255)
        )
        draw.text((2, position - text_height // 2), label, fill=(0, 0, 0), font=font)

def _draw_marks(draw, marks):
    if marks is not None:
        for mark_x, mark_y in marks:
            # Draw a red circle at the marked coordinate
            mark_radius = 10
            draw.ellipse(
                [(mark_x - mark_radius, mark_y - mark_radius),
                 (mark_x + mark_radius, mark_y + mark_radius)],
                fill=(255, 0, 0, 128),  # Red, semi-transparent
                outline=(255, 0, 0) # Red outline
            )
