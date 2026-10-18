---
id: learning.zephyr-docs.boards-sipeed-sparkfun.page-12
title: ARC IoT Development Kit
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/snps/iotdk/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="iotdk"></a>

# 第12章\_ARC物联网开发套件（IoT Development Kit）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/snps/iotdk/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/iotdk.jpg](images/iotdk.jpg)](images/iotdk.jpg)

ARC物联网开发套件（IoT Development Kit）

名称（Name）：

`iotdk`

厂商（Vendor）：

[Synopsys, Inc.](https://docs.zephyrproject.org/latest/boards/index.html#vendor=snps)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arc](https://docs.zephyrproject.org/latest/boards/index.html#arch=arc)

片上系统（SoC）：

[arc_iot](https://docs.zephyrproject.org/latest/boards/index.html#soc=arc_iot)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/snps/iotdk/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

DesignWare ARC IoT Development Kit提供硬件及软件，用于加速传感器融合、语音识别及人脸检测等设计的开发与调试。它包含采用中芯国际（SMIC）55 nm超低功耗工艺、运行于144 MHz的ARC Data Fusion IP子系统芯片，以及USB、UART、SPI、I2C、PWM、SDIO及ADC等常见物联网外设。

板卡详情见ARC IoT Development Kit（IoTDK）。（[ARC物联网开发套件（IoTDK）](https://www.synopsys.com/dw/ipdir.php?ds=arc_iot_development_kit)）

<a id="hardware"></a>

## 硬件（Hardware）

硬件功能详情见[ARC IoT Development Kit](https://embarc.org/project/arc-iot-development-kit/)。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`iotdk`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

在物联网开发套件上运行Zephyr RTOS应用还需要以下硬件及软件。


- Micro-USB线可为开发板供电；独立运行时，也可使用套件随附的通用开关电源，将110—240 V交流转换为5 V直流。
- [Zephyr软件开发套件（SDK）](../toolchains/P002_ZephyrSDK.md#toolchain-zephyr-sdk)
- <a id="id7"></a>

  用于USB转UART的终端仿真软件，原文建议[PuTTY网站](https://www.putty.software)[注3](#id6)所提供的软件。
- <a id="id5"></a>

  可选Pmod、Arduino或Mikro模块，见[Digilent Pmod Modules](http://store.digilentinc.com/pmod-modules) [注2](#id4)，也可自行开发连接Pmod的接口。

<a id="set-up-the-arc-iot-development-kit"></a>

### 设置ARC物联网开发套件

在物联网开发套件运行Zephyr前，需要正确设置开发板。


- 通过Digilent USB线将主机连接开发板。
- 可选：连接5 V直流电源。

<a id="set-up-zephyr-software"></a>

### 设置Zephyr软件

<a id="building-sample-applications"></a>

### 构建示例应用（Building Sample Applications）

可尝试多种示例或测试，这里以[samples/hello_world](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/hello_world)中的[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)为例。

<a id="configuring"></a>

#### 配置（Configuring）

若示例没有prj_arc.conf，可能需自行编写。随后通过menuconfig配置目标，选择iotdk板级配置以启用对应Zephyr支持。

```text
# From the root of the zephyr repository
west build -b iotdk samples/hello_world
west build -t menuconfig
```

<a id="building"></a>

#### 构建（Building）

可按常规方法构建应用，详情见“构建应用”，以下以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)为例。（[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)）

```text
# From the root of the zephyr repository
west build -b iotdk samples/hello_world
```

<a id="connecting-serial-output"></a>

### 连接串口输出（Connecting Serial Output）

默认Zephyr物联网开发套件镜像通过板上USB转UART输出串口日志，启用方法如下：


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

原文说明Zephyr SDK 0.9及更新版本可直接调试并加载物联网开发套件；这里保留原文版本门槛。

一种方式是通过常规Zephyr构建命令构建并调试应用。

```text
west build -b iotdk <my app>
west debug
```

随后可按常规调试，设置断点，再输入c继续执行。

另一种方式是启动调试服务器：

```text
west build -b iotdk <my app>
west debugserver
```

再打开第二个终端，在包含输出zephyr.elf的构建目录连接物联网开发套件调试服务器。

```text
$ cd <my app>
$ $ZEPHYR_SDK_INSTALL_DIR/arc-zephyr-elf/bin/arc-zephyr-elf-gdb zephyr.elf
(gdb) target remote localhost:3333
(gdb) load
(gdb) b main
(gdb) c
```

<a id="flashing"></a>

### 烧录（Flashing）

若只需将应用下载到物联网开发套件的紧耦合存储器（CCM）并运行，可按常规方式操作。

```text
west build -b iotdk <my app>
west flash
```

此命令通过OpenOCD及GDB将ELF加载到物联网开发套件后立即运行；由于未写入闪存，断电后应用会丢失。

开发期间通常通过OpenOCD及GDB调试，程序经USB下载到代码及数据存储器，而非每次写入闪存。

需要复位或上电后自动启动时，可按步骤将程序放入SPI闪存或内部嵌入式闪存（eFlash）。

<a id="id3"></a>

闪存写入步骤见[embARC网站](https://www.embarc.org)[注1](#id2)上的物联网开发套件文档。

<a id="release-notes"></a>

## 发布说明（Release Notes）

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://www.embarc.org](https://www.embarc.org)

<a id="id4"></a>

〔[2](#id5)〕 [http://store.digilentinc.com/pmod-modules](http://store.digilentinc.com/pmod-modules)

<a id="id6"></a>

〔[3](#id7)〕 [https://www.putty.software](https://www.putty.software)

## 译注

IoT Development Kit使用144 MHz ARC Data Fusion IP。USB可供电，独立运行可使用5 V适配器；不能照搬EM SDP／HSDK的12 V供电。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [pmod-modules](http://store.digilentinc.com/pmod-modules)：HTTP Error 403: Forbidden。
- [](https://embarc.org/project/arc-iot-development-kit/)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。
- [www.embarc.org](https://www.embarc.org)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。
- [ipdir.php?ds=arc_iot_development_kit](https://www.synopsys.com/dw/ipdir.php?ds=arc_iot_development_kit)：HTTP Error 403: Forbidden。

---

[上一章](P011_Synopsys.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P013_ARC_nSIM_and_HAPS_FPGA_boards.md)
