from homeassistant.components import persistent_notification
from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
)

from .const import (
    DOMAIN,
    KEY_COORDINATOR,
    KEY_DEVICE,
    NOTIFICATION_IDENTIFIER,
    NOTIFICATION_MESSAGE,
    NOTIFICATION_TITLE,
)
from .devices import Hpe1820Device
from .helpers import generate_entity_id


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    device = hass.data[DOMAIN][entry.entry_id][KEY_DEVICE]
    coordinator = hass.data[DOMAIN][entry.entry_id][KEY_COORDINATOR]
    ports = []

    # Iterate through the ports of the device and create PortPoeSwitch objects
    for port_id, _ in device.ports:
        unique_id = f"{entry.entry_id}_{DOMAIN}_{port_id}"
        ports.append(PoePortSwitch(hass, unique_id, port_id, port_id.zfill(2), coordinator, device))

    async_add_entities(ports)


class PoePortSwitch(CoordinatorEntity, SwitchEntity):
    """Representation of a poe port switch."""

    _attr_has_entity_name = True

    def __init__(
        self,
        hass: HomeAssistant,
        unique_id: str,
        port_id: str,
        name: str,
        coordinator: DataUpdateCoordinator,
        device: Hpe1820Device,
    ) -> None:
        """Construct."""
        super().__init__(coordinator)
        self.entity_id = generate_entity_id(device.serial_number, name)
        self._name = name
        self._device = device
        self._unique_id = unique_id
        self._port_id = port_id
        self.hass = hass

    @property
    def unique_id(self) -> str:
        """Return the unique identifier."""
        return self._unique_id

    @property
    def name(self) -> str:
        """Return the name of this entity."""
        return self._name

    @property
    def icon(self) -> str:
        """Return the icon used by this entity."""
        return "hass:power-standby"

    @property
    def is_on(self) -> bool:
        """Return the switch status (on/off)."""
        return self._device.get_port_state(self._port_id)

    @property
    def device_info(self) -> DeviceInfo:
        """Return the device info."""
        return DeviceInfo(
            identifiers={(DOMAIN, self._device.serial_number)},
            name="HPE1820",  # TODO: fetch from dashboard page
            manufacturer="HPE",
            model="HPE 1820-24G-PoE+",
            model_id="J9983A",
            via_device=(DOMAIN, self._device.serial_number),
        )

    async def async_turn_off(self):
        """Turn the entity off."""
        result = await self._device.set_port_state(self._port_id, False)
        if not result:
            persistent_notification.async_create(
                self.hass, NOTIFICATION_MESSAGE, NOTIFICATION_TITLE, NOTIFICATION_IDENTIFIER
            )
        else:
            self.coordinator.async_set_updated_data(self._device.ports)

    async def async_turn_on(self):
        """Turn the entity off."""
        result = await self._device.set_port_state(self._port_id, True)
        if not result:
            persistent_notification.async_create(
                self.hass, NOTIFICATION_MESSAGE, NOTIFICATION_TITLE, NOTIFICATION_IDENTIFIER
            )
        else:
            self.coordinator.async_set_updated_data(self._device.ports)
