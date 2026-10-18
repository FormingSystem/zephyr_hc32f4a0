---
id: learning.zephyr-docs.boards-phytec.page-4
title: phyBOARD-Lyra AM62x A53 Core
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/phytec/phyboard_lyra/doc/phyboard_lyra_am62xx_a53.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="phyboard-lyra-am62x-a53-core"></a>

<a id="phyboard-lyra-am62xx-a53"></a>

# 第4章\_phyBOARD-Lyra AM62x A53核

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/phytec/phyboard_lyra/doc/phyboard_lyra_am62xx_a53.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

PHYTEC phyBOARD-Lyra AM62x基于TI Sitara应用处理器，包含一个四Cortex-A53集群及一个Cortex-M4核。此页Zephyr移植运行于Cortex-A53。


- 开发板特性（Board Features）：


  - RAM：2 GB DDR4
  - 存储（Storage）：


    - 16 GB嵌入式多媒体卡存储器（eMMC）
    - 64 MB八线SPI NOR闪存（OSPI NOR）
    - 4 KB EEPROM
  - 以太网（Ethernet）

详情见[PHYTEC AM62x产品页](https://www.phytec.com/product/phycore-am62x/)。

<a id="id1"></a>

![官方原图：phyBOARD-Lyra AM62x](images/phyCORE-AM62x_Lyra_frontside.webp)

搭载phyCORE-AM62x SoM的PHYTEC phyBOARD-Lyra

<a id="supported-features"></a>

### 支持的功能（Supported Features）

Zephyr的phyboard_lyra/am6234/a53配置支持以下硬件功能：

<table>
<tr>
<th>接口（Interface）</th>
<th>控制器（Controller）</th>
<th>驱动／组件（Driver/Component）</th>
</tr>
<tr>
<td>GIC-v3</td>
<td>片上（On-Chip）</td>
<td>中断控制器（Interrupt Controller）</td>
</tr>
<tr>
<td>Arm定时器（ARM TIMER）</td>
<td>片上（On-Chip）</td>
<td>系统时钟（System Clock）。</td>
</tr>
<tr>
<td>引脚控制（PINCTRL）</td>
<td>片上（On-Chip）</td>
<td>pinctrl</td>
</tr>
<tr>
<td>通用异步收发器（UART）</td>
<td>片上（On-Chip）</td>
<td>串口（Serial Port）。</td>
</tr>
<tr>
<td>邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>核间通信邮箱（IPC Mailbox）</td>
</tr>
</table>

<a id="devices"></a>

### 设备（Devices）

<a id="system-clock"></a>

#### 系统时钟（System Clock）

此配置使用200 MHz系统时钟。

<a id="ddr-ram"></a>

#### DDR随机存取存储器（DDR RAM）

此板有2 GB DDR RAM，配置为Zephyr分配1 MB，即0x82000000至0x82100000。

<a id="serial-port"></a>

#### 串口（Serial Port）

此配置通过CPU的UART0提供唯一串行通信通道。

<a id="sd-card"></a>

## SD卡（SD Card）

下载PHYTEC官方[WIC](https://download.phytec.de/Software/Linux/BSP-Yocto-AM62x/BSP-Yocto-Ampliphy-AM62x-PD23.2.1/images/ampliphy-xwayland/phyboard-lyra-am62xx-3/phytec-qt5demo-image-phyboard-lyra-am62xx-3.wic.xz)及[bmap](https://download.phytec.de/Software/Linux/BSP-Yocto-AM62x/BSP-Yocto-Ampliphy-AM62x-PD23.2.1/images/ampliphy-xwayland/phyboard-lyra-am62xx-3/phytec-qt5demo-image-phyboard-lyra-am62xx-3.wic.bmap)文件，用bmap-tools将WIC镜像写入SD卡。

```text
bmaptool copy phytec-qt5demo-image-phyboard-lyra-am62xx-3.wic.xz /dev/sdX
```

<a id="building"></a>

## 构建（Building）

可按常规方法构建应用，详情见“构建应用”，以下以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)为例。（[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)）

```text
# From the root of the zephyr repository
west build -b phyboard_lyra/am6234/a53 samples/hello_world
```

<a id="programming"></a>

## 编程（Programming）

将编译的zephyr.bin复制到SD卡第一个FAT分区，插入开发板，上电后在提示符处停止U-Boot执行。

用U-Boot加载并启动zephyr.bin：

```text
fatload mmc 1:1 0x82000000 zephyr.bin; dcache flush; icache flush; dcache off; icache off; go 0x82000000
```

## 译注

Lyra A53版本使用200 MHz系统时钟，为Zephyr分配0x82000000至0x82100000的1 MB DDR；启动与M4F版本分开。

---

[上一章](P003_phyBOARD-Electra_AM64x_M4F_Core.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P005_phyBOARD-Lyra_AM62x_M4F_Core.md)
