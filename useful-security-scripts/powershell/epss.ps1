########################################################
### The following script uses the EPSS API to get    ###
### the EPSS Score and then output it with a         ###
### corresponding Color.                             ###
########################################################

function Fetch-EpssData {
    param (
        [Parameter(Mandatory=$true)]
        [string]$CVE,

        [Parameter(Mandatory=$true)]
        [string]$Date
    )

    # Construct the API URL
    $url = "https://api.first.org/data/v1/epss?envelope=true&pretty=true&cve=$CVE&date=$Date"

    try {
        # Send the HTTP GET request
        $response = Invoke-RestMethod -Uri $url -Method Get

        # Extract and process EPSS and Percentile values
        if ($response -and $response.data.Count -gt 0) {
            $epss = [float]$response.data[0].epss * 100
            $percentile = [float]$response.data[0].percentile * 100

            Write-Host "`nEPSS: $([math]::Round($epss, 2))%" -ForegroundColor Green
            Print-WithColor $percentile
        } else {
            Write-Host "No data available for the given CVE and date." -ForegroundColor Yellow
        }
    } catch {
        # Handle errors
        Write-Host "Error: $($_.Exception.Message)" -ForegroundColor Red
    }
}

function Print-WithColor {
    param (
        [Parameter(Mandatory=$true)]
        [float]$Percentile
    )

    # Print Percentile with color based on its value
    if ($Percentile -ge 0 -and $Percentile -lt 30) {
        Write-Host "Percentile: $([math]::Round($Percentile, 2))%" -ForegroundColor Green
    } elseif ($Percentile -ge 30 -and $Percentile -lt 75) {
        Write-Host "Percentile: $([math]::Round($Percentile, 2))%" -ForegroundColor Yellow
    } elseif ($Percentile -ge 75) {
        Write-Host "Percentile: $([math]::Round($Percentile, 2))%" -ForegroundColor Red -NoNewline
        Write-Host " (High Risk)" -ForegroundColor Red -BackgroundColor White
    }
}

# Prompt the user for input
$CVE = Read-Host "Enter the CVE (e.g., CVE-2022-26332)"
$Date = Read-Host "Enter the date (YYYY-MM-DD)"

# Fetch and display the data
Fetch-EpssData -CVE $CVE -Date $Date
