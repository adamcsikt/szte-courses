# Standalone Windows 10 LTSC VM

This container provisions a fully hardware-accelerated Windows 10 LTSC virtual machine using Docker and KVM passthrough. 

## Standalone `docker-compose.yml` Configuration
Unlike the monorepo setup, this standalone version uses Docker's default bridge network and exposes ports directly to the host.

```yaml
services:
  windows:
    image: dockurr/windows
    container_name: windows10-ltsc
    privileged: true
    environment:
      VERSION: "10l"
      RAM_SIZE: "6G"
      CPU_CORES: "4"
      CPU_MODEL: "EPYC-Milan"
      TZ: "Europe/Budapest"
    devices:
      - /dev/kvm
    cap_add:
      - NET_ADMIN
    ports:
      - 8006:8006          # Re-exposed for standalone Web UI access
      - 3389:3389/tcp
      - 3389:3389/udp
    volumes:
      - ./win_storage_docker:/storage
      - ./shared_folder:/shared:z
      - ./oem:/oem:z
    stop_grace_period: 2m
```

## Prerequisites

1. **KVM Enabled:** The host system must support and have KVM enabled (`/dev/kvm`).
2. **Drive Health / Btrfs Configuration (Fedora/Linux):** 
   If the host uses the Btrfs file system, you **must** disable Copy-on-Write (CoW) on the storage folder before the VM disk is generated. Because a virtual machine disk is a massive, constantly changing file, CoW causes severe disk fragmentation. This cripples IO performance and causes excessive write amplification that rapidly burns out your SSD's lifespan.

    ```bash
    mkdir win_storage_docker
    sudo chattr +C win_storage_docker
    ```

## Usage

Because this VM is resource-heavy (4 Cores, 6GB RAM), it should be managed using the project name flag (`-p windows`). This feature allows you to control the VM from any terminal directory on your host without needing to `cd` into the folder where this `docker-compose.yml` file lives.

**Initial Build (Must be run from this folder):**
    
    docker compose up -d

**Daily Usage (Run from anywhere on the host):**

    docker compose -p windows start
    docker compose -p windows stop

**⚠️ Warning on `down` vs `stop`:**
Always use `start/stop` for daily management. If you use `docker compose -p windows down`, Docker completely destroys the container and erases its hidden metadata. If you then try to run `docker compose -p windows up` from another folder, it will fail because Docker no longer has the container metadata to know where the actual `.yml` file is located to rebuild it.

## Advanced Configuration Flags Explained

* **`CPU_MODEL` Configuration Strategies**: This variable dictates how the KVM hypervisor presents your physical processor to the Windows guest OS.
  * **When to use `host` (The Standard Choice):** For most users, and on standard hardware, you should set `CPU_MODEL: "host"`. This passes your exact physical processor directly through to the VM, providing near bare-metal performance.
  * **When to use a specific architecture (e.g., `"EPYC-Milan"`):** You must manually specify an architecture if your physical CPU is significantly newer than the guest operating system. For example, running an older Windows 10 LTSC build on a newer Ryzen CPU can result in Blue Screens (BSOD), boot loops, or missing instruction sets because the older Windows kernel does not recognize the new CPU's microcode. By setting it to `"EPYC-Milan"` (a highly stable, feature-rich AMD Zen 3 server architecture), KVM translates the newer Ryzen CPU's power into a format that the older Windows OS natively understands and can fully optimize for. If you encounter similar OS-age conflicts on a new Intel chip, you would use an Intel equivalent like `"Cascadelake-Server"`.
* **`cap_add: - NET_ADMIN`**: Docker containers are locked down by default and cannot modify network routing. The Windows VM requires internal virtual network adapters (TAP interfaces/bridges) to actually connect the guest operating system to the internet. The `NET_ADMIN` capability grants the container the specific Linux permissions required to create and manage these virtual networking devices.

## Access

* **Remote Desktop (RDP):** `localhost:3389`
* **Web UI (VNC):** `http://localhost:8006`
* **Shared Folders:** Host folders mapped with the `:z` flag will appear in Windows under the `\\host.lan\` network drive.
  * **What is the `:z` flag?** This is required on Linux distributions that enforce **SELinux** security policies (such as Fedora, RHEL, and CentOS). It instructs SELinux to automatically relabel the host directory's security context, explicitly granting the Docker container the legal rights to read and write to those files. Without the `:z` flag, SELinux will silently block the VM from interacting with the shared folder.
