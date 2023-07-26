"""
    Text Utils for drawing text on images
"""

def textShade(draw, text , x, y, font,color=(255,255,255), border_color=(40,40,40), shade=[1]) -> None:
    """  draw text with a shade or border """

    # Draw Shade to Draw border add [1,-1,0] to make it all sides 
    for x_offset in shade:
        for y_offset in shade:
            draw.text((x + x_offset, y + y_offset), text, font=font, fill=border_color)
    
    # Draw text on top of border
    draw.text((x, y), text, color, font=font)