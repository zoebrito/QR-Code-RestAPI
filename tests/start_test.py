# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long

import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_login_for_access_token():
    form_data = {
        "username": "admin",
        "password": "secret",
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/token", data=form_data)
        assert response.status_code == 401

@pytest.mark.asyncio
async def test_create_and_delete_qr_code():
    form_data = {
        "username": "admin",
        "password": "secret",
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Authenticate and get the access token
        response = await ac.post("/token", data=form_data)
        assert response.status_code == 200
        access_token = response.json()["access_token"]

        # Use the access token to create a QR code
        qr_request = {
            "url": "https://example.com",
            "fill_color": "red",
            "back_color": "white",
            "size": 10,
        }
        create_response = await ac.post("/qr-codes/", json=qr_request, headers={"Authorization": f"Bearer {access_token}"})
        assert create_response.status_code in [201, 409]

        # If the QR code was created, attempt to delete it
        if create_response.status_code == 201:
            qr_code_url = create_response.json().get("qr_code_url")
            qr_filename = qr_code_url.split('/')[-1]
            delete_response = await ac.delete(f"/qr-codes/{qr_filename}", headers={"Authorization": f"Bearer {access_token}"})
            assert delete_response.status_code == 204
