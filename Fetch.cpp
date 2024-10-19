#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <direct.h>

int main() {
    // Define the path
    char path[] = "C:\\Users\\Rakshit\\Desktop";

    // Change the current working directory to the specified path
    _chdir(path);

    // Open a file for writing
    FILE *file = fopen("C:\\Users\\Rakshit\\Desktop\\fetch1st.txt", "w");

    if (file == NULL) {
        perror("Error opening file");
        return -1;
    }

    // Execute the command and redirect output to the file
    FILE *commandOutput = _popen("powershell.exe -Command \"cd .; Get-Process | Select-Object -Property NPM, PM, WS, Id, ProcessName\"", "r");

    if (commandOutput == NULL) {
        perror("Error executing command");
        return -1;
    }

    char buffer[256];
    while (fgets(buffer, sizeof(buffer), commandOutput) != NULL) {
        fprintf(file, "%s", buffer);
    }

    // Close the file and command output
    fclose(file);
    _pclose(commandOutput);
    

    // Open a new file for writing to store CMD command output
    FILE *cmdOutputFile = fopen("C:\\Users\\Rakshit\\Desktop\\cmd_output.txt", "w");

    if (cmdOutputFile == NULL) {
        perror("Error opening CMD output file");
        return -1;
    }

    // Execute the CMD command and redirect output to the new file
    FILE *cmdOutput = _popen("cmd.exe /c wmic process get Caption,ProcessId,Priority", "r");

    if (cmdOutput == NULL) {
        perror("Error executing CMD command");
        return -1;
    }

    while (fgets(buffer, sizeof(buffer), cmdOutput) != NULL) {
        fprintf(cmdOutputFile, "%s", buffer);
    }

    // Close the CMD output file and command output
    fclose(cmdOutputFile);
    _pclose(cmdOutput);

    return 0;
}

