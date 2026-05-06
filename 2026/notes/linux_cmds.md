# linux cmds

- `ps -ef` (process status)
- `ps aux`
  - find running pids
  - RSS = _resident set size_ -> amount of physical memory used by the process
  - get STAT column to see run status
  - `cat /proc/[pid]/status` as another way to see this info

- `lsof -p [pid]` (list open files)
