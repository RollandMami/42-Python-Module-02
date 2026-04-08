# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_raise_exception.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mamiandr <mamiandr@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/25 12:44:03 by mamiandr          #+#    #+#              #
#    Updated: 2026/04/07 15:15:42 by mamiandr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def input_temperature(temp_str: str) -> int:
	try:
		temp = int(temp_str)
		if temp > 40:
			raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
		elif temp < 0:
			raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
		return temp
	except Exception as e:
		print(f"Caught input_temperature error: {e}\n")
		return None

def test_temperature()-> None:
    print("=== Garden Temperature ===\n")
    input_data = '25'
    print(f"Input data is '{input_data}'")
    temperature: int = input_temperature(input_data)
    if temperature is not None:
        print(f"Temperature is now {temperature}°C\n")
    input_data = 'abc'
    print(f"Input data is '{input_data}'")
    temperature = input_temperature(input_data)
    if temperature is not None:
        print(f"Temperature is now {temperature}°C\n")
    input_data = 100
    print(f"Input data is '{input_data}'")
    temperature = input_temperature(input_data)
    if temperature is not None:
        print(f"Temperature is now {temperature}°C\n")
    input_data = -50
    print(f"Input data is '{input_data}'")
    temperature = input_temperature(input_data)
    if temperature is not None:
        print(f"Temperature is now {temperature}°C\n")
    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature()
