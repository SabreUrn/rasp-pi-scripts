import smbus

write_addr = 0x48
poten_addr = 0x03

bus = smbus.SMBus(1)

bus.write_byte(write_addr, poten_addr)
reading=read_byte(write_addr)
print reading
