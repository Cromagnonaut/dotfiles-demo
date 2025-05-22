FROM mcr.microsoft.com/devcontainers/base:ubuntu-24.04

# This copies the mise binary from the mise container and copies it to the local container
COPY --from=jdxcode/mise /usr/local/bin/mise /usr/local/bin 

# make sure mise is activated in both zsh and bash. Might be overridden by a user's dotfiles.
RUN echo 'eval "$(mise activate bash)"' >> /home/vscode/.bashrc && \
  echo 'eval "$(mise activate zsh)"' >> /home/vscode/.zshrc
