$outputDir = "C:\Users\s.jaubert\OneDrive - CFAI Centre\IA\Cours\Activités\A0_organisation_documents\incoming"

# Create the directory if it doesn't exist
if (-not (Test-Path -Path $outputDir -PathType Container)) {
    New-Item -Path $outputDir -ItemType Directory -Force
}

1..50 | ForEach-Object {
    $year = Get-Random -Minimum 2020 -Maximum 2025
    $month = Get-Random -Minimum 1 -Maximum 13 # Max is exclusive
    $day = Get-Random -Minimum 1 -Maximum 29 # Max is exclusive, so 1-28

    # Format the date components with leading zeros if necessary
    $monthStr = "{0:D2}" -f $month
    $dayStr = "{0:D2}" -f $day

    $randomString = -join ((65..90) + (97..122) | Get-Random -Count 8 | ForEach-Object {[char]$_})
    $fileName = "$year-$monthStr-$dayStr`_$randomString.pdf"
    $filePath = Join-Path -Path $outputDir -ChildPath $fileName

    # Create an empty file
    New-Item -Path $filePath -ItemType File
}

Write-Host "50 PDF files created in $outputDir"
