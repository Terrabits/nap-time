from lib.temperature import DS18B20Sensor, init_sensor

assert init_sensor()
sensor = DS18B20Sensor()

print(sensor.read_f())
