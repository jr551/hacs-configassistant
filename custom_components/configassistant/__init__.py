"""The Config Assistant integration."""
from __future__ import annotations

import os
import shutil
import logging
import voluptuous as vol

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
import homeassistant.helpers.config_validation as cv

from .panel import async_setup_panel

_LOGGER = logging.getLogger(__name__)

DOMAIN = "configassistant"
PLATFORMS: list[Platform] = [Platform.SENSOR]

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema({})
    }, 
    extra=vol.ALLOW_EXTRA
)

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the Config Assistant integration."""
    _LOGGER.info("Setting up Config Assistant integration")

    # Create www directory if it doesn't exist
    www_path = os.path.join(hass.config.path("www"), "config-assistant")
    os.makedirs(www_path, exist_ok=True)

    # Copy our www content
    component_path = os.path.dirname(__file__)
    www_source = os.path.join(component_path, "www")
    
    if os.path.exists(www_source):
        for item in os.listdir(www_source):
            source = os.path.join(www_source, item)
            dest = os.path.join(www_path, item)
            if os.path.isfile(source):
                shutil.copy2(source, dest)

    # Set up panel
    await async_setup_panel(hass)
    _LOGGER.info("Config Assistant panel setup complete")

    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Config Assistant from a config entry."""
    _LOGGER.info("Setting up Config Assistant entry")
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    _LOGGER.info("Unloading Config Assistant entry")
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
