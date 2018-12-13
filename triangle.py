def hypotenuse(side_1, side_2):
    """Can determine hypotenuse of triangle if the two other sides are given"""
    hyp = (side_1**2 + side_2**2)**.5
    print(f"{hyp}")

hypotenuse(3,4)
