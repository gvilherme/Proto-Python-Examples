import fisrt_msg_with_pkg_pb2 as fmwpkg_pb2

sample_message = fmwpkg_pb2.Person()

sample_message.age = 10
sample_message.first_name = "Gui"
sample_message.last_name = "Rod"
sample_message.is_verified = True
sample_message.height = 7.2

sample_message.phone_numbers.append("(11) 95973-1135")

with open("ptb.bin", 'wb') as f:
    ptb = sample_message.SerializeToString()
    f.write(ptb)
    f.close()

with open("ptb.bin", 'rb') as f:
    simple_message_read = fmwpkg_pb2.Person.FromString(f.read())
    print("DEU?")

print(simple_message_read)