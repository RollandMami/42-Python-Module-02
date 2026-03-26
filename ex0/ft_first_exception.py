# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_first_exception.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mamiandr <mamiandr@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/25 11:46:58 by mamiandr          #+#    #+#              #
#    Updated: 2026/03/25 11:46:58 by mamiandr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
	try:
		temp = int(temp_str)
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
    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature()