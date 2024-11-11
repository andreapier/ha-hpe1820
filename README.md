# Home Assistant HPE1820 Integration

[![Linting](https://github.com/andreapier/ha-hpe1820/actions/workflows/linting.yaml/badge.svg)](https://github.com/andreapier/ha-hpe1820/actions/workflows/linting.yaml)
[![Testing](https://github.com/andreapier/ha-hpe1820/actions/workflows/testing.yaml/badge.svg)](https://github.com/andreapier/ha-hpe1820/actions/workflows/testing.yaml)
[![Coverage Status](https://coveralls.io/repos/github/andreapier/ha-hpe1820/badge.svg?branch=main)](https://coveralls.io/github/andreapier/ha-hpe1820?branch=main)
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/andreapier/ha-hpe1820)



This project is a [Home Assistant](https://www.home-assistant.io/) integration for your HPE1820 switch.

## Supported Systems

This integration supports HPE1820. The following systems are known to work:
- [J9983A](https://support.hpe.com/hpesc/public/docDisplay?docId=c04625984&page=GUID-1105B59F-E442-4FBA-A857-12BF25586E53.html&docLocale=en_US)

**Available functionalities**
- Configuration flow implemented to add login credentials
- Power ona nd off POE ports

## Installation

### Download the Integration
1. Create a new folder in your configuration folder (where the `configuration.yaml` lives) called `custom_components`
2. Download the [latest version](https://github.com/andreapier/ha-hpe1820/releases) into the `custom_components`
   folder so that the full path from your config folder is `custom_components/hpe1820/`
3. Restart Home Assistant. If it's your only custom component you'll see a warning in your logs.
4. Once Home Assistant is started, from the UI go to Configuration > Integrations > Add Integrations. Search for
   "HPE1820". After selecting, dependencies will be downloaded and it could take up to a minute.

### Setup

<img src="https://github.com/andreapier/ha-hpe1820/images/setup.png" width="400">

- Ip: is the LAN IP of the switch.
- Username: is your username to access the admin page via web.
- Password: is your password to access the admin page via web.

### Options

In the option page you can configure the polling timeout. To proceed with the configuration,
open the integration page and click on HPE1820 integration. Once the page is opened, you should see the following integration page:

<img src="https://github.com/andreapier/ha-hpe1820/images/configure.png" width="400"/>

To configure the integration, click on "Configure".

<img src="https://github.com/andreapier/ha-hpe1820/images/options.png" width="400"/>

## Troubleshooting

If you encounter an issue, providing `DEBUG` logs can greatly assist in identifying the bug. Please follow these steps to send the debug logs:

1. Navigate to the integration configuration page in Home Assistant: **Settings > Devices & Services > HPE1820**.
2. Enable debug logging by clicking on **Enable debug logging**.
3. Reload the integration by selecting **Reload** from the three-dot menu.
4. Reproduce the error (e.g., power on/off a port, configure the integration, etc.).
5. After reproducing the error, return to the Integration configuration page and click **Disable debug logging**.
6. Your browser will prompt you to download the log file.
7. Ensure that the logs do not contain sensitive information, as we do not log credentials or access tokens.
8. Send the logs via a secure method. **Do not post your logs on public platforms**.

<img src="https://github.com/andreapier/ha-hpe1820/images/debug.png">

## Contributing

We are very open to the community's contributions - be it a quick fix of a typo, or a completely new feature!
You don't need to be a Python expert to provide meaningful improvements. To learn how to get started, check
out our [Contributor Guidelines](https://github.com/andreapier/ha-hpe1820/blob/main/CONTRIBUTING.md) first,
and ask for help in our [Discord channel](https://discord.gg/NSmAPWw8tE) if you have questions.

## Development

We welcome external contributions, even though the project was initially intended for personal use. If you think some
parts could be exposed with a more generic interface, please open a [GitHub issue](https://github.com/andreapier/ha-hpe1820/issues)
to discuss your suggestion.

### Dev Environment

To create a virtual environment and install the project and its dependencies, execute the following commands in your
terminal:

```bash
# Initialize the environment with the latest version of Home Assistant
E_HASS_VERSION=$(curl --silent "https://api.github.com/repos/home-assistant/core/releases/latest" | grep -Po "(?<=\"tag_name\": \").*(?=\")")
./scripts/init $E_HASS_VERSION
source venv/bin/activate

# Install pre-commit hooks
pre-commit install
```

Instead, if you want to develop and test this integration with a different Home Assistant version, just pass the
version to the init script:
```bash
# Initialize the environment Home Assistant 2024.1.1
./scripts/init 2024.1.1
source venv/bin/activate

# Install pre-commit hooks
pre-commit install
```

### Testing Changes in Home Assistant

To test your changes in an actual Home Assistant environment, you may use the Docker container available in our
`compose.yaml` file. Launch the container with the following command:

```bash
docker compose up -d
```

Then, navigate to `http://localhost:8123` in your web browser to set up your Home Assistant instance. Follow the standard
procedure to install the integration, as you would in a typical installation.

The container is configured to automatically mount the `custom_components/` and `config/` directories from your local
workspace. To see changes reflected in Home Assistant, make sure to restart the instance through the UI each time
you update the integration.

### Coding Guidelines

To maintain a consistent codebase, we utilize [flake8][1] and [black][2]. Consistency is crucial as it
helps readability, reduces errors, and facilitates collaboration among developers.

To ensure that every commit adheres to our coding standards, we've integrated [pre-commit hooks][3].
These hooks automatically run `flake8` and `black` before each commit, ensuring that all code changes
are automatically checked and formatted.

For details on how to set up your development environment to make use of these hooks, please refer to the
[Development][4] section of our documentation.

[1]: https://pypi.org/project/flake8/
[2]: https://github.com/ambv/black
[3]: https://pre-commit.com/
[4]: https://github.com/andreapier/ha-hpe1820#development

### Testing

Ensuring the robustness and reliability of our code is paramount. Therefore, all contributions must include
at least one test to verify the intended behavior.

To run tests locally, execute the test suite using `pytest` with the following command:
```bash
pytest tests --cov --cov-branch -vv
```

For a comprehensive test that mirrors the Continuous Integration (CI) environment across all supported Python
versions, use `tox`:
```bash
tox
```

**Note**: To use `tox` effectively, ensure you have all the necessary Python versions installed. If any
versions are missing, `tox` will provide relevant warnings.
