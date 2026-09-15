# Kali 官方文档全量索引

从 <https://www.kali.org/docs/> 同步的 **270** 篇官方文档，按官方章节组织。每篇给出标题、原文链接与内文标题大纲，便于定位。

> 本文件由 `scripts/fetch_kali_docs.py` 自动生成。配套的中文精读笔记见本目录其余 `NN-*.md` 文件。

## 章节速览

| 章节 | 中文 | 篇数 | 说明 |
|------|------|------|------|
| [introduction](#introduction) | 介绍 | 12 | Kali 是什么、能做什么、版本与政策 |
| [installation](#installation) | 安装 | 10 | 镜像获取、安装方式、加密磁盘、USB 启动 |
| [general-use](#general-use) | 常规使用 | 30 | sudo、SSH、桌面环境、软件源、Python、显卡驱动 |
| [tools](#tools) | 工具相关 | 7 | 工具分类说明与 metapackage 结构 |
| [virtualization](#virtualization) | 虚拟化 | 22 | VirtualBox / VMware / Hyper-V / QEMU / Docker / WSL |
| [containers](#containers) | 容器 | 5 | Docker、Podman 与容器化 Kali |
| [cloud](#cloud) | 云环境 | 4 | AWS / Azure / Linode 等云上 Kali |
| [wsl](#wsl) | WSL | 5 | Windows Subsystem for Linux 中的 Kali |
| [usb](#usb) | USB 启动 | 10 | 制作启动盘、持久化存储、加密持久化 |
| [arm](#arm) | ARM 与单板机 | 43 | 树莓派、ARM 设备、chroot |
| [nethunter](#nethunter) | Kali NetHunter | 53 | 移动端渗透平台 |
| [nethunter-pro](#nethunter-pro) | NetHunter Pro | 2 | NetHunter Pro 设备与用法 |
| [development](#development) | 开发与打包 | 21 | Debian 打包、Kali 源码、贡献流程 |
| [troubleshooting](#troubleshooting) | 故障排查 | 12 | 常见问题、显卡、网络、双系统 |
| [policy](#policy) | 政策与法律 | 10 | 使用政策、商标、法律边界 |
| [community](#community) | 社区 | 8 | 论坛、Discord、参与方式 |
| [(根)](#root) | 根文档 | 16 | 文档入口页 |

## 介绍（`introduction`）

Kali 是什么、能做什么、版本与政策 · 共 **12** 篇

### [Download Kali Linux Images Securely](<https://www.kali.org/docs/introduction/download-images-securely/>)

摘要：When you download an image, be sure to download the SHA256SUMS and SHA256SUMS.gpg files that are next to the downloaded image (i.e. in the same directory on the Kali Linux Download Server ). Before ve…

### [Downloading Kali Linux](<https://www.kali.org/docs/introduction/download-official-kali-linux-images/>)

摘要：IMPORTANT! Never download Kali Linux images from anywhere other than the official sources. Always be sure to verify the SHA256 checksums of the file you’ve downloaded against our official values . It …

### [Kali ARM History](<https://www.kali.org/docs/introduction/kali-on-arm-a-bit-of-history/>)

摘要：When BackTrack ARM first came out, it was one image, for a Motorola Xoom. The work was done on the Xoom itself by @muts . He started from an Ubuntu image for it, built all of the packages for BackTrac…

### [Kali Linux History](<https://www.kali.org/docs/introduction/kali-linux-history/>)

摘要：Kali Linux is based on years of knowledge and experience of building a pentestion testing Operating Systems, which has spanned over multiple previous projects. During all these project’s life-time, th…

### [Kali Linux Image Overview](<https://www.kali.org/docs/introduction/kali-linux-image-overview/>)

摘要：Below is an overview of where you can get Kali Linux that is kept up-to-date when a new platform or system is added. Each entry that has a Kali docs page available will have their page linked. WSL doe…

### [Kali NetHunter History](<https://www.kali.org/docs/introduction/kali-nethunter-history/>)

摘要：Kali NetHunter is a custom OS for Android devices. This takes Kali Linux desktop and makes it mobile. Kali NetHunter is made up of three parts: ROM App (and AppStore) Kali Chroot Kali NetHunter was fi…

### [Kali Press Release](<https://www.kali.org/docs/introduction/press-release/>)

内文小节：`Introducing Kali Linux` · `Pricing and Availability` · `About Kali Linux` · `About OffSec`

摘要：Introducing Kali Linux Free All-in-One Solution for Professional Security Auditing Popular BackTrack Linux Evolves Into Mature, Enterprise-Ready Penetration Testing Toolkit. Black Hat Europe, Amsterda…

### [Kali Undercover](<https://www.kali.org/docs/introduction/kali-undercover/>)

摘要：Kali Undercover is a set of scripts that change the theme of your Kali Linux to a Windows 10 alike theme. It was released with Kali Linux 2019.4 with an important concept in mind, to hide in plain sig…

### [Kali's Default Credentials](<https://www.kali.org/docs/introduction/default-credentials/>)

内文小节：`Default Tool Credentials`

摘要：Kali changed to a non-root user policy by default since the release of 2020.1 . This means: During the installation of amd64 images , it will prompt you for a standard user account to be created. Any …

### [Should I Use Kali Linux?](<https://www.kali.org/docs/introduction/should-i-use-kali-linux/>)

摘要：What’s Different About Kali Linux? Kali Linux is specifically geared to meet the requirements of professional penetration testing and security auditing. To achieve this, several core changes have been…

### [What is Kali Linux?](<https://www.kali.org/docs/introduction/what-is-kali-linux/>)

内文小节：`About Kali Linux` · `Kali Linux Features`

摘要：About Kali Linux Kali Linux (formerly known as BackTrack Linux ) is an open-source , Debian-based Linux distribution which allows users to perform advanced penetration testing and security auditing. I…

### [Which Image Should I Download?](<https://www.kali.org/docs/introduction/what-image-to-download/>)

摘要：In this section, we will describe the process of installing Kali Linux on 64-bit hardware using the images published on the Kali Linux download page . Content Which image to choose Which desktop envir…


## 安装（`installation`）

镜像获取、安装方式、加密磁盘、USB 启动 · 共 **10** 篇

### [Bare-bones Kali](<https://www.kali.org/docs/installation/barebone-kali/>)

内文小节：`Installing a bare-bones Kali`

摘要：Kali traditionally has been solely recommended as a penetration testing distribution, and for good reason. However, through the years Kali has become more stable and evolved into something that users …

### [BTRFS Install (Kali Unkaputtbar)](<https://www.kali.org/docs/installation/btrfs/>)

摘要：Have you ever wished you could travel back in time after deleting that all important customer report or installing a broken driver just before heading into the board meeting? Well, you better read on,…

### [Deploying Kali over Network PXE Install](<https://www.kali.org/docs/installation/network-pxe/>)

内文小节：`Manually setting up a PXE Server with dnsmasq` · `Download Kali PXE Netboot Images` · `Configure Target to Boot From Network` · `Troubleshooting` · `Post Installation` · `Pre-seeding PXE` · `Using netbootxyz to host our PXE files`

摘要：It is possible to boot and installing Kali Linux over the network, using Preboot eXecution Environment ( PXE ). There is a range of environments where this beneficial such as a single laptop install w…

### [Dual Booting Kali with Linux](<https://www.kali.org/docs/installation/dual-boot-kali-with-linux/>)

内文小节：`Installation Prerequisites` · `Resize Linux Procedure` · `Kali Linux Installation Procedure` · `Post Installation`

摘要：Installing Kali Linux alongside another Linux installation can be quite useful. However, you need to exercise caution during the setup process. First, make sure that you’ve backed up any important dat…

### [Dual Booting Kali with macOS/OS X](<https://www.kali.org/docs/installation/dual-boot-kali-with-mac/>)

内文小节：`Installation Prerequisites` · `Resize macOS/OS X Procedure` · `Kali Linux Installation Procedure` · `Installing rEFInd` · `Configuring rEFInd` · `Post Installation`

摘要：IMPORTANT! Newer Mac hardware (e.g. T2/Apple Silicon) do not run Linux well, or at all. This is true for Linux in general , not just Kali Linux. The model & year of the device will determine how succe…

### [Dual Booting Kali with Windows](<https://www.kali.org/docs/installation/dual-boot-kali-with-windows/>)

内文小节：`Installation Prerequisites` · `Resize Windows Procedure` · `Kali Linux Installation Procedure` · `Post Installation`

摘要：Installing Kali Linux next to a Windows installation has its benefits. However, you need to exercise caution during the setup process. First, make sure that you’ve backed up any important data on your…

### [Installing Kali Linux](<https://www.kali.org/docs/installation/hard-disk-install/>)

内文小节：`System Requirements` · `Installation Prerequisites` · `Preparing for the Installation` · `Kali Linux Installation Procedure` · `Post Installation`

摘要：Installing Kali Linux (single boot) on your computer is an easy process. This guide will cover the basic install (which can be done on bare metal or guest VM ), with the option of encrypting the parti…

### [Installing Kali on Mac Hardware](<https://www.kali.org/docs/installation/hard-disk-install-on-mac/>)

内文小节：`Installation Prerequisites` · `Kali Linux Installation Procedure` · `Kali Linux Installation Procedure` · `Troubleshooting macOS/OS X` · `Post Installation`

摘要：IMPORTANT! Newer Mac hardware (e.g. T2/M1 chips) do not run Linux well, or at all. This is true for Linux in general , not just Kali Linux. The model & year of the device will determine how successful…

### [Installing old i386 images](<https://www.kali.org/docs/installation/installing-old-i386/>)

内文小节：`Foreword` · `Using old i386 images`

摘要：Foreword Since October 2024, there is no longer a i386 kernel, nor i386 images for Kali Linux. As a reminder, i386 is the name used in Kali (and Debian) to refer to the 32-bit x86 CPU architecture. In…

### [Kali Installation Sizes](<https://www.kali.org/docs/installation/installation-sizes/>)

摘要：Kali has a lot of customization that can be done during the package selection part of installation. Specifically, there are a total of 20 ways to configure your system during package selection. To hel…


## 常规使用（`general-use`）

sudo、SSH、桌面环境、软件源、Python、显卡驱动 · 共 **30** 篇

### [All about sudo](<https://www.kali.org/docs/general-use/sudo/>)

内文小节：`Sudo on Kali` · `In use`

摘要：Non-root user With 2020.1 Kali has swapped to a privileged non-root user by default. This means that root has no password set, and the account created during installation is the one to use. It is poss…

### [Configuring Yubikeys for SSH Authentication](<https://www.kali.org/docs/general-use/configuring-yubikeys-for-ssh-authentication/>)

摘要：This document explains how to configure a Yubikey for SSH authentication Prerequisites Install Yubikey Personalization Tool and Smart Card Daemon kali@kali:~$ sudo apt install -y yubikey-personalizati…

### [Enabling Root](<https://www.kali.org/docs/general-use/enabling-root/>)

内文小节：`Permanent vs temporary usage` · `Enabling the root account` · `Enabling root for SSH` · `Enabling root for GNOME and KDE login`

摘要：Permanent vs temporary usage There are some cases where you may need to use superuser, root, for an extended period of time. In these cases we can easily access the root account with a simple sudo su …

### [Everything you need to know about the switch to Python 3](<https://www.kali.org/docs/general-use/python3-transition/>)

内文小节：`About the transition` · `Keeping backwards compatibility in Kali` · `Frequently Asked Questions`

摘要：About the transition Kali Linux fully switched to Python 3. This means that any tool packaged by Kali that was using Python 2 has been either dropped or converted to use Python 3. Any tool converted t…

### [Fixing DPI (Dots Per Inch) / Large Fonts](<https://www.kali.org/docs/general-use/fixing-dpi/>)

内文小节：`Issue` · `Locating the Problem` · `Why is it wrong?` · `Finding the correct value` · `Fixing` · `References`

摘要：Upon starting Kali Linux up, certain things may appear larger than expected. This could be because of DPI ( Dots Per Inch ) / PPI ( Pixels Per Inch ) being incorrect. If things are looking smaller tha…

### [Get the latest unreleased features and bug fixes with Kali Bleeding Edge](<https://www.kali.org/docs/general-use/kali-bleeding-edge/>)

内文小节：`Introduction` · `Use cases` · `Ensure you have the latest version of a specific tool` · `Verify bug fixes committed by upstream authors` · `Caution: watch for the blood` · `How to enable the repository interactively` · `How to enable the repository programmatically` · `Install a package from kali-bleeding-edge` · `Switch back to the stable version`

摘要：Introduction kali-bleeding-edge is the name of a Kali repository that you can enable in your APT configuration to have access to packages built with the latest version of the source code found in the …

### [HiDPI (High Dots Per Inch) Display](<https://www.kali.org/docs/general-use/hidpi/>)

内文小节：`Desktop Environments - Xfce` · `Scaling Factor` · `Cursor size` · `Login Screen - LightDM`

摘要：Upon starting Kali Linux up, certain things ( Windows/buttons or text/font ) may appear smaller than expected . This could be because of HiDPI (aka High DPI ). It all depends on the software in questi…

### [Install NVIDIA GPU Drivers](<https://www.kali.org/docs/general-use/install-nvidia-drivers-on-kali-linux/>)

内文小节：`Prerequisites` · `Dedicated cards` · `Optimus cards` · `Installation` · `Dots Per Inch (DPI) & Pixels Per Inch PPI` · `Verify Driver Installation` · `Hashcat` · `Troubleshooting`

摘要：Live boot currently is not supported. The following documentation assumes an installed version of Kali Linux, whether that is a VM or bare-metal. This document explains how to install NVIDIA GPU drive…

### [Installing Python Applications via pipx](<https://www.kali.org/docs/general-use/python3-external-packages/>)

内文小节：`Introduction: say good-bye to pip install` · `Prefer installing packages and programs via APT` · `Not packaged in Kali? Too old in Kali? Install it with pipx` · `Pipx troubleshooting` · `Install pipx` · `Add ~/.local/sbin to the path`

摘要：Introduction: say good-bye to pip install Starting Kali Linux 2024.4 , using pip to install external Python packages is strongly discouraged . Instead, we recommend using pipx . On the surface, it pro…

### [Kali Branches](<https://www.kali.org/docs/general-use/kali-branches/>)

内文小节：`What is a Branch?` · `Kali Branches` · `Development` · `Branches Used to Assist With Other Branches` · `Mapping` · `Debian’s Relation` · `The kali-rolling Repository` · `The kali-dev Repository`

摘要：What is a Branch? A branch is an alternative version of some software, in this case of the Kali OS. Kali Linux has multiple branches which allows for users to decide how up-to-date their packages will…

### [Kali In The Browser (Guacamole)](<https://www.kali.org/docs/general-use/guacamole-kali-in-browser/>)

摘要：There are various ways you can interact with Kali, such as sitting down and being direct at the console (more often than not, for a graphic experience), alternatively using Kali remotely via SSH (whic…

### [Kali In The Browser (noVNC)](<https://www.kali.org/docs/general-use/novnc-kali-in-browser/>)

摘要：There are various ways you can interact with Kali, such as sitting down and being direct at the console (more often than not, for a graphic experience), alternatively using Kali remotely via SSH (whic…

### [Kali Linux Forensics Mode](<https://www.kali.org/docs/general-use/kali-linux-forensics-mode/>)

摘要：Kali Linux “Live” provides a “forensic mode”, a feature first introduced in BackTrack Linux . The “Forensic mode live boot” option has proven to be very popular for several reasons: Kali Linux is wide…

### [Kali Linux Metapackages](<https://www.kali.org/docs/general-use/metapackages/>)

内文小节：`System` · `Desktop environments/Window managers` · `Tools` · `Menu` · `Others`

摘要：What are metapackages Metapackages are used to install many packages at one time, created as a list of dependencies on other packages. Kali Linux uses these in a few ways. One way is allowing users to…

### [Kali Linux Xfce FAQ](<https://www.kali.org/docs/general-use/xfce-faq/>)

摘要：The new Kali Linux Desktop is incredibly fast and absolutely gorgeous. Here are some tips and tricks to help you find your way around it quickly. Topics Desktop Environments, Switching HiDPI Theme Ter…

### [Kali Network Repositories (/etc/apt/sources.list)](<https://www.kali.org/docs/general-use/kali-apt-sources/>)

内文小节：`Default APT Network Repositories Configuration` · `Modernizing the APT Network Repositories Configuration` · `Switching Kali Main Branch` · `Enabling Kali Additional Branches` · `Format of kali.sources and sources.list Files` · `Default Offline Install Values` · `Non-Kali Repositories` · `Mirrors` · `Source Repositories`

摘要：The topic of repositories is always a large one, and comes up frequently. It is an item which people often get wrong and confused with. Please take the time to read the information below and any refer…

### [Kali Preseed Examples](<https://www.kali.org/docs/general-use/kali-preseeding/>)

摘要：Being based off of Debian, Kali is able to utilize preseed files . To help explain the ways that these files can be used, and to provide usable preseed files, we have created a GitLab repo that contai…

### [Kali Training](<https://www.kali.org/docs/general-use/kali-training/>)

内文小节：`What can I do next?`

摘要：What is Kali Training? Kali Training is the official site for the book all about Kali – Kali Linux Revealed. Kali Training will allow you to go through the book’s material and take practice exams to t…

### [Kernel Configuration](<https://www.kali.org/docs/general-use/kernel-configuration/>)

内文小节：`WiFi injection (Patch)` · `dmesg unrestricted (sysctl)` · `Privileged ports (sysctl)` · `Misc (Patches)`

摘要：The Kali Linux kernel differs slightly from the “usual” kernel. For the purposes of penetration testing, we chose to use some defaults that differ from general-purpose Linux distributions, and we also…

### [OpenSSL Configuration](<https://www.kali.org/docs/general-use/openssl-configuration/>)

摘要：Since our release of Kali Linux 2021.3 OpenSSL has been configured for wider compatibility to allow Kali to talk to as many services as possible. This means that legacy protocols (such as TLS 1.0 and …

### [Packages That Behave Differently With Non-root](<https://www.kali.org/docs/general-use/nonroot-behavioral-differences-in-packages/>)

内文小节：`Nmap`

摘要：There are many packages that require privileged access to use. There are also packages that may run without privileged access but lose some of their functionality. This page will be continually update…

### [Resolving APT Errors Caused by an Expired Kali Linux Signing Key](<https://www.kali.org/docs/general-use/gpgkey-expiry/>)

内文小节：`The Issue` · `Preventing the Issue`

摘要：The Issue A GPG key is used to sign the repository to ensure authenticity, integrity and trust while updating the packages. Every 2-3 years, the Kali team either extends the lifetime of the GPG key us…

### [Samba Configuration](<https://www.kali.org/docs/general-use/samba-configuration/>)

摘要：Since our release of Kali Linux 2021.4 , the Samba client has been configured for wider compatibility to allow Kali to talk to as many Samba servers as possible. This means that legacy protocols (such…

### [Setting up RDP with Xfce](<https://www.kali.org/docs/general-use/xfce-with-rdp/>)

摘要：Kali Linux is supported on many different devices and systems. On some of those systems, you may only get a bare-bones install and occasionally may not have direct access to a GUI such as with WSL or …

### [SSH Configuration](<https://www.kali.org/docs/general-use/ssh-configuration/>)

内文小节：`SSH client: Wide Compatibility vs Strong Security` · `SSH client: Restoring removed functionality via the ssh1 package` · `SSH client: Support for GSS-API` · `SSH server: automatic host keys generation`

摘要：SSH client: Wide Compatibility vs Strong Security Since our release of Kali Linux 2022.1 it is possible to easily configure the SSH client for wider compatibility to allow Kali to talk to as many SSH …

### [Switching Desktop Environments](<https://www.kali.org/docs/general-use/switching-desktop-environments/>)

摘要：During install a user may select whichever desktop environment that they prefer. However, when using the official VM this is not a possibility. In these cases, and many others, a user may wish to chan…

### [Updating a Package](<https://www.kali.org/docs/general-use/updating-a-package/>)

内文小节：`Updating all Packages` · `Upgrading a specific Package`

摘要：To update a package in Kali Linux, you can use the package management tools provided by Debian, which Kali Linux is based on. The primary package management tool is apt. Regularly updating your system…

### [Updating Kali](<https://www.kali.org/docs/general-use/updating-kali/>)

内文小节：`When should you update Kali?` · `How to update Kali?`

摘要：When should you update Kali? If you have a default installation of Kali, you should be checking for updates every few days or weeks. If you need a new version of a tool, or hear about a security updat…

### [Using EoL Python Versions on Kali](<https://www.kali.org/docs/general-use/using-eol-python-versions/>)

摘要：In December of 2019 we released a blog post talking about how we will deal with Python 2’s End-of-Life. Since then there has been quite a lot of tools that users use that have not been ported to Pytho…

### [Wayland](<https://www.kali.org/docs/general-use/wayland/>)

内文小节：`What is Wayland? Or X11?` · `Wayland in Kali Linux` · `Am I using Wayland in Kali Linux?` · `Xfce` · `GNOME` · `KDE`

摘要：What is Wayland? Or X11? On Linux systems, the display server is a central part of the graphics stack, it’s involved in displaying everything you see on the screen, and it also deals with user input (…


## 工具相关（`tools`）

工具分类说明与 metapackage 结构 · 共 **7** 篇

### [Installing Flatpak on Kali Linux](<https://www.kali.org/docs/tools/flatpak/>)

摘要：Install Instructions On Kali Linux, flatpak can be installed through: kali@kali:~$ sudo apt update kali@kali:~$ kali@kali:~$ sudo apt install -y flatpak kali@kali:~$ kali@kali:~$ sudo flatpak remote-a…

### [Installing snapd on Kali Linux](<https://www.kali.org/docs/tools/snap/>)

摘要：Install Instructions On Kali Linux, snap can be installed through: kali@kali:~$ sudo apt update kali@kali:~$ kali@kali:~$ sudo apt install -y snapd kali@kali:~$ Enabling and starting snapd and snapd.a…

### [Installing Tor Browser on Kali Linux](<https://www.kali.org/docs/tools/tor/>)

摘要：Install Instructions Open the terminal then run the following commands: kali@kali:~$ sudo apt update kali@kali:~$ kali@kali:~$ sudo apt install -y tor torbrowser-launcher kali@kali:~$ As user run the …

### [Kali Tools](<https://www.kali.org/docs/tools/kali-tools/>)

内文小节：`Local information` · `Online information`

摘要：Users have a few areas where they can look for information about a tool in Kali. Local information The first place users should look to is whatever local information is available. Through man pages an…

### [Metasploit Framework](<https://www.kali.org/docs/tools/starting-metasploit-framework-in-kali/>)

内文小节：`Quick way` · `MSFDB` · `Start the Kali PostgreSQL Service` · `Initialize the Metasploit PostgreSQL Database` · `Launch msfconsole in Kali`

摘要：In keeping with the Kali Linux Network Services Policy , no network services, including database services, run on boot as a default, so there are a couple of steps that need to be taken in order to ge…

### [Removed Tools From Kali](<https://www.kali.org/docs/tools/removed-tools/>)

摘要：Unfortunately for various reasons why, we can’t always keep every tool in Kali. Below is a list of tools removed from Kali Linux: Package Date Reason apt2 2020-03-30 Python 2 ( #1 ) automater 2019-09-…

### [Submitting tools to Kali](<https://www.kali.org/docs/tools/submitting-tools/>)

内文小节：`Preparations` · `Where to submit the tool` · `Requesting the tool:`

摘要：Preparations In order for a tool to be added to any Debian-based distribution it needs to be packaged, this can be seen by a debian/ directory in the source code. For developers, we have documentation…


## 虚拟化（`virtualization`）

VirtualBox / VMware / Hyper-V / QEMU / Docker / WSL · 共 **22** 篇

### [Converting VMX to an OVA](<https://www.kali.org/docs/virtualization/converting-vmx-to-ova/>)

摘要：VMware has VMX format which works for VMware products. The other commonly found format which is OVF , as this is a open standard ( OVA is OVF but compressed into a single file). There are times where …

### [Customizing a Kali Vagrant Vagrantfile](<https://www.kali.org/docs/virtualization/customizing-kali-vagrant/>)

内文小节：`Vagrantfile configuration to improve Kali`

摘要：Vagrant has a great feature when getting started where you create a Vagrantfile unique to the box you are trying to install. For example, Kali has this Vagrantfile when starting up a Kali Vagrant mach…

### [Import Pre-Made Kali Hyper-V VM](<https://www.kali.org/docs/virtualization/import-premade-hyper-v/>)

内文小节：`Troubleshooting and extra tips`

摘要：Importing the Kali Hyper-V image is very straightforward. We first need to extract the Hyper-V image. For that we need to use the official 7z app . Note: If we are on Windows 11 the option will be hid…

### [Import Pre-Made Kali VirtualBox VM](<https://www.kali.org/docs/virtualization/import-premade-virtualbox/>)

摘要：Importing the Kali VirtualBox image is very straightforward. We first need to extract the VirtualBox image: kali@kali:~$ 7z x kali-linux-2026.2-virtualbox-amd64.7z [...] kali@kali:~$ If we are using W…

### [Import Pre-Made Kali VMware VM](<https://www.kali.org/docs/virtualization/import-premade-vmware/>)

摘要：Importing the Kali VMware image is very straightforward. We first need to extract the VMware image: kali@kali:~$ 7z x kali-linux-2026.2-vmware-amd64.7z [...] kali@kali:~$ If we are using Windows we ca…

### [Improving Virtual Machine Performance for VMware](<https://www.kali.org/docs/virtualization/improving-vm-performance-vmware/>)

摘要：Setting Memory Limits for your Virtual Machines When you are running a virtual machine on your host operating system, they tend to not behave well when they run low on free memory for their own use. I…

### [Installing Hyper-V Enhanced Session Mode (Guest Tools)](<https://www.kali.org/docs/virtualization/install-hyper-v-guest-enhanced-session-mode/>)

内文小节：`Configurating Kali` · `Changing the Setting of the Virtual Machine` · `Test and Troubleshooting` · `Disabling Hyper-V Enhanced Session Mode` · `Further notes`

摘要：Installing “Guest VM Packages”, gives a better user experience with VMs in general. This is why since Kali Linux 2019.3 , during the setup process it should detect if Kali Linux is inside a VM . If it…

### [Installing VirtualBox Guest Addition (Guest Tools)](<https://www.kali.org/docs/virtualization/install-virtualbox-guest-additions/>)

内文小节：`virtualbox-guest-x11`

摘要：Installing “Guest Addition”, gives a better user experience with VirtualBox VMs (e.g. proper mouse and screen integration, as well as folder sharing) . This is why since Kali Linux 2019.3 , during the…

### [Installing VirtualBox on Kali (Host)](<https://www.kali.org/docs/virtualization/install-virtualbox-host/>)

内文小节：`Preparation` · `1. From Kali Linux repositories` · `2. From Oracle Virtualbox third-party repository` · `Download` · `Setup`

摘要：You can install VirtualBox on Kali Linux, allowing you to use virtual machines (VMs) inside of Kali Linux. However if you are wanting to install Kali Linux as a VM, you want our Kali Linux Guest Virtu…

### [Installing VMware on Apple Silicon (M1/M2/M3) Macs (Host)](<https://www.kali.org/docs/virtualization/install-vmware-silicon-host/>)

摘要：You need to be running at least VMware Fusion 13.x.x. Due to a limitation of the VMware updater software, if you are on an earlier version, it will report that there are no updates available. You need…

### [Installing VMware on Kali (Host)](<https://www.kali.org/docs/virtualization/install-vmware-host/>)

内文小节：`Preparation` · `Download` · `Setup` · `Troubleshooting`

摘要：You can install VMware workstation or player on Kali Linux, allowing you to use Virtual Machines (VMs) inside of Kali Linux. However if you wish to use Kali Linux as a virtual machine, you will want o…

### [Installing VMware Tools (Guest Tools)](<https://www.kali.org/docs/virtualization/install-vmware-guest-tools/>)

内文小节：`Open-VM-Tools` · `Adding Support for Shared Folders When Using OVT`

摘要：Installing “Guest Tools”, gives a better user experience with VMware VMs. This is why since Kali Linux 2019.3 , during the setup process it should detect if Kali Linux is inside a VM . If it is, then …

### [Kali inside Hyper-V (Guest VM)](<https://www.kali.org/docs/virtualization/install-hyper-v-guest-vm/>)

内文小节：`Expanding Storage`

摘要：For most Windows users Hyper-V is already enabled. However, in case it isn’t enabled on your system you can follow one of the following docs pages from Microsoft: For Windows 8, 8.1 For Windows 10, 11…

### [Kali inside Parallels (Guest VM)](<https://www.kali.org/docs/virtualization/install-parallels-guest-vm/>)

内文小节：`Wizard`

摘要：This guide is about virtualizing Kali Linux inside of Parallels, allowing you to have a Kali VM. This is a great way to use Kali, as it is completely separate from the host, allows you to interact wit…

### [Kali inside Proxmox (Guest VM)](<https://www.kali.org/docs/virtualization/install-proxmox-guest-vm/>)

内文小节：`Kali as a Proxmox VM (Virtualization) using prebuilt virtual machine` · `Kali as a Proxmox VM (Virtualization)` · `Kali as a Proxmox CT (Containerization)`

摘要：Due to the type of hypervisor Proxmox is we do not have a documentation page on how to install it. However, this can be found through Proxmox’s official page . Proxmox has two ways of accessing a nest…

### [Kali inside QEMU/LibVirt with virt-manager (Guest VM)](<https://www.kali.org/docs/virtualization/install-qemu-guest-vm/>)

摘要：We understand there are a lot of options for interfacing with KVM and QEMU to create different VMs, however for the purposes of this guide we will be using the most common option. To get a Debian base…

### [Kali inside UTM (Guest VM)](<https://www.kali.org/docs/virtualization/install-utm-guest-vm/>)

摘要：To install and set up a UTM VM it is pretty straightforward. We first download UTM and then launch the app. After this we can click create VM and start the short process: We will select Virtualize, as…

### [Kali inside Vagrant (Guest VM)](<https://www.kali.org/docs/virtualization/install-vagrant-guest-vm/>)

摘要：Vagrant is, according to their website , “a tool for building and managing virtual machine environments in a single workflow.” This is all controlled through a single configuration file that has a lar…

### [Kali inside VirtualBox (Guest VM)](<https://www.kali.org/docs/virtualization/install-virtualbox-guest-vm/>)

内文小节：`Wizard` · `Expanding Storage`

摘要：This guide is about virtualizing Kali Linux inside of VirtualBox, allowing you to have a Kali VM. This is a great way to use Kali, as it is completely separate from the host, allows you to interact wi…

### [Kali inside VMware (Guest VM)](<https://www.kali.org/docs/virtualization/install-vmware-guest-vm/>)

内文小节：`Wizard` · `Edit Settings` · `Expand Storage`

摘要：This guide is about virtualizing Kali Linux inside of VMware, allowing you to have a Kali VM. This is a great way to use Kali, as it is completely separate from the host, allows you to interact with o…

### [Running Kali Linux as a Virtual Machine in Windows](<https://www.kali.org/docs/virtualization/running-kali-vm-windows/>)

内文小节：`Setting an Exclusion Folder in Windows Security` · `References`

摘要：As time moves on Antivirus and EDR programs are working to implement new capabilities to identify hacking tools. These hacking tools are usually signatured by Antivirus programs to protect the host op…

### [Troubleshooting Kali VMware VM](<https://www.kali.org/docs/virtualization/troubleshooting-vmware/>)

摘要：Fix copy/paste, drag and drop with KDE desktop This is for users of the Kali KDE desktop, within a VMware virtual machine. It is a known issue that copy/paste and drag and drop won’t work out of the b…


## 容器（`containers`）

Docker、Podman 与容器化 Kali · 共 **5** 篇

### [Installing Docker on Kali Linux](<https://www.kali.org/docs/containers/installing-docker-on-kali/>)

摘要：To install Docker on Kali you need to remember that there is already a package named “docker”, therefore Docker has to be installed under a different name. If you install docker you will not end up wi…

### [Kali Linux LXC/LXD Images](<https://www.kali.org/docs/containers/kalilinux-lxc-images/>)

内文小节：`Content:` · `Overview` · `Command line Kali LXD container on Ubuntu host` · `GUI Kali LXD container on Ubuntu host` · `Privileged Kali LXC container on Kali host` · `Unprivileged Kali LXC container on Kali host` · `References:`

摘要：Content: Overview Command line Kali LXD container on Ubuntu host Gui Kali LXD container on Ubuntu host Privileged Kali LXC container on Kali host Unprivileged Kali LXC container on Kali host Reference…

### [Official Kali Linux Docker Images](<https://www.kali.org/docs/containers/official-kalilinux-docker-images/>)

摘要：Kali provides official Kali Docker images that are updated once a week on Docker Hub . You can thus easily build your own Kali containers on top of those that we provide. We offer various images to tr…

### [Using Kali Linux Docker Images](<https://www.kali.org/docs/containers/using-kali-docker-images/>)

摘要：To use the Kali Linux Docker image , we will do the following commands: kali@kali:~$ docker pull docker.io/kalilinux/kali-rolling kali@kali:~$ kali@kali:~$ docker run --tty --interactive kalilinux/kal…

### [Using Kali Linux Podman Images](<https://www.kali.org/docs/containers/using-kali-podman-images/>)

摘要：Podman has very nice documentation on how to install it on various systems. We recommend to follow the official documentation, however for a Debian-based system it is a very simple command: kali@kali:…


## 云环境（`cloud`）

AWS / Azure / Linode 等云上 Kali · 共 **4** 篇

### [AWS](<https://www.kali.org/docs/cloud/aws/>)

内文小节：`Creating our AWS instance` · `Connecting to the AWS instance` · `After connecting` · `Metapackages` · `Graphical User Interface (GUI)` · `NVIDIA drivers`

摘要：As of February 2023 the following is how to set up an AWS Kali instance. AWS’s interface is constantly being updated, and in the future may not be 100% accurate. Should this be the case, please file a…

### [Azure](<https://www.kali.org/docs/cloud/azure/>)

内文小节：`Creating a Kali VM`

摘要：As of Kali 2022.3 , Kali is back on Azure. With this return we will discuss how to get Kali on Azure. The very first thing to do is create an Azure account. Only once we see the following screen are w…

### [Digital Ocean](<https://www.kali.org/docs/cloud/digitalocean/>)

内文小节：`Get the netboot ISO` · `Create the Virtual Machine` · `Update the System` · `Install Required Packages` · `Prepare for SSH` · `Cleanup` · `Uploading` · `Starting a Droplet`

摘要：DigitalOcean is a cloud provider similar to AWS, Microsoft Azure, Google Cloud Platform, and many others. They offer instances, called “droplets”, with different Linux distributions such as Debian, Ub…

### [Linode](<https://www.kali.org/docs/cloud/linode/>)

内文小节：`Kali as a Distribution` · `Kali as a Distribution Configuration` · `Kali Default Tools In Linode` · `Kali from the Marketplace` · `Kali from the Marketplace Configuration`

摘要：Before we begin we would like to call out a great video from Linode themselves! Here you can find a video that talks about what Kali Linux is and how to get and use it with Linode. Thank you Linode! T…


## WSL（`wsl`）

Windows Subsystem for Linux 中的 Kali · 共 **5** 篇

### [Kali WSL](<https://www.kali.org/docs/wsl/wsl-preparations/>)

内文小节：`Modern WSL Distribution Architecture (2025)` · `The different versions of WSL` · `Quick Method` · `Windows Version` · `Check Version` · `Install WSL 1` · `WSL helper-script` · `Dism` · `PowerShell` · `Manually Upgrade WSL 1 to WSL 2` · `WSL in Microsoft Store` · `Install Kali WSL`

摘要：Modern WSL Distribution Architecture (2025) As of November 2024, there is a new distribution architecture for WSL that allows for use of tar compressed root filesystems to be imported into WSL. To get…

### [Win-KeX](<https://www.kali.org/docs/wsl/win-kex/>)

内文小节：`Installation` · `Prerequisites` · `Install Win-KeX` · `Run Win-KeX` · `Window Mode` · `Enhanced Session Mode` · `Seamless Mode` · `Optional Steps` · `Kali’s Default Tools` · `Windows Terminal` · `Help`

摘要：Win-KeX provides a GUI desktop experience for Kali Linux in Windows Subsystem for Linux (WSL 2) with the following features: Window mode : start a Kali Linux desktop in a dedicated window Seamless mod…

### [Win-KeX Enhanced Session Mode](<https://www.kali.org/docs/wsl/win-kex-esm/>)

内文小节：`Usage` · `Start Session` · `Start Root Session` · `Sound Support` · `Session Management` · `Stop Session`

摘要：Win-KeX in Enhanced Session Mode (ESM) will run a Kali Linux desktop session in a separate window using protocols and clients native to Windows. ESM mode is the only supported mode on ARM devices. ESM…

### [Win-KeX Seamless Mode](<https://www.kali.org/docs/wsl/win-kex-sl/>)

内文小节：`Prerequisites` · `Usage` · `Start Session` · `Sound Support` · `Multiscreen Support` · `Stop Session`

摘要：Win-KeX in Seamless Mode (SL) will launch a Kali Linux panel on the screen top of the Windows desktop. Applications started via the panel will share the desktop with Microsoft Windows applications. Se…

### [Win-KeX Window Mode](<https://www.kali.org/docs/wsl/win-kex-win/>)

内文小节：`Overview` · `Usage` · `Start Session` · `Start Root Session` · `Session Management` · `Sound Support` · `Multiscreen Support` · `Stop Session`

摘要：Overview Win-KeX in Window Mode (Win) will run a Kali Linux desktop session in a separate window. Window mode helps keeping the Windows and Kali environments visually apart. Win-KeX utilises TigerVNC …


## USB 启动（`usb`）

制作启动盘、持久化存储、加密持久化 · 共 **10** 篇

### [Adding Encrypted Persistence to a Kali Linux Live USB Drive](<https://www.kali.org/docs/usb/usb-persistence-encryption/>)

内文小节：`Emergency Self Destruction of Data in Kali`

摘要：Kali Linux “Live” has two options in the default boot menu which enable persistence - the preservation of data on the “Kali Live” USB drive - across reboots of “Kali Live”. You can either do: USB Pers…

### [Adding Persistence to a Kali Linux Live USB Drive](<https://www.kali.org/docs/usb/usb-persistence/>)

内文小节：`Multiple Persistence Stores`

摘要：Kali Linux “Live” has two options in the default boot menu which enable persistence - the preservation of data on the “Kali Live” USB drive - across reboots of “Kali Live”. You can either do: USB Pers…

### [Making a Kali Bootable USB Drive (Linux)](<https://www.kali.org/docs/usb/live-usb-install-with-linux/>)

内文小节：`What You’ll Need` · `Kali Linux Live USB Install Procedure` · `Creating a Bootable Kali USB Drive on Linux (DD)` · `Creating a Bootable Kali USB Drive on Linux (Etcher)`

摘要：Our favourite way, and the fastest method, for getting up and running with Kali Linux is to run it “live” from a USB drive. This method has several advantages: It’s non-destructive - it makes no chang…

### [Making a Kali Bootable USB Drive (macOS/OS X)](<https://www.kali.org/docs/usb/live-usb-install-with-mac/>)

内文小节：`What You’ll Need` · `Kali Linux Live USB Install Procedure` · `Creating a Bootable Kali USB Drive on macOS/OS X (DD)` · `Creating a Bootable Kali USB Drive on macOS/OS X (Etcher)` · `Booting USB on Apple`

摘要：Our favorite way, and the fastest method, for getting up and running with Kali Linux is to run it “live” from a USB drive. This method has several advantages: It’s non-destructive - it makes no change…

### [Making a Kali Bootable USB Drive on Windows](<https://www.kali.org/docs/usb/live-usb-install-with-windows/>)

内文小节：`What You’ll Need` · `Creating a Bootable Kali USB Drive on Windows (Etcher)` · `Creating a Bootable Kali USB Drive on Windows (Rufus)` · `Booting A USB Drive In Windows`

摘要：One of the fastest method, for getting up and running with Kali Linux is to run it “live” from a USB drive. This method has several advantages: It’s non-destructive - it makes no changes to the host s…

### [Standalone Kali Linux 2021.4 Installation on a USB Drive, Fully Encrypted](<https://www.kali.org/docs/usb/usb-standalone-encrypted/>)

内文小节：`Outline` · `Preparation` · `Kali Linux 2021.4 Bare Metal Installer` · `Xubuntu 20.04 LTS Installer` · `Partitioning the Target USB Drive` · `Installation of Kali Linux 2021.4` · `Setting Up the Installer` · `Partitioning` · `Btrfs Adjustments` · `The File System Table` · `Actual Installation` · `Setting Up the Initial RAM Disk`

摘要：Standalone Kali Linux 2021.4 Installation on a USB Drive, Fully Encrypted These instructions allow you to create a fully encrypted standalone installation of Kali Linux 2021.4 on an external USB drive…

### [Updating Kali Linux on USB](<https://www.kali.org/docs/usb/updating-kali-on-usb/>)

内文小节：`Requirements` · `Process`

摘要：Requirements In order to properly update Kali Linux on a USB, persistence must be setup. If persistence is not setup, re-imaging the USB with an ISO from the weekly build will be a suitable update. Pr…

### [USB Boot in VirtualBox](<https://www.kali.org/docs/usb/boot-usb-in-virtualbox/>)

摘要：To get started we first will need to download the Oracle VM VirtualBox Extension Pack . After downloading this pack we can launch VirtualBox and select ‘Preferences’ under the ‘File’ tab. From here we…

### [USB Boot in VMware](<https://www.kali.org/docs/usb/boot-usb-in-a-vm/>)

内文小节：`Process` · `Troubleshooting USB Connections` · `Troubleshooting EFI` · `Final option`

摘要：A few years ago we released a blog post on VMware Fusion Kali USB Boot . This can come in handy if a USB is not working how it should, as it can reduce time from needing to reboot or transfer it to an…

### [Verifying USB Write](<https://www.kali.org/docs/usb/verify-usb-write/>)

内文小节：`Check USB Contents` · `On Linux/MacOS` · `On Windows` · `Verifying the Checksum` · `On Linux/MacOS` · `On Windows` · `Troubleshooting` · `USB not booting` · `Checksum mismatch`

摘要：After writing the Kali ISO to a USB, it is a good practice to verify that: Files were copied correctly to the USB The USB is bootable. Making sure that the ISO wasn’t corrupted. Check USB Contents On …


## ARM 与单板机（`arm`）

树莓派、ARM 设备、chroot · 共 **43** 篇

### [Acer Tegra Chromebook 13" (Nyan)](<https://www.kali.org/docs/arm/chromebook-nyan/>)

内文小节：`Kali on Acer Tegra Chromebook - Build-Script Instructions` · `Kali on Acer Tegra Chromebook - User Instructions`

摘要：The Acer Tegra Chromebook is an ultraportable laptop. Boasting a Tegra K1 2.1GHz quad core processor and 4GB of RAM, the Chromebook is a fast ARM laptop. Kali Linux fits on an external full-size SD ca…

### [ASUS Chromebook Flip (Veyron)](<https://www.kali.org/docs/arm/chromebook-veyron/>)

内文小节：`Kali on ASUS Chromebook Flip - Build-Script Instructions` · `Kali on ASUS Chromebook Flip - User Instructions` · `Kali on ASUS Chromebook Flip - Image Customization`

摘要：The ASUS Chromebook Flip is a quad core 1.8GHz, with 2GB or 4GB of RAM Chromebook with a 10.1" 10 point mult-touch touchscreen. Kali Linux fits on an external microSD card or USB drive. By default, th…

### [Banana Pi](<https://www.kali.org/docs/arm/banana-pi/>)

内文小节：`Kali on Banana Pi - Build-Script Instructions` · `Kali on Banana Pi - User Instructions`

摘要：The Banana Pi has a dual core 1GHz Cortex™-A7 processor with a Mali400MP2 GPU and 1GB DDR3 RAM. Kali Linux can run from an external microSD card. By default, the Kali Linux Banana Pi image contains th…

### [Banana Pro](<https://www.kali.org/docs/arm/banana-pro/>)

内文小节：`Kali on Banana Pro - Build-Script Instructions` · `Kali on Banana Pro - User Instructions`

摘要：The Banana Pro has a dual core 1GHz Cortex™-A7 processor with a Mali400MP2 GPU and 1GB DDR3 RAM. Kali Linux can run from an external microSD card. By default, the Kali Linux Banana Pro image contains …

### [BeagleBone Black](<https://www.kali.org/docs/arm/beaglebone-black/>)

内文小节：`Kali on Beaglebone Black - Build-Script Instructions` · `Kali on Beaglebone Black - User Instructions`

摘要：The BeagleBone Black is a low-cost, community-supported ARM-based development platform aimed at developers and hobbyists. The BeagleBone Black runs a 1GHz Cortex-A8 CPU and includes hardware-based flo…

### [CubieBoard2](<https://www.kali.org/docs/arm/cubieboard2/>)

内文小节：`Kali on CubieBoard2 - Build-Script Instructions` · `Kali on CubieBoard2 - User Instructions`

摘要：The CubieBoard2 is a dual core 1.4GHz, with 1GB of RAM. Kali Linux fits on an external microSD card. By default, the Kali Linux CubieBoard2 image contains the kali-linux-default metapackage similar to…

### [CubieTruck (CubieBoard3)](<https://www.kali.org/docs/arm/cubietruck/>)

内文小节：`Kali on CubieTruck - Build-Script Instructions` · `Kali on CubieTruck - User Instructions`

摘要：The CubieTruck (aka CubieBoard3) is a dual core 1GHz, with 2GB of RAM. Kali Linux fits on an external microSD card. By default, the Kali Linux CubieTruck image contains the kali-linux-default metapack…

### [CuBox](<https://www.kali.org/docs/arm/cubox/>)

内文小节：`Kali on CuBox - Build-Script Instructions` · `Kali on CuBox - User Instructions`

摘要：The CuBox is a low end, low cost ARM computer. Despite its less-than-stellar specifications, its affordability makes it an excellent option for a tiny Linux system and it can do far more than act as a…

### [CuBox-i4Pro](<https://www.kali.org/docs/arm/cubox-i4pro/>)

内文小节：`Kali on CuBox-i4Pro - Build-Script Instructions` · `Kali on CuBox-i4Pro - User Instructions`

摘要：SolidRun’s CuBox-i4Pro is the “world’s smallest computer”. The specifications are Quad core i.MX6 1GHZ processor, 2GB RAM, Gigabit ethernet, eSata port, and microSD card slot. This image for the “Free…

### [Gateworks Newport](<https://www.kali.org/docs/arm/gateworks-newport/>)

内文小节：`Kali on the Gateworks Newport - User Instructions` · `Kali on the Gateworks Newport - Image Customization`

摘要：The Gateworks Newport implementing a flash drive sized computer. Kali Linux fits on a microSD card for it. This image is for the “Cavium OcteonTX” based boards. By default, the Kali Linux Gateworks Ne…

### [Gateworks Ventana](<https://www.kali.org/docs/arm/gateworks-ventana/>)

内文小节：`Kali on the Gateworks Ventana - User Instructions` · `Kali on the Gateworks Ventana - Image Customization`

摘要：The Gateworks Ventana implementing a flash drive sized computer. Kali Linux fits on a microSD card for it. This image is for the “NXP (formerly Freescale) i.MX6” based boards. By default, the Kali Lin…

### [Mini-X](<https://www.kali.org/docs/arm/mini-x/>)

内文小节：`Kali on Mini-X - Build-Script Instructions` · `Kali on Mini-X - User Instructions`

摘要：The Mini-X is a dual core 1GHz, with 1GB of RAM. Kali Linux fits on an external microSD card. By default, the Kali Linux Mini-X image does not contains the kali-linux-default metapackage which is ofte…

### [NanoPC-T3](<https://www.kali.org/docs/arm/nanopc-t/>)

内文小节：`Kali on NanoPC-T3 microSD card - User Instructions` · `Kali on the NanoPC-T3 - Tips` · `Kali on NanoPC-T3 - Image Customization`

摘要：The NanoPC-T3 has an Samsung S5P6818, Octa Core Cortex™-A53 (ARMv8 64-bit) processor and either 1GB or 2GB DDR3 RAM. The NanoPC-T3 has an 8GB eMMC, which is too small for a default Kali installation, …

### [NanoPi NEO Plus2](<https://www.kali.org/docs/arm/nanopi-neo-plus2/>)

内文小节：`Kali on NanoPi NEO Plus2 - Build-Script Instructions` · `Kali on NanoPi NEO Plus2 - User Instructions` · `Kali on the NanoPi NEO Plus2 - Tips`

摘要：The NanoPi NEO Plus2 has an Allwinner H5, Quad Core Cortex™-A53 (ARMv8 64-bit) processor with Triple Core Mali-450 MP4 GPU and 1GB DDR3 RAM. The NanoPi NEO Plus2 has an 8GB eMMC, which is too small fo…

### [ODROID-C0/C1/C1+](<https://www.kali.org/docs/arm/odroid-c/>)

内文小节：`Kali on ODROID-C0/C1/C1+ - Build-Script Instructions` · `Kali on ODROID-C0/C1/C1+ - User Instructions`

摘要：The ODROID-C1 is a quad core 1.5GHz Cortex A5, with 1GB of RAM development board. Kali Linux fits on an external microSD card or on an eMMC module. The ODROID-C0 and ODROID-C1+ are both essentially th…

### [ODROID-C2](<https://www.kali.org/docs/arm/odroid-c2/>)

内文小节：`Kali on ODROID-C2 - Build-Script Instructions` · `Kali on ODROID-C2 - User Instructions` · `Kali on the ODROID-C2 - Tips`

摘要：The ODROID-C2 has an Amlogic S905, Quad Core Cortex™-A53 (ARMv8 64-bit) processor with Triple Core Mali-450 GPU and 2GB DDR3 (32-bit / 912Mhz) of RAM. Kali Linux can run from either an external microS…

### [ODROID-U2/U3](<https://www.kali.org/docs/arm/odroid-u/>)

内文小节：`Kali on ODROID-U2/U3 - Build-Script Instructions` · `Kali on ODROID-U2/U3 - User Instructions` · `Troubleshooting`

摘要：The ODROID-U2 is a tricky piece of hardware as console output is not a given. Ideally, when purchasing an ODROID-U2, you should also get a USB UART cable, used for serial debugging of the boot process…

### [ODROID-XU3](<https://www.kali.org/docs/arm/odroid-xu3/>)

内文小节：`Kali on ODROID-XU3/XU4 - Build-Script Instructions` · `Kali on ODROID-XU3/XU4 - User Instructions`

摘要：The ODROID-XU3 is an octacore development board. Boasting 4 A15 cores and 4 A7 cores and 4GB of RAM, the ODROID-XU3 is a fast ARM device. Kali Linux fits on an external microSD card or on an eMMC modu…

### [Pinebook](<https://www.kali.org/docs/arm/pinebook/>)

内文小节：`Kali on the Pinebook microSD card - User Instructions` · `Kali on the Pinebook eMMC - User Instructions` · `Kali on the Pinebook - Image Customization`

摘要：The Pinebook has an Allwinner A64 Quad Core SOC with Mali 400 MP2 GPU, and 2GB LPDDR3 RAM. Kali Linux can run from either microSD card, or the internal eMMC. By default, the Kali Linux Pinebook image …

### [Pinebook Pro](<https://www.kali.org/docs/arm/pinebook-pro/>)

内文小节：`Kali on the Pinebook Pro microSD card - User Instructions` · `Kali on the Pinebook Pro eMMC - User Instructions` · `Kali on the Pinebook Pro - Image Customization`

摘要：The Pinebook Pro has a Rockchip RK3399 SOC with Mali T860 MP4 GPU and 4GB LPDDR4 RAM. Kali Linux can run from either external microSD card, or the internal eMMC. By default, the Kali Linux Pinebook Pr…

### [Radxa Zero (eMMC)](<https://www.kali.org/docs/arm/radxa-zero-emmc/>)

内文小节：`Kali on Radxa Zero (eMMC) - Build-Script Instructions` · `Kali on Radxa Zero (eMMC) - User Instructions`

摘要：The Radxa Zero has a quad core 1.8GHz, with 512MB, 1GB, 2GB, or 4GB of LPDDR4 RAM. There are multiple eMMC versions available, we recommend at least 32GB. By default, the Kali Linux Radxa Zero image c…

### [Radxa Zero (sdcard)](<https://www.kali.org/docs/arm/radxa-zero-sdcard/>)

内文小节：`Kali on Radxa Zero (sdcard) - Build-Script Instructions` · `Kali on Radxa Zero (sdcard) - User Instructions`

摘要：The Radxa Zero has a quad core 1.8GHz, with 512MB, 1GB, 2GB, or 4GB of LPDDR4 RAM. Kali Linux fits on an external microSD card. By default, the Kali Linux Radxa Zero image contains the kali-linux-defa…

### [Raspberry Pi 1 (Original)](<https://www.kali.org/docs/arm/raspberry-pi/>)

内文小节：`Kali on Raspberry Pi 1 - User Instructions` · `Kali on the Raspberry Pi 1 - Tips` · `Kali on Raspberry Pi 1 - Image Customization`

摘要：The early revisions of Raspberry Pi 1 (Original) boards have a full-size SD card slot, however later board revisions moved to a microSD card slot. We document using the full-size SD card, but the proc…

### [Raspberry Pi 2](<https://www.kali.org/docs/arm/raspberry-pi-2/>)

内文小节：`Kali on Raspberry Pi 2 - User Instructions` · `Kali on Raspberry Pi 2 - Tips` · `Kali on Raspberry Pi 2 - Image Customization`

摘要：If your Raspberry Pi 2 has Raspberry Pi 2 Model B V1.2 printed on the PCB above the CPU, we suggest to follow the Raspberry Pi 2 v1.2 documentation . However if it says Raspberry Pi 2 Model B V1.1 , k…

### [Raspberry Pi 2 v1.2](<https://www.kali.org/docs/arm/raspberry-pi-64-bit/>)

内文小节：`Kali on Raspberry Pi2 v1.2 - User Instructions` · `Kali on Raspberry Pi 2 v1.2 - Tips` · `Kali on Raspberry Pi 2 v1.2 - Image Customization`

摘要：The Raspberry Pi 2 v1.2 has Raspberry Pi 2 Model B V1.2 printed on the PCB above the CPU. If your Raspberry Pi 2 does NOT have this, you should follow the Raspberry Pi 2 documentation The Raspberry Pi…

### [Raspberry Pi 3](<https://www.kali.org/docs/arm/raspberry-pi-3/>)

内文小节：`Kali on Raspberry Pi 3 - User Instructions` · `Kali on Raspberry Pi 3 - Tips and Tricks` · `Kali on Raspberry Pi 3 Headless - Tips and Tricks` · `Kali on Raspberry Pi 3 - Image Customization`

摘要：The Raspberry Pi 3 has a quad core 1.2GHz processor, with 1GB of RAM. Kali Linux fits on an external microSD card. By default, the Kali Linux Raspberry Pi 3 image contains the kali-linux-default metap…

### [Raspberry Pi 4](<https://www.kali.org/docs/arm/raspberry-pi-4/>)

内文小节：`Kali on Raspberry Pi 4 - User Instructions` · `Kali on Raspberry Pi 4 - Tips and Tricks` · `Kali on the Raspberry Pi 4 - Examples` · `Kali on Raspberry Pi 4 - Image Customization`

摘要：The Raspberry Pi 4 has a quad core 1.5GHz processor, with 2GB, 4GB or 8GB of RAM, depending on model. Kali Linux runs on a microSD card. By default, the Kali Linux Raspberry Pi 4 image contains the ka…

### [Raspberry Pi 400](<https://www.kali.org/docs/arm/raspberry-pi-400/>)

内文小节：`Kali on Raspberry Pi400 - User Instructions` · `Kali on Raspberry Pi400 - Tips and Tricks` · `Kali on Raspberry Pi400 - Image Customization`

摘要：The Raspberry Pi 400 has a quad core 1.8GHz processor, with 4GB of RAM, in a keyboard formfactor. Kali Linux runs on a microSD card. By default, the Kali Linux Raspberry Pi 400 image contains the kali…

### [Raspberry Pi 5](<https://www.kali.org/docs/arm/raspberry-pi-5/>)

内文小节：`Kali on Raspberry Pi 5 - User Instructions` · `Kali on Raspberry Pi 5 - Tips and Tricks` · `Kali on Raspberry Pi 5 - Image Customization`

摘要：The Raspberry Pi 5 has a quad core 2.4GHz processor, with 4GB, 8GB or 16GB of RAM, depending on model. Kali Linux runs on a microSD card. By default, the Kali Linux Raspberry Pi 5 image contains the k…

### [Raspberry Pi Zero](<https://www.kali.org/docs/arm/raspberry-pi-zero/>)

内文小节：`Kali on Raspberry Pi Zero - User Instructions` · `Kali on Raspberry Pi Zero - Image Customization`

摘要：The Raspberry Pi Zero is a single core 1GHz, with 512MB of RAM. Unlike the Raspberry Pi Zero W , the Raspberry Pi Zero has no networking on the board, so you will need to use a USB adapter for network…

### [Raspberry Pi Zero 2 W](<https://www.kali.org/docs/arm/raspberry-pi-zero-2-w/>)

内文小节：`Kali on Raspberry Pi Zero 2 W - User Instructions` · `Kali on Raspberry Pi Zero 2 W - Image Customization`

摘要：The Raspberry Pi Zero 2 W has Raspberry Pi Zero 2 printed on the bottom of the PCB. The Raspberry Pi Zero 2 W has a quad core 1GHz, with 512MB of RAM. Kali Linux fits on an external microSD card, or U…

### [Raspberry Pi Zero W](<https://www.kali.org/docs/arm/raspberry-pi-zero-w/>)

内文小节：`Kali on Raspberry Pi Zero W - User Instructions` · `Kali on Raspberry Pi Zero W - Image Customization`

摘要：The Raspberry Pi Zero W has Raspberry Pi Zero W V1.1 printed on the bottom of the PCB. The Raspberry Pi Zero W has a single core 1GHz, with 512MB of RAM. Kali Linux fits on an external microSD card. U…

### [Raspberry Pi Zero W P4wnP1 A.L.O.A](<https://www.kali.org/docs/arm/raspberry-pi-zero-w-p4wnp1-aloa/>)

内文小节：`Introduction` · `Quick install and usage` · `Features`

摘要：Introduction The Raspberry Pi Zero W P4wnP1 A.L.O.A. ( A L ittle O ffensive A pplication) image is a highly customized version of Kali Linux. It allows you to connect the Raspberry Pi to a computer, a…

### [Raspberry Pi-Tail Zero 2 W](<https://www.kali.org/docs/arm/raspberry-pi-zero-2-w-pi-tail/>)

内文小节：`Quick install and usage:` · `How it works:`

摘要：Pi-Tail Kali for RaspberryPi 2 zero w optimised for tethering Simple, one cable solution for Bluetooth and Wi-Fi tether Image, configure, connect, boot up in two minutes from scratch Just install Conn…

### [Raspberry Pi-Tail Zero W](<https://www.kali.org/docs/arm/raspberry-pi-zero-w-pi-tail/>)

内文小节：`Quick install and usage:` · `How it works:` · `Troubleshooting` · `Alternatively you might want to add a script that will change the ip address for you`

摘要：Pi-Tail Kali-Pi0 optimised for tethering Simple, one cable solution for Bluetooth and Wi-Fi tether Image, configure, connect, boot up in two minutes from scratch Just install ConnectBot and VNC viewer…

### [RIoTboard](<https://www.kali.org/docs/arm/riotboard/>)

内文小节：`Kali on RIoTboard - Build-Script Instructions` · `Kali on RIoTboard - User Instructions`

摘要：The RIoTboard is a Cortex A9 1GHz, with 1GB of RAM. Kali Linux fits on an external microSD card. By default, the Kali Linux RIoTboard image contains the kali-linux-default metapackage similar to most …

### [Running x86 code on ARM devices](<https://www.kali.org/docs/arm/x86-on-arm/>)

摘要：There is currently a potential issue with the current version of the qemu-user-static package which can cause some programs to not perform properly. Kali has released a patched version of this package…

### [Samsung Chromebook (daisy_snow) & Samsung Chromebook 2 (peach_pi / peach_pit) & HP Chromebook (daisy_spring)](<https://www.kali.org/docs/arm/chromebook-exynos/>)

内文小节：`Kali on Samsung/HP Chromebook - Build-Script Instructions` · `Kali on Samsung/HP Chromebook - User Instructions`

摘要：The ChromiumOS code names for the: Samsung Chromebook is daisy_snow . Samsung Chromebook 2 is peach_pi (1080p screen) or peach_pit (1366x768). HP Chromebook is daisy_spring We use exynos for the scrip…

### [Trimslice](<https://www.kali.org/docs/arm/trimslice/>)

内文小节：`Kali on Trimslice - Build-Script Instructions` · `Kali on Trimslice - User Instructions`

摘要：The Trimslice is a dual core 1GHz, with 1GB of RAM. Kali Linux fits on an external microSD card. By default, the Kali Linux Trimslice image contains the kali-linux-default metapackage similar to most …

### [USB Armory MKI](<https://www.kali.org/docs/arm/usb-armory-mki/>)

内文小节：`Kali on USB Armory MKI - Build-Script Instructions` · `Kali on USB Armory MKI - User Instructions` · `Kali on USB Armory MKI - Image Customization`

摘要：The USB Armory MKI from Inverse Path is an open source hardware design, implementing a flash drive sized computer. Kali Linux fits on a microSD card for it. By default, the Kali Linux USB Armory MKI i…

### [USB Armory MKII](<https://www.kali.org/docs/arm/usb-armory-mkii/>)

内文小节：`Kali on USB Armory MKII - User Instructions` · `Kali on USB Armory MKII - Image Customization`

摘要：The USB Armory MKII from Inverse Path is an open source hardware design, implementing a flash drive sized computer. Kali Linux fits on a microSD card for it. By default, the Kali Linux USB Armory MKII…

### [Using the Raspberry Pi Imager software to write Kali Raspberry Pi Images](<https://www.kali.org/docs/arm/using-rpi-imager-to-write-raspberry-pi-images/>)

摘要：An additional option for writing Kali Raspberry Pi images to either a MicroSD card or USB device is to use the Raspberry Pi Imager software which is available for Windows, macOS, and Linux. At this ti…

### [Utilite Pro](<https://www.kali.org/docs/arm/utilite-pro/>)

内文小节：`Kali on Utilite Pro - Build-Script Instructions` · `Kali on Utilite Pro - User Instructions`

摘要：The Utilite Pro is a quad core 1.2GHz Cortex A9, with 2GB of RAM. Kali Linux fits on an external microSD card. By default, the Kali Linux Utilite Pro image contains the kali-linux-default metapackage …


## Kali NetHunter（`nethunter`）

移动端渗透平台 · 共 **53** 篇

### [Adding your device](<https://www.kali.org/docs/nethunter/nethunter-kernel-8-adding-your-device/>)

内文小节：`Adding your own device to the devices repo`

摘要：Adding your own device to the devices repo Congratulations! You have successfully built your own Kali NetHunter kernel. Feel free to add it to our kernel repo, supporting the community. Please follow …

### [Building NetHunter](<https://www.kali.org/docs/nethunter/building-nethunter/>)

内文小节：`Clone` · `Bootstrap` · `Help` · `Examples`

摘要：Clone Those of you who want to build a Kali NetHunter image from our GitLab repository may do so using our Python build-scripts: kali@kali:~$ git clone https://gitlab.com/kalilinux/nethunter/build-scr…

### [Configuring the 3.x Kernel - USB](<https://www.kali.org/docs/nethunter/nethunter-kernel-6-config-5/>)

内文小节：`Kernel Configuration cont.` · `USB Modem` · `USB Gadget support` · `Exit, save, and build`

摘要：Kernel Configuration cont. If your kernel is above 4.x please skip to the next page USB Modem CDC ACM support is required for Proxmark and similar devices Navigate to Device Drivers -> USB support and…

### [Configuring the 4.x Kernel - USB](<https://www.kali.org/docs/nethunter/nethunter-kernel-7-config-6/>)

内文小节：`Kernel Configuration cont.` · `USB Modem` · `USB Gadget support` · `Exit, save, and build`

摘要：Kernel Configuration cont. USB Modem CDC ACM support is required for Proxmark and similar devices Navigate to Device Drivers -> USB support and select the following option: select “USB Modem (CDC ACM)…

### [Configuring the Kernel - CAN](<https://www.kali.org/docs/nethunter/nethunter-kernel-9-config-8/>)

内文小节：`CAN support` · `Hlcan driver` · `ISO 15765-2 Driver CAN-ISOTP (Optional)`

摘要：CAN support CAN support will be needed for CARsenal usage. In section “Networking support” : Select “CAN bus subsystem support” Select “Network physical/parent device Netlink interface” Under “CAN bus…

### [Configuring the Kernel - General](<https://www.kali.org/docs/nethunter/nethunter-kernel-2-config-1/>)

内文小节：`Kernel Configuration` · `General` · `Modules` · `Kernel Image`

摘要：Kernel Configuration General In section “General Setup”: clear “Local version” set “Default host name” to “kali” select “System V IPC” (CONFIG_SYSVIPC=y) Modules We want to enable modules in Enable Lo…

### [Configuring the Kernel - Network](<https://www.kali.org/docs/nethunter/nethunter-kernel-3-config-2/>)

内文小节：`Kernel Configuration cont.` · `Bluetooth` · `MAC80211` · `Ethernet`

摘要：Kernel Configuration cont. Bluetooth Navigate to “Networking support → Bluetooth subsystem support → Bluetooth device drivers” select “HCI USB driver” (CONFIG_BT_HCIBTUSB=y) select “Broadcom protocol …

### [Configuring the Kernel - NFS](<https://www.kali.org/docs/nethunter/nethunter-kernel-8-config-7/>)

内文小节：`NFS Support`

摘要：NFS Support NFS client and server support is required in case it’s disabled by default. Navigate to File Systems -> Network File Systems and select the following option: select “Network File Systems” …

### [Configuring the Kernel - SDR](<https://www.kali.org/docs/nethunter/nethunter-kernel-5-config-4/>)

内文小节：`Kernel Configuration` · `SDR`

摘要：Kernel Configuration SDR Please note some devices have the Digital TV support in a submenu, and some kernel 3.x versions don’t support RF hardware by default . Navigate to “Device Drivers -> Multimedi…

### [Configuring the Kernel - Wifi](<https://www.kali.org/docs/nethunter/nethunter-kernel-4-config-3/>)

内文小节：`Kernel Configuration cont.` · `Wireless LAN`

摘要：Kernel Configuration cont. Wireless LAN Navigate to Device Drivers -> Network Device Support -> Wireless LAN and make the following selections: select “Atheros/Qualcomm devices” (CONFIG_WLAN_VENDOR_AT…

### [Installing Kali NetHunter](<https://www.kali.org/docs/nethunter/installing-nethunter/>)

内文小节：`1. Kali NetHunter pre-built images and support` · `2. Putting your device in “Developer Mode”` · `3. Unlocking, rooting, and installing a custom recovery on your android device` · `4. Flashing Universal DM-Verity & ForceEncrypt Disabler` · `5. Installing the Kali NetHunter Image (Recovery)` · `5. Installing the Kali NetHunter Image (Magisk module)`

摘要：1. Kali NetHunter pre-built images and support The Kali NetHunter team builds and publishes pre-created images for a selected list of devices, on the official NetHunter download page . If your device …

### [Installing NetHunter on the Gemini PDA](<https://www.kali.org/docs/nethunter/installing-nethunter-on-the-gemini-pda/>)

内文小节：`1. Flash stock rooted Android` · `2. Run Magisk Manager to finish the rooting process` · `3. Install TWRP recovery` · `4. Install NetHunter` · `Enjoy Kali NetHunter on the Gemini PDA` · `Current status`

摘要：From unpacking to running NetHunter in 4 steps: Flash stock rooted Android image Run Magisk Manager to finish the rooting process Install TWRP recovery Install NetHunter 1. Flash stock rooted Android …

### [Installing NetHunter on the OnePlus 5T](<https://www.kali.org/docs/nethunter/installing-nethunter-on-the-oneplus-5t/>)

内文小节：`Overview` · `Developer Options, OEM Unlocking & USB Debug Mode` · `Installing LineageOS` · `Rooting the Device` · `Installing NetHunter`

摘要：Overview We’ll be covering how to install NetHunter on OnePlus 5T. Steps are as follows: Enable Developer options, OEM Unlocking and USB Debugging Install LineageOS Root the device with Magisk and TWR…

### [Installing NetHunter on the OnePlus 7](<https://www.kali.org/docs/nethunter/installing-nethunter-on-the-oneplus-7/>)

内文小节：`1. Flash latest stock (OOS) Android 10` · `2. Flash TWRP and Magisk` · `3. Disable force ecryption of data partition` · `4. Install NetHunter` · `5. Disable OnePlus update service` · `Enjoy Kali NetHunter on the OnePlus 7`

摘要：From a reset to running NetHunter in 4 steps: Flash latest Android 10 with the unbrick tool Flash TWRP and Magisk Disable force encryption of data partition Install NetHunter Disable OnePlus update se…

### [Installing NetHunter on the OnePlus One](<https://www.kali.org/docs/nethunter/installing-nethunter-on-the-oneplus-one/>)

内文小节：`Overview` · `Links/Downloads` · `Guide` · `Configure Host` · `Configure Device` · `Unlock The Bootloader` · `Flash Back To Stock (Mostly)` · `Upgrade System ROM (Update Android Version)` · `Root Device` · `Install Kali NetHunter` · `First Time Using Kali NetHunter` · `Post Installation`

摘要：We are going to be covering how to install Kali NetHunter on a OnePlus One. This guide will use Kali Linux (as the host), a USB cable (to connect), TWRP (for recovery), Magisk (for root access) and Li…

### [Installing NetHunter on the Samsung Galaxy S10](<https://www.kali.org/docs/nethunter/installing-nethunter-on-the-samsung-galaxy-s10/>)

内文小节：`Features` · `Supported Version` · `Flash Stock Rom` · `OEM Unlocking` · `USB Debugging` · `ROM Flashing` · `Flash Recovery` · `Flash LineageOS ROM` · `Rooting` · `NetHunter` · `Magisk Modules (optional)` · `Nexmon`

摘要：This installation guide and files used is for Samsung Galaxy S10 Exynos9820 version. Features Feature Supported BT_RFCOMM ✅ INTERNAL_BT ✅ RTL_BT ✅ HID-4 ✅ Injection ✅ ATH9K_HTC ✅ RTL88XX ✅ RTL8812AU ✅…

### [Installing NetHunter on the TicWatch Pro](<https://www.kali.org/docs/nethunter/installing-nethunter-on-the-ticwatch-pro/>)

内文小节：`1. Unlock the bootloader` · `2. Flash vendor image, TWRP, and optimized WearOS` · `3. Resize system partition in TWRP` · `4. Flash and launch Magisk app to finish the rooting process` · `5. Flash NetHunter` · `6. Set NetHunter watch face` · `Enjoy Kali NetHunter on the TicWatch Pro` · `Download links` · `Additional supported apps` · `Supported features` · `Hardware limitations`

摘要：All variants are supported (TicWatch Pro, Pro 2020, Pro 4G/LTE) From unpacking to running NetHunter in 6 steps: Unlock the bootloader Flash vendor image, TWRP, and optimized WearOS Resize system parti…

### [Installing NetHunter on the TicWatch Pro 3](<https://www.kali.org/docs/nethunter/installing-nethunter-on-the-ticwatch-pro-3/>)

内文小节：`1. Unlock the bootloader` · `2. Revert to stock WearOS2` · `3. Flash TWRP, OneOS image, Magisk, dm-verity disabler` · `4. Finalise Magisk app to finish rooting` · `5. Install NetHunter` · `6. Set NetHunter watch face (optional)` · `Enjoy Kali NetHunter on the TicWatch Pro 3` · `Downloads` · `Additional recommended apps` · `Supported features` · `Upcoming features (not guaranteed)` · `Hardware limitations`

摘要：All variants are supported (TicWatch Pro 3 GPS/LTE/Ultra GPS/Ultra LTE). From unpacking to running NetHunter in 6 steps: Unlock the bootloader Revert to stock WearOS2 Flash TWRP, WearOS image, Magisk,…

### [Installing NetHunter on the Xiaomi Mi A2](<https://www.kali.org/docs/nethunter/installing-nethunter-on-the-xiaomi-mi-a2/>)

内文小节：`1. Installing adb and fastboot` · `2. Unlock Bootloader` · `3. Flash PixelExperience Recovery and setup for LineageOS` · `4. Flash LineageOS 22.1 and Magisk 27` · `5. Install NetHunter` · `Enjoy Kali NetHunter on the Xiaomi Mi A2` · `Troubleshooting` · `Broken SSH` · `Broken APT` · `Broken Ctrl+C`

摘要：From unpacking to running NetHunter in 5 steps: Installing adb and fastboot Unlock Bootloader Flash PixelExperience Recovery and setup for LineageOS Flash LineageOS 22.1 and Magisk 27 Install NetHunte…

### [Installing NetHunter on the Xiaomi Mi A3](<https://www.kali.org/docs/nethunter/installing-nethunter-on-the-xiaomi-mi-a3/>)

内文小节：`1. Installing adb and fastboot` · `2. Unlock Bootloader` · `3. Flash LineageOS Recovery and LineageOS 22 and Magisk` · `4. Install NetHunter` · `Enjoy Kali NetHunter on the Xiaomi Mi A3`

摘要：From unpacking to running NetHunter in 4 steps: Installing adb and fastboot Unlock Bootloader Flash LineageOS Recovery and LineageOS 22 and Magisk Install NetHunter 1. Installing adb and fastboot kali…

### [NetHunter Application - KeX](<https://www.kali.org/docs/nethunter/nethunter-kex/>)

摘要：This application allows you to connect to your running session of Kali VNC. The default settings will require only password to be added in order to connect to localhost:1:5900 (port 5901). Updated on:…

### [NetHunter Application - Terminal](<https://www.kali.org/docs/nethunter/nethunter-terminal/>)

摘要：This application allows you to open up one of several kinds of terminals - a chrooted Kali terminal, a standard Android terminal, and a root Android terminal. Updated on: 2025-Jun-11 Authors: re4son ,…

### [NetHunter Audio](<https://www.kali.org/docs/nethunter/nethunter-audio/>)

摘要：Introduction This modules enables Audio in KeX session. Here is the step-by-step instructions for setting up and using the Audio Manager with Kali NetHunter. Follow the steps carefully to enable live …

### [NetHunter BadUSB Attack](<https://www.kali.org/docs/nethunter/nethunter-badusb/>)

摘要：This is our implementation of the BadUSB attack as demonstrated at Black Hat USA 2014. Enabling this USB mode will turn your device with its OTG USB cable into a network interface when plugged into a …

### [NetHunter Bluetooth-Arsenal](<https://www.kali.org/docs/nethunter/nethunter-btarsenal/>)

内文小节：`Start Bluetooth Arsenal` · `Main Menu` · `Tools` · `Spoof` · `Carwhisperer` · `Bad Bluetooth`

摘要：Bluetooth-Arsenal is the control centre for Bluetooth based attacks. Start Bluetooth Arsenal Click on the hamburger menu item and select “Bluetooth Arsenal” to open the Bluetooth menu. Here you can st…

### [NetHunter CARsenal](<https://www.kali.org/docs/nethunter/nethunter-carsenal/>)

内文小节：`Prerequisite - Kernel Modification` · `CARsenal Documentations` · `Resources` · `Credits` · `Main` · `Main : CAN Interfaces` · `Main : Services` · `VIN Info` · `Tools` · `Tools : Provided tools` · `CAN-USB` · `Caribou`

摘要：CARsenal is used to provide a Automotive Security toolset. Prerequisite - Kernel Modification Your kernel should have CAN support enabled. For more informations, follow “Configuring the Kernel - CARse…

### [NetHunter Chroot Manager](<https://www.kali.org/docs/nethunter/nethunter-chroot-manager/>)

摘要：The NetHunter chroot manager allows you to download and install a Kali Linux chroot (if one does not already exist), backup and restore a chroot, as well as remove an existing chroot. In addition, one…

### [NetHunter Components](<https://www.kali.org/docs/nethunter/nethunter-components/>)

内文小节：`Custom Android Kernel` · `Kali Linux chroot` · `NetHunter Android Application`

摘要：The NetHunter ROM overlay is composed of several parts that interact and rely on each other for proper operation. These parts include a custom Android Kernel, a Kali Linux Chroot, and a NetHunter Andr…

### [NetHunter Custom Commands](<https://www.kali.org/docs/nethunter/nethunter-custom-commands/>)

摘要：One of the cool features of the NetHunter Android application is the ability to add your own custom commands and functions. For example, if you do a lot of Wi-Fi work, it would make sense to add a cus…

### [NetHunter DuckHunter Attacks](<https://www.kali.org/docs/nethunter/nethunter-duckhunter/>)

内文小节：`Demo Video`

摘要：The DuckHunter HID option allows you to quickly and easily convert USB Rubber Ducky scripts into NetHunter HID Attacks format. You can choose an option from the Example presets menu or choose from a l…

### [NetHunter EvilTwin](<https://www.kali.org/docs/nethunter/nethunter-eviltwin/>)

内文小节：`Features` · `Requirements` · `Credits`

摘要：The EvilTwin attack module captures the handshake of the target network and creates a rogue access point with a captive portal to phish for passwords using handshake verification. You can run a fake A…

### [NetHunter Exploit Database SearchSploit](<https://www.kali.org/docs/nethunter/nethunter-searchsploit/>)

摘要：The SearchSploit pane allows you to easily search The Exploit Database archive for entries based on criteria of your choosing. Once you’ve found an exploit of interest, you can choose to view it onlin…

### [NetHunter HID Keyboard Attacks](<https://www.kali.org/docs/nethunter/nethunter-hid-attacks/>)

摘要：The NetHunter HID Attacks turn your device and its OTG USB cable into a pre-programmed keyboard, able to type any given commands. Previously, only “Teensy” type devices were able to do this… but no lo…

### [NetHunter Home Screen](<https://www.kali.org/docs/nethunter/nethunter-home-screen/>)

摘要：The NetHunter Home screen provides a common place to see some useful, frequently-used information about your device, including both external and internal IP addresses, as well as the availability of y…

### [NetHunter Kali Services](<https://www.kali.org/docs/nethunter/nethunter-kali-services/>)

摘要：The Kali Services pane allows you to start and stop various chrooted services such as SSH, Apache, OpenVPN, etc. To start or stop any of the available network services, simply tap on the appropriate b…

### [NetHunter Kernel](<https://www.kali.org/docs/nethunter/nethunter-kernel/>)

摘要：Here you can check if there’s a kernel available for your device, downloand, and flash it. If your device doesn’t support runtime flashing, you can use the same zip in recovery. Credits to HuskyDG for…

### [NetHunter KeX Manager](<https://www.kali.org/docs/nethunter/nethunter-kex-manager/>)

摘要：Being mobile doesn’t mean putting up with tiny! Kali NetHunter Desktop Experience puts the Kali Linux desktop in the palm of your hand. Connect a monitor via HDMI or screen casting and you have a Kali…

### [NetHunter MAC Changer](<https://www.kali.org/docs/nethunter/nethunter-mac-changer/>)

摘要：The MAC Changer pane allows you to change the MAC address of your NetHunter device network interfaces. You can choose to have the MAC address set to a random value or you can enter it manually using t…

### [NetHunter Metasploit Payload Generator](<https://www.kali.org/docs/nethunter/nethunter-mpg/>)

摘要：The MSFvenom Payload Creator (MFSPC) was written by g0tmi1k to take the pain out of generating payloads using the Metasploit msfvenom utility. Simply select your payload, set its options, and generate…

### [NetHunter Modules](<https://www.kali.org/docs/nethunter/nethunter-modules/>)

摘要：Load modules, if you have any. Most kernels come with all drivers as builtin, then this tab won’t be needed. However some kernels doesn’t build successfully, therefore those drivers have to be enabled…

### [NetHunter Nmap Scan](<https://www.kali.org/docs/nethunter/nethunter-nmap/>)

摘要：The Nmap Scan pane gives you easy access to the most commonly-used options of the immensely powerful Nmap scanner, allowing you to easily launch in-depth scans on targets or networks, without having t…

### [NetHunter Rootless](<https://www.kali.org/docs/nethunter/nethunter-rootless/>)

内文小节：`NetHunter Rootless Edition` · `Prerequisite:` · `Installation:` · `Usage:` · `NetHunter Editions:` · `Tips:`

摘要：NetHunter Rootless Edition Maximum flexibility with no commitment Install Kali NetHunter on any stock, unrooted Android device without voiding the warranty. Prerequisite: Android Device (Stock unmodif…

### [NetHunter Settings](<https://www.kali.org/docs/nethunter/nethunter-settings/>)

摘要：The settings lets you choose a custom bootanimation. You can also backup and restore nh_files, modify SELinux status, and set terminal style. Updated on: 2025-Jun-11 Author: yesimxev…

### [NetHunter Social Engineer Toolkit](<https://www.kali.org/docs/nethunter/nethunter-set/>)

摘要：The Social Engineer Toolkit phishing email template creator gives you the possibility to customise 3 phishing email templates. Insert your own link, thumbnail, name, and subject. The templates are sav…

### [NetHunter USB-Arsenal](<https://www.kali.org/docs/nethunter/nethunter-usbarsenal/>)

摘要：USB-Arsenal is the control centre for USB based attacks. It is used to enable USB gadget modes using the USB Function Selector : If mass storage gadget mode has been enabled then .iso and .img files c…

### [NetHunter Wardriving](<https://www.kali.org/docs/nethunter/nethunter-wardriving/>)

内文小节：`Options` · `GPS` · `Kismet` · `Workflow` · `Logging`

摘要：Wardriving NetHunter’s Wardriving panel merges your Android device’s GPS and external radios into Kismet, producing a real-time, geotagged RF heatmap. Use its toggles to feed Kismet live location and …

### [NetHunter WifiPumpkin](<https://www.kali.org/docs/nethunter/nethunter-wifipumpkin/>)

摘要：The WifiPumpkin3 is an evil access-point implementation by P0cL4bs that performs rogue Wi-Fi AP and MitM attacks. You can run a fake Access Point with or without a captive portal. Customise the settin…

### [NetHunter WPS Attacks](<https://www.kali.org/docs/nethunter/nethunter-wps/>)

摘要：Run WPS attacks, even without an external adapter! OneShot allows you to run Pixie Dust, online bruteforce, Push Button Connection, and PIN prediction without monitor mode with the wpa_supplicant. Upd…

### [Patching the Kernel](<https://www.kali.org/docs/nethunter/nethunter-kernel-1-patching/>)

内文小节：`Patching`

摘要：We will continue from the Porting NetHunter page and work on the Google Nexus 6P kernel as an example. The idea stays the same though. Patching By default, we apply Wi-Fi injection patches and patches…

### [Porting NetHunter to New Devices manually](<https://www.kali.org/docs/nethunter/porting-nethunter/>)

内文小节：`Getting Started` · `Kernel Version` · `Finding Kernel Sources` · `Making a Test Kernel`

摘要：In order to port NetHunter to a new device, it’s important to understand how NetHunter is separated. NetHunter is divided by the rootfs (also known as the chroot but will be referred to here as rootfs…

### [Porting NetHunter to New Devices with kernel builder](<https://www.kali.org/docs/nethunter/porting-nethunter-kernel-builder/>)

内文小节：`Getting Started` · `Kernel Version` · `Finding Kernel Sources` · `Making a Test Kernel`

摘要：In order to port NetHunter to a new device, it’s important to understand how NetHunter is separated. NetHunter is divided by the rootfs (also known as the chroot but will be referred to here as rootfs…

### [Testing Checklist](<https://www.kali.org/docs/nethunter/testing-checklist/>)

摘要：Beginning a checklist for testing new devices: Does it boot? Did applications install and do they work? Android VNC BlueNMEA DriveDroid Hacker’s Keyboard Kali NetHunter Application RF Analyzer SuperSU…

### [Wireless Cards and NetHunter](<https://www.kali.org/docs/nethunter/wireless-cards/>)

摘要：External wireless cards are necessary because Android devices do not support monitor mode on most devices apart from some Qualcomm chips used in modern Snapdragon SOC. There are some devices that can …


## NetHunter Pro（`nethunter-pro`）

NetHunter Pro 设备与用法 · 共 **2** 篇

### [NetHunter Pro - Enable OTG in SDM845 (OnePlus6/6T and POCO F1)](<https://www.kali.org/docs/nethunter-pro/enable-otg-sdm845/>)

内文小节：`Video Guide` · `Install pre-requisites` · `NOTE:` · `Steps to modify the dtb`

摘要：Video Guide Install pre-requisites sudo apt install -y abootimg device-tree-compiler NOTE: A few devices, like the POCO F1, require externally powered OTG cables to function. So, make sure to connect …

### [Waydroid on NetHunter Pro](<https://www.kali.org/docs/nethunter-pro/waydroid/>)

内文小节：`What is Waydroid` · `Install Instructions`

摘要：What is Waydroid Waydroid is an open-source project that allows you to run the Android operating system in a container on a Linux system, effectively letting you run Android apps alongside Linux apps …


## 开发与打包（`development`）

Debian 打包、Kali 源码、贡献流程 · 共 **21** 篇

### [Advanced Packaging Step-By-Step Example (FinalRecon & Python-icmplib)](<https://www.kali.org/docs/development/advanced-packaging-example/>)

内文小节：`FinalRecon Code Overview` · `Missing Tag Releases` · `License` · `Dependencies` · `Description(s)` · `Maintainer(s)` · `Setting Up The Environment` · `Downloading Git Snapshot` · `Creating Package Source Code` · `FinalRecon (Pip) Dependencies` · `Editing FinalRecon Package Source Code` · `Changelog`

摘要：This guide is accurate at the time of writing. As it references a lot of external resources out of our control, items may be different over time (as software gets updated). FinalRecon is a Python 3 ap…

### [ARM Build Scripts](<https://www.kali.org/docs/development/arm-build-scripts/>)

内文小节：`Building` · `Help` · `Custom Values`

摘要：These are the same build scripts that we use to generate the pre-generated official Kali Linux ARM images, found here: https://www.kali.org/get-kali/ There are additional scripts included in the repos…

### [ARM Cross-Compilation](<https://www.kali.org/docs/development/arm-cross-compilation-environment/>)

内文小节：`Setting Up Your Development Box` · `Install Dependencies` · `Download Linaro Toolchain` · `Set Environment Variables`

摘要：The following guide will demonstrate how to set up an ARM cross-compilation environment in Kali Linux. This guide is the starting point for many of our contributed “Custom ARM Images” articles. You’ll…

### [Building Custom Kali ISOs](<https://www.kali.org/docs/development/dojo-mastering-live-build/>)

内文小节：`The Awesomeness of Live Build`

摘要：One of the most powerful features of Kali Linux is the ability to create your own flavours of the distribution containing customized tools, desktop managers, and services. This workshop will show you …

### [Contributing run-time tests with autopkgtest](<https://www.kali.org/docs/development/contributing-runtime-tests/>)

内文小节：`Why Kali could benefit from your help` · `A bit of autopkgtest background` · `Structuring Test Files` · `Learning by examples` · `What to do` · `Running tests locally`

摘要：Why Kali could benefit from your help With Kali Linux being a rolling distribution it will occasionally have packages that break due to changes in their dependencies. To best combat this, we have set …

### [Creating A Custom Kali ISO](<https://www.kali.org/docs/development/live-build-a-custom-kali-iso/>)

内文小节：`An Introduction to Building Your Own Kali ISO` · `Where Should You Build Your ISO?` · `Kali Environment` · `Non-Kali Debian-Based Environment` · `Re-building the Latest Kali Image` · `Configuring The Kali ISO Build (Optional)` · `Building a Kali Linux ISO for Different Architectures (Optional)` · `Using A Custom Network Mirror For Building (Optional)` · `Help Screen` · `Testing Built Image`

摘要：An Introduction to Building Your Own Kali ISO Building a customized Kali Linux image is not as complex as you may be thinking. It is easy, fun, and rewarding! Kali Linux traditionally, has been a Live…

### [Custom Beaglebone Black Image](<https://www.kali.org/docs/development/custom-beaglebone-black-image/>)

内文小节：`01. Create a Kali rootfs` · `02. Create the Image File` · `03. Partition and Mount the Image File` · `04. Copy and Modify the Kali rootfs` · `05. Compile the Beaglebone Black Kernel and Modules`

摘要：The following document describes our own method of creating a custom Kali Linux Beaglebone Black ARM image and is targeted at developers. If you would like to install a pre-made Kali image, check out …

### [Custom Chromebook Image](<https://www.kali.org/docs/development/custom-chromebook-kernel-image/>)

摘要：The following document describes our own method of creating a custom Kali Linux Samsung Chromebook ARM image and is targeted at developers. If you would like to install a pre-made Kali image, check ou…

### [Custom CuBox Image](<https://www.kali.org/docs/development/custom-cubox-image/>)

内文小节：`01. Create a Kali rootfs` · `02. Create the Image File` · `03. Partition and Mount the Image File` · `04. Copy and Modify the Kali rootfs` · `05. Compile the CuBox Kernel and Modules`

摘要：The following document describes our own method of creating a custom Kali Linux CuBox ARM image and is targeted at developers. If you would like to install a pre-made Kali image, check out our Install…

### [Custom EfikaMX Image](<https://www.kali.org/docs/development/custom-efikamx-image/>)

内文小节：`01. Create a Kali rootfs` · `02. Create the Image File` · `03. Partition and Mount the Image File` · `04. Copy and Modify the Kali rootfs` · `05. Compile the EfikaMX Kernel and Modules`

摘要：The following document describes our own method of creating a custom Kali Linux EfikaMX ARM image and is targeted at developers. If you would like to install a pre-made Kali image, check out our Insta…

### [Custom MK/SS808 Image](<https://www.kali.org/docs/development/custom-kali-arm-ss808-image/>)

内文小节：`01. Create a Kali rootfs` · `02. Create the Image File` · `03. Partition and Mount the Image File` · `04. Copy and Modify the Kali rootfs` · `05. Compile the rk3066 Kernel and Modules` · `07. dd the Image to a USB device`

摘要：The following document describes our own method of creating a custom Kali Linux MK/SS808 ARM image and is targeted at developers. If you would like to install a pre-made Kali image, check out our Inst…

### [Custom ODROID X2 U2 Image](<https://www.kali.org/docs/development/custom-odroid-kernel-image/>)

摘要：The following document describes our own method of creating a custom Kali Linux ODROID image and is targeted at developers. If you would like to install a pre-made Kali ODROID image, check our Install…

### [Custom Raspberry Pi Image](<https://www.kali.org/docs/development/custom-raspberry-pi-image/>)

内文小节：`01. Create a Kali rootfs` · `02. Create the Image File` · `03. Partition and Mount the Image File` · `04. Copy and Modify the Kali rootfs` · `05. Compile the Raspberry Pi Kernel and Modules`

摘要：The following document describes our own method of creating a custom Kali Linux Raspberry Pi ARM image and is targeted at developers. If you would like to install a pre-made Kali image, check out our …

### [Generate an Updated Kali ISO](<https://www.kali.org/docs/development/generate-updated-kali-iso/>)

摘要：Kali Linux allows you to generate updated ISOs of Kali using Debian live-build scripts on the fly. The easiest way to generate these images is from within a pre existing Kali Linux environment . You w…

### [Intermediate packaging step-by-step example](<https://www.kali.org/docs/development/intermediate-packaging-example/>)

内文小节：`Photon Code Overview` · `Setting Up Environment` · `Downloading Tag Release` · `Creating Package Source Code` · `Collecting Information` · `License/Maintainers` · `Dependencies/Maintainers` · `Maintainers` · `Description` · `Editing Package Source Code` · `Changelog` · `Control`

摘要：Photon Photon is a Python3 application with multiple dependencies. This makes it a more interesting package than Instaloader as potentially more work is involved. Photon Code Overview Like before with…

### [Introduction to packaging step-by-step example](<https://www.kali.org/docs/development/intro-to-packaging-example/>)

内文小节：`Instaloader Code Overview` · `Setting Up The Environment` · `Downloading Tag Releases` · `Creating Package Source Code` · `Collecting Information` · `License/Maintainers` · `Dependencies/Maintainers` · `Maintainers` · `Description` · `Editing Package Source Code` · `Changelog` · `Control`

摘要：Instaloader Instaloader is a Python 3 application with a single dependency (Python’s requests ). This makes it a relatively simple package, however not as straightforward as only packaging up a shell …

### [Packaging Applications with Kaboxer](<https://www.kali.org/docs/development/packaging-apps-with-kaboxer/>)

内文小节：`Introduction to Kaboxer` · `Packaging a simple application with Kaboxer` · `Prerequisites` · `Creating a Docker image` · `Adding Kaboxer meta-information` · `Building the image and testing it` · `Adding Debian packaging files` · `More Kaboxer features` · `Sharing resources (network or file system)` · `Multi-component applications` · `Integrating the application in the Kali menu` · `Convenience command-line helpers`

摘要：Some applications can’t be packaged properly, for example when they have dependencies on obsolete libraries that are no longer available in Kali. Others need to run in isolation because their behaviou…

### [Preparing a Kali Linux ARM chroot](<https://www.kali.org/docs/development/kali-linux-arm-chroot/>)

内文小节：`Some Notes on This Procedure` · `Real-World Custom Kali Linux Builds for ARM Devices` · `An Annotated Example of a Generic ARM Build of Kali Linux` · `Install Required Tools and Dependencies` · `Enable Cross-Compilation` · `Define Architecture and Custom Packages` · `Build the Kali rootfs` · `Manual Configuration Within the chroot` · `Cleanup`

摘要：Although you can download pre-rolled Kali ARM images from our download area, there may be applications which will require building your own custom bootstrapped Kali rootfs for ARM. The following proce…

### [Rebuilding a Source Package](<https://www.kali.org/docs/development/rebuilding-a-package-from-source/>)

内文小节：`Downloading the Package Source` · `Edit the Package Source Code` · `Check for Build Dependencies` · `Install Build Dependencies` · `Build the Modified Package` · `Install the New Package`

摘要：Kali Linux is easy to customize at a per-package level , and it’s equally simple to make modifications to individual packages and rebuild them from their source code for inclusion in your custom ISO o…

### [Recompiling the Kali Linux Kernel](<https://www.kali.org/docs/development/recompiling-the-kali-linux-kernel/>)

内文小节：`Install Build Dependencies` · `Download the Kali Linux Kernel Source Code` · `Configure Your Kernel` · `Build the Kernel` · `Install the Modified Kernel`

摘要：The customizability of Kali Linux extends all the way down into the Linux kernel. Depending on your requirements, you might want to add drivers, patches, or kernel features that are not included in th…

### [Setting up a system for packaging](<https://www.kali.org/docs/development/setting-up-packaging-system/>)

内文小节：`VM or install?` · `Setting up the VM` · `Installing packages` · `User accounts and keys` · `Setting up files` · `Sbuild` · `Approx (caching proxy)`

摘要：VM or install? In this walkthrough we will be explaining certain things that are only on a VM. It is your choice if you want to install a full Kali system (or if you already have one, if you want to u…


## 故障排查（`troubleshooting`）

常见问题、显卡、网络、双系统 · 共 **12** 篇

### [Common Cloud Based Setup Information](<https://www.kali.org/docs/troubleshooting/common-cloud-setup/>)

内文小节：`Kali in the cloud`

摘要：A cloud image is designed to be lightweight while having the core tools to get the job done. If the base install is lacking something that may be needed, then the following should cover most questions…

### [Discovering Problems With Download Speed](<https://www.kali.org/docs/troubleshooting/download-speed-issues/>)

内文小节：`How our downloads work` · `Determining which mirror we are at` · `Submitting bugs` · `Using a different mirror`

摘要：How our downloads work Kali Linux operates off of a network of community and official mirrors. What this means is that when you click to download Kali Linux there are some steps that are done before y…

### [Fixing Dual Boot](<https://www.kali.org/docs/troubleshooting/dual-boot/>)

内文小节：`Assumptions` · `Troubleshooting and fixing`

摘要：This page explains how to fix Dual Boot, in the particular case where the GRUB boot menu only allows you to boot Kali Linux, and doesn’t show entries for other operating systems. Assumptions This guid…

### [Fixing PostgreSQL 'collation version mismatch'](<https://www.kali.org/docs/troubleshooting/postgresql-collation-mismatch-error/>)

摘要：After a system upgrade, when running tools such as Metasploit, GVM, or Bloodhound, you may encounter PostgreSQL error messages. These errors prevent the tools from functioning properly, citing “collat…

### [Graphics issues on bare-metal installation](<https://www.kali.org/docs/troubleshooting/graphics-issues-on-bare-metal-installation/>)

内文小节：`Kernel Update and DKMS Module Issues` · `GNOME on Wayland Issues`

摘要：This document covers several common graphics issues that occur when running Kali Linux on bare-metal systems (physical hardware) rather than in virtual machines. Users with NVIDIA graphics cards frequ…

### [Handling common APT problems](<https://www.kali.org/docs/troubleshooting/handling-common-apt-errors/>)

内文小节：`A foreword: please run ‘apt update’` · `Package is to be installed, however it is not going to be: please use ‘apt full-upgrade’` · `The following package has been kept back` · `A package needs a newer version, but there is no new version available` · `A package is trying to overwrite a file and causing an error` · `EXPKEYSIG / “Missing key” / repository signature errors`

摘要：This page is due for more content as issues come up that need addressing. If you have an issue with APT that is not addressed in this page, please create a merge request with the steps to solve the pr…

### [Minimum Install Setup Information](<https://www.kali.org/docs/troubleshooting/common-minimum-setup/>)

内文小节：`WSL` · `Docker`

摘要：A minimum install is one that does not have kali-linux-headless or at least one of the kali-tools- installed. There may be many reasons for this, however should those reasons change and someone want t…

### [No sound on Kali 2023.2](<https://www.kali.org/docs/troubleshooting/no-sound/>)

内文小节：`Background` · `Upgrading to PipeWire` · `Missing firmware for Intel SOF audio devices` · `Issues with VMware Workstation`

摘要：Background Starting with Kali 2023.2 , Kali Linux uses PipeWire to deal with audio, for both the XFCE desktop and the GNOME desktop. Before that, Kali Linux used another sound server named PulseAudio …

### [The Basics of Troubleshooting](<https://www.kali.org/docs/troubleshooting/basic-troubleshooting/>)

内文小节：`Log files` · `Commands and processes` · `The most important tool`

摘要：Troubleshooting Linux can be very confusing due to all of the moving parts. This doc will aim to cover as much as possible while still being understandable. If you believe something is missing or coul…

### [Troubleshooting Installations Failures](<https://www.kali.org/docs/troubleshooting/troubleshooting-a-kali-linux-install/>)

摘要：There can be a wide variety of reasons for a Kali Linux installation to fail. This could include issues such as a corrupt or incomplete ISO download, not enough disk space on the target machine, etc. …

### [Troubleshooting Wireless Drivers](<https://www.kali.org/docs/troubleshooting/troubleshooting-wireless-driver-issues/>)

内文小节：`1. No Interface` · `2. Interface But Can’t Do Anything` · `3. No Monitor Mode` · `4. Injection` · `Additional Links`

摘要：Troubleshooting wireless driver issues in Linux can be a frustrating experience if you don’t know what to look for. This article is meant to be used as a general guideline to better help you find the …

### [Windows Anti-virus Warning](<https://www.kali.org/docs/troubleshooting/windows-antivirus-warning/>)

摘要：When downloading Kali Linux from the official source you may run into an anti-virus warning on Window machines. This warning is triggered as Kali Linux contains many pentesting tools that Windows flag…


## 政策与法律（`policy`）

使用政策、商标、法律边界 · 共 **10** 篇

### [Cookie Policy](<https://www.kali.org/docs/policy/cookie/>)

内文小节：`What is a Cookie?` · `First-party cookies and third-party cookies` · `Persistent and session cookies` · `How do I manage cookies?` · `What kind of Cookies do we use?` · `Updates to this Cookie Policy`

摘要：Cookie Policy | Kali Linux Documentation :root{--primary-color:#367BF0;--body-color:light-dark(#f9f9f9, #010409);--text-color:light-dark(#636363, #eeeeec);--text-color-dark:light-dark(#242738, white);…

### [Kali Linux EULA](<https://www.kali.org/docs/policy/eula/>)

摘要：For Kali Linux’s End-User License Agreement (EULA), please see the following page: kali.org/docs/policy/eula/EULA.txt . Updated on: 2025-Jun-11 Author: g0tmi1k…

### [Kali Linux Network Service Policy](<https://www.kali.org/docs/policy/kali-linux-network-service-policy/>)

摘要：Kali Linux is a penetration testing toolkit, and may potentially be used in “hostile” environments. Accordingly, Kali Linux deals with network services in a very different way than typical Linux distr…

### [Kali Linux Open Source Policy](<https://www.kali.org/docs/policy/kali-linux-open-source-policy/>)

摘要：Kali Linux is a Linux distribution that aggregates thousands of free software packages in its main section. As a Debian derivative, all of the core software in Kali Linux complies with the Debian Free…

### [Kali Linux Trademark Policy](<https://www.kali.org/docs/policy/trademark/>)

内文小节：`Linux` · `Kali & OffSec` · `Some of our Trademarks` · `Use in Print, Web, Media and Public Display` · `Contact`

摘要：Linux The registered trademark Linux® is used pursuant to a sublicense from the Linux Foundation , the exclusive licensee of Linus Torvalds, owner of the mark on a worldwide basis. Kali & OffSec Kali …

### [Kali Linux Update Policies](<https://www.kali.org/docs/policy/kali-linux-security-update-policies/>)

摘要：The majority of the packages comprising the Kali Linux distribution are drawn directly from the Debian repositories. For those packages which have been incorporated into Kali Linux “as-is” - i.e. the …

### [Kali Linux User Policy](<https://www.kali.org/docs/policy/kali-linux-user-policy/>)

摘要：In order to execute commands at a privileged level, Kali uses two methods to do so: pkexec (GUI & cli) sudo (cli) It is also worth bearing in mind, some tools may perform differently without super-use…

### [Kali's Relationship With Debian](<https://www.kali.org/docs/policy/kali-linux-relationship-with-debian/>)

内文小节：`Forked Packages` · `Additional Packages`

摘要：The Kali Linux distribution is based on Debian Testing . Therefore, most of the Kali packages are imported, as-is, from the Debian repositories. In some cases, newer packages may be imported from Debi…

### [Penetration Testing Tools Policy](<https://www.kali.org/docs/policy/penetration-testing-tools-policy/>)

内文小节：`New Tool Requests`

摘要：One of the key tasks in transitioning from BackTrack to Kali was combing through the packages and selecting the “best of breed” from what was available. We realize that there are many tools or scripts…

### [Privacy Policy](<https://www.kali.org/docs/policy/privacy/>)

内文小节：`Collection of Information` · `Cookie/Tracking Technology` · `Distribution of Information` · `Commitment to Data Security` · `Privacy Contact Information`

摘要：Thank you for visiting our web site. The following privacy policy tells you how we use personal information collected at this site. Please read this privacy policy before using the site or submitting …


## 社区（`community`）

论坛、Discord、参与方式 · 共 **8** 篇

### [How And Where To Get Help](<https://www.kali.org/docs/community/getting-help/>)

内文小节：`Local Documentation` · `Online Documentation` · `Troubleshooting` · `Reporting`

摘要：This doc shares some of the same information as our basics of troubleshooting doc . If you feel like you do not need a lot of extra information or explanation, basics of troubleshooting may be the doc…

### [Kali Linux Community Forums](<https://www.kali.org/docs/community/kali-linux-community-forums/>)

内文小节：`Forum Rules`

摘要：The official community forums for the Kali Linux project are located at forums.kali.org . It’s our goal that everyone feel welcome in the Kali Linux community, and to ensure that everyone understands …

### [Kali Linux IRC Channel](<https://www.kali.org/docs/community/kali-linux-irc-channel/>)

内文小节：`#kali-linux IRC Rules and Guidelines` · `Registered nickname` · `How to Treat Other Users` · `How to Argue` · `Language` · `Staying on Topic`

摘要：Kali Linux has an official IRC channel, #kali-linux , on the OFTC network. Please take a few moments to review the rules and guidelines below before joining the channel. #kali-linux IRC Rules and Guid…

### [Official Kali Linux Mirrors](<https://www.kali.org/docs/community/kali-linux-mirrors/>)

内文小节：`Using Official Repositories`

摘要：Using Official Repositories The Kali Linux distribution has two repositories , which are mirrored world-wide: http.kali.org ( mirrorlist ): the main package repository; cdimage.kali.org ( mirrorlist )…

### [Official Kali Linux Sites](<https://www.kali.org/docs/community/list-of-official-kali-sites/>)

内文小节：`Public Websites` · `Documentation` · `Community` · `Mirrors` · `Development` · `Infrastructure` · `External` · `Social Media Networks` · `Marketplaces and Stores`

摘要：The Kali Linux project uses various subdomains of kali.org, each with a specific purpose. This article lists the official Kali sites and the purpose each one of them serves. Note that these sites are …

### [Setting Up a Kali Linux Mirror](<https://www.kali.org/docs/community/setting-up-a-kali-linux-mirror/>)

内文小节：`How to Set Up a Public Kali Linux Mirror` · `Requirements` · `Create a User Account for the Mirror` · `Create Directories for the Mirror` · `Configure rsync` · `Configure Your Mirror` · `Set Up the SSH Keys` · `Making it Public - Getting in Contact` · `Initial Sync` · `Firewall Rules` · `Set Up cron to Manually Mirror ISO Images` · `How to Set Up a Private Kali Linux Mirror`

摘要：How to Set Up a Public Kali Linux Mirror The explanations below are of interest to you if you want to contribute a publicly accessible mirror and if you want to integrate it in one of the mirror redir…

### [Submitting Bugs for Kali Linux](<https://www.kali.org/docs/community/submitting-issues-kali-bug-tracker/>)

内文小节：`Introduction` · `How to Report a Bug` · `Browsing Without an Account` · `Be Sure You Are Not Duplicating a Previous Report` · `Signing Up For a Bug Tracker Account` · `Creating the Report` · `Building the Description Scenario` · `The Importance of Reproducibility` · `Providing Steps to Reproduce the Issue` · `Providing Additional Information`

摘要：Introduction This article is a guide for putting together a bug report so that it gets addressed as quickly as possible. First, Kali Linux is a labor of love, born out of a desire to give back to the …

### [Where and How to Contribute to Kali](<https://www.kali.org/docs/community/contribute/>)

内文小节：`Kali Community` · `GitLab` · `Forums` · `Discord` · `IRC` · `Bug Tracker` · `Kali Linux Docs` · `Kali Tools` · `Kali Packages` · `Upstream Package Updates` · `Packaging New Tools` · `Autopkgtests (debci)`

摘要：Kali Linux is a large project made up of many different parts. One of the most popular questions that the Kali team receives is “ How can I help ?” To help answer that question, this page will contain…


## 根文档（`docs`）

文档入口页 · 共 **16** 篇

### [Cloud](<https://www.kali.org/docs/cloud/>)

摘要：Cloud | Kali Linux Documentation :root{--primary-color:#367BF0;--body-color:light-dark(#f9f9f9, #010409);--text-color:light-dark(#636363, #eeeeec);--text-color-dark:light-dark(#242738, white);--white-…

### [Community](<https://www.kali.org/docs/community/>)

摘要：Community | Kali Linux Documentation :root{--primary-color:#367BF0;--body-color:light-dark(#f9f9f9, #010409);--text-color:light-dark(#636363, #eeeeec);--text-color-dark:light-dark(#242738, white);--wh…

### [Containers](<https://www.kali.org/docs/containers/>)

摘要：Containers | Kali Linux Documentation :root{--primary-color:#367BF0;--body-color:light-dark(#f9f9f9, #010409);--text-color:light-dark(#636363, #eeeeec);--text-color-dark:light-dark(#242738, white);--w…

### [General Use](<https://www.kali.org/docs/general-use/>)

摘要：General Use | Kali Linux Documentation :root{--primary-color:#367BF0;--body-color:light-dark(#f9f9f9, #010409);--text-color:light-dark(#636363, #eeeeec);--text-color-dark:light-dark(#242738, white);--…

### [Installation](<https://www.kali.org/docs/installation/>)

摘要：Installation | Kali Linux Documentation :root{--primary-color:#367BF0;--body-color:light-dark(#f9f9f9, #010409);--text-color:light-dark(#636363, #eeeeec);--text-color-dark:light-dark(#242738, white);-…

### [Introduction](<https://www.kali.org/docs/introduction/>)

摘要：Introduction | Kali Linux Documentation :root{--primary-color:#367BF0;--body-color:light-dark(#f9f9f9, #010409);--text-color:light-dark(#636363, #eeeeec);--text-color-dark:light-dark(#242738, white);-…

### [Kali Development](<https://www.kali.org/docs/development/>)

摘要：Kali Development | Kali Linux Documentation :root{--primary-color:#367BF0;--body-color:light-dark(#f9f9f9, #010409);--text-color:light-dark(#636363, #eeeeec);--text-color-dark:light-dark(#242738, whit…

### [Kali NetHunter](<https://www.kali.org/docs/nethunter/>)

内文小节：`Overview` · `1.0 NetHunter Editions` · `2.0 NetHunter Supported Devices and ROMs` · `3.0 Downloading NetHunter` · `4.0 Building NetHunter` · `5.0 Installing NetHunter on top of Android` · `6.0 Post Installation Setup` · `7.0 Kali NetHunter Application` · `Nethunter management` · `Tools` · `Attacks` · `8.0 Porting NetHunter to New Devices`

摘要：Kali NetHunter is a free & Open-source Mobile Penetration Testing Platform for Android devices, based on Kali Linux. Overview Kali NetHunter is available for un-rooted devices (NetHunter Rootless), fo…

### [Kali NetHunter Pro](<https://www.kali.org/docs/nethunter-pro/>)

内文小节：`Content:` · `Overview` · `2.0 NetHunter Pro Supported Devices` · `3.0 Installing NetHunter Pro`

摘要：Kali NetHunter Pro is Pure Kali Linux for Mainline devices like PinePhone/Pro and QCOM Devices. Content: Overview NetHunter Pro Supported Devices Installing NetHunter Pro Overview Kali NetHunter Pro i…

### [Kali On ARM](<https://www.kali.org/docs/arm/>)

摘要：For a device, image and kernel overview, see arm.kali.org Updated on: 2025-Jun-11 Author:…

### [Policy](<https://www.kali.org/docs/policy/>)

摘要：Policy | Kali Linux Documentation :root{--primary-color:#367BF0;--body-color:light-dark(#f9f9f9, #010409);--text-color:light-dark(#636363, #eeeeec);--text-color-dark:light-dark(#242738, white);--white…

### [Tools](<https://www.kali.org/docs/tools/>)

摘要：Tools | Kali Linux Documentation :root{--primary-color:#367BF0;--body-color:light-dark(#f9f9f9, #010409);--text-color:light-dark(#636363, #eeeeec);--text-color-dark:light-dark(#242738, white);--white-…

### [Troubleshooting](<https://www.kali.org/docs/troubleshooting/>)

摘要：Troubleshooting | Kali Linux Documentation :root{--primary-color:#367BF0;--body-color:light-dark(#f9f9f9, #010409);--text-color:light-dark(#636363, #eeeeec);--text-color-dark:light-dark(#242738, white…

### [USB](<https://www.kali.org/docs/usb/>)

摘要：USB | Kali Linux Documentation :root{--primary-color:#367BF0;--body-color:light-dark(#f9f9f9, #010409);--text-color:light-dark(#636363, #eeeeec);--text-color-dark:light-dark(#242738, white);--white-co…

### [Virtualization](<https://www.kali.org/docs/virtualization/>)

摘要：Virtualization | Kali Linux Documentation :root{--primary-color:#367BF0;--body-color:light-dark(#f9f9f9, #010409);--text-color:light-dark(#636363, #eeeeec);--text-color-dark:light-dark(#242738, white)…

### [WSL](<https://www.kali.org/docs/wsl/>)

摘要：WSL | Kali Linux Documentation :root{--primary-color:#367BF0;--body-color:light-dark(#f9f9f9, #010409);--text-color:light-dark(#636363, #eeeeec);--text-color-dark:light-dark(#242738, white);--white-co…

