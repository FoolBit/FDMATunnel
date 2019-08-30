# TUNTAP
IFF_TUN		= 0x0001   # tunnel IP packets
IFF_TAP		= 0x0002   # tunnel ethernet frames
IFF_NO_PI	= 0x1000   # don't pass extra packet info
IFF_ONE_QUEUE	= 0x2000   # beats me ;)
TUNSETIFF = 0x400454ca
TUN_IP = "10.0.0.1"

SRC_ADDR = "10.0.0.1"

# USRP params
NUM_USRP = 2
ADDR_USRPS = ["addr=192.168.10.2", "addr=192.168.10.4"]	# ip
TXFREQ_USRPS = [900000000.0, 20000000000.0]			    # frequence 900M/2G
RXFREQ_USRPS = [9000000.0, 20000000000.0]			    # frequence 900M/2G
BAND_USRPS = [4000000.0, 4000000.0]		                # bandwidth 4M

# -------- UD params -------
# trans data by USRP 1/2
DEST_ADDRS = ["10.0.0.2", "10.0.0.3"]

# packet params
HEADER_LEN = 10

CTL_NORM = 0
CTL_ACK = 1
CTL_CHANGE_BW = 2
CTL_DUMMY = 3

# ARQ params
WAIT_INTERVAL = 0.016

# debug
DEBUG = 0
