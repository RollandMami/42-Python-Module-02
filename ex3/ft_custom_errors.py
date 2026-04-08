# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_custom_errors.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mamiandr <mamiandr@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/07 15:22:51 by mamiandr          #+#    #+#              #
#    Updated: 2026/04/08 14:59:41 by mamiandr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GardenError(Exception):
    def __init__(self, message:str = "Unknown plant error"):
        self.message = message
        super().__init__(message)


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def test_custom_error():
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!\n")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!\n")
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        raise WaterError("Not enough water in the tank!\n")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_error()
