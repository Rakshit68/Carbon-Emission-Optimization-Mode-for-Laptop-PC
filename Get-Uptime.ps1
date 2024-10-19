Get-Process |
    Where-Object { $_.StartTime -ne $null } |
    Sort-Object -Property Name |
    Get-Unique -AsString |
    Select-Object Name, @{Name="RunningTime"; Expression={(Get-Date) - $_.StartTime}} |
    ForEach-Object {
        $_.Name + " - " + [string]::Format("{0:D2}:{1:D2}:{2:D2}", $_.RunningTime.Hours, $_.RunningTime.Minutes, $_.RunningTime.Seconds)
    } |
    Out-File -FilePath "C:\Users\Rakshit\Desktop\ProcessUptime.txt"