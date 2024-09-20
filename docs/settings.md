# Syntax for settings.yaml

Reference the tables below for the valid configuration parameters that may be included in `settings.yaml`. **If a parameter is required, with no default value, an error will be thrown if FABS attempts to reference a non-existent parameter.**

If you want to see an example of what `settings.yaml` should look like, see the example `data/user/settings.default.yaml` file. You can even copy this file and rename the copy to `settings.yaml` if you want to use it as a base!

## Hierarchy

Parent: `settings:` (`settings.yaml` must start with this)
| Keyword | Description |
| ------- | ----------- |
| `lab` | Defines lab settings |
| `links` | List of links to be created between devices in the lab topology. **Only used if `lab: linkSource: manual` is set, ignored otherwise**. *Requires common Layer 2 segment between devices - links are created using virtual 802.1Q subinterfaces* |

## Lab Settings

| Keyword | Valid Options | Required? | Default Value | Description |
| ------- | ------------- | --------- | ------------- | ----------- |
| `platform` | `cml`, `eveng`, `gns3`| Yes | None | Defines the network emulation platform that the lab is running in |
| `emulatorAddress` | IPv4/IPv6 address or DNS name | Yes | None | Defines the IP address/DNS name for the network emulator host for FABS to interact with via API |
| `emulatorAuthMethod` | `settings`, `env`, `runtime` | Yes | None | Defines the method used to provide FABS with network emulator credentials - `settings` uses the plain-text definition of the username/password in `settings.yaml` (see `emulatorUser` and `emulatorPass` parameters), `env` uses the `FABS_EMULATOR_USER` and `FABS_EMULATOR_PW` environment variables, and `runtime` allows you to type in the credentials every time FABS runs using the `--username` and `--password` parameters |
| `emulatorUser` | String; username | Yes, **if `emulatorAuthMethod` is set to `settings`**; No, otherwise | None | Defines the username FABS uses to communicate with the network emulator via API |
| `emulatorPass` | String; password | Yes, **if `emulatorAuthMethod` is set to `settings`**; No, otherwise | None | Defines the password FABS uses to communicate with the network emulator via API **in plain-text**. |
| `linkSource` | `topology`, `manual` | No | `topology` | Defines the method FABS uses to gather link data (getting the links directly from the topology or from the `links` hierarchy in settings.yaml) |

## Link Settings
