# Creating Dev Containers in VS Code

In software development, it is common to use Dev Containers within VS Code. Microsoft provides a full guid on how to use and install Dev Containers in VS Code in their [documentation for Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers).
However, to create a basic container within VS Code, only the following steps are required:

1. Install the "Dev Containers" extension
2. Type "_> New Dev Container_" into the search-bar
3. From the new selection window, select a container for the environment you want to work in, e.g "Python 3". After confirming a container is created and the environment is set-up wihtin it. After the creation is done, a full environment is ready to use.

## Configuring the Dev Container

Dev Containers can be configured for specfic need through the `devcontainer.json` in the `.devcontainer`-directory. The parameters that can be set are documented in the [specification](https://containers.dev/implementors/spec/) along with the [reference](https://containers.dev/implementors/json_reference/) which lists the possible properties.

## Workarounds

As I am using an immutable distro ([Fedora Sway Atomic](https://fedoraproject.org/atomic-desktops/sway/)). The standrad way to install application on this distro is done through Flatpak. These have limited access to the host. I followed [David Sebeks's excellent guide](https://howtos.davidsebek.com/vscodium-containers.html) to set it up.


