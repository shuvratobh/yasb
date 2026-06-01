$icons = "C:\Users\shuvr\.config\yasb\icons"
New-Item -ItemType Directory -Force -Path $icons | Out-Null

# YouTube logo (high quality)
Invoke-WebRequest -Uri "https://www.google.com/s2/favicons?domain=youtube.com&sz=128" -OutFile "$icons\youtube.png"

# TorrentBD logo
Invoke-WebRequest -Uri "https://www.google.com/s2/favicons?domain=torrentbd.com&sz=128" -OutFile "$icons\torrentbd.png"

# Letterboxd logo
Invoke-WebRequest -Uri "https://www.google.com/s2/favicons?domain=letterboxd.com&sz=128" -OutFile "$icons\letterboxd.png"

Write-Host "All logos downloaded to $icons"
