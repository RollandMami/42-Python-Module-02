# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_different_errors.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mamiandr <mamiandr@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/07 15:16:04 by mamiandr          #+#    #+#              #
#    Updated: 2026/04/07 15:16:10 by mamiandr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def garden_operations(operation_number: str) -> None:
	try:
		if operation_number == 0:
			int("abc")
		elif operation_number == 1:
			result = 2 / 0
		elif operation_number == 2:
			with open("/non/existent/file", "r") as f:
				content = f.read()
		elif operation_number == 3:
			result = 'str' + 2
		elif operation_number == 4:
			result = 3 + 3
	except ValueError as e:
		print(f"Caught ValueError: {e}")
		return None
	except ZeroDivisionError as e:
		print(f"Caught ZeroDivisionError: {e}")
		return None
	except FileNotFoundError as e:
		print(f"Caught FileNotFoundError: {e}")
		return None
	except TypeError as e:
		print(f"Caught TypeError: {e}")
		return None
	except Exception as e:
		print(f"zzz: {e}")
		return None
	else:
		print("Operation completed successfully\n")

def test_error_types() -> None:
	print("=== Garden Error Types Demo ===\n")
	i = 0
	while i < 5:
		print(f"Testing operation {i}...")
		garden_operations(i)
		i += 1
	print("All tests completed - program didn't crash!")

if __name__ == "__main__":
	test_error_types()
