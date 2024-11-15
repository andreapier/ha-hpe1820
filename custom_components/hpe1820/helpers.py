from homeassistant.util import slugify

from .const import DOMAIN


def generate_entity_id(serial_number: str, port_name: str) -> str:
    """Generate an entity ID based on system configuration or username.

    Args:
        config (ConfigEntry): The configuration entry from Home Assistant containing system
                              configuration or username.
        name (str]): Additional name component to be appended to the entity name.

    Returns:
        str: The generated entity id, which is a combination of the domain and either the configured
             system name or the username, optionally followed by the provided name.

    Raises:
        ValueError: If name is not provided

    Example:
        >>> config.data = {"system_name": "Seaside Home"}
        >>> generate_entity_name(entry, "window")
        "elmo_iess_alarm.seaside_home_window"
    """
    if port_name is None or not port_name or port_name.isspace():
        raise ValueError("name is mandatory")

    # Generate the entity ID and use Home Assistant slugify to ensure it's a valid value
    # NOTE: We append DOMAIN twice as HA removes the domain from the entity ID name. This is unexpected
    # as it means we lose our namespacing, even though this is the suggested method explained in HA documentation.
    # See: https://www.home-assistant.io/faq/unique_id/#can-be-changed
    entity_name = slugify(f"{serial_number}_{port_name}")
    return f"{DOMAIN}.{DOMAIN}_{entity_name}"
