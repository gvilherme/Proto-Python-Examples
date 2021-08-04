#Bible https://developers.google.com/protocol-buffers/docs/pythontutorial

import first_msg_with_pkg_pb2 as fmwpkg_pb2

sample_message = fmwpkg_pb2.Person()

sample_message.age = 10
sample_message.first_name = "Gui"
sample_message.last_name = "Rod"
sample_message.is_verified = True
sample_message.height = 7.2

#REPEATED examples
sample_message.phone_numbers.append("(11) 95973-1135")
sample_message.phone_numbers.extend(["(11) 95973-143134", "WHAT THE HECK"])
my_list = sample_message.phone_numbers
my_list.append("WOW")

#ENUM example
sample_message.certification = sample_message.practitioner

#Nested Message example
"""This example refers to the birthday attribute, that relies on a Message declared outside first-msg-with-pkg.proto, date.proto"""
sample_message.birthday.year = 2021
sample_message.birthday.month = 1
sample_message.birthday.day = 21 

#Repeated Nested Message examples
"""This example refers to the addresses attribute(s), that relies on a Message declared inside first-msg-with-pkg.proto"""
sample_message.addresses.add(address_line_1="idk", address_line_2="idek")
second_address = sample_message.addresses.add()
second_address.address_line_1="idk either"
second_address.address_line_2="neither me!"
"""And now explicity show that address is underlying Person"""
third_address = fmwpkg_pb2.Person.Address()
third_address.address_line_1="am I going nuts?"
third_address.address_line_2="Yes, I am"
sample_message.addresses.extend([third_address])

with open("ptb.bin", 'wb') as f:
    ptb = sample_message.SerializeToString()
    f.write(ptb)
    f.close()

with open("ptb.bin", 'rb') as f:
    simple_message_read = fmwpkg_pb2.Person.FromString(f.read())
    print("DEU?")

print(simple_message_read)