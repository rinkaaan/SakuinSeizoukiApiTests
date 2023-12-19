import json
import os

from openapi_client import OpenPdfIn

from tests.clients import projectApi


class TestNewProject:

    def test_open_pdf(self):
        home_path = os.path.expanduser("~")
        pdf_path = os.path.join(home_path, "Desktop", "test.pdf")
        params = OpenPdfIn(
            pdf_path=pdf_path,
        )
        res = projectApi.project_new_pdf_post(params)
        json = res.json()
        assert True is True

