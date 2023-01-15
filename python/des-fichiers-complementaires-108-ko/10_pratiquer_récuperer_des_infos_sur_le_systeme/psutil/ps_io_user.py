import psutil
import humanfriendly as hf

AC = 'ACCESS_DENIED'
USERNAME = 'chris'

total_rd = 0
total_wr = 0

total_users = {}

for proc in psutil.process_iter():
    with proc.oneshot():
        pinfo = proc.as_dict(attrs=['pid', 'name', 'username', 'io_counters'], ad_value=AC)
        if pinfo['io_counters'] != AC :
            total_rd += pinfo['io_counters'].read_chars 
            total_wr += pinfo['io_counters'].write_chars
            total_users[ pinfo['username'] ] = ( total_rd, total_wr )

print("User".center(19), "|", "read_chars".center(18), "|", "write_chars".center(19))
for user in total_users.keys():
    print("%20s" % user, end="")
    print("|", end="")
    print("%20s" % hf.format_size(total_users[user][0]), end="")
    print("|", end="")
    print("%20s" % hf.format_size(total_users[user][1]), end="")
    print()
