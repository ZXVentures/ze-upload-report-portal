import requests
import sys
import os
from rename_xml import save_new_xml

api_url = os.environ['API_URL']
access_token = os.environ['ACCESS_TOKEN_REPORT_PORTAL']
description = os.environ['DESCRIPTION']
project_name = os.environ['PROJECT_NAME']
pipe_name = os.environ['PIPE_NAME']
repo_name = os.environ['REPO_NAME']
branch_name = os.environ['BRANCH_NAME']
path_archive_xml_old = os.environ['PATH_ARCHIVE_XML']

path_archive_xml = save_new_xml (branch_name, pipe_name, repo_name, path_archive_xml_old )

def send_report():
    url = f"{api_url}/launch/import"
    headers = {"Authorization": f"bearer {access_token}"}
    file_name = f"{path_archive_xml}"
    payload = {"projectName": project_name}
    files = [("file", (file_name, open(file_name, "rb",), "text/xml",),)]

    print("Initiating file upload...")
    response = requests.post(url, headers=headers, data=payload, files=files)

    print("return response", response.json())

    assert response.status_code == 200

    print(f"File {response.json()['message'][17:53]} successfully uploaded.")
    return response.json()["message"][17:53]


def get_launch_id(launch_uuid):
    url = f"{api_url}/launch/uuid/{launch_uuid}"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"bearer {access_token}",
    }

    response = requests.get(url, headers=headers)
    return response.json()["id"], response.json()["number"]


def update_launch_id(launch_id, launch_number):
    url = f"{api_url}/launch/{launch_id}/update"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"bearer {access_token}",
    }

    payload = {
        "attributes": [{"key": "run_number", "value": launch_number}],
        "description": description,
        "mode": "DEFAULT",
    }

    response = requests.put(url, headers=headers, json=payload)
    assert response.status_code == 200
    print("Launch successfully updated.")


def send_report_and_assign_number_to_report():
    launch_uuid = send_report()
    launch_id, launch_number = get_launch_id(launch_uuid)
    update_launch_id(launch_id, launch_number)
    print(f"Launch id {launch_id} updated.")

def main():
    send_report_and_assign_number_to_report()


if __name__ == "__main__":
    main()
