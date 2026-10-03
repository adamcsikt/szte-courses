# Windows 10 LTSC Development VM

This container provisions a fully hardware-accelerated Windows 10 LTSC virtual machine using KVM passthrough. It is attached to the shared university bridge network, allowing direct access to the isolated PostgreSQL and NGINX containers running on the host.

## Prerequisites

1. **Host Network:** The `uni-infra` master project must be running first to establish the `uni-infra_public-network` bridge.
2. **KVM Enabled:** The host must support and have KVM enabled (`/dev/kvm`).
3. **Btrfs Optimization (Fedora/Linux):** 
   If the host uses Btrfs, you **must** disable Copy-on-Write (CoW) on the storage folder before the VM disk is generated to prevent severe IO fragmentation.

    sudo chattr +C win_storage_docker

## Usage

Because this VM is resource-heavy (4 Cores, 6GB RAM), it should be started and stopped by project name to preserve the metadata without destroying the container.

**Initial Build (Run from this folder):**
    
    docker compose up -d

**Daily Usage (Run from anywhere on the host):**

    docker compose -p windows start
    docker compose -p windows stop

## Access

* **Remote Desktop:** `localhost:3389`
* **Web UI (VNC):** `http://localhost:8006`
* **Shared Folders:** Host folders mapped with the `:z` flag will appear in Windows under the `\\host.lan\` network drive.
