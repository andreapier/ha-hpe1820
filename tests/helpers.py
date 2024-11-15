def _(mock_path: str) -> str:
    """Helper to simplify Mock path strings.

    Args:
        mock_path (str): The partial path to be appended to the standard prefix for mock paths.

    Returns:
        str: The full mock path combined with the standard prefix.

    Example:
        >>> _("module.Class.method")
        "custom_components.hpe1820.module.Class.method"
    """
    return f"custom_components.hpe1820.{mock_path}"
