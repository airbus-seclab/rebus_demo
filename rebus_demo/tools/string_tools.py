import subprocess


def extract_strings(inbuf):
    "Extract printable strings from a binary string usint 'strings' external program"

    p = subprocess.Popen(["strings", "-a", "-n 10"], 
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    outbuf = p.communicate(input=inbuf)[0]

    return outbuf
    
