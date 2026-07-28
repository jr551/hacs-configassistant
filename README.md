# Config Assistant

A [HACS](https://hacs.xyz/) custom integration for Home Assistant that adds a
**Config Assistant** panel to the sidebar, intended to help with Home
Assistant configuration (e.g. via ChatGPT-assisted suggestions).

> **Status: early / work in progress.** The integration installs and adds the
> sidebar panel, but the panel UI is currently a placeholder and the
> configuration-assistance logic is not implemented yet. Not recommended for
> production use.

## Features

- Installable via HACS as a custom integration
- Adds a "Config Assistant" panel to the Home Assistant sidebar
- Config flow based setup (no YAML required)

## Installation

### Via HACS (recommended)

1. In HACS, add this repository as a custom repository:
   `https://github.com/jr551/hacs-configassistant`
2. Install "Config Assistant" from HACS.
3. Restart Home Assistant.
4. Go to **Settings → Devices & Services → Add Integration** and search for
   "Config Assistant".

### Manual installation

1. Copy the `custom_components/configassistant` folder into your Home
   Assistant `custom_components` directory.
2. Restart Home Assistant.
3. Add the integration through **Settings → Devices & Services → Add
   Integration**.

## Configuration

Configuration is done entirely through the Home Assistant UI config flow —
no YAML is required. After adding the integration, a "Config Assistant"
entry appears in the sidebar.

## Requirements

- Home Assistant Core 2023.12.0 or later

## Contributing

Issues and pull requests are welcome:
https://github.com/jr551/hacs-configassistant/issues
