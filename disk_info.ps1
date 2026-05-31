$c_free = 0
$x_free = 0
try {
    $c = Get-PSDrive C -ErrorAction Stop
    $c_free = [math]::Round($c.Free / 1GB, 1)
} catch {}

try {
    $x = Get-PSDrive X -ErrorAction Stop
    $x_free = [math]::Round($x.Free / 1GB, 1)
} catch {}

@{c=$c_free; x=$x_free} | ConvertTo-Json -Compress
