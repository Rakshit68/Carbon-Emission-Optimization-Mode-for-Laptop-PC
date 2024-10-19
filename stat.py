import psutil
from datetime import datetime
import csv

def get_power_consumption():
    battery = psutil.sensors_battery()
    return battery.power_plugged, battery.percent if battery else None

def calculate_average_running_hours():
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    now = datetime.now()
    uptime = now - boot_time
    return uptime.total_seconds() / 3600

def calculate_annual_power_consumption():
    power_plugged, battery_percent = get_power_consumption()

    if battery_percent is None:
        return None

    # Assuming average consumption is 20W (you can adjust this based on your specific system)
    average_consumption = 20  # in watts

    # Calculate hours since last boot
    running_hours = calculate_average_running_hours()

    # Calculate days in a year
    days_in_year = 365.25  # accounting for leap years

    # Calculate total power consumption in kWh
    total_power_consumption = (running_hours * average_consumption * days_in_year) / 1000  # convert to kWh
    return total_power_consumption

def main():
    power_plugged, battery_percent = get_power_consumption()

    # Write system information to a text file
    with open(r"C:\Users\Rakshit\Desktop\system_info.txt", "w") as file:
        file.write(f"Power Source: {'Plugged In' if power_plugged else 'Battery'}\n")
        if battery_percent is not None:
            file.write(f"Battery Percentage: {battery_percent}%\n")

        file.write(f"Average Running Hours: {calculate_average_running_hours():.2f} hours\n")

        total_annual_power_consumption = calculate_annual_power_consumption()
        if total_annual_power_consumption is not None:
            file.write(f"Total Annual Power Consumption: {total_annual_power_consumption:.2f} kWh\n")
        else:
            file.write("Unable to determine power consumption.\n")

if __name__ == "__main__":
    main()
