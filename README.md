[![License][licensing-shield]](LICENSE)

# Home Assistant Android TV Controls
Uses the Android-TV integration to send predefined commands to it via adb.

For more info [click here][android-tv-hass-adb]

- [Requirements](#requirements)
- [Installation](#installation)
- [How To Use](#how-to-use)
    - [Send ADB Command to Android TV](#send-adb-command-to-android-tv)
- [Work in Progress](#work-in-progress)
- [Changelog](#changelog)

## Requirements

- [Android TV Integration](https://www.home-assistant.io/integrations/androidtv/)
- HACS ([docs][hacs-docs])
    - PyScript Integration ([docs][pyscript-docs])
      
## Installation
### Procedure
1. **Clone this repository in your `config/deps/` directory**
   ```sh
   cd config/deps
   git clone https://github.com/Vinalti/hass-pyscript-android-tv-control.git
   ```
2. **Add `android-tv-adb` in your `pyscript/config.yaml`**
   ```yaml
   # config/configuration.yaml
   pyscript: 
     apps:
       # (...)
       android-tv-adb:
   ```
3. **Link the files in the `pyscript` directory**
   ```sh
   # use `mkdir -p /config/pyscript/apps/` if the directory doesn't exist
   cd /config/pyscript/apps/
   
   # Create a symbolic link to the apps directory named `android-tv-adb`
   ln -s ../../deps/hass-pyscript-android-tv-control/android-tv-adb
   ```
   
### Updating
In order to update the script to a newer version:
```sh
cd deps/hass-pyscript-android-tv-control/
git pull
```
If you made manual modifications to the file you will need to undo them before pulling.
Report to  `git` documentation for more information.

> ⚠️ **See changelog before updating.**  
> The project is still in developpement and breaking changes may occurs.

### Installation Notes
- A symbolic link is symbolic and represent the exact path you enter, if you move the targeted file or if the target is 
  outside of the container (e.g. when using docker) the link will not work. Make sure that you are using a relative path
  that is accessible for the host reading the link. 
- Ensure that `pyscript` is operational before to install this script.

## How To Use
This script provides the following services in Home Assisant.
You can call it from the `Developer Tools` for testing, or directly inside your scripts and automations.

> Please note that updating the script may breaks backward compatibility.

### Summary
- [Send ADB Command to Android TV (`pyscript.androidtv_command`)](#send-adb-command-to-android-tv)

### 🔸Send ADB Command to Android TV
`pyscript.androidtv_command`

_Send a command to Android TV. Commands available via a dropdown list._

**Parameters:**
- **`device`** (_entity:media_player_)  
    The device to control with the command. That must be a androidtv ADB device, not just a chromecast casting device.

- **`command`** (_dropdown_)  
    The command to send to the device. Choose among the list. Not all commands work with all devices, you can check
    the documentation of your device to see which commands are supported.
    To shorten the list, I didn't list all commands (such as color buttons or other special buttons) but the most
    important ones are there.


## Work in Progress
The script works fine but is still work in progress.

If you have any problem, remarks or suggestion feel free to open an issue.


## Changelog
### 2023.01.15 - v0.1.0
- **Add Service `androidtv_command`**  



[android-tv-hass-adb]: https://www.home-assistant.io/integrations/androidtv/#androidtvadb_command
[licensing-shield]: https://img.shields.io/github/license/Vinalti/hss-pyscript-android-tv-control?style=flat-square
[hacs-docs]: https://hacs.xyz/docs/setup/prerequisites
[pyscript-docs]: https://hacs-pyscript.readthedocs.io/en/latest/installation.html
