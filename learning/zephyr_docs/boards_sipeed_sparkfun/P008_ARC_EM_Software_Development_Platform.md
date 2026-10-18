---
id: learning.zephyr-docs.boards-sipeed-sparkfun.page-8
title: ARC EM Software Development Platform
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/snps/emsdp/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="emsdp"></a>

# 第8章\_ARC EM软件开发平台（Software Development Platform）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/snps/emsdp/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/emsdp.jpg](images/emsdp.jpg)](images/emsdp.jpg)

ARC EM软件开发平台（Software Development Platform）

名称（Name）：

`emsdp`

厂商（Vendor）：

[Synopsys, Inc.](https://docs.zephyrproject.org/latest/boards/index.html#vendor=snps)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arc](https://docs.zephyrproject.org/latest/boards/index.html#arch=arc)

片上系统（SoC）：

[emsdp_em4](https://docs.zephyrproject.org/latest/boards/index.html#soc=emsdp_em4)、[emsdp_em7d_esp](https://docs.zephyrproject.org/latest/boards/index.html#soc=emsdp_em7d_esp)、[emsdp_em6](https://docs.zephyrproject.org/latest/boards/index.html#soc=emsdp_em6)、[emsdp_em5d](https://docs.zephyrproject.org/latest/boards/index.html#soc=emsdp_em5d)、[emsdp_em9d](https://docs.zephyrproject.org/latest/boards/index.html#soc=emsdp_em9d)、[emsdp_em11d](https://docs.zephyrproject.org/latest/boards/index.html#soc=emsdp_em11d)、[emsdp_em7d](https://docs.zephyrproject.org/latest/boards/index.html#soc=emsdp_em7d)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/snps/emsdp/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

DesignWare ARC EM Software Development Platform（SDP）是基于ARC EM处理器子系统的软件快速开发平台，旨在加速物联网、传感器融合及语音等超低功耗嵌入式应用的开发与调试。

板卡详情见DesignWare ARC EM Software Development Platform（EM SDP）。（[DesignWare ARC EM软件开发平台（EM SDP）](https://www.synopsys.com/dw/ipdir.php?ds=arc-em-software-development-platform)）

<a id="hardware"></a>

## 硬件（Hardware）

EM SDP支持EM4、EM5D、EM6、EM7D、EM7D+ESP、EM9D及EM11D等核配置，需以emsdp/<core>形式提供板级变体。对应core分别为emsdp_em4、emsdp_em5D、emsdp_em6、emsdp_em7d、emsdp_em7d_esp、emsdp_em9d及emsdp_em11d；原文EM5D标识在此使用大写D。

下表列出不同核配置支持的硬件功能：

<table>
<tr>
<th>功能（Features）</th>
<th>EM4</th>
<th>EM6</th>
<th>EM5D</th>
<th>EM7D</th>
<th>EM7D_ESP</th>
<th>EM9D</th>
<th>EM11D</th>
</tr>
<tr>
<td>缓存（Caches）</td>
<td>N</td>
<td>Y</td>
<td>N</td>
<td>Y</td>
<td>Y</td>
<td>N</td>
<td>Y</td>
</tr>
<tr>
<td>数字信号处理（DSP）</td>
<td>N</td>
<td>N</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>XY存储器（XY Memory）</td>
<td>N</td>
<td>N</td>
<td>N</td>
<td>N</td>
<td>N</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>安全功能（Secure）</td>
<td>N</td>
<td>N</td>
<td>N</td>
<td>N</td>
<td>Y</td>
<td>N</td>
<td>N</td>
</tr>
</table>

下表列出Zephyr目前提供的驱动：

<table>
<tr>
<th>接口（Interface）</th>
<th>控制器（Controller）</th>
<th>EMSDP</th>
<th>驱动／组件（Driver/Component）</th>
</tr>
<tr>
<td>SD输入输出接口（SDIO）</td>
<td>片上（On-Chip）</td>
<td>N</td>
<td>SD卡控制器</td>
</tr>
<tr>
<td>通用异步收发器（UART）</td>
<td>Arduino及三个Pmod</td>
<td>Y</td>
<td>串口轮询及串口中断</td>
</tr>
<tr>
<td>串行外设接口（SPI）</td>
<td>Arduino、Pmod及ADC</td>
<td>Y</td>
<td>串行外设接口（spi）</td>
</tr>
<tr>
<td>模数转换器（ADC）</td>
<td>一个Pmod</td>
<td>N</td>
<td>通过SPI访问的ADC</td>
</tr>
<tr>
<td>集成电路间总线（I2C）</td>
<td>Arduino及Pmod</td>
<td>N</td>
<td>集成电路间总线（i2c）</td>
</tr>
<tr>
<td>通用输入输出（GPIO）</td>
<td>Arduino、Pmod及引脚</td>
<td>Y</td>
<td>通用输入输出（gpio）</td>
</tr>
<tr>
<td>脉宽调制（PWM）</td>
<td>Arduino及Pmod</td>
<td>N</td>
<td>pwm</td>
</tr>
<tr>
<td>集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>N</td>
<td>音频接口（Audio Interface）</td>
</tr>
</table>

支持两个32 MB四线SPI（QSPI）闪存，其中一个仅保存FPGA镜像，另一个是通过SPI总线连接的用户闪存，对应示例位于samples/drivers/spi_flash。

ARC EM SDP提供单个USB 2.0主机端口；原文如此称呼此端口，同时说明它用于访问FPGA配置存储器及调试／UART。

通过USB连接电脑时，EM SDP表现为大容量存储设备，可拖放FPGA比特流到配置存储器。上电复位或按配置按键时，镜像自动加载到FPGA。

硬件功能详情见[ARC EM Software Development Platform](https://embarc.org/project/arc-em-software-development-platform-sdp/)。

<a id="peripheral-driver-test-and-sample"></a>

### 外设驱动测试及示例（Peripheral Driver Test and Sample）

tests/drivers/spi/spi_loopback验证DesignWare SPI驱动，无需外接MISO与MOSI，因为DW SPI寄存器配置为内部回环。测试以两种速度及异步功能验证传输；DW SPI仅在SPI0及SPI1提供。

samples/drivers/spi_flash验证SPI1上的DW SPI及SPI闪存：先擦除整个闪存，再写入4字节数据，读回并与缓冲区比较以检查功能。

<a id="pinmux-interface"></a>

### 引脚复用接口（Pinmux Interface）

支持以下外设模块引脚复用标准：


- 三个Digilent Pmod

EM SDP具有Pmod_A、Pmod_B及Pmod_C三个12引脚连接器，可编程为GPIO、UART、SPI、I2C及PWM。支持两类UART Pmod接口，其中UARTA为较新版。软件通过PMOD_MUX_CTRL寄存器控制复用。


- 一个Arduino接口

<a id="id3"></a>

EM SDP提供Arduino扩展板（Shield）接口，通过ARDUINO_MUX_CTRL寄存器控制复用。部分I/O必须成组编程，无法单独设置，详情见平台用户指南[注1](#id2)表9。（[EM软件开发平台用户指南](https://www.synopsys.com/dw/ipdir.php?ds=arc-em-software-development-platform)）


- 一个MikroBUS接口

MikroBUS与Arduino共享控制器，因此只有ARDUINO_MUX_CTRL处于默认GPIO模式时，MikroBUS功能才可用。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`emsdp`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
<th>连接调试会话（attach）</th>
<th>实时传输（rtt）</th>
<th>调试服务器（debugserver）</th>
</tr>
<tr>
<td>mdb-hw</td>
<td>✅</td>
<td>✅</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-openocd">openocd</a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

<a id="required-hardware-and-software"></a>

### 所需硬件及软件（Required Hardware and Software）

在EM SDP上运行Zephyr RTOS应用还需要以下硬件及软件。


- 连接电脑的Micro-USB线
- 套件随附通用开关电源适配器，将110—240 V交流转换为12 V直流，为开发板供电；原文此处将输出写作12 DC。
- [Zephyr软件开发套件（SDK）](../toolchains/P002_ZephyrSDK.md#toolchain-zephyr-sdk)
- <a id="id7"></a>

  用于USB转UART的终端仿真软件，原文建议[PuTTY网站](https://www.putty.software)[注3](#id6)所提供的软件。
- <a id="id5"></a>

  可选Pmod、Arduino或Mikro模块，见[Digilent Pmod Modules](http://store.digilentinc.com/pmod-modules) [注2](#id4)，也可自行开发连接Pmod的接口。

<a id="set-up-the-em-software-development-platform"></a>

### 设置EM软件开发平台

在EM软件开发平台运行Zephyr前，需要正确设置开发板。


- 将12 V直流电源连接开发板。
- 通过Digilent USB线将主机连接开发板。

<a id="set-up-zephyr-software"></a>

### 设置Zephyr软件

<a id="building-sample-applications"></a>

### 构建示例应用（Building Sample Applications）

可尝试多种示例或测试，这里以[samples/hello_world](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/hello_world)中的[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)为例。

<a id="configuring"></a>

#### 配置（Configuring）

若示例没有prj_arc.conf，可能需自行编写。随后通过menuconfig配置目标；选择emsdp板级配置并指定处理器核，例如em7d：

```text
# From the root of the zephyr repository
west build -b emsdp/emsdp_em7d samples/hello_world
west build -t menuconfig
```

<a id="building"></a>

#### 构建（Building）

应用可按常规方式构建，详情见“构建应用”。下面以em4上的[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)为例。（[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)）

```text
# From the root of the zephyr repository
west build -b emsdp/emsdp_em4 samples/hello_world
```

<a id="connecting-serial-output"></a>

### 连接串口输出（Connecting Serial Output）

默认Zephyr EM SDP镜像通过板上USB转UART输出串口日志，启用方法如下：


- 打开串口终端，例如Linux中的minicom、PuTTY或screen。
- 指定tty设备名，例如Linux中的/dev/ttyUSB0。
- 通信参数设为：

<table>
<tr>
<th>参数（Parameter）</th>
<th>值（Value）</th>
</tr>
<tr>
<td>波特率（Baud）：</td>
<td>115200</td>
</tr>
<tr>
<td>数据位（Data）：</td>
<td>8位数据位</td>
</tr>
<tr>
<td>奇偶校验（Parity）：</td>
<td>无（None）</td>
</tr>
<tr>
<td>停止位（Stop Bits）：</td>
<td>1</td>
</tr>
</table>

<a id="debugging"></a>

### 调试（Debugging）

原文说明使用Zephyr SDK 0.9及更新版本可直接调试及加载IoT Development Kit；此句在EM SDP页也被复用，保留并提示其板名差异。

一种方式是通过常规Zephyr构建命令构建并调试，例如em6：

```text
west build -b emsdp/emsdp_em6 <my app>
west debug
```

随后可按常规调试，设置断点，再输入c继续执行。

另一种方式是启动调试服务器：

```text
west build -b emsdp/emsdp_em6 <my app>
west debugserver
```

再打开第二个终端，在包含输出zephyr.elf的构建目录连接EM SDP调试服务器。

```text
$ cd <my app>
$ $ZEPHYR_SDK_INSTALL_DIR/sysroots/x86_64-pokysdk-linux/usr/bin/ \
   arc-zephyr-elf/arc-zephyr-elf-gdb zephyr.elf
(gdb) target remote localhost:3333
(gdb) load
(gdb) b main
(gdb) c
```

<a id="flashing"></a>

### 烧录（Flashing）

若只需将应用下载到EM SDP的紧耦合存储器（CCM）并运行，可按常规方式操作。

```text
west build -b emsdp/emsdp_em6 <my app>
west flash
```

此命令通过OpenOCD及GDB加载ELF后立即运行。由于没有写入闪存，断电后应用会丢失。

开发期间通常通过OpenOCD及GDB调试，程序经USB下载到代码及数据存储器，而非每次写入闪存。

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://www.synopsys.com/dw/ipdir.php?ds=arc-em-software-development-platform](https://www.synopsys.com/dw/ipdir.php?ds=arc-em-software-development-platform)

<a id="id4"></a>

〔[2](#id5)〕 [http://store.digilentinc.com/pmod-modules](http://store.digilentinc.com/pmod-modules)

<a id="id6"></a>

〔[3](#id7)〕 [https://www.putty.software](https://www.putty.software)

## 译注

EM SDP核目标格式为emsdp/<core>，原文EM5D标识在一处为emsdp_em5D，而型号列表使用小写d。MikroBUS与Arduino共享控制器，Arduino复用须为GPIO模式。闪存示例先整片擦除；这里只翻译命令，未执行。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [pmod-modules](http://store.digilentinc.com/pmod-modules)：HTTP Error 403: Forbidden。
- [](https://embarc.org/project/arc-em-software-development-platform-sdp/)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。
- [ipdir.php?ds=arc-em-software-development-platform](https://www.synopsys.com/dw/ipdir.php?ds=arc-em-software-development-platform)：HTTP Error 403: Forbidden。

---

[上一章](P007_ARC_EM_Starter_Kit.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P009_ARC_HS_Development_Kit.md)
