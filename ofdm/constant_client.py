# TUNTAP
IFF_TUN		= 0x0001   # tunnel IP packets
IFF_TAP		= 0x0002   # tunnel ethernet frames
IFF_NO_PI	= 0x1000   # don't pass extra packet info
IFF_ONE_QUEUE	= 0x2000   # beats me ;)
TUNSETIFF = 0x400454ca
TUN_IP = "10.0.0.1/24"

SRC_ADDR = "10.0.0.1"

# USRP params
ADDR_USRP = "addr=192.168.10.4"	# ip 
TXFREQ_USRP = 2000000000.0			# frequence 900M
RXFREQ_USRP = 3800000000.0			# frequence 900M
BAND_USRP = 4000000.0			# bandwidth

# packet params
HEADER_LEN = 10

CTL_NORM = 0
CTL_ACK = 1
CTL_CHANGE_BW = 2
CTL_DUMMY = 3

# server
DEST_ADDR = "10.0.0.2"

# ARQ params
WAIT_INTERVAL = 0.016

# denug
DEBUG = 0

