---
id: learning.zephyr-docs.boards-ublox-misc.page-24
title: UP Squared Pro 7000
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/up-bridge-the-gap/up_squared_pro_7000/doc/up_squared_pro_7000.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="up_squared_pro_7000"></a>

# 第24章\_UP Squared Pro 7000

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/up-bridge-the-gap/up_squared_pro_7000/doc/up_squared_pro_7000.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`up_squared_pro_7000`

厂商（Vendor）：

[UP Bridge the Gap](https://docs.zephyrproject.org/latest/boards/index.html#vendor=up-bridge-the-gap)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[x86](https://docs.zephyrproject.org/latest/boards/index.html#arch=x86)

片上系统（SoC）：

[alder_lake](https://docs.zephyrproject.org/latest/boards/index.html#soc=alder_lake)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/up-bridge-the-gap/up_squared_pro_7000/doc/up_squared_pro_7000.rst/../..)<a id="overview"></a>

## 概述（Overview）

UP Squared Pro 7000是UP Boards系列第三代掌上开发板，采用Intel Alder Lake N，即Intel N系列平台。

Intel N系列平台更多信息见[Alder Lake N](../boards_intel_ite/P001_Alder_Lake_N.md#intel-adl-n)。

此板级配置为UP Squared Pro 7000启用内核支持。

<a id="hardware"></a>

## 硬件（Hardware）

<a id="id2"></a>

开发板的一般信息见[UP Squared Pro 7000](https://up-board.org/up-squared-pro-7000/)网站[注1](#id1)。

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

<a id="id3"></a>

更多信息见[UP Squared Pro 7000](https://up-board.org/up-squared-pro-7000/)网站[注1](#id1)。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`up_squared_pro_7000`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
</tr>
<tr>
<td>misc-flasher</td>
<td>✅（默认 / default）</td>
<td></td>
</tr>
</table>

按以下步骤在UP Squared Pro 7000上启动镜像。

<a id="contents"></a>


- <a id="id8"></a>

  [构建Zephyr应用（Build Zephyr Application）](#build-zephyr-application)
- <a id="id9"></a>

  [连接串口控制台（Serial Console）](#connect-serial-console)
- <a id="id10"></a>

  [通过UEFI启动UP Squared Pro 7000](#booting-the-up-squared-pro-7000-board-using-uefi)
- <a id="id11"></a>

  [通过网络启动UP Squared Pro 7000](#booting-the-up-squared-pro-7000-board-over-network)

<a id="build-zephyr-application"></a>

### [构建Zephyr应用（Build Zephyr Application）](#contents)


1. 构建Zephyr应用，例如为UP Squared Pro 7000构建hello_world：

  ```text
  # From the root of the zephyr repository
  west build -b up_squared_pro_7000 samples/hello_world
  ```

  注意（Note）

  应用构建完成后，构建目录中会自动生成名为`zephyr.efi`的Zephyr EFI镜像文件。

<a id="connect-serial-console"></a>

### [连接串口控制台（Serial Console）](#contents)

<a id="id5"></a>

当前配置假定串口控制台连接到CN14 USB 2.0／UART 1×10P Wafer连接器。位置及连接器说明见用户手册[注2](#id4)。（[用户手册（User Manual）](https://downloads.up-community.org/download/up-squared-pro-7000-user-manual/)）

<a id="id7"></a>

串口连接设置的更多信息见[UP Serial Console](https://github.com/up-board/up-community/wiki/Serial-Console)[注3](#id6)。

<a id="booting-the-up-squared-pro-7000-board-using-uefi"></a>

### [通过UEFI启动UP Squared Pro 7000](#contents)

<a id="preparing-the-boot-device"></a>

#### 准备启动设备（Preparing the Boot Device）

准备一个USB闪存盘，用于在开发板上启动Zephyr应用镜像。


1. 将USB闪存盘格式化为FAT32。

  在Windows中打开文件资源管理器，右键单击USB闪存盘并选择“格式化（Format...）”。确认“文件系统（File System）”选择FAT32，点击“格式化（Format）”按钮，等待完成。

  Linux下可使用gparted等图形工具，将USB闪存盘格式化为FAT32。也可在终端中找出对应设备节点，例如`/dev/sdd`，然后执行以下命令：

  ```text
  $ mkfs.vfat -F 32 <device-node>
  ```

  重要提示（Important）

  必须确认设备节点确实属于该USB闪存盘，否则可能擦除系统中的其他存储设备，导致系统无法使用。
2. 将Zephyr EFI镜像文件`zephyr/zephyr.efi`复制到USB闪存盘。

<a id="booting-zephyr-on-a-board"></a>

#### 在开发板上启动Zephyr（Booting Zephyr）

连接USB闪存盘，将开发板启动到EFI Shell。


1. 将准备好的启动设备，即USB闪存盘，插入开发板。
2. 通过串口线将开发板连接主机，并配置主机监听串口数据。更多信息见开发板网站。

  注意（Note）

  波特率使用115200。
3. 给开发板上电。
4. 出现以下输出时，按F7：

  ```text
  Press <DEL> or <ESC> to enter setup.
  ```
5. 在显示的菜单中选择对应EFI Shell的菜单项。
6. 在EFI Shell中选择要启动的Zephyr EFI镜像。

  ```text
  Shell> fs0:zephyr.efi
  ```
7. 启动过程结束后，Zephyr应用镜像即已启动。

<a id="booting-the-up-squared-pro-7000-board-over-network"></a>

### [通过网络启动UP Squared Pro 7000](#contents)

<a id="prepare-linux-host"></a>

#### 准备Linux主机（Prepare Linux Host）


1. 安装DHCP及TFTP服务器，例如dnsmasq。

  ```text
  $ sudo apt-get install dnsmasq
  ```
2. 配置DHCP服务器，dnsmasq配置如下：

  ```text
  # Only listen to this interface
  interface=eno2
  dhcp-range=10.1.1.20,10.1.1.30,12h
  ```
3. 配置TFTP服务器。

  ```text
  # tftp
  enable-tftp
  tftp-root=/srv/tftp
  dhcp-boot=zephyr.efi
  ```

  `zephyr.efi`是前面生成的Zephyr EFI二进制文件。
4. 将Zephyr EFI镜像`zephyr/zephyr.efi`复制到`/srv/tftp`目录。

  > ```text
  > $ cp zephyr/zephyr.efi /srv/tftp
  > ```
5. TFTP根目录应如下所示：

  ```text
  $ tree /srv/tftp
  /srv/tftp
  └── zephyr.efi
  ```
6. 重启dnsmasq服务：

  ```text
  $ sudo systemctl restart dnsmasq.service
  ```

<a id="prepare-the-board-for-network-boot"></a>

#### 为开发板准备网络启动（Network Boot）


1. 在BIOS设置中启用PXE网络启动。
2. 将网络启动设为第一启动选项。

<a id="booting-the-board"></a>

#### 启动开发板（Booting the Board）


1. 通过串口线将开发板连接主机，并配置主机监听串口数据。更多信息见开发板网站。

  注意（Note）

  波特率使用115200。
2. 给开发板上电。
3. 确认开发板已获得IP地址。在Linux主机运行：

  ```text
  $ journalctl -f -u dnsmasq
  dnsmasq-dhcp[5386]: DHCPDISCOVER(eno2) 00:07:32:52:25:88
  dnsmasq-dhcp[5386]: DHCPOFFER(eno2) 10.1.1.28 00:07:32:52:25:88
  dnsmasq-dhcp[5386]: DHCPREQUEST(eno2) 10.1.1.28 00:07:32:52:25:88
  dnsmasq-dhcp[5386]: DHCPACK(eno2) 10.1.1.28 00:07:32:52:25:88
  ```
4. 确认网络启动已开始：

  ```text
  $ journalctl -f -u dnsmasq
  dnsmasq-tftp[5386]: sent /srv/tftp/zephyr.efi to 10.1.1.28
  ```
5. 启动过程结束后，Zephyr应用镜像即已启动。

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔1〕 ([1](#id2),[2](#id3)) [https://up-board.org/up-squared-pro-7000/](https://up-board.org/up-squared-pro-7000/)

<a id="id4"></a>

〔[2](#id5)〕 [https://downloads.up-community.org/download/up-squared-pro-7000-user-manual/](https://downloads.up-community.org/download/up-squared-pro-7000-user-manual/)

<a id="id6"></a>

〔[3](#id7)〕 [https://github.com/up-board/up-community/wiki/Serial-Console](https://github.com/up-board/up-community/wiki/Serial-Console)

## 译注

UP Squared Pro 7000的串口假定位于CN14 USB 2.0／UART 1×10P连接器；不能照搬旧UP Squared板的接线。

---

[上一章](P023_UP_Squared.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P025_DART-MX8M-PLUS.md)
