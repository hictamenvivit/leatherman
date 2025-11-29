import sys
import os


def build_message(issue_number, backend_mr, tests_mr=None):
    message = f"""Hello, on https://axione.atlassian.net/browse/NB-{issue_number}
- backend : https://gitlab.m2m.axione.fr/axione/elbaf/sact/backend/-/merge_requests/{backend_mr}/diffs"""

    if tests_mr:
        message += f"\n- integration-tests : https://gitlab.m2m.axione.fr/axione/elbaf/sact/integration-tests/-/merge_requests/{tests_mr}/diffs"
    return message


if __name__ == "__main__":
    message = build_message(*sys.argv[1:])
    os.system(f"echo '{message}' | pbcopy")
    print("Message copied to clipboard")
