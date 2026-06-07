@echo off
chcp 65001 >nul
title 消消乐 - 本地服务器
cd /d "%~dp0"

echo.
echo   ╔════════════════════════╗
echo   ║   消消乐 Match-3      ║
echo   ╚════════════════════════╝
echo.
echo   服务器启动中...
echo   游戏地址: http://127.0.0.1:8000
echo.
echo   关闭本窗口即可停止服务器
echo.

start "" http://127.0.0.1:8000

"C:\Users\qsj\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" -m uvicorn main:app --host 0.0.0.0 --port 8000

echo.
echo 服务器已停止
pause
