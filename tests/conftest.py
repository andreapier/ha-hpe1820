import asyncio
import logging
from unittest.mock import AsyncMock

import pytest
from aiohttp import ClientSession
from aiohttp.client_exceptions import ClientResponseError
from aiohttp.client_reqrep import RequestInfo
from homeassistant.config_entries import ConfigEntryState

from custom_components.hpe1820 import async_setup
from custom_components.hpe1820.config_flow import Hpe1820ConfigFlow
from custom_components.hpe1820.const import DOMAIN
from custom_components.hpe1820.coordinator import Hpe1820Coordinator
from custom_components.hpe1820.devices import Hpe1820Device

from .hass.fixtures import MockConfigEntry
from .helpers import _

pytest_plugins = ["tests.hass.fixtures"]


@pytest.fixture
def anyio_backend():
    return "asyncio"


def pytest_configure(config: pytest.Config) -> None:
    """Keeps the default log level to WARNING.

    Home Assistant sets the log level to `DEBUG` if the `--verbose` flag is used.
    Considering all the debug logs of this integration and `econnect-python`, this is very
    noisy. This is an override for `tests/hass/fixtures.py` as described in this
    issue: https://github.com/andreapier/ha-hpe1820/issues/134
    """
    if config.getoption("verbose") > 0:
        logging.getLogger().setLevel(logging.WARNING)


@pytest.fixture
async def hass(hass):
    """Create a Home Assistant instance for testing.

    This fixture forces some settings to simulate a bootstrap process:
    - `custom_components` is reset to properly test the integration
    - `async_setup()` method is called
    """
    await async_setup(hass, {})
    hass.data["custom_components"] = None
    hass.data[DOMAIN]["test_entry_id"] = {}
    yield hass


@pytest.fixture(scope="function")
def device(config_entry, client):
    """Yields an instance of Hpe1820Device.

    This fixture provides a scoped instance of Hpe1820Device initialized with
    the provided client.
    The device is connected and updated with mocked data

    Args:
        client: The client used to initialize the Hpe1820Device.

    Yields:
        An instance of Hpe1820Device.
    """
    m_device = Hpe1820Device(config_entry, client)

    m_device._ports = {"1": True, "2": False}
    m_device._serial_number = "test_serial_number"

    m_device.update = AsyncMock()
    m_device.update.return_value = dict(m_device._ports)

    yield m_device


@pytest.fixture(scope="function")
def coordinator(hass, config_entry, device):
    """Fixture to provide a test instance of the Hpe1820Coordinator.

    This sets up an Hpe1820Device and its corresponding DataUpdateCoordinator.

    Args:
        hass: Mock Home Assistant instance.
        config_entry: Mock config entry.

    Yields:
        Hpe1820Coordinator: Initialized test instance of the Hpe1820Coordinator.
    """
    coordinator = Hpe1820Coordinator(hass, device, 5)
    # Override Configuration and Device with mocked versions
    coordinator.config_entry = config_entry
    # Initializes the Coordinator to skip the first setup
    coordinator.data = {}
    yield coordinator


@pytest.fixture(scope="function")
def client(mocker):
    """Creates an instance of `Hpe1820Client` which emulates the behavior of a real client for
    testing purposes.
    """
    m_client = mocker.patch(_("config_flow.Hpe1820Client"))
    m_client.login = AsyncMock()
    m_client.logout = AsyncMock()
    m_client.get_poe_state = AsyncMock()
    m_client.set_poe_state = AsyncMock()
    m_client.get_serial_number = AsyncMock()

    yield m_client


@pytest.fixture(scope="function")
def config_entry(hass):
    """Creates a mock config entry for testing purposes.

    This config entry is designed to emulate the behavior of a real config entry for
    testing purposes.
    """
    config = MockConfigEntry(
        version=Hpe1820ConfigFlow.VERSION,
        domain=DOMAIN,
        entry_id="test_entry_id",
        options={},
        data={
            "username": "test_user",
            "password": "test_password",
            "system_ip": "test_ip",
        },
        state=ConfigEntryState.SETUP_IN_PROGRESS,
    )
    config.add_to_hass(hass)
    return config


@pytest.fixture(scope="function")
def client_response_error():
    def create_client_response_error(status: int, method: str = "POST"):
        return AsyncMock(side_effect=ClientResponseError(RequestInfo("", method, {}), (), status=status))

    return create_client_response_error


@pytest.fixture(scope="function")
def session():
    loop = asyncio.get_event_loop()
    return ClientSession(loop=loop)
