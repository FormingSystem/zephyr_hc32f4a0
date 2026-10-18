---
id: learning.zephyr-docs.boards-intel-ite.page-2
title: Zephyr Audio DSP Development on Chromebooks
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/intel/adsp/doc/chromebooks_adsp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="zephyr-audio-dsp-development-on-chromebooks"></a>

<a id="id1"></a>

# 第2章\_在Chromebook上开发Zephyr音频DSP（Audio DSP Development）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/intel/adsp/doc/chromebooks_adsp.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

Intel Chromebook的音频数字信号处理器（Audio DSP）配置为使用SOF“社区（Community）”密钥签名固件，因此可以接受用户自行开发的固件，例如Zephyr应用，SOF本身也是其中之一，包括Zephyr示例及测试套件。

<a id="initial-tgl-chromebook-setup"></a>

## TGL Chromebook初始设置（Initial Setup）

这些说明专门针对代号“delbin”的Asus Flip CX5编写，但应当也适用于较新的其他Intel设备。

打开设备电源并连接无线网络。设备可能会下载固件更新，原作者的设备就是如此。先让更新完成，以确保有两个可用的操作系统镜像。

<a id="enable-developer-mode"></a>

### 启用开发者模式（Developer Mode）

关闭设备，可使用右下角菜单，或长按侧面电源键。

按住Esc和Refresh，再按电源键，进入恢复模式（Recovery Mode）。Refresh是数字3上方带圆形箭头的重新加载键。恢复模式不支持触摸屏及触摸板，应使用方向键导航。

选择“Advanced Options”，再选择“Enable Developer Mode”，确认启用。在引导加载程序界面选择“Boot from Internal Storage”。此后每次启动都会显示该界面，提示启动未经验证。

等待设备完成所需的数据擦除。原作者的设备完整写入有状态分区（Stateful Partition）约需15分钟。重启后再次选择“Boot from Internal Storage”，并重新用Google账户设置设备。

<a id="make-a-recovery-drive"></a>

### 制作恢复盘（Recovery Drive）

原文提醒，开发过程中可能使设备无法正常运行，需要恢复盘。应从Google Web Store安装Chromebook Recovery Utility并制作恢复盘。

任何安装Chrome的计算机及操作系统都可以制作恢复盘，但直接在Chromebook上最方便，因为它知道自身设备ID，例如Asus Tiger Lake开发板的“DELBIN-XHVI D4B-H4D-G4G-Q9A-A9P”。恢复操作不会改变开发者模式或固件设置，但会清除根文件系统及对`/usr/local`所做的定制。因此，应采取能够承受实验设备数据丢失的工作方式。

<a id="make-the-root-filesystem-writable"></a>

### 使根文件系统可写（Writable Root Filesystem）

出于安全考虑，ChromeOS对只读根文件系统签名，并通过Linux的dm-verity功能，以密码学方式验证所有访问。修改根文件系统，例如为定制内核安装模块，需要先关闭dm-verity层：

先按Ctrl-Alt-T打开终端，在`crosh>`提示符输入`shell`，进入以chronos用户运行的Shell。最后，在开发者模式下执行`sudo su -`即可获得root提示符。

```text
crosh> shell
chronos@localhost / $ sudo su -
localhost ~ #
```

接着需要关闭引导加载程序的签名验证，因为后续修改会破坏原有签名。签名验证由ROM引导加载程序执行，属于操作系统之外的启动阶段；此设置是仅在开发者模式可用、传递给该启动代码的指令。

```text
cros# crossystem dev_boot_signed_only=0
```

为清楚区分环境，本文在ChromeOS核心Shell中输入的命令使用主机名`cros`作为前缀。

接下来禁用验证步骤：

```text
cros# /usr/share/vboot/bin/make_dev_ssd.sh --remove_rootfs_verification
```

此命令会失败，提示正在修改整个运行中系统的设置，并建议使用仅修改当前分区的`–partitions X`参数。按提示运行修改后的命令，然后重启。

重启后，Chromebook会将原始存储设备，例如`/dev/nvme0n1p5`，挂载为根文件系统，而不再使用dm-0验证设备；根文件系统也变为可读写。

该命令实际修改的是已安装内核镜像的命令行，并在`/mnt/stateful_partition/cros_sign_backups`保存备份，使根设备参数为`root=<guid>`，而不再是`root=dm-0`。其他verity配置似乎仍然保留，只是不再尝试挂载所得的、签名现已无效的分区。

原作者补充：后续很可能会替换此内核，因此本可直接编辑新内核的命令行，省去烧录并重启这个修改后内核的步骤。不过，作者选择分步操作，以免同时处理过多事项。

<a id="enable-chromeos-ssh"></a>

### 启用ChromeOS SSH

以可写分区启动后，可用以下命令开启内置SSH服务器：

```text
cros# /usr/libexec/debugd/helpers/dev_features_ssh
```

chronos及root账户默认都没有密码。因此，除非打算手动输入SSH密钥，一般应先为首次登录设置密码，再运行`ssh-copy-id`：

```text
cros# passwd
```

然后通过SSH登录Chromebook，像其他Linux系统一样，将密钥加入`.ssh/authorized_keys`。

<a id="install-crouton"></a>

## 安装Crouton

Zephyr集成工具需要完整Linux环境，无法在ChromeOS的精简发行版中运行。因此需要安装一个Linux运行环境。原文明确要求不要使用ChromeOS开发者设置中的“Linux Development Environment”，即Crostini：它运行于虚拟机（VM），而这些工具需要访问真实硬件上的实际内核。应安装Crouton（[https://github.com/dnschneid/crouton](https://github.com/dnschneid/crouton)），这是社区提供的chroot环境，可保留对真实硬件sysfs及`/dev`文件系统的访问。以下说明安装cli-extra软件包集；若希望直接在设备屏幕工作，也可选启用X11的软件包集，详见项目页面。

在root Shell中下载并执行安装器。`/usr/local`是唯一未设置noexec的可写文件系统，二进制文件必须放在那里才能运行：

```text
cros# mkdir -p /usr/local/bin
cros# curl -L https://github.com/dnschneid/crouton/raw/master/installer/crouton \
              > /usr/local/bin/crouton
cros# chmod 755 /usr/local/bin/crouton
cros# crouton -r focal -t cli-extra
```

启动Crouton chroot环境：

```text
cros# startcli
```

现在命令在Ubuntu环境内执行。为Crouton启用入站SSH，但使用22以外的端口，因为22已由ChromeOS原生SSH服务器占用。原作者使用222，便于记忆，且未在`/etc/services`中注册：

```text
crouton# apt install iptables openssh-server
crouton# echo "Port 222" >> /etc/ssh/sshd_config
crouton# mkdir /run/sshd
crouton# iptables -I INPUT -p tcp --dport 222 -j ACCEPT
crouton# /usr/sbin/sshd
```

与上文类似，此处使用主机名`crouton`表示独立的Linux运行环境。

每次重启chroot都需执行mkdir、iptables及sshd命令。为方便起见，可将它们放入`/etc/rc.local`。Crouton不运行systemd，因为它并不控制整个系统，所以openssh-server等Ubuntu服务无法自行启动。

<a id="building-and-installing-a-custom-kernel"></a>

## 构建并安装定制内核（Custom Kernel）

在构建主机上获取ChromeOS内核源码树。原作者所用出厂设备运行5.4内核，5.10源码树也可用，并持续回移上游驱动，因此主要硬件驱动较新，约落后主线5至6周。示例为方便起见，将源码放在主目录：

```text
dev$ cd $HOME
dev$ git clone https://chromium.googlesource.com/chromiumos/third_party/kernel
dev$ cd kernel
dev$ git switch chromeos-5.10
```

此处又切换到另一个Shell，使用主机名`dev`表示构建内核及Zephyr应用的开发计算机。也可直接在Chromebook上构建，但原文不建议这样做，因为系统恢复需要擦除磁盘。

若已有Linux源码树，将ChromeOS仓库添加为远端并只获取差异会快得多，因为ChromeOS紧密跟随上游。

接着需要`.config`文件。Chromebook内核已构建configs模块，可在运行中的内核暴露配置，只需加载模块并读取文件。

```text
dev$ cd /path/to/kernel
dev$ ssh root@cros modprobe configs
dev$ ssh root@cros zcat /proc/config.gz > .config
```

以下配置需与ChromeOS默认值不同，可直接编辑`.config`或使用menuconfig等工具：


- `CONFIG_HUGETLBFS=y`：Zephyr加载工具需要此功能。
- `CONFIG_EXTRA_FIRMWARE_DIR=n`：原配置引用了

  Google构建环境中的构建目录，本地并不存在该目录。
- `CONFIG_SECURITY_LOADPIN=n`：该选项将模块固定为

  只能从一个文件系统加载，这会限制定制内核的使用。
- `CONFIG_MODVERSIONS=n`：允许从经过修改、具有未提交更改的“dirty”源码树

  构建并安装模块。

像构建其他内核一样构建：

```text
dev$ make olddefconfig     # Or otherwise update .config
dev$ make bzImage modules  # Probably want -j<whatever> for parallel build
```

模块可直接复制到设备上现在可写的根文件系统。该文件系统原本设计为只读，空间非常有限，因此必须设置`INSTALL_MOD_STRIP=1`；可能还需要定期清理旧内核模块以释放空间：

```text
dev$ make INSTALL_MOD_PATH=mods INSTALL_MOD_STRIP=1 modules_install
dev$ (cd mods/lib/modules; tar cf - .) | ssh root@cros '(cd /lib/modules; tar xfv -)'
```

<a id="pack-and-install-chromeos-kernel-image"></a>

### 封装并安装ChromeOS内核镜像（Pack and Install）

内核bzImage文件需要签名并封装为ChromeOS vboot包，然后直接写入内核分区。所需工具已在Debian／Ubuntu软件仓库提供：

```text
$ sudo apt install vboot-utils vboot-kernel-utils
```

找出设备当前使用的内核分区。可将引导加载程序传入的`kernel_guid`命令行参数与启动磁盘分区表对照，例如：

```text
dev$ KPART=`ssh root@cros 'fdisk -l -o UUID,Device /dev/nvme0n1 | \
                           grep -i $(sed "s/.*kern_guid=//" /proc/cmdline \
                                     | sed "s/ .*//") \
                           | sed "s/.* //"'`
dev$ echo $KPART
/dev/nvme0n1p4
```

从该镜像提取命令行，保存到本地文件：

```text
dev$ ssh root@cros vbutil_kernel --verify /dev/$KPART | tail -1 > cmdline.txt
```

随后可用vboot工具封装新内核镜像。大多数参数是固定不变的样板配置。命令提供密钥，是因为启动流程仍要求有效签名，尽管当前配置不会使用它。作为bootloader传入的占位文件实际不能是空文件，这是早期需要EFI存根（EFI Stub）的ROM版本留下的要求。

```text
dev$ echo dummy > dummy.efi
dev$ vbutil_kernel --pack kernel.img --config cmdline.txt \
       --vmlinuz arch/x86_64/boot/bzImage \
       --keyblock /usr/share/vboot/devkeys/kernel.keyblock \
       --signprivate /usr/share/vboot/devkeys/kernel_data_key.vbprivk \
       --version 1 --bootloader dummy.efi --arch x86_64
```

如有需要，可用`vbutil_kernel –verify`验证镜像。

接着将文件复制到设备，并写入其分区：

```text
$ scp kernel.img root@cros:/tmp
$ ssh root@cros dd if=/tmp/kernel.img of=/dev/nvme0n1p4
```

重启后，如果一切正常，设备就会运行新内核。

<a id="wifi-firmware-fixup"></a>

### 修复Wi-Fi固件（Firmware Fixup）

在原文的Tiger Lake Chromebook环境中，相对于5.10内核，`/lib/firmware`内容较旧。iwlwifi驱动请求的固件文件不存在，导致设备无法联网。问题虽然简单，若不修复却会使后续操作无法联网。原作者认为，将旧版本链接到新文件名即可解决；更合适的方法可能是从近期kernel.org检出的`/lib/firmware`复制正确版本：

```text
cros# cd /lib/firmware
cros# ln -s iwlwifi-QuZ-a0-hr-b0-62.ucode iwlwifi-QuZ-a0-hr-b0-64.ucode
```

<a id="build-and-run-a-zephyr-application"></a>

## 构建并运行Zephyr应用（Build and Run）

新内核启动后，终于可以运行Zephyr代码。

<a id="build-rimage-signing-tool"></a>

### 构建rimage签名工具（Signing Tool）

首先下载并构建Sound Open Firmware的rimage工具。为清晰起见，以下说明放在主目录，实际可使用其他位置：

```text
dev$ cd $HOME
dev$ git clone https://github.com/thesofproject/rimage
dev$ git submodule init
dev$ git submodule update
dev$ cd tools/rimage/
dev$ cmake .
dev$ make
```

<a id="copy-integration-scripting-to-chromebook"></a>

### 将集成脚本复制到Chromebook（Integration Scripting）

设备需要Python脚本，并在前面安装的Crouton环境中运行。复制如下：

```text
dev$ scp soc/intel/intel_adsp/tools/cavstool.py user@crouton:
```

然后在Crouton环境中启动服务：

```text
crouton$ sudo ./cavstool.py user@crouton:
```

<a id="build-and-sign-zephyr-app"></a>

### 构建并签名Zephyr应用（Build and Sign）

此平台的Zephyr应用按通常方式构建，原文通过给`west flash`增加少量参数完成签名。Tiger Lake DSP使用SOF的3k密钥，不同于较旧硬件使用的原始密钥。输出产物为`zephyr.ri`，需复制到设备。

```text
dev$ west build -b intel_adsp/cavs25 samples/hello_world
dev$ west sign --tool-data=~/rimage/config -t ~/rimage/rimage -- \
            -k $ZEPHYR_BASE/boards/intel/adsp/support/otc_private_key_3k.pem
```

<a id="run-it"></a>

### 运行应用（Run It）

加载脚本以已签名的rimage文件为参数。脚本报告成功后，应用立即运行，其控制台输出位于SOF共享内存跟踪缓冲区（Shared Memory Trace Buffer），可通过日志脚本读取。

```text
dev$ west flash --remote-host crouton
Hello World! intel_adsp
```

<a id="misc-references"></a>

## 其他参考资料（Misc References）

这些说明依据以下上游文档编写：

此页是很好的启动流程参考：

[https://www.chromium.org/chromium-os/developer-library/reference/device/disk-format](https://www.chromium.org/chromium-os/developer-library/reference/device/disk-format)

此页也很有帮助，重点讨论启动ChromeOS之外的系统：

[https://www.chromium.org/chromium-os/developer-library/reference/development/developer-information-for-chrome-os-devices/custom-firmware/](https://www.chromium.org/chromium-os/developer-library/reference/development/developer-information-for-chrome-os-devices/custom-firmware/)

## 译注

本页是原作者针对特定Chromebook及ChromeOS版本的操作记录，内核版本、固件变通方法和工具兼容性按来源保留。开发者模式、恢复和内核分区写入涉及数据擦除；本文仅翻译，未在本仓库环境执行。本页以west flash签名的旧流程，与ADSP通用页注明的Zephyr 3.6.0起west flash不再签名有版本差异。cros、crouton和dev是原文用于区分命令执行环境的主机名。

---

[上一章](P001_Alder_Lake_N.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P003_Intel_ADSP.md)
