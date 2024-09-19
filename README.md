## **WARNING: This project isn't finished yet. Still in development. It's public for the sole purposes of code review. Basically nothing below about how to use this utility or what it supports is accurate yet.**

# Forget About the Boring Stuff (FABS)
You can replace "stuff" with...your favorite s-word :D

Have you ever wanted to create a large lab with Cisco IOS-XE/IOS-XR/NX-OS or Juniper JunOS and spent an inordinate amount of time copying basic IP configuration and IGP configs just to get to the part where you can finally START labbing what you want?

> CCIEs/CCIE candidates, you feel me here. "I want to lab some advanced BGP/MPLS stuff! Oh, great, time to configure 10,000 IP addresses for the 10,000th time!"

Not any more! Meet FABS, your automated assistant. It can slice, it can dice-

---
Alrighty, jokes aside. FABS is a command line and API utility built to bootstrap your networking labs and help you stop wasting time doing boring stuff you already know how to do, allowing you to focus on learning what you're trying to learn in the first place.

No GUI? Yep. I was too lazy to build one :)

> **NOTE**: This utility is not designed to be used to help you skip the fundamentals. Fundamentals are important. If you still need practice configuring interface IP addresses, *you shouldn't use this utility yet.*

FABS is built to integrate with the following network emulation solutions:
* CML
* EVE-NG
* GNS3

FABS currently supports the following network operating systems:
* Cisco
    * IOS-XE
    * IOS-XR
    * NX-OS
* Juniper
    * Junos (non-Evolved)

---
### The following functionality is currently available:
* Query the API of your network emulation solution to find the lab and gather topology data
* Assign IP addresses to point-to-point and multi-access links within the topology (subinterfaces/multiple logical VLAN interfaces are supported!)
* Generate mass loopback interfaces with dummy IP addresses for lab use
* Configure IGP (single-area OSPF, single-area IS-IS, Cisco EIGRP)
* Configure BGP (eBGP/iBGP peerings, network advertisement, route reflectors)
* Configure MPLS L3VPN (IPv4 + IPv6 6PE/6VPE)
* Configure MPLS L2VPN (Carrier Ethernet + VPLS + EVPN)


### The following functionality is planned:
* Allow import of Jinja2 templates to generate configurations for custom/non-predefined network operating systems
* Implement support for ArubaOS, Arista EOS, MikroTik RouterOS, and some other network operating systems
* Configure Layer 2 features (VLANs, trunks, STP, etc) - currently, only Layer 3 technologies are supported. See above for more details.
* Expand Layer 3 functionality

---
## How do you use FABS?

Before you use FABS, make sure you have the following prerequisite components installed onto your system:
* Python 3
* pip
    * FABS requires certain Python modules to be installed in order to properly function. There is a `requirements.txt` file that contains a list of Python module requirements. To install all necessary Python modules, navigate to this folder in your command line and run `python -m pip install -r requirements.txt`. You may need to change `python` to something else, like `python3`, based on your installation.
* Git 

Afterwards, it's simple! First, clone this repository to your local system as a folder. You can do this by using the following command in your command line: `git clone https://github.com/kelvintechie1/fabsutil.git`

After cloning the repository, open up the `settings.yaml` file in the `settings` folder and modify the configuration for the utility. Reference the `settings.md` file in the `docs` folder to find the valid parameters within the settings YAML file.

With your `settings.yaml` file properly configured, you can run the `main.py` file in the root directory to launch the utility. Note that there are command-line flags available. Run `main.py -?` to obtain more information pertaining the flags. **No flags are required to execute the utility in interactive mode.**

---
### Developer Info
**Kelvin Tran** - CBT Nuggets Trainer\
[LinkedIn](https://www.linkedin.com/in/tran-kelvin)\
[CBT Nuggets](https://www.cbtnuggets.com/trainers/kelvin-tran)\
[Twitter](https://www.twitter.com/kelvintechie)