"""
A module for converting an Azure DevOps work item ID and title to a git branch name.

Usage: Azure2GitBranch.py <Azure DevOps work item ID>
Example: Azure2GitBranch.py 12345
Output: 12345-This-is-an-Azure-DevOps-work-item-title

This module provides a command-line interface for converting an Azure DevOps work item ID and title to a git branch name. The module requires an Azure DevOps organization URL, a personal access token (PAT) for authentication, and a project name. The module uses the Azure DevOps Python library to interact with the Azure DevOps API.

The module provides two functions:
- GetAzureDevOpsInstance(): Returns an authenticated Azure DevOps instance using the organization URL and PAT token from the config module.
- ConvertAzureDevOpsWorkItemToGitBranchName(workItemId): Converts an Azure DevOps work item ID and title to a git branch name.

The module also provides a main() function that takes the Azure DevOps work item ID as a command line argument and prints the corresponding git branch name.
"""

import sys
from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
from azure.devops.exceptions import AzureDevOpsServiceError
import config

def GetAzureDevOpsInstance() -> Connection:
    """
    Returns an authenticated Azure DevOps instance using the organization URL and PAT token from the config module.
    """
    credentials = BasicAuthentication('', config.AZURE_PAT_TOKEN)
    connection = Connection(base_url=config.AZURE_DEVOPS_ORGANIZATION_URL, creds=credentials)

    return connection


def ConvertAzureDevOpsWorkItemToGitBranchName(workItemId: str) -> str:
    """
    Converts an Azure DevOps work item ID and title to a git branch name.

    Parameters:
    workItemId (str): The Azure DevOps work item ID.

    Returns:
    str: The git branch name in the format of <workItemId>-<workItemTitle>.
    """
    # Get a work item
    connection = GetAzureDevOpsInstance()
    work_item_client = connection.clients.get_work_item_tracking_client()
    try:
        work_item = work_item_client.get_work_item(int(workItemId))
    except AzureDevOpsServiceError as ex:
        print(f"Error: {ex}")
        sys.exit(1)

    # Get the work item title
    work_item_title = work_item.fields['System.Title']

    # Replace invalid characters with hyphens
    invalid_chars = ['\\', '/', ':', '*', '?', '"', '<', '>', '|', ' ']
    work_item_title = work_item_title.replace(' - ', '-')
    for char in invalid_chars:
        work_item_title = work_item_title.replace(char, '_')

    for i in range(2, 5).__reversed__():
        work_item_title = work_item_title.replace('_'*i , '_')

    # Return the git branch name
    return f"\n{workItemId}-{work_item_title}\n"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: Azure2GitBranch.py <Azure DevOps work item ID>")
        sys.exit(1)

    work_item_id = sys.argv[1]
    git_branch_name = ConvertAzureDevOpsWorkItemToGitBranchName(work_item_id)
    print(git_branch_name)