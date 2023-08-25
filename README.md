# JiraToGitBranch

A Python module for converting a Jira ticket number and title to a git branch name.

## Usage

```bash
JiraToGitBranch.py <Jira ticket number> <Jira ticket title>
```

Example:

```bash
JiraToGitBranch.py ABC-1234 This is a Jira ticket title
```

Output:

```
ABC-1234-This-is-a-Jira-ticket-title
```

## Requirements

- Python 3.x
- JIRA Python library
- JIRA server URL
- Personal access token (PAT) for authentication

## Installation

1. Clone the repository:

```
git clone https://github.com/IsacSvensson/Jira2GitBranch.git
```

2. Install the JIRA Python library:

```
pip install jira
```

3. Update the `config.py` file with your JIRA server URL and PAT token.

## Functions

- `GetJiraInstance()`: Returns an authenticated JIRA instance using the server URL and PAT token from the `config` module.
- `ConvertJiraTicketToGitBranchName(ticketNumber)`: Converts a Jira ticket number and title to a git branch name.

## Example

```
import JiraToGitBranch

branch_name = JiraToGitBranch.ConvertJiraTicketToGitBranchName("ABC-1234")
print(branch_name)
```

Output:

```
ABC-1234-This-is-a-Jira-ticket-title
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.