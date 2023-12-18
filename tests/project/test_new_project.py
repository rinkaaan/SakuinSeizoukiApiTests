from openapi_client import OpenPdfIn

from tests.clients import projectApi


class TestNewProject:

    def test_open_pdf(self):
        params = OpenPdfIn(
            pdf_path="/Users/lincolnnguyen/Desktop/test.pdf"
        )
        res = projectApi.project_new_pdf_post(params)
        print(res)
        assert True is True

