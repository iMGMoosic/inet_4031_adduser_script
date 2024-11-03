# Add Users Script and User List

## Program Description

This program takes a colon-delimited list of users, passwords, first and last names, and groups, and adds them to a Linux device.

## Program Operation

Your input list should be formatted as the following:

[username]:[password]:[last name]:[first name]:[groups]

If you do not want to assign a group to a user, use '-' in the group spot.
If you want to skip over a user, append '#' to the beginning of a line.

Run with sudo permissions, using < to pipe in data.
