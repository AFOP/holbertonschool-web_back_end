#!/usr/bin/env python3
"""
filter_datum: returns the log message obfuscated
Arguments: 
    fields: a list of strings representing all fields to obfuscate
    redaction: a string representing by what the field will be obfuscated
    message: a string representing the log line
    separator: a string representing by which character is separating all fields in the log line (message)
Return: the log message obfuscated
"""


import re

def filter_datum(fields, redaction, message, separator):
    return re.sub(r"(\w+)=([a-zA-Z0-9@\.\-\(\)\ \:\^\<\>\~\$\%\@\?\!\/]*)",
                  lambda match: match.group(1) + "=" + redaction
                  if match.group(1) in fields else match.group(0), message)
