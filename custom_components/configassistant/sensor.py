"""Platform for sensor integration."""
from __future__ import annotations

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import StateType

from .const import DOMAIN

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    async_add_entities([ExampleSensor(config_entry.data["name"])])

class ExampleSensor(SensorEntity):
    """Representation of a Sensor."""

    def __init__(self, name: str) -> None:
        """Initialize the sensor."""
        self._attr_name = name
        self._attr_unique_id = f"{name}_sensor"
        self._attr_native_value = None

    async def async_update(self) -> None:
        """Fetch new state data for the sensor."""
        # TODO: Implement actual sensor data fetching
        self._attr_native_value = "Example Value"
