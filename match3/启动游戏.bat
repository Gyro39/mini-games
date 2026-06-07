@echo off
chcp 65001 >nul
title 消消乐
cd /d "%~dp0"
start "" "%~dp0static\index.html"
