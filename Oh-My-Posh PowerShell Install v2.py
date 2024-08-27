import subprocess

print("\033[33m!\033[0m You can see all themes at \033[34mhttps://ohmyposh.dev/docs/themes\033[0m.")
themeFirst = input("\033[34m?\033[0m Enter the name of the theme: ")

commandFirst = "$PSVersionTable.PSEdition"
commandSecond = f"""Set-ExecutionPolicy Bypass -Scope Process -Force; Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://ohmyposh.dev/install.ps1'))
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/JanDeDobbeleer/oh-my-posh/main/themes/{themeFirst}.omp.json" -OutFile "$env:USERPROFILE\\{themeFirst}.omp.json"
Add-Content -Path $PROFILE -Value "oh-my-posh init pwsh --config '$env:USERPROFILE\\{themeFirst}.omp.json' | Invoke-Expression"
. $PROFILE"""

resultFirst = subprocess.run(
    ["powershell", "-Command", commandFirst], text=True, capture_output=True)

if resultFirst.stdout.strip() == "Desktop":
    resultSecond = subprocess.run(
        ["powershell", "-Command", commandSecond], text=True, capture_output=True)
    print(resultSecond.stdout.strip())
elif resultFirst.stdout.strip() == "Core":
    resultSecond = subprocess.run(
        ["pwsh", "-Command", commandSecond], text=True, capture_output=True)
    print(resultSecond.stdout.strip())
