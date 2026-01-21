JOULES_PER_KCAL = 4184
JOULES_PER_WH = 3600


def compare_energy(calories_burned, watt_hours_used):
    """
    Compare l'energie depensee lors d'un exercice physique
    a l'energie consommee par des appareils.

    :param calories_burned: energie brulee en kilocalories
    :param watt_hours_used: energie consommee en watt-heures
    :return: 'Workout', 'Devices' ou 'Equal'
    """
    joules_burned = calories_burned * JOULES_PER_KCAL
    joules_used = watt_hours_used * JOULES_PER_WH

    if joules_burned > joules_used:
        return "Workout"
    if joules_burned < joules_used:
        return "Devices"
    return "Equal"


if __name__ == "__main__":
    print(compare_energy(250, 50)) # should return "Workout"
    print(compare_energy(100, 200)) # should return "Devices"
    print(compare_energy(450, 523)) # should return "Equal"
    print(compare_energy(300, 75)) # should return "Workout"
    print(compare_energy(200, 250)) # should return "Devices"
    print(compare_energy(900, 1046)) # should return "Equal"