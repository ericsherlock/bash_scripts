# bash_scripts

Collection of bash shell scripts. Currently Includes:

-->Wireshark Packet Analyzer : Takes Wireshark packet captures as a plain text file and manipulates it to print various aspects of packets. Can currently pick out: hex, ascii, and headers (individually or sorted). 

-->Antivirus scanner : Small script that uses ClamAV to conduct an antivirus scan and save the results to a file. If you have a preconfigured mail server, the script can also email you if there are infected files found on the system. 

-->System Backup : This script is used to backup files to a particular hard drive.

-->Diagnose script : Uses linux built-ins to print out system information. Can print information for: BIOS, CPU, Hard Drive, Firewall, GPU, Interface, Memory, Motherboard, OS, User.

-->Encryption Script : Encrypts/Decrypts files/directories with password protection. Uses 'gpg' command with 256-bit encryption. Also uses 'shred' command to delete unencrypted version of files/directories left behind. 

--> VPN/SSH Connection : This script uses OpenVPN and SSH/SFTP to securely and easily tunnel into a different computer. 

--> Anonymous Browser : Uses Proxychains to route web traffic through 5 different high-anonymity proxies in other countries.  
