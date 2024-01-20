Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\w32time\TimeProviders\NtpServer"
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\w32time\TimeProviders\NtpServer" -Name "Enabled" -Value 1
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\services\W32Time\Config" -Name "AnnounceFlags" -Value 5
Restart-Service w32Time
New-NetFirewallRule `  -Name "NTP Server Port" `  -DisplayName "NTP Server Port" `  -Description 'Allow NTP Server Port' `  -Profile Any `  -Direction Inbound `  -Action Allow `  -Protocol UDP `  -Program Any `  -LocalAddress Any `  -LocalPort 123