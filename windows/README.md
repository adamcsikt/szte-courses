# Windows 10 LTSC Development VM

This container provisions a fully hardware-accelerated Windows 10 LTSC virtual machine using KVM passthrough. It is attached to the shared university bridge network, allowing direct access to the isolated PostgreSQL and NGINX containers running on the host.

## Prerequisites

1. **Host Network:** The `uni-infra` master project must be running first to establish the `uni-infra_public-network` bridge.
2. **KVM Enabled:** The host must support and have KVM enabled (`/dev/kvm`).
3. **Drive Health / Btrfs Configuration (Fedora/Linux):** 
   If the host uses the Btrfs file system, you **must** disable Copy-on-Write (CoW) on the storage folder before the VM disk is generated. Because a virtual machine disk is a massive, constantly changing file, CoW causes severe disk fragmentation. This cripples IO performance and causes excessive write amplification that rapidly burns out your SSD's lifespan.

    ```bash
    sudo chattr +C win_storage_docker
    ```

## Usage

**Initial Build (Must be run from this folder):**
    
    docker compose up -d

**Daily Usage (Run from anywhere on the host):**

    docker compose -p windows start
    docker compose -p windows stop

**⚠️ Warning on `down` vs `stop`:**
Always use `start/stop` for daily management. If you use `docker compose -p windows down`, Docker completely destroys the container and erases its hidden metadata. If you then try to run `docker compose -p windows up` from another folder, it will fail because Docker no longer has the container metadata to know where the actual `.yml` file is located to rebuild it.

## Access

* **Remote Desktop (RDP):** `localhost:3389`
* **Web UI (VNC):** `http://localhost/windows/` (Routed via NGINX)
* **Shared Folders:** Host folders mapped with the `:z` flag will appear in Windows under the `\\host.lan\` network drive.
  * **What is the `:z` flag?** This is required on Linux distributions that enforce **SELinux** security policies (such as Fedora, RHEL, and CentOS). It instructs SELinux to automatically relabel the host directory's security context, explicitly granting the Docker container the legal rights to read and write to those files. Without the `:z` flag, SELinux will silently block the VM from interacting with the shared folder.
