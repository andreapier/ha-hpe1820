import pytest
from homeassistant.core import valid_entity_id

from custom_components.hpe1820.helpers import generate_entity_id


def test_generate_entity_name_empty():
    with pytest.raises(ValueError):
        generate_entity_id("test_serial_number", "")


def test_generate_entity_name_space():
    with pytest.raises(ValueError):
        generate_entity_id("test_serial_number", " ")


def test_generate_entity_name_with_none():
    with pytest.raises(ValueError):
        generate_entity_id("test_serial_number", None)


def test_generate_entity_name_with_name():
    entity_id = generate_entity_id("test_serial_number", "01")
    assert entity_id == "hpe1820.hpe1820_test_serial_number_01"
    assert valid_entity_id(entity_id)


def test_generate_entity_name_empty_system(hass, config_entry):
    hass.config_entries.async_update_entry(config_entry, data={"system_ip": "127.0.0.1"})
    with pytest.raises(ValueError):
        generate_entity_id("test_serial_number", "")


def test_generate_entity_name_space_system(hass, config_entry):
    hass.config_entries.async_update_entry(config_entry, data={"system_ip": "127.0.0.1"})
    with pytest.raises(ValueError):
        generate_entity_id("test_serial_number", " ")


def test_generate_entity_name_with_none_system(hass, config_entry):
    hass.config_entries.async_update_entry(config_entry, data={"system_ip": "127.0.0.1"})
    with pytest.raises(ValueError):
        generate_entity_id("test_serial_number", None)


def test_generate_entity_name_with_name_system(hass, config_entry):
    hass.config_entries.async_update_entry(config_entry, data={"system_ip": "127.0.0.1"})
    entity_id = generate_entity_id("test_serial_number", "01")
    assert entity_id == "hpe1820.hpe1820_test_serial_number_01"
    assert valid_entity_id(entity_id)
