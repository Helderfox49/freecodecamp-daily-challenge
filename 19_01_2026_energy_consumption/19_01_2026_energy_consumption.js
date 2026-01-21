const JOULES_PER_KCAL = 4184;
const JOULES_PER_WH = 3600;

function compareEnergy(caloriesBurned, wattHoursUsed) {
    const joulesBurned = caloriesBurned * JOULES_PER_KCAL;
    const joulesUsed = wattHoursUsed * JOULES_PER_WH;

    if (joulesBurned > joulesUsed) {
        return "Workout";
    }
    if (joulesBurned < joulesUsed) {
        return "Devices";
    }
    return "Equal";
}

