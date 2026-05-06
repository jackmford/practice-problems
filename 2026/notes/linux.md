# linux

- resources a process has can be obtained from /proc/<pid>
- clone() creates a new thread/process
  - used by fork() and pthread_create()

- fork()
  - creates a new **process**
  - new process has its own memory space, a copy of the parent
  - new process has a new pid
  - copies text, data, heap, and stack segments from the parent to the child
    - the _copy on write_ mechanism will point the child and parent page tables to the same physical memory until any of those segments (data, heap, stack) are modified, at which point a copy will be made and the page table for that process updated
    - text segment is marked read only

- exec <cmd>
  - runs a given command in place of current shell
  - does not create a new process
  - actually the _execve()_ system call, "exec" is a monicer
  - no command will modify the current shells file descriptors (stdin, stdout, stderr)
    - redirect stdout of current shell to file == exec > output.txt

- wait()
  - parent process pauses execution until a child process changes state
  - if wait is not called after a child process terminates it becomes a zombie
  - used in conjunction with fork() to create child processes

- process vs. thread
  - threads execute within a process and share memory+resources with other threads in that process
  - threads allow for concurrent execution in a process
  - processes are isolated from one another, running in their own memory
  - threads context switch much faster than processes, don't need to load/reload states
  - processes require more time and resources to create (heavier)

- threads
  - have their own stacks and registers
  - share code section, data section, open files

- SIGTERM vs. SIGKILL
  - sigkill is a force kill, doesn't clean up resources, only use it for unresponsive processes
  - SIGKILL can create zombie processes because child processes are killed before telling parent

- PCB
  - process control block
  - data structure to manage processes
  - contains:
    - PID
    - process state (running, waiting, terminated)
    - memory info
    - scheduling info (prio, elapsed time)
    - parent and child IDs
  - allows the operating system to switch between processes
  - kernel maintains a list of all active PCBs

_typical flow for forking and executing another process_

- fork() -> execve() the new program the child process wants to execute -> child calls exit() -> parent has called wait() to read the status of the child exit

**virtual memory**

- developed to avoid having to deal directly with physical memory
- enables the OS to use disk space as additional RAM, allowing it to run larger programs and handle more concurrent processes
- **virtual address space** -> range of memory addresses a single process can use
  - divided into different regions (code, data, stack)
- **page tables** are used to map info between virtual pages and physical pages
- **swapping** is when linux moves a process from memory to disk if running low on memory
- **paging** moves pages of memory between physical memory and disk
- use `free -h` or `cat /proc/meminfo` to see mem usage
- you can actually adjust how aggressively linux manages swapping with `vm.swappiness` on a 0 to 100 scale
- `ulimit` is how you set limits on how much memory a process can use

- the **transaction lookaside buffer (TLB)** is used to cache memory translations on the CPU to save having to access memory for them

- the **oom killer** sacrifices tasks to allow the kernel to continue to operate in the case that memory is exhausted

- **compaction** will rearrange used memory pages in order to make a large contiguous physical area of memory at the top of the zone if contiguous memory allocation is needed

- memfree is **total** unused physical memory while memavailable is an estimate of how much memory can be used without causing memory pressure (no swapping)

- a page fault occurs if a process attempts access on a memory page that is not in physical memory, causing the page to be loaded from disk and updating the virtual address space
  - invalid page fault can cause a segmentation fault if a process is trying to reach out of it's virtual address space
