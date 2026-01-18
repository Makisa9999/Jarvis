import pyaudio

p = pyaudio.PyAudio()

print("Available Input Microphone Devices...")
for i in range(p.get_device_count()):
    dev_info = p.get_device_info_by_index(i)
    print(f"{i}: {dev_info['name']}")
