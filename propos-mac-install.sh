brew install git curl gcc pkg-config libssl-dev openssl sqlite python pip3
pip3 install --upgrade pip
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
rustup default 1.32.0
rustup component add clippy
rustup component add rustfmt
pip3 install toml mock responses