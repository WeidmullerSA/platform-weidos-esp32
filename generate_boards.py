"""
Copyright (c) 2023 Boot&Work Corp., S.L. All rights reserved

This file is part of platform-industrialshields-esp32.

platform-weidos-esp32 is free software: you can redistribute
it and/or modify it under the terms of the GNU General Public License
as published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

platform-weidos-esp32 is distributed in the hope that it will
be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.


PLC Configuration Generator

This script generates all the configuration files that PlatformIO
needs for all theWeidmuller PLCs based on ESP32 boards.
"""
from json_generator import JSON_PLC
import os
from itertools import chain



SCRIPT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
BOARDS_DIRECTORY = os.path.join(SCRIPT_DIRECTORY, "boards/")


esp32_basejson = """
{
  "build": {
    "arduino":{
      "ldscript": "esp32_out.ld"
    },
    "core": "weidmuller",
    "extra_flags": "",
    "f_cpu": "240000000L",
    "f_flash": "40000000L",
    "flash_mode": "dio",
    "mcu": "esp32",
    "variant": ""
  },
  "connectivity": [
    "wifi",
    "bluetooth",
    "ethernet"
  ],
  "frameworks": [
    "arduino"
  ],
  "name": "",
  "upload": {
    "flash_size": "4MB",
    "maximum_ram_size": 327680,
    "maximum_size": 1310720,
    "require_upload_port": true,
    "speed": 460800
  },
  "url": "",
  "vendor": "Weidmuller"
}
"""



def E(file_name: str, name: str, variant: str, extra_flags: str, url: str) \
        -> JSON_PLC:
    """
    Create a JSON_PLC instance for ESP32 based PLCs.
    """
    return JSON_PLC(file_name, name, variant, extra_flags, url, esp32_basejson)

    
esp32plcs = [E("weidos_esp32_a1", "WEIDOS-ESP32-A1","-DESP32", "https://www.weidmuller.es/es/ventas/application_iot_centre/weidos_devices/index.jsp"),
             E("weidos_esp32_lora_a1", "WEIDOS-ESP32-LORA-A1","-DESP32 -DWEIDOS_LORA", "https://www.weidmuller.es/es/ventas/application_iot_centre/weidos_devices/index.jsp"),
             E("weidos_esp32_nbiot_a1","WEIDOS-ESP32-NBIOT-A1","-DESP32 -DWEIDOS_NBIOT", "https://www.weidmuller.es/es/ventas/application_iot_centre/weidos_devices/index.jsp")]


for plc in chain(esp32plcs):
    plc.generate_file(BOARDS_DIRECTORY)
