import csv

# Create an empty list to store elements from the first column
elements_list = []

# Create a dictionary to store elements from the first column as keys, and values from the 4th and 5th columns as values
elements_dict = {}

# Read the CSV file and extract elements from the first, 4th, and 5th columns
with open(r"C:\Users\Rakshit\Desktop\FinalOutput.csv", 'r') as file:
    csv_reader = csv.reader(file)
    for i, row in enumerate(csv_reader):
        if i > 0 and len(row) >= 5:
            element = row[0]
            power_usage = row[3]
            priority = row[4]
            
            # Remove '.exe' suffix if present
            if element.lower().endswith('.exe'):
                element = element[:-4]
            
            elements_list.append(element)
            
            # Store the 4th and 5th column values in the dictionary
            elements_dict[element] = (power_usage, priority)

sys_list = ['svchost', 'System Idle Process', 'System', 'smss', 'wininit', 'services', 'lsass', 'winlogon',
            'csrss', 'explorer', 'dwm', 'spoolsv', 'lsass', 'winlogon', 'smss', 'ACCStd', 'AMDRSServ',
            'ApplicationFrameHost', 'cmd', 'conhost', 'ctfmon', 'dllhost', 'ePowerButton_NB', 'explorer',
            'HostAppServiceUpdater', 'LocationNotificationWindows', 'nvcontainer', 'NVIDIA Web Helper',
            'nvsphelper64', 'PSAgent', 'QAAgent', 'RadeonSoftware', 'RtkAudUService64', 'RuntimeBroker',
            'SDXHelper', 'SearchHost', 'SecurityHealthSystray', 'ShellExperienceHost', 'sihost', 'smartscreen',
            'StartMenuExperienceHost', 'StorPSCTL', 'svchost', 'SystemSettings', 'taskhostw', 'UserOOBEBroker',
            'Widgets', 'WidgetService', 'WindowsTerminal', 'powershell', 'gamingservices', 'QAAdminAgent',
            'gamingservicesnet', 'timeout', 'Registry', 'WmiPrvSE', 'ACCSvc', 'atiesrxx', 'KillerNetworkService',
            'QASvc', 'AggregatorHost', 'KillerAnalyticsService', 'Memory Compression', 'NVDisplay.Container',
            'PSAdminAgent', 'DtsApo4Service', 'unsecapp', 'amdfendrsr', 'SgrmBroker', 'OpenConsole',
            'SecurityHealthService', 'SearchIndexer', 'SearchProtocolHost', 'atieclxx', 'MsMpEng', 'NisSrv',
            'fontdrvhost', 'gameinputsvc', 'sppsvc', 'xTendUtility', 'xTendUtilityService', 'OfficeClickToRun',
            'PSSvc', 'wlanext', 'SearchFilterHost', 'SystemSettingsBroker', 'msedgewebview2', 'mintty', 'LockApp',
            'ai', 'zWebview2Agent','splwow64','backgroundTaskHost','ConsolePauser']

set1 = set(elements_list)
set2 = set(sys_list)

# Find elements present in list1 but not in list2
elements_in_list1_not_in_list2 = list(set1 - set2)

# Create a list to store tuples of (element, carbon_emission)
element_carbon_emission_list = []

# Calculate carbon emission and store it in the list of tuples
for element in elements_in_list1_not_in_list2:
    power_usage, _ = elements_dict[element]
    # Calculate the value using the provided formula
    calculated_value = (float(power_usage) * 8 * 365 / 1000) * 0.33
    element_carbon_emission_list.append((element, calculated_value))

# Sort the list of tuples by carbon emission in descending order
element_carbon_emission_list.sort(key=lambda x: x[1], reverse=True)

# Create a new CSV file to export the data
output_file = r"C:\Users\Rakshit\Desktop\Final.csv"

# Write the data to the new CSV file
with open(output_file, 'w', newline='') as file:
    csv_writer = csv.writer(file)
    # Write the header row with the additional column
    csv_writer.writerow(["Applications", "Power usage", "Priority", "Carbon emission"])
    # Write the data rows with sorted values
    for element, carbon_emission in element_carbon_emission_list:
        power_usage, priority = elements_dict[element]
        csv_writer.writerow([element, power_usage, priority, carbon_emission])

print(f"Data exported to {output_file}")
