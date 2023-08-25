"""
A module for converting a Jira ticket number and title to a git branch name.

Usage: JiraToGitBranch.py <Jira ticket number>
Example: JiraToGitBranch.py ABC-1234
Output: ABC-1234-This-is-a-Jira-ticket-title

This module provides a command-line interface for converting a Jira ticket number and title to a git branch name. The module requires a JIRA server URL and a personal access token (PAT) for authentication. The module uses the JIRA Python library to interact with the JIRA API.

The module provides two functions:
- GetJiraInstance(): Returns an authenticated JIRA instance using the server URL and PAT token from the config module.
- ConvertJiraTicketToGitBranchName(ticketNumber): Converts a Jira ticket number and title to a git branch name.

The module also provides a main() function that takes the Jira ticket number as a command line argument and prints the corresponding git branch name.
"""

import sys
from jira import JIRA, exceptions as JiraExceptions
import config

def GetJiraInstance() -> JIRA:    
    """
    Returns an authenticated JIRA instance using the server URL and PAT token from the config module.
    """
    jira = JIRA(config.JIRA_SERVER_URL, token_auth=(config.PAT_TOKEN))

    return jira


def ConvertJiraTicketToGitBranchName(ticketNumber: str) -> str:
    """
    Converts a Jira ticket number and title to a git branch name.

    Parameters:
    ticketNumber (str): The Jira ticket number.

    Returns:
    str: The git branch name in the format of <ticketNumber>-<ticketTitle>.
    """
    # Get an issue
    jira = GetJiraInstance()

    try:
        issue = jira.issue(ticketNumber)
    except JiraExceptions.JIRAError as e:
        print("Error: " + str(e))
        exit(1)

    branch_name = ticketNumber + "-" + issue.fields.summary.replace(" ", "-")

    return branch_name

def main():
    """
    The main function that takes the Jira ticket number as a command line argument and prints the corresponding git branch name.
    """
    sys.argv.pop(0)
    if len(sys.argv) != 1:
        print("\nJira2Branch v1.0\nIsac Svensson")
        print('-' * 30)
        print("Usage: jira2Branch <Jira ticket number>")
        print("Example: jira2Branch ABC-1234")
        print("Output: ABC-1234-This-is-a-Jira-ticket-title\n")
        exit(1)
    else:
        ticketNumber = sys.argv.pop(0)

        print('\n' + ConvertJiraTicketToGitBranchName(ticketNumber) + "\n")

if __name__ == "__main__":
    main()