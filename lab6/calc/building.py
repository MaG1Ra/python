def calculate_building(length, width, height, rooms, floors):
    area = length * width * rooms * floors * 3
    volume = area * height
    heat_power = (volume * 30 * 3) / 3.6
    return area, heat_power
