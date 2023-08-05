# Utility Documentation
Oh, hello there.

This is a Markdown file documenting the structure of the utility.

The overall architecture of the FABS utility is based on a fairly standard MVC (model-view-controller) architecture. 

## Folders
Here is what the various folders within the utility hold:

0. **Root Directory**
    * The root directory holds general config files for the utility, the initial `main.py` file used to execute the utility, and the README file.
1. **API**
    * Because CML/EVE/GNS3 present their lab/topology data so differently, there are components in this utility that are specific to the network emulation platform that:
        * Gather the lab data
        * Gather the topology data
        * Most importantly: standardize the data before being passed onto other functions/methods within the utility
2. **Config**
3. **Data**
    * This folder holds miscellaneous/temporary data files that various functions within the utility require to function, including communication between various utility functions. Clearing the contents of this folder essentially clears the state of the utility.
4. **Device**
5. **Docs**
6. **Intent**

