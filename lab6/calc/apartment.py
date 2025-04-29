def calculate_apartment(length, width, height, rooms):
    area = length * width * rooms
    volume = area * height
    heat_power = (volume * 30 * 3) / 3.6
    return area, heat_power
