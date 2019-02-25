# Readme

Fluxbox intermittenly fails. When you instantiate the remote browswer with '--start-maximized', chrome doesn't respect the resolution of the display set to 1920x1080 in this case.

```
docker-compose up -d

open vnc://:secret@localhost:5900

python test_selenium.py
```