# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_finally_block.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mamiandr <mamiandr@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/08 17:02:21 by mamiandr          #+#    #+#              #
#    Updated: 2026/04/08 17:51:10 by mamiandr         ###   ########.fr        #
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


def water_plant(plant_name:str):
    if (plant_name != plant_name.capitalize()):
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system():
    print("=== Garden Watering System ===\n")
    try:
        print("Testing valid plants...")
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        return
    finally:
        print("Closing watering system\n")
    try:
        print("Testing invalid plants...")
        water_plant("Tomato")
        water_plant("lettuce")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system\n")

if __name__ == "__main__":
    try:
        test_watering_system()
    except:
        pass
    finally:
        print("Cleanup always happens, even with errors!")

