# PowerShell Script to Query Shodan CVE Database and Output Relevant Information with Color-Coded EPSS

# Prompt the user to input the CVE identifier
$CVE = Read-Host "Enter the CVE identifier (e.g., CVE-2023-12345)"

# Check if the input is empty or null
if ([string]::IsNullOrWhiteSpace($CVE)) {
    Write-Error "No CVE identifier provided. Please run the script again and provide a valid CVE."
    exit
}

# Construct the URL using the provided CVE identifier
$BaseUrl = "https://cvedb.shodan.io/cve"
$Url = "$BaseUrl/$CVE"

try {
    # Send a GET request to the URL
    $Response = Invoke-RestMethod -Uri $Url -Method Get

    # Calculate EPSS and Ranking EPSS as percentages
    $EPSSPercentage = [math]::Round($Response.epss * 100, 2)
    $RankingEPSSPercentage = [math]::Round($Response.ranking_epss * 100, 2)

    # Define a helper function for color output
    function Write-ColorOutput {
        param (
            [string]$Text,
            [float]$Value
        )
        if ($Value -le 30) {
            Write-Host $Text -ForegroundColor Green
        } elseif ($Value -le 69) {
            Write-Host $Text -ForegroundColor Yellow
        } else {
            Write-Host $Text -ForegroundColor Red
        }
    }

    # Output specific fields in a readable format with color-coded EPSS
    Write-Host "Response for CVE: $CVE" -ForegroundColor Cyan
    Write-Host "=============================" -ForegroundColor Cyan
    Write-Host "CVE ID: $($Response.cve_id)" -ForegroundColor White
    Write-Host "Summary: $($Response.summary)" -ForegroundColor White
    Write-Host "CVSS Version: $($Response.cvss_version)" -ForegroundColor DarkBlue
    Write-Host "CVSS v2: $($Response.cvss_v2)" -ForegroundColor DarkBlue
    Write-Host "CVSS v3: $($Response.cvss_v3)" -ForegroundColor DarkBlue
    Write-ColorOutput "EPSS: $EPSSPercentage%" $EPSSPercentage
    Write-ColorOutput "Ranking EPSS: $RankingEPSSPercentage%" $RankingEPSSPercentage
    Write-Host "References:" -ForegroundColor White
    $Response.references | ForEach-Object { Write-Host "- $_" -ForegroundColor Gray }
    Write-Host "Published Time: $($Response.published_time)" -ForegroundColor White
    Write-Host "=============================" -ForegroundColor Cyan
} catch {
    # Handle errors and provide feedback
    Write-Error "Failed to retrieve data for CVE: $CVE. Please check the CVE identifier and try again."
    Write-Error $_.Exception.Message
}
