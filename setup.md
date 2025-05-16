# How to setup a devcontainer

Dev Containers run in a predefined directory on the system. This serves as the "repo". The directory must include a `.devcontainer`-directory. This directory containes the configuration for the Dev container. 

## Fedora Atomic

On immutable OS's, different installation methods are available. 

1. Using containers (toolbox/distrobox)
2. Package-layering dependencies via `rpm-ostree` and using an AppImage
3. Direct installation in the users home directoty (the method I choose for now)

### In the users home directory

I set the DevPod-Cli in the users home directory via `curl -L -o ~/bin/devpod "https://github.com/loft-sh/devpod/releases/latest/download/devpod-linux-amd64"` and `chmod +x ~/bin/devpod`. This must be added to PATH: `echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc`. Then source the `.bashrc` via `source ~/.bashrc`

To be able to use the `foot`-terminal with ssh to devcontainers the `terminfo` has to be copied this can be done by creating a `foot.terminfo`-file via `infocmp -x foot > foot.terminfo` and copy it into the devcontainer via `scp foot.terminfo <DEVPOD-NAME>:~/`
