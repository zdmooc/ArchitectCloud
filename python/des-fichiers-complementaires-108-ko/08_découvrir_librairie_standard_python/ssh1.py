import spur

shell = spur.SshShell(hostname="192.168.0.30", username="chris", password="")
with shell:
    result = shell.run(["echo", "-n", "hello"])
    print(result.output) # prints hello
    result = shell.run(["ls", "-l"])
    print(result.output)
