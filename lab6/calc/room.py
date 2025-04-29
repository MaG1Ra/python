def calculate_room(length, width, height):
    area = length * width
    volume = area * height
    heat_power = (volume * 30 * 3) / 3.6
    return area, heat_power
