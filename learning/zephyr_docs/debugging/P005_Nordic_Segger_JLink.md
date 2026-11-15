---
id: learning.zephyr-docs.debugging.page-5
title: Nordic_Segger_JLink
kind: reference
status: maintained
domains: [zephyr, debugging, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/flash_debug/nordic_segger.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="nordic-nrf5x-segger-j-link"></a>
<a id="nordic-segger"></a>

# 第5章\_Nordic\_Segger\_JLink

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/flash_debug/nordic_segger.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 5.1\_概览（Overview）

原文说明，Nordic nRF5x开发套件（Development Kit，DK）、预览开发套件（Preview Development Kit，PDK）和Dongle配有Atmel ATSAM3U2C调试芯片（Debug IC），提供以下功能：

- SEGGER J-Link固件与桌面工具。
- 面向nRF5x芯片的串行线调试（Serial Wire Debug，SWD）。
- 用于拖放固件烧录的大容量存储设备（Mass Storage Device，MSD）。
- 桥接到nRF5x通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）的USB CDC ACM串口；CDC ACM表示通信设备类的抽象控制模型（Communications Device Class, Abstract Control Model）。
- SEGGER RTT控制台（Console）。
- SEGGER Ozone调试器（Debugger）。

> 译注——板型边界：上述概括沿用原文，不能推断所有nRF5x Dongle均带J-Link。官方[nRF52840 Dongle调试说明](https://docs.zephyrproject.org/latest/boards/nordic/nrf52840dongle/doc/index.html#debugging)明确该板没有板载J-Link调试芯片，需要连接外部调试器。本页仅翻译Zephyr官方的Nordic工具说明，不把Nordic板的硬件能力移用于其他芯片或本仓库目标。

<a id="segger-j-link-software-installation"></a>

## 5.2\_安装J-Link软件（Segger J-Link Software Installation）

安装J-Link软件及文档包（Software and Documentation Pack）：


<a id="id20"></a>

1. 从[J-Link软件及文档包下载页](https://www.segger.com/jlink-software.html)下载适合主机系统的软件包。

2. 按平台安装软件包或执行安装器。

3. 连接支持J-Link的nRF5x DK、PDK或Dongle后，应看到一个对应USB大容量存储设备的驱动器，以及一个串口。

<a id="nrf5x-command-line-tools-installation"></a>

## 5.3\_安装nRF5x命令行工具（nRF5x Command-Line Tools Installation）

<a id="id4"></a>

nRF5x命令行工具（Command-Line Tools）用于从命令行控制设备，包括复位、擦除或写入闪存（Flash）。前往[下载页](https://www.nordicsemi.com/Software-and-Tools/Development-Tools/nRF-Command-Line-Tools)并选择主机操作系统。

安装后确认 `nrfjprog` 位于可执行程序搜索路径（PATH）中，才能从任意目录调用。

<a id="flashing"></a>
<a id="nordic-segger-flashing"></a>

> 译注——工具维护状态：2026-10-14复核[Nordic原下载入口](https://www.nordicsemi.com/Software-and-Tools/Development-Tools/nRF-Command-Line-Tools)时，厂商已说明nRF Command Line Tools归档并由nRF Util替代，nrfjprog已弃用。以下仍完整保留Zephyr原页流程，供既有环境对照；新环境应同时核对目标板当前工具说明，不能把这份旧命令流程当作厂商最新推荐。

## 5.4\_烧录（Flashing）

先完成J-Link软件和nRF5x命令行工具安装，并取得已经编译的Zephyr镜像。原流程如下。

1. 用micro-USB线连接nRF5x板和计算机。
2. 擦除nRF5x芯片闪存：

```bash
nrfjprog --eraseall -f nrf5<x>
```

`<x>` 为1时表示nRF51系列，为2时表示nRF52系列。

3. 从所选示例目录烧录Zephyr镜像：

```bash
nrfjprog --program outdir/<board>/zephyr.hex -f nrf5<x>
```

`<board>` 是构建时 `BOARD` 指定的板名，例如 `nrf52dk/nrf52832`；`<x>` 仍按nRF51／nRF52选择1／2。


4. 复位并启动Zephyr：

```bash
nrfjprog --reset -f nrf5<x>
```

`<x>` 的含义相同。

> 译注——执行前提与路径：以上是原文的工具流程，不是可无条件粘贴的模板；尖括号占位符须先替换。eraseall会擦除目标内容。outdir/&lt;board&gt;/zephyr.hex属于原文构建布局，应先确认本次构建实际产生的镜像位置，再传给nrfjprog；不能因为本页写了这个目录就认为文件已存在。目录和工具未确认时应返回构建及安装步骤。本批没有连接设备或执行擦除、烧录、复位。

<a id="usb-cdc-acm-serial-port-setup"></a>

## 5.5\_USB\_CDC\_ACM串口设置（USB CDC ACM Serial Port Setup）

**重要：**原文记录的nRF5x板J-Link固件问题可能在某些计算机上引起USB CDC ACM串口数据丢失或损坏。规避方式是按[下节](#nordic-segger-msd)禁用板上的大容量存储设备功能。

<a id="windows"></a>

### 5.5.1\_Windows（Windows）

串口显示为 `COMxx`，可在设备管理器（Device Manager）的“端口（COM和LPT）”中查看。

<a id="gnu-linux"></a>

### 5.5.2\_GNU\_Linux（GNU/Linux）

串口显示为 `/dev/ttyACMx`，默认不向所有用户开放。以下命令把当前用户加入dialout组以获取串口访问权限，重新登录后才生效：

```bash
sudo usermod -a -G dialout `whoami`
```

<a id="id16"></a>

原文指出，较新版本的ModemManager会向类似TTY的设备发送AT命令，参见[相关问题记录](https://bugs.freedesktop.org/show_bug.cgi?id=85007)。Nordic开发套件也在其中，这可能占用串口数秒，并使读取UART数据的应用行为异常。原文将下面的操作描述为运行应用前“临时禁用ModemManager”：

```bash
systemctl stop ModemManager.service
systemctl disable ModemManager.service
```

> 译注——服务状态：按[systemctl官方手册源码](https://raw.githubusercontent.com/systemd/systemd/main/man/systemctl.xml)，stop停止当前运行的服务，disable移除启用链接、影响后续启动配置，且本身不等于停止服务。因此原文两条命令的效果不能统称为临时停止。是否恢复启动及启用配置应以机器原状态为准；本批未改变任何服务。

<a id="id18"></a>

另一种方式是[修改udev规则](http://www.at91.com/linux4sam/bin/view/Linux4SAM/SoftwareTools#Device_or_resource_busy_dev_ttyA)将SEGGER设备加入忽略列表，让ModemManager不处理它们：

```bash
sudo sh -c 'echo "ATTRS{idVendor}==\"1366\", ENV{ID_MM_DEVICE_IGNORE}=\"1\" " \
  >> /etc/udev/rules.d/99-segger-modemmanager-blocklist.rules'
sudo service udev restart
```

> 译注——文件修改：这段Bash命令向系统udev规则文件追加内容并重启udev服务，不是仓库文件操作。重复执行会继续追加同一行。应按实际发行版的规则管理方式核对；此处完整保留原命令，没有在主机执行。

原文预期ModemManager 1.8及新版SEGGER接口微控制器（Interface MCU，IMCU）固件修复该问题。

> 译注——时间边界：上句属于该页面保留的历史预期，不表示本次验证了现有主机或探针固件仍有同样问题。

<a id="apple-macos-os-x"></a>

### 5.5.3\_Apple\_macOS（Apple macOS (OS X)）

串口显示为 `/dev/tty.usbmodemXXXX`。

<a id="disabling-the-mass-storage-device-functionality"></a>
<a id="nordic-segger-msd"></a>

## 5.6\_禁用大容量存储功能（Disabling the Mass Storage Device functionality）

原文记录，受J-Link固件已知问题及主机系统／版本影响，USB CDC ACM串口使用大于64字节的数据包时可能发生损坏或丢包；GNU/Linux和macOS均有此现象。

规避方法：GNU/Linux或macOS在终端打开 `JLinkExe`，Windows打开“JLink Commander”。在工具交互界面输入：

```text
MSDDisable
```

<a id="id6"></a>

然后拔下并重新连接开发板。大容量存储设备应不再出现，虚拟串口应可发送长数据包。更多信息见[SEGGER SAM3U说明](https://wiki.segger.com/J-Link-OB_SAM3U)。

> 译注——输入位置：MSDDisable是J-Link交互命令，不是在系统Shell中直接执行的程序名。预期现象是关闭拖放存储功能；不等于禁用目标UART或卸载整套J-Link工具。

<a id="rtt-console"></a>

## 5.7\_RTT控制台（RTT Console）

<a id="id8"></a>

J-Link支持[实时跟踪RTT（原文Real-Time Tracing）](https://www.segger.com/jlink-rtt.html)，可在目标nRF5x板与开发主机之间建立双向终端连接，用于日志输出和输入。Zephyr支持nRF5x的RTT；UART经USB CDC ACM用于其他目的时，例如hci_uart应用的主机控制器接口（Host Controller Interface，HCI）流量，RTT尤其有用。

在应用 `.conf` 配置文件中加入：

```kconfig
CONFIG_USE_SEGGER_RTT=y
CONFIG_RTT_CONSOLE=y
```

**警告：**`HAS_SEGGER_RTT` 表示平台支持SEGGER J-Link RTT，由SoC的Kconfig文件自动设置，不要与 `USE_SEGGER_RTT` 混淆；后者依赖前者。

若没有RTT输出，可能要禁用具体示例或应用默认启用、与RTT冲突的其他控制台。例如在 `.conf` 文件中关闭UART控制台：

```kconfig
CONFIG_UART_CONSOLE=n
```

启用RTT后重新编译并烧录，再用以下方式查看消息。

<a id="id1"></a>

### 5.7.1\_Windows（Windows）

打开“J-Link RTT Viewer”，选择：

| 选项 | 设置 |
| --- | --- |
| 连接（Connection） | USB |
| 目标器件（Target Device） | 从列表选择实际芯片 |
| 目标接口与速度（Target Interface and Speed） | SWD，4000 KHz |
| RTT控制块（RTT Control Block） | 自动检测（Auto Detection） |

<a id="gnu-linux-and-macos-os-x"></a>

### 5.7.2\_GNU\_Linux与macOS（GNU/Linux and macOS (OS X)）

从终端打开 `JLinkRTTLogger`，选择：

| 选项 | 设置 |
| --- | --- |
| 器件名（Device Name） | 实际芯片的完整器件名 |
| 目标接口（Target Interface） | SWD |
| 接口速度（Interface Speed） | 4000 KHz |
| RTT控制块地址（RTT Control Block address） | 自动检测（auto-detection） |
| RTT通道名或索引（RTT Channel name or index） | 0 |
| 输出文件（Output file） | 文件名；或 `/dev/stdout`，直接显示在终端 |

<a id="python-viewer"></a>

### 5.7.3\_Python查看器（Python viewer）

<a id="id10"></a>

[pyrtt-viewer](https://github.com/thomasstenersen/pyrtt-viewer)仓库提供Python RTT查看器工具。

<a id="segger-ozone"></a>

## 5.8\_SEGGER\_Ozone（Segger Ozone）

<a id="id12"></a>

<a id="id14"></a>

J-Link兼容可视化调试器[Segger Ozone](https://www.segger.com/ozone.html)，可从[Ozone下载页](https://www.segger.com/downloads/jlink#Ozone)取得。安装后配置：

| 选项 | 设置 |
| --- | --- |
| 目标器件（Target Device） | 从列表选择实际芯片 |
| 目标接口（Target Interface） | SWD |
| 目标接口速度（Target Interface Speed） | 4 MHz |
| 主机接口（Host Interface） | USB |

配置完成后，通过“文件→打开”（File→Open）选择构建目录中的 `zephyr.elf`。

> 译注——配置与验证：本页4 MHz／4000 KHz是原文参数，不保证适用于所有板与连接。应用配置、构建、烧录、调试器连接和看到输出是不同阶段；没有输出时先确认目标和构建配置，再核对RTT通道及冲突控制台。本批没有执行这些硬件步骤。

<a id="references"></a>

## 5.9\_参考资料（References）

<a id="id3"></a>

1. [nRF命令行工具](https://www.nordicsemi.com/Software-and-Tools/Development-Tools/nRF-Command-Line-Tools)。
<a id="id5"></a>

2. [J-Link-OB SAM3U](https://wiki.segger.com/J-Link-OB_SAM3U)。
<a id="id7"></a>

3. [SEGGER RTT](https://www.segger.com/jlink-rtt.html)。
<a id="id9"></a>

4. [Python RTT查看器](https://github.com/thomasstenersen/pyrtt-viewer)。

<a id="id11"></a>

5. [Ozone调试器](https://www.segger.com/ozone.html)。

<a id="id13"></a>

6. [Ozone下载入口](https://www.segger.com/downloads/jlink#Ozone)。

<a id="id15"></a>

7. [ModemManager相关问题](https://bugs.freedesktop.org/show_bug.cgi?id=85007)。

<a id="id17"></a>

8. [原文udev规则说明](http://www.at91.com/linux4sam/bin/view/Linux4SAM/SoftwareTools#Device_or_resource_busy_dev_ttyA)。

<a id="id19"></a>

9. [J-Link软件包](https://www.segger.com/jlink-software.html)。


对应官方文档源码：[doc/develop/flash_debug/nordic_segger.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/flash_debug/nordic_segger.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/develop/flash_debug/nordic_segger.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：烧录与调试主机工具](P004_烧录与调试主机工具.md) · [本模块主线目录](../reading/debugging.md) · [全部主线](../reading/README.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P004_烧录与调试主机工具.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
