BEGIN {
    FS = ","
}

{
    if ($11 != "") print $11
    if ($12 != "") print $12
    if ($13 != "") print $13
}