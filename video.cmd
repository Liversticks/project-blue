REM Run VLC and capture images in a specified directory

@ECHO OFF

start vlc %1 --video-filter=scene --start-time=%2 --stop-time=%3 --scene-ratio=240 --scene-path=%4 vlc://quit