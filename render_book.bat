@echo off
cd /d "G:\My Drive\book drafts\antitrust"
echo Rendering Quarto book...
quarto render --to html
echo.
echo Done! Press any key to close.
pause
