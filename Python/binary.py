#convert a number to binary
"""
user_string = input("Enter a number to convert to binary\n")
user_number = int(user_string)

converted_number = bin(user_number)

print(converted_number)
"""

#convert an IP address to binary
user_ip_string = input("Enter an IP address\n")
user_ip_octets = user_ip_string.split(".")

first_octet = int(user_ip_octets[0])
second_octet = int(user_ip_octets[1])
third_octet = int(user_ip_octets[2])
fourth_octet = int(user_ip_octets[3])

first_octect_binary = bin(first_octet)
second_octect_binary = bin(second_octet)
third_octect_binary = bin(third_octet)
fourth_octect_binary = bin(fourth_octet)

print(f"{first_octect_binary}.{second_octect_binary}.{third_octect_binary}.{fourth_octect_binary}")


