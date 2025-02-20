# pip install pynvml

import pynvml
from pprint import pprint


def get_gpu_info():
    pynvml.nvmlInit()
    results = {}

    try:
        device_count = pynvml.nvmlDeviceGetCount()

        for i in range(device_count):
            results[i] = {}
            handle = pynvml.nvmlDeviceGetHandleByIndex(i)

            name = pynvml.nvmlDeviceGetName(handle)
            results[i]["name"] = name

            memory_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
            results[i]["memory_total"] = memory_info.total / 1024**2
            results[i]["memory_used"] = memory_info.used / 1024**2
            results[i]["memory_free"] = memory_info.free / 1024**2

            utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)
            results[i]["utilization_gpu"] = utilization.gpu / 100
            results[i]["utilization_memory"] = utilization.memory / 100

            temperature = pynvml.nvmlDeviceGetTemperature(
                handle, pynvml.NVML_TEMPERATURE_GPU
            )
            results[i]["temperature"] = temperature

            try:
                fan_speed = pynvml.nvmlDeviceGetFanSpeed(handle)
                results[i]["fan_speed"] = fan_speed
            except pynvml.NVMLError_NotSupported:
                print("  Fan Speed: Not Supported")

            power_usage = pynvml.nvmlDeviceGetPowerUsage(handle)
            results[i]["power_usage"] = power_usage

            power_limit = pynvml.nvmlDeviceGetPowerManagementLimit(handle)
            results[i]["power_limit"] = power_limit  # in W

        return results

    finally:
        pynvml.nvmlShutdown()


pprint(get_gpu_info())
