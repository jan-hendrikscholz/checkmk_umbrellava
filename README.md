# checkmk_umbrellava
CheckMK 2.0 plugin for Cisco Umbrella virtual appliance specific services

# Installation

## For CheckMK Raw Edition users (mkp):
  1. Download the mkp file either from the release section, or [CheckMK Exchange](https://exchange.checkmk.com/p/umbrellava).
  2. Transfer the file to /omd/sites/<YOURSITE>/share/check_mk/optional_packages/ .
  3. Log on as site user `omd su <YOURSITE>` 
  4. Perform the installation via `mkp install ~/share/check_mk/optional_packages/<PACKAGENAME>.mkp`
  
## For CheckMK Enterprise Edition users (mkp):
  1. Download the mkp file either from the release section, or [CheckMK Exchange](https://exchange.checkmk.com/p/umbrellava).
  2. Logon to your instance. Make sure you have permissions to install mkp's.
  3. Navigate to Setup --> Maintenance --> Extension packages
  4. Click on "Upload package" and select the mkp.
  5. Make sure the plugin is enabled, if not, press the green tickmark.
  6. Activate your changes.
  
## Manual installation
  1. Download the individual files, or use `git clone https://github.com/jan-hendrikscholz/checkmk_umbrellava.git` to bring them to your CheckMK server
  2. Copy all files (or the checks you need) to `/opt/omd/sites/<YOURSITE>/local/lib/check_mk/base/plugins/agent_based/`
  
# Usage
After the installation is done, rediscover your Umbrella virtual appliances. Make sure, you have SNMP enabled and the community is correct.
