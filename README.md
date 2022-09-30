# plusclouds-cli

PlusClouds command line interface (CLI) aims to be the command-line tool to access offered services and features. After user validation through a token taken from the PlusClouds website,  users can create domains, virtual machines, virtual disk images, cloud storage, virtual network cards, networks, datacenter nodes, network pools, and storage. Users can also list existing operational services and features that PlusClouds provides and show currently registered credit cards, countries, addresses, accounts, categories, and many more. Apart from creating services and listing existing information, the system can connect to virtual machines created in the PlusClouds ecosystem through SSH, allowing users to create, view, and manage services through CLI.

#### To initiate this repository please execute the following command:

```shell
python3 -m pip install -r requirements.txt
```

#### To test the repository execute the following script

```shell
 python3 -m pytest tests/
```

#### To execute the file
```shell
python3 -m plusclouds
```
