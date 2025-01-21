########################################################
### The following script uses the EPSS API to get    ###
### the EPSS Score and then output it with a         ###
### corresponding Color.                             ###
########################################################

# Function to fetch EPSS data from the API
function Fetch-EpssData {
    param (
        [string]$CVE,
        [string]$Date
    )

    $url = "https://api.first.org/data/v1/epss?envelope=true&pretty=true&cve=$CVE&date=$Date"

    try {
        $response = Invoke-RestMethod -Uri $url -Method Get -ErrorAction Stop
        return $response
    } catch {
        return @{ error = $_.Exception.Message }
    }
}

# Function to determine the color for a percentile value
function Get-Color {
    param (
        [float]$Percentile
    )

    if ($Percentile -lt 30) {
        return "`e[32m" # Green
    } elseif ($Percentile -ge 30 -and $Percentile -lt 75) {
        return "`e[33m" # Yellow
    } else {
        return "`e[31m" # Red
    }
}

# Main script execution
$CVE = Read-Host "Enter the CVE (e.g., CVE-2022-26332)"
$Date = Read-Host "Enter the date (YYYY-MM-DD)"

# Fetch data from the API
$result = Fetch-EpssData -CVE $CVE -Date $Date

if ($result.error) {
    Write-Host "Error: $($result.error)" -ForegroundColor Red
} else {
    try {
        if (-not $result.data) {
            Write-Host "The CVE $CVE is not in the EPSS repository." -ForegroundColor Yellow
        } else {
            $data = $result.data[0]
            $epss = [math]::Round([float]$data.epss * 100, 2)
            $percentile = [math]::Round([float]$data.percentile * 100, 2)

            $color = Get-Color -Percentile $percentile
            $resetColor = "`e[0m"

            Write-Host "EPSS: $epss% (Chance of it being exploited in the next 30 days)"
            Write-Host "$color`Percentile: $percentile%$resetColor"
        }
    } catch {
        Write-Host "Error processing API response: $($_.Exception.Message)" -ForegroundColor Red
    }
}
