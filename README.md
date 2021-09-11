# Advanced Encryption Standard

Project1AES runs the AES protocol on a 128-, 192-, and 256-bit keys in Python.

## Dependencies

- Python 3

## Instructions

Program prints to the terminal. To redirect output to a file:

```
python3 Project1AES.py > output.txt
```

To check it against appendix_c.txt:

```
vimdiff output.txt appendix_c.txt
```

The only differences between the two files is the lack of the Equivalent Inverse Cipher sections, which was not implemented.

## Sources Used

<ul> <li> <a href="https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf" target="_blank" rel="noopener noreferrer">FIPS Publication 197</a> is the official standard for AES. Each section in the requirements below will reference the appropriate section in this document.</li> <li><a href="https://userlab.utk.edu/courses/cosc483/resources/aes-arrays">Useful arrays</a></li> <li><a href="https://userlab.utk.edu/courses/cosc483/resources/aes-unit-tests">Unit tests</a></li> <li> <a href="https://www.youtube.com/watch?v=gP4PqVGudtg" target="_blank" rel="noopener noreferrer">Animation of AES</a> on YouTube</li> <li><a href="http://www.moserware.com/assets/stick-figure-guide-to-advanced/A%20Stick%20Figure%20Guide%20to%20the%20Advanced%20Encryption%20Standard%20%28AES%29.pdf" target="_blank" rel="noopener noreferrer">Stick figure guide to AES</a></li> <li>Wikipedia has a nice <a href="http://en.wikipedia.org/wiki/Advanced_Encryption_Standard" target="_blank" rel="noopener noreferrer">overview of AES</a>