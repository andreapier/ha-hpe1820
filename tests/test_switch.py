import logging

import pytest
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from custom_components.hpe1820.const import DOMAIN
from custom_components.hpe1820.switch import PoePortSwitch, async_setup_entry


@pytest.mark.asyncio
async def test_async_setup_entry_in_use(hass, config_entry, device, coordinator):
    # Ensure the async setup all poe ports
    hass.data[DOMAIN][config_entry.entry_id] = {
        "device": device,
        "coordinator": coordinator,
    }

    def ensure_only_in_use(ports):
        assert len(ports) == 2

    await async_setup_entry(hass, config_entry, ensure_only_in_use)


class TestPoePortSwitch:
    def test_switch_name(self, hass, device):
        # Ensure the switch has the right name
        coordinator = DataUpdateCoordinator(hass, logging.getLogger(__name__), name="hpe1820")
        entity = PoePortSwitch(hass, "test_id", "1", "01", coordinator, device)
        assert entity.name == "01"

    def test_switch_name_with_system_ip(self, hass, config_entry, device):
        # The ip doesn't change the Entity name
        hass.config_entries.async_update_entry(config_entry, data={"system_ip": "127.0.0.1"})
        coordinator = DataUpdateCoordinator(hass, logging.getLogger(__name__), name="hpe1820")
        entity = PoePortSwitch(hass, "test_id", "1", "01", coordinator, device)
        assert entity.name == "01"

    def test_switch_entity_id(self, hass, device):
        # Ensure the switch has a valid Entity ID
        coordinator = DataUpdateCoordinator(hass, logging.getLogger(__name__), name="hpe1820")
        entity = PoePortSwitch(hass, "test_id", "1", "01", coordinator, device)
        assert entity.entity_id == "hpe1820.hpe1820_test_serial_number_01"

    def test_switch_entity_id_with_system_ip(self, hass, config_entry, device):
        # Ensure the Entity ID takes into consideration the ip
        hass.config_entries.async_update_entry(config_entry, data={"system_ip": "127.0.0.1"})
        coordinator = DataUpdateCoordinator(hass, logging.getLogger(__name__), name="hpe1820")
        entity = PoePortSwitch(hass, "test_id", "1", "01", coordinator, device)
        assert entity.entity_id == "hpe1820.hpe1820_test_serial_number_01"

    def test_switch_unique_id(self, hass, device):
        # Ensure the switch has the right unique ID
        coordinator = DataUpdateCoordinator(hass, logging.getLogger(__name__), name="hpe1820")
        entity = PoePortSwitch(hass, "test_id", "1", "01", coordinator, device)
        assert entity.unique_id == "test_id"

    def test_switch_icon(self, hass, device):
        # Ensure the switch has the right icon
        coordinator = DataUpdateCoordinator(hass, logging.getLogger(__name__), name="hpe1820")
        entity = PoePortSwitch(hass, "test_id", "1", "01", coordinator, device)
        assert entity.icon == "hass:power-standby"

    def test_switch_is_off(self, hass, device):
        # Ensure the switch attribute is_on has the right status False
        coordinator = DataUpdateCoordinator(hass, logging.getLogger(__name__), name="hpe1820")
        entity = PoePortSwitch(hass, "test_id", "2", "02", coordinator, device)
        assert entity.is_on is False

    def test_switch_is_on(self, hass, device):
        # Ensure the switch attribute is_on has the right status True
        coordinator = DataUpdateCoordinator(hass, logging.getLogger(__name__), name="hpe1820")
        entity = PoePortSwitch(hass, "test_id", "1", "01", coordinator, device)

        assert entity.is_on is True

    def test_switch_device_info(self, hass, device):
        # Ensure the switch returns info about device it belongs to
        coordinator = DataUpdateCoordinator(hass, logging.getLogger(__name__), name="hpe1820")
        entity = PoePortSwitch(hass, "test_id", "1", "01", coordinator, device)

        print(entity.device_info["identifiers"])
        print(type(entity.device_info["identifiers"]))
        assert ("hpe1820", "test_serial_number") in entity.device_info["identifiers"]
        assert entity.device_info["via_device"] == ("hpe1820", "test_serial_number")

    async def test_switch_async_turn_off(self, hass, device):
        # Ensure turn_off executes the command and updates the state
        coordinator = DataUpdateCoordinator(hass, logging.getLogger(__name__), name="hpe1820")
        entity = PoePortSwitch(hass, "test_id", "1", "01", coordinator, device)

        await entity.async_turn_off()

        assert device._ports["1"] is False
        assert device._client.set_poe_state.call_count == 1
        assert device._client.set_poe_state.call_args.args == ("1", False)

    async def test_switch_async_turn_off_with_error(self, hass, device):
        # Ensure turn_off does not updates the state if error occurs
        device._client.set_poe_state.side_effect = Exception("Unexpected error")
        coordinator = DataUpdateCoordinator(hass, logging.getLogger(__name__), name="hpe1820")
        entity = PoePortSwitch(hass, "test_id", "1", "01", coordinator, device)

        await entity.async_turn_off()

        assert device._ports["1"] is True
        assert device._client.set_poe_state.call_count == 1
        assert device._client.set_poe_state.call_args.args == ("1", False)

    async def test_switch_async_turn_on(self, hass, device):
        # Ensure turn_on executes the command and updates the state
        coordinator = DataUpdateCoordinator(hass, logging.getLogger(__name__), name="hpe1820")
        entity = PoePortSwitch(hass, "test_id", "2", "02", coordinator, device)

        await entity.async_turn_on()

        assert device._ports["2"] is True
        assert device._client.set_poe_state.call_count == 1
        assert device._client.set_poe_state.call_args.args == ("2", True)

    async def test_switch_async_turn_on_with_error(self, hass, device):
        # Ensure turn_on does not updates the state if error occurs
        device._client.set_poe_state.side_effect = Exception("Unexpected error")
        coordinator = DataUpdateCoordinator(hass, logging.getLogger(__name__), name="hpe1820")
        entity = PoePortSwitch(hass, "test_id", "2", "02", coordinator, device)

        await entity.async_turn_on()

        assert device._ports["2"] is False
        assert device._client.set_poe_state.call_count == 1
        assert device._client.set_poe_state.call_args.args == ("2", True)
