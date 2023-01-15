import sys
import datetime
import zipfile

def pr_info(archive):

    SYSTEM = { 0:'Windows', 3:'Unix' }

    zf = zipfile.ZipFile(archive)
    fmt = "{f:30s} | {d:10s} | {s:8s} | {v:5d} | {c_size:10d} | {u_size:10d} |"
    for info in zf.infolist():
        if info.filename.endswith('/'):
            if len(info.filename) <= 29:
                fname = info.filename
            else:
                fname = info.filename[28:]
        else:
            fname = info.filename.split('/')[-1]

        data = {
                'f': fname,
                'd': datetime.datetime(*info.date_time).strftime("%Y-%m-%d"),
                's': SYSTEM[info.create_system],
                'v': info.create_version,
                'c_size': info.compress_size,
                'u_size': info.file_size
                }
        print( fmt.format( **data ) )

if __name__ == '__main__':
    pr_info(sys.argv[1])

