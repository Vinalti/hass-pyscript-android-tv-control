"""
@Author: github.com/Vinalti
@Date: 2023-01-15
@Links: github.com/Vinalti/hass-pyscript-android-tv-control
"""

@service
def androidtv_command(device, command):
    """yaml
name: Send ADB Command to Android TV
description: Send command to Android TV via ADB using Home Assistant's 'Android TV' Integration.
fields:
  device:
    name: device
    description: Target Android-TV Device (from android-tv integration)
    example: media_player.android_tv_192_168_1_42
    default:
    required: true
    selector:
      entity:
        domain: media_player

  command:
    name: command
    description: command to send via adb
    example: POWER
    default:
    required: true
    selector:
      select:
        mode: dropdown
        options:
          - HOME
          - POWER
          - SLEEP
          - WAKEUP
          - VOLUME_UP
          - VOLUME_DOWN
          - MUTE
          - UP
          - DOWN
          - LEFT
          - RIGHT
          - CENTER
          - ENTER
          - BACK
          - ESCAPE
          - MENU
          - SEARCH
          - SETTINGS
          - FAST_FORWARD
          - REWIND
          - RESUME
          - END
          - INPUT
          - VGA
          - HDMI1
          - HDMI2
          - MOVE_HOME
          - PAIRING
          - SUSPEND
          - SYSDOWN
          - SYSLEFT
          - SYSRIGHT
          - SYSUP
          - TEXT
          - TOP
    """
    service.call("androidtv", "adb_command", entity_id=device, command=command)
