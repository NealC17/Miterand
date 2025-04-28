import subprocess
import sys
import threading


class PythonREPL:
    def __init__(self, python_cmd=None, prompt=">>> "):
        """
        Spawn a fresh, un-buffered, interactive Python subprocess
        and sync up until its first prompt.
        """
        python_cmd = python_cmd or [sys.executable, "-u", "-i"]
        self.prompt = prompt
        self.proc = subprocess.Popen(
            python_cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,  # line-buffered
        )
        # drain the initial banner up to the first '>>> '
        self._read_until(self.prompt)

    def _read_until(self, marker):
        """
        Read from self.proc.stdout until the output ends with `marker`.
        Returns everything read (including the marker).
        """
        buf = ""
        while not buf.endswith(marker):
            chunk = self.proc.stdout.read(1)
            if chunk == "":
                # EOF
                break
            buf += chunk
        return buf

    def run(self, code):
        """
        Send a chunk of code (one line or many), then read back
        everything up to the next prompt.
        Returns the full raw text (including the trailing prompt).
        """
        if not code.endswith("\n"):
            code = code + "\n"
        self.proc.stdin.write(code)
        self.proc.stdin.flush()
        return self._read_until(self.prompt)

    def close(self):
        """Terminate the subprocess."""
        self.proc.terminate()
        self.proc.wait()
