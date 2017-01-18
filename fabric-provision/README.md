# README

Currently the `fabfile.py` uses `~/.ssh/id_rsa.pub` located in `config.py`.
I am purposesly ignoring dynamic inventory so I can read DockerCloud hosts since at
the time their API lacks some needed information.

## Install
You need a few requirements on your host machine. Do omit `-r` to read the file.
```
pip install -r requirements.txt
```

## Folders and Files
These are the purposes of the folders and files

- `/client` - Stores the API Client(s)
- `/dynamic_hosts` - Stores the generated Python files for all host IP's to use for Fabric
- `config.py` - Keeps the API keys and configure folder paths
- `fabfile.py` - Python fabric, which is run with `fab <command>`
- `requirements.txt` - The required Python packages


## Get Hosts on Docker Cloud
Run the `app.py` to call a REST API for all IP's.
This generates or updates the Python file `/dynamic_hosts/<dockercloud|digitalocean>.py` which is read within the `fabfile.py`.

```
./app.py digitalocean
./app.py dockercloud
```

## Run Command across all Hosts

Edit `fabfile.py` and add or remove `run()` commands.

Example usage:
```
fab test
```

You can create your own methods as well. Using Parallel decorator is 10x faster, eg:
```
@parallel
def update():
    run('apt-get update')
```

To run the above you simply run:
```
fab update
```

## Troubleshooting

If you get connection or SSH errors, ensure you have your key added to the Docker Droplet. You may need to ask someone with an existing key to add your `pubkey`.
