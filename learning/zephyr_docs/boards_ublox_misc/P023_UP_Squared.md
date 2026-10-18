---
id: learning.zephyr-docs.boards-ublox-misc.page-23
title: UP Squared
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/up-bridge-the-gap/up_squared/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="up_squared"></a>

# 第23章\_UP Squared

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/up-bridge-the-gap/up_squared/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id2"></a>

[![官方原图：../../../../_images/up_squared.jpg](images/up_squared.jpg)](images/up_squared.jpg)

UP Squared

名称（Name）：

`up_squared`

厂商（Vendor）：

[UP Bridge the Gap](https://docs.zephyrproject.org/latest/boards/index.html#vendor=up-bridge-the-gap)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[x86](https://docs.zephyrproject.org/latest/boards/index.html#arch=x86)

片上系统（SoC）：

[apollo_lake](https://docs.zephyrproject.org/latest/boards/index.html#soc=apollo_lake)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/up-bridge-the-gap/up_squared/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

UP²（UP Squared）是一款高性能、低功耗的超紧凑单板计算机，采用Intel Apollo Lake Celeron及Pentium处理器，场景设计功耗（Scenario Design Power）仅4 W，并搭载灵活的Intel Altera MAX 10 FPGA。原文称处理器为最新型号，这是原页面的历史描述。

此板级配置为[UP Squared](https://www.up-board.org/upsquared/specifications)启用内核支持。

注意（Note）

该配置适用于分别采用Intel Pentium、Celeron或Atom SoC的三种[UP Squared](https://www.up-board.org/upsquared/specifications)变体。

<a id="hardware"></a>

## 硬件（Hardware）

开发板的一般信息见[UP Squared](https://www.up-board.org/upsquared/specifications)网站。

<a id="supported-features"></a>

### 支持的功能（Supported Features）

除高精度事件定时器（HPET）、本地及I/O高级可编程中断控制器（APIC）等标准架构设备外，Zephyr还支持以下Apollo Lake专用SoC设备：


- 高速UART（HSUART）
- 通用输入输出（GPIO）
- 集成电路间总线（I2C）

<a id="hsuart-high-speed-serial-port-support"></a>

#### 高速串口（HSUART）支持

Apollo Lake UART兼容NS16550，并提供高速能力。

额外配置后，UART支持高于115.2 kbit/s、最高3.6864 Mbit/s的波特率。输入主时钟经过PLL生成波特率主时钟。每个UART使用32位PRV_CLOCK_PARAMS寄存器，亦称PCP，控制PLL，格式如下：

<table>
<tr>
<th>注31</th>
<th>[30:16]</th>
<th>[15:1]</th>
<th>注0</th>
</tr>
<tr>
<td>使能（Enable）</td>
<td><code>m</code></td>
<td><code>n</code></td>
<td>翻转（Toggle）</td>
</tr>
</table>

生成的波特率主时钟频率为(n/m) * master。

通常主时钟为100 MHz，固件默认将PCP设为0x3d090240，即n = 288、m = 15625，得到常用的1.8432 MHz波特率主时钟，最高波特率115.2 kbit/s。要提高波特率，需修改PCP并向Zephyr提供新的主时钟频率。

通过设备树设置目标UART块中的PRV_CLOCK_PARAMS。通常在应用目录放置板级设备树覆盖文件，例如up_squared.overlay，内容如下：

> ```text
> / {
>     soc {
>         uart@0 {
>             pcp = <0x3d090900>;
>             clock-frequency = <7372800>;
>             current-speed = <230400>;
>         };
>     };
> };
> ```

相关变量为pcp，即PRV_CLOCK_PARAMS寄存器值，以及clock-frequency，即生成的波特率主时钟。current-speed含义不变，仍指定初始波特率。

<a id="gpio"></a>

#### 通用输入输出（GPIO）

GPIO通过HAT排针引出，可用UP2_HAT_PIN3等预定义宏引用。物理引脚连接到作为电平转换器的板载FPGA，因此必须先在BIOS中设置功能及输入／输出方向。进入Advanced菜单的HAT Configurations，选择对应引脚为GPIO后，再按用途设置方向，GPIO才能正确工作。

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

连接图见[UP Squared](https://www.up-board.org/upsquared/specifications)网站及[UP Squared引脚图](https://wiki.up-community.org/Pinout)网站。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`up_squared`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

按以下步骤在UP Squared上启动镜像。

<a id="contents"></a>


- <a id="id3"></a>

  [构建Zephyr应用（Build Zephyr Application）](#build-zephyr-application)
- <a id="id4"></a>

  [通过统一可扩展固件接口（UEFI）启动UP Squared](#booting-the-up-squared-board-using-uefi)
- <a id="id5"></a>

  [通过网络启动UP Squared](#booting-the-up-squared-board-over-network)

<a id="build-zephyr-application"></a>

### [构建Zephyr应用（Build Zephyr Application）](#contents)


1. 构建Zephyr应用，例如为UP Squared构建hello_world：

  ```text
  # From the root of the zephyr repository
  west build -b up_squared samples/hello_world
  ```

  注意（Note）

  应用构建完成后，构建目录中会自动生成名为`zephyr.efi`的Zephyr EFI镜像文件。

<a id="booting-the-up-squared-board-using-uefi"></a>

### [通过统一可扩展固件接口（UEFI）启动UP Squared](#contents)

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

注意（Note）

串口控制台连接方法见UP Squared Serial Console Wiki页面。（[UP Squared串口控制台Wiki页面](https://wiki.up-community.org/Serial_console)）

注意（Note）

若出现以下消息，原文说明可安全忽略：

```text
WARNING: no console will be available to OS
```

<a id="booting-the-up-squared-board-over-network"></a>

### [通过网络启动UP Squared](#contents)

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

注意（Note）

串口控制台连接方法见UP Squared Serial Console Wiki页面。（[UP Squared串口控制台Wiki页面](https://wiki.up-community.org/Serial_console)）

注意（Note）

为UP Squared启用预启动执行环境（PXE）网络启动的步骤如下：


1. 在BIOS设置中启用网络。

  ```text
  Advanced -> Network Stack Configuration -> Enable Network Stack -> Enable Ipv4 PXE Support
  ```
2. 将网络启动设为第一启动选项。

  ```text
  Boot -> Boot Option #1 : [Network]
  ```

## 译注

UP Squared的高速UART需同时设置PCP及clock-frequency；GPIO经过FPGA电平转换，还须在BIOS设定功能与方向。

---

[上一章](P022_UP_Bridge_the_Gap..md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P024_UP_Squared_Pro_7000.md)
