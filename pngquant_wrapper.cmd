@ECHO OFF
REM Run pngquant from image %2 and output it to %1

start pngquant -o %1 -- %2