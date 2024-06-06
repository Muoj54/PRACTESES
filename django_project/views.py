from django.shortcuts import render

# Dummy data for devices
devices = [
    {"name": "Device 1", "specs": "Specs for Device 1"},
    {"name": "Device 2", "specs": "Specs for Device 2"},
    {"name": "Device 3", "specs": "Specs for Device 3"},
    {"name": "Device 4", "specs": "Specs for Device 4"},
]

def compare_devices(request):
    if request.method == 'POST':
        device1_name = request.POST.get('device1')
        device2_name = request.POST.get('device2')

        device1 = next((device for device in devices if device["name"] == device1_name), None)
        device2 = next((device for device in devices if device["name"] == device2_name), None)

        return render(request, 'templates/index.html', {
            'devices': devices,
            'device1': device1,
            'device2': device2
        })

    return render(request, 'templates/index.html', {'devices': devices})
