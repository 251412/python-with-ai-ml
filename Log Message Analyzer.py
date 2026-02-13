

logs = [
    "ERROR Disk full",
    "INFO User logged in",
    "ERROR Network issue",
    "WARNING Low memory",
    "INFO File saved",
    "ERROR Timeout"
]
log_count = {}
for log in logs:
    level = log.split()[0]   
    if level in log_count:
        log_count[level] += 1
    else:
        log_count[level] = 1
print(log_count)
