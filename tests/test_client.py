import pytest
from aiohttp.client_exceptions import ClientResponseError
from aioresponses import aioresponses

from custom_components.hpe1820.client import Hpe1820Client

from .data.responses import GET_POS_STATUS


def test_client_constructor(session):
    # Ensure that the client is initialized correctly
    client = Hpe1820Client(session, "test_ip", "test_protocol")
    assert client._session == session
    assert client._base_url == "test_protocol://test_ip"


def test_client_constructor_with_default(session):
    # Ensure that the client is initialized correctly with default protocol
    client = Hpe1820Client(session, "test_ip")
    assert client._session == session
    assert client._base_url == "http://test_ip"


@pytest.mark.asyncio
async def test_client_login_successful_adds_cookie(mocker, session):
    client = Hpe1820Client(session, "127.0.0.1")
    mocker.spy(session.cookie_jar, "update_cookies")
    with aioresponses() as mocked:
        mocked.post(
            "http://127.0.0.1/htdocs/login/login.lua",
            status=200,
            payload=dict(error=""),
            headers={"Set-Cookie": "SID=test_cookie"},
        )
        await client.login("test_username", "test_password")
        mocked.assert_called_once_with(
            "http://127.0.0.1/htdocs/login/login.lua",
            method="POST",
            data={"username": "test_username", "password": "test_password"},
        )
        session.cookie_jar.update_cookies.assert_called_once()
        assert session.cookie_jar.update_cookies.call_args[0][0]["SID"].coded_value == "test_cookie"


@pytest.mark.asyncio
async def test_client_login_wrong_username_does_not_add_cookie(mocker, session):
    client = Hpe1820Client(session, "127.0.0.1")
    mocker.spy(session.cookie_jar, "update_cookies")
    with aioresponses() as mocked:
        mocked.post(
            "http://127.0.0.1/htdocs/login/login.lua",
            status=401,
            headers={"Set-Cookie": "SID=test_cookie"},
        )
        with pytest.raises(ClientResponseError):
            await client.login("wrong_username", "test_password")
            mocked.assert_called_once_with(
                "http://127.0.0.1/htdocs/login/login.lua",
                method="POST",
                data={"username": "wrong_username", "password": "test_password"},
            )
            assert session.cookie_jar.update_cookies.call_count == 0


@pytest.mark.asyncio
async def test_client_login_wrong_password_does_not_add_cookie(mocker, session):
    client = Hpe1820Client(session, "127.0.0.1")
    mocker.spy(session.cookie_jar, "update_cookies")
    with aioresponses() as mocked:
        mocked.post(
            "http://127.0.0.1/htdocs/login/login.lua",
            status=401,
            headers={"Set-Cookie": "SID=test_cookie"},
        )
        with pytest.raises(ClientResponseError):
            await client.login("test_username", "wrong_password")
            mocked.assert_called_once_with(
                "http://127.0.0.1/htdocs/login/login.lua",
                method="POST",
                data={"username": "test_username", "password": "wrong_password"},
            )
            assert session.cookie_jar.update_cookies.call_count == 0


@pytest.mark.asyncio
async def test_client_login_unknow_auth_error_does_not_add_cookie(mocker, session):
    client = Hpe1820Client(session, "127.0.0.1")
    mocker.spy(session.cookie_jar, "update_cookies")
    with aioresponses() as mocked:
        mocked.post(
            "http://127.0.0.1/htdocs/login/login.lua",
            status=200,
            payload=dict(error="auth error"),
            headers={"Set-Cookie": "SID=test_cookie"},
        )
        with pytest.raises(ClientResponseError):
            await client.login("test_username", "test_password")
            mocked.assert_called_once_with(
                "http://127.0.0.1/htdocs/login/login.lua",
                method="POST",
                data={"username": "test_username", "password": "test_password"},
            )
            assert session.cookie_jar.update_cookies.call_count == 0


@pytest.mark.asyncio
async def test_client_logout_successful_removes_cookie(mocker, session):
    client = Hpe1820Client(session, "127.0.0.1")
    mocker.spy(session.cookie_jar, "update_cookies")
    with aioresponses() as mocked:
        mocked.get(
            "http://127.0.0.1/htdocs/pages/main/logout.lsp",
            status=200,
        )
        await client.logout()
        mocked.assert_called_once_with(
            "http://127.0.0.1/htdocs/pages/main/logout.lsp",
            method="GET",
        )
        session.cookie_jar.update_cookies.assert_called_once()
        assert session.cookie_jar.update_cookies.call_args[0][0]["SID"] is None


@pytest.mark.asyncio
async def test_client_set_poe_status_true(session):
    client = Hpe1820Client(session, "127.0.0.1")
    with aioresponses() as mocked:
        mocked.post(
            "http://127.0.0.1/htdocs/pages/base/poe_port_cfg_modal.lsp",
            status=200,
        )
        await client.set_poe_state("1", True)
        mocked.assert_called_once_with(
            "http://127.0.0.1/htdocs/pages/base/poe_port_cfg_modal.lsp",
            method="POST",
            data={
                "admin_mode_sel[]": "enabled",
                "schedule_sel[]": "none",
                "priority_sel[]": "low",
                "high_power_mode_sel[]": "disable",
                "power_detect_type_sel[]": "4pt_dot3af",
                "power_limit_type_sel[]": "dot3af",
                "power_limit": "",
                "intfStr": "1",
                "b_modal1_clicked": "b_modal1_submit",
            },
        )


@pytest.mark.asyncio
async def test_client_set_poe_status_false(session):
    client = Hpe1820Client(session, "127.0.0.1")
    with aioresponses() as mocked:
        mocked.post(
            "http://127.0.0.1/htdocs/pages/base/poe_port_cfg_modal.lsp",
            status=200,
        )
        await client.set_poe_state("1", False)
        mocked.assert_called_once_with(
            "http://127.0.0.1/htdocs/pages/base/poe_port_cfg_modal.lsp",
            method="POST",
            data={
                "admin_mode_sel[]": "disabled",
                "schedule_sel[]": "none",
                "priority_sel[]": "low",
                "high_power_mode_sel[]": "disable",
                "power_detect_type_sel[]": "4pt_dot3af",
                "power_limit_type_sel[]": "dot3af",
                "power_limit": "",
                "intfStr": "1",
                "b_modal1_clicked": "b_modal1_submit",
            },
        )


@pytest.mark.asyncio
async def test_client_get_poe_status(session):
    client = Hpe1820Client(session, "127.0.0.1")
    with aioresponses() as mocked:
        mocked.get("http://127.0.0.1/htdocs/pages/base/poe_port_cfg.lsp", status=200, body=GET_POS_STATUS)
        await client.get_poe_state()
        mocked.assert_called_once_with(
            "http://127.0.0.1/htdocs/pages/base/poe_port_cfg.lsp",
            method="GET",
        )
