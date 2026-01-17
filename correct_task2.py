def count_valid_emails(emails):
    if not emails:
        return 0

    count = 0

    for email in emails:
        if isinstance(email, str):
            email = email.strip()
            if "@" in email:
                local, _, domain = email.partition("@")
                if local and "." in domain:
                    count += 1

    return count
