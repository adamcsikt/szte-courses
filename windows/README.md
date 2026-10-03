# Windows 10 LTSC Development VM
> **Note:** If you want to run this VM independently without the `uni-infra` host network, please refer to the [Standalone Configuration](README-standalone.md).

This container provisions a fully hardware-accelerated Windows 10 LTSC virtual machine using KVM passthrough. It is attached to the shared university bridge network, allowing direct access to the isolated PostgreSQL and NGINX containers running on the host.

## Prerequisites

1. **Host Network:** The `uni-infra` master project must be running first to establish the `uni-infra_public-network` bridge.
2. **KVM Enabled:** The host must support and have KVM enabled (`/dev/kvm`).
3. **Drive Health / Btrfs Configuration (Fedora/Linux):** 
   If the host uses the Btrfs file system, you **must** disable Copy-on-Write (CoW) on the storage folder before the VM disk is generated. Because a virtual machine disk is a massive, constantly changing file, CoW causes severe disk fragmentation. This cripples IO performance and causes excessive write amplification that rapidly burns out your SSD's lifespan.

    ```bash
    mkdir win_storage_docker
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

## Advanced Configuration Flags Explained

* **`CPU_MODEL` Configuration Strategies**: This variable dictates how the KVM hypervisor presents your physical processor to the Windows guest OS.
  * **When to use `host` (The Standard Choice):** For most users, and on standard hardware, you should set `CPU_MODEL: "host"`. This passes your exact physical processor directly through to the VM, providing near bare-metal performance.
  * **When to use a specific architecture (e.g., `"EPYC-Milan"`):** You must manually specify an architecture if your physical CPU is significantly newer than the guest operating system. For example, running an older Windows 10 LTSC build on a newer Ryzen CPU can result in Blue Screens (BSOD), boot loops, or missing instruction sets because the older Windows kernel does not recognize the new CPU's microcode. By setting it to `"EPYC-Milan"` (a highly stable, feature-rich AMD Zen 3 server architecture), KVM translates the newer Ryzen CPU's power into a format that the older Windows OS natively understands and can fully optimize for. If you encounter similar OS-age conflicts on a new Intel chip, you would use an Intel equivalent like `"Cascadelake-Server"`.
* **`cap_add: - NET_ADMIN`**: Docker containers are locked down by default and cannot modify network routing. The Windows VM requires internal virtual network adapters (TAP interfaces/bridges) to actually connect the guest operating system to the internet. The `NET_ADMIN` capability grants the container the specific Linux permissions required to create and manage these virtual networking devices.

## Access

* **Remote Desktop (RDP):** `localhost:3389`
* **Web UI (VNC):** `http://localhost/windows/` (Routed via NGINX)
* **Shared Folders:** Host folders mapped with the `:z` flag will appear in Windows under the `\\host.lan\` network drive.
  * **What is the `:z` flag?** This is required on Linux distributions that enforce **SELinux** security policies (such as Fedora, RHEL, and CentOS). It instructs SELinux to automatically relabel the host directory's security context, explicitly granting the Docker container the legal rights to read and write to those files. Without the `:z` flag, SELinux will silently block the VM from interacting with the shared folder.
