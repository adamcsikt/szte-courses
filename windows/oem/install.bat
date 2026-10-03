@echo off
setlocal enabledelayedexpansion

set LOG=C:\OEM\provision.log
echo [%date% %time%] Starting automated provisioning > "%LOG%"

:: --- Wait for network to be ready (defensive retry loop) ---
echo Waiting for network... >> "%LOG%"
set RETRIES=0
:waitnet
ping -n 1 8.8.8.8 >nul 2>&1
if errorlevel 1 (
    set /a RETRIES+=1
    if !RETRIES! GEQ 30 (
        echo Network not available after 30 tries, continuing anyway... >> "%LOG%"
        goto :afterwait
    )
    timeout /t 5 /nobreak >nul
    goto :waitnet
)
:afterwait
echo Network ready. >> "%LOG%"

:: --- WebView2 Runtime (required by Visual Studio's ServiceHub) ---
echo Installing WebView2 Runtime... >> "%LOG%"
powershell -NoProfile -ExecutionPolicy Bypass -Command "Invoke-WebRequest -Uri 'https://go.microsoft.com/fwlink/p/?LinkId=2124703' -OutFile '%TEMP%\webview2.exe'"
start /wait "" "%TEMP%\webview2.exe" /silent /install

:: --- Visual C++ Redistributable (required by ServiceHub) ---
echo Installing VC++ Redistributable... >> "%LOG%"
powershell -NoProfile -ExecutionPolicy Bypass -Command "Invoke-WebRequest -Uri 'https://aka.ms/vs/17/release/vc_redist.x64.exe' -OutFile '%TEMP%\vc_redist.x64.exe'"
start /wait "" "%TEMP%\vc_redist.x64.exe" /install /quiet /norestart

echo [%date% %time%] Provisioning finished >> "%LOG%"
endlocal
