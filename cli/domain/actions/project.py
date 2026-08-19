"""List Organizational Folders."""

import os

from cli.domain.services.project import get_project

print("Retrieving project information...")
project = get_project(
    project_id=os.getenv("GCP_PROJECT_ID"),
    name=os.getenv("GCP_PROJECT_NAME"),
    organization_id=os.getenv("GCP_ORGANIZATION_ID"),
)
print(f"Project ID: {project.id}")
print(f"Project Name: {project.name}")
print(f"Organization ID: {project.organization_id}")
