function isIntegerHypotenuse(a, b) {
    hypothenuse = Math.sqrt(a**2 + b**2);
    return hypothenuse === Math.floor(hypothenuse);
}