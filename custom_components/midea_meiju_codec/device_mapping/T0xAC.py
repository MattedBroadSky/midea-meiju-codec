from homeassistant.const import *
from homeassistant.components.sensor import SensorStateClass, SensorDeviceClass
from homeassistant.components.switch import SwitchDeviceClass

DEVICE_MAPPING = {
    "default": {
        "manufacturer": "美的",
        "rationale": ["off", "on"],
        "queries": [{}, {"query_type": "prevent_straight_wind"}],
        "centralized": ["power", "temperature", "small_temperature", "mode", "eco", "comfort_power_save",
                        "comfort_sleep", "strong_wind", "wind_swing_lr", "wind_swing_lr", "wind_speed",
                        "ptc", "dry"],
        "entities": {
            Platform.CLIMATE: {
                "thermostat": {
                    "name": "Thermostat",
                    "power": "power",
                    "hvac_modes": {
                        "off": {"power": "off"},
                        "heat": {"power": "on", "mode": "heat"},
                        "cool": {"power": "on", "mode": "cool"},
                        "auto": {"power": "on", "mode": "auto"},
                        "dry": {"power": "on", "mode": "dry"},
                        "fan_only": {"power": "on", "mode": "fan"}
                    },
                    "preset_modes": {
                        "none": {
                            "eco": "off",
                            "comfort_power_save": "off",
                            "comfort_sleep": "off",
                            "strong_wind": "off"
                        },
                        "eco": {"eco": "on"},
                        "comfort": {"comfort_power_save": "on"},
                        "sleep": {"comfort_sleep": "on"},
                        "boost": {"strong_wind": "on"}
                    },
                    "swing_modes": {
                        "off": {"wind_swing_lr": "off", "wind_swing_ud": "off"},
                        "both": {"wind_swing_lr": "on", "wind_swing_ud": "on"},
                        "horizontal": {"wind_swing_lr": "on", "wind_swing_ud": "off"},
                        "vertical": {"wind_swing_lr": "off", "wind_swing_ud": "on"},
                    },
                    "fan_modes": {
                        "silent": {"wind_speed": 20},
                        "low": {"wind_speed": 40},
                        "medium": {"wind_speed": 60},
                        "high": {"wind_speed": 80},
                        "full": {"wind_speed": 100},
                        "auto": {"wind_speed": 102}
                    },
                    "target_temperature": ["temperature", "small_temperature"],
                    "current_temperature": "indoor_temperature",
                    "aux_heat": "ptc",
                    "min_temp": 17,
                    "max_temp": 30,
                    "temperature_unit": TEMP_CELSIUS,
                    "precision": PRECISION_HALVES,
                }
            },
            Platform.SWITCH: {
                "dry": {
                    "name": "Dry",
                    "device_class": SwitchDeviceClass.SWITCH,
                },
                "prevent_straight_wind": {
                    "name": "防直吹",
                    "device_class": SwitchDeviceClass.SWITCH,
                    "rationale": [1, 2]
                }
            },
            Platform.SENSOR: {
                "indoor_temperature": {
                    "name": "室内温度",
                    "device_class": SensorDeviceClass.TEMPERATURE,
                    "unit_of_measurement": TEMP_CELSIUS,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "outdoor_temperature": {
                    "name": "室外机温度",
                    "device_class": SensorDeviceClass.TEMPERATURE,
                    "unit_of_measurement": TEMP_CELSIUS,
                    "state_class": SensorStateClass.MEASUREMENT
                },
            },
            Platform.BINARY_SENSOR: {
                "power": {}
            },
            Platform.SELECT: {
                "preset_modes": {
                    "options": {
                        "none": {
                            "eco": "off",
                            "comfort_power_save": "off",
                            "comfort_sleep": "off",
                            "strong_wind": "off"
                        },
                        "eco": {"eco": "on"},
                        "comfort": {"comfort_power_save": "on"},
                        "sleep": {"comfort_sleep": "on"},
                        "boost": {"strong_wind": "on"}
                    }
                },
                "hvac_modes": {
                    "options": {
                        "off": {"power": "off"},
                        "heat": {"power": "on", "mode": "heat"},
                        "cool": {"power": "on", "mode": "cool"},
                        "auto": {"power": "on", "mode": "auto"},
                        "dry": {"power": "on", "mode": "dry"},
                        "fan_only": {"power": "on", "mode": "fan"}
                    }
                }
            },
            Platform.WATER_HEATER:{
                "water_heater": {
                    "name": "热水器",
                    "power": "power",
                    "operation_list": {
                        "off": {"power": "off"},
                        "heat": {"power": "on", "mode": "heat"},
                        "cool": {"power": "on", "mode": "cool"},
                        "auto": {"power": "on", "mode": "auto"},
                        "dry": {"power": "on", "mode": "dry"},
                        "fan_only": {"power": "on", "mode": "fan"}
                    },
                    "target_temperature": ["temperature", "small_temperature"],
                    "current_temperature": "indoor_temperature",
                    "min_temp": 17,
                    "max_temp": 30,
                    "temperature_unit": TEMP_CELSIUS,
                    "precision": PRECISION_HALVES,
                }
            },
            Platform.FAN: {
                "fan": {
                    "power": "power",
                    "preset_modes": {
                        "off": {"power": "off"},
                        "heat": {"power": "on", "mode": "heat"},
                        "cool": {"power": "on", "mode": "cool"},
                        "auto": {"power": "on", "mode": "auto"},
                        "dry": {"power": "on", "mode": "dry"},
                        "fan_only": {"power": "on", "mode": "fan"}
                    },
                    "oscillate": "wind_swing_lr",
                    "speeds": list({"wind_speed": value + 1} for value in range(0, 100)),
                }
            }
        }
    }
}