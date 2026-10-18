---
id: learning.zephyr-docs.boards-madmachine-to-mediatek.page-15
title: Genio 700 EVK
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/mediatek/mt8390_genio_700_evk/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mt8390_genio_700_evk"></a>

# 第15章\_Genio 700评估套件（EVK）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/mediatek/mt8390_genio_700_evk/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/mt8390_genio_700_evk.webp](images/mt8390_genio_700_evk.webp)](images/mt8390_genio_700_evk.webp)

Genio 700评估套件（EVK）

名称（Name）：

`mt8390_genio_700_evk`

厂商（Vendor）：

[联发科技（MediaTek Inc.）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=mediatek)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm64](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm64)

片上系统（SoC）：

[mt8188](https://docs.zephyrproject.org/latest/boards/index.html#soc=mt8188)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/mediatek/mt8390_genio_700_evk/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

[MediaTek Genio 700 EVK](https://genio.mediatek.com/doc/iot-yocto/latest/hw/g700-evk.html)是Genio 700，即MT8390应用处理器的评估板，面向边缘AI及物联网应用。

Genio 700平台采用MT8390 SoC。其SoC IP基于MT8188驱动及设备树，MT8390仅出现在开发板名称中。

MT8390采用6 nm工艺，集成两个2.2 GHz Cortex-A78、六个2.0 GHz Cortex-A55、Arm Mali-G57 MC3 GPU、4.0 TOPS NPU及Tensilica HiFi 5音频DSP。

Zephyr作为Jailhouse客户系统（Inmate），与Linux并行运行在此板的一个Cortex-A55内核上，详见编程和调试。（[烧录与调试（Programming and Debugging）](#programming-and-debugging)）

<a id="hardware"></a>

## 硬件（Hardware）


- MediaTek Genio 700评估套件（EVK）
- 8 GB LPDDR4X DRAM
- 64 GB eMMC 5.1及microSD卡槽
- AzureWave AW-XB468NF Wi-Fi模块，采用MT7921
- 10／100／1000M以太网
- 一个USB Type-C主机端口及一个Micro-USB设备端口
- 两个M.2插槽，分别提供PCIe／USB及SDIO
- 两个四通道MIPI CSI摄像头接口
- 40针2.54 mm扩展排针，引脚分配兼容Raspberry Pi
- 三个Micro-USB连接器，通过USB转UART桥传输串口跟踪日志
- 2.0 mm插座输入12 V直流电源

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`mt8390_genio_700_evk`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="mt8390_genio_700_evk-hw-features"></a>

<a id="mt8390_genio_700_evk-mt8390_genio_700_evk/mt8188/a55-hw-features-section"></a>

#### `mt8390_genio_700_evk/mt8188/a55`目标（Target）

<a id="mt8390_genio_700_evk-mt8390_genio_700_evk/mt8188/a55-hw-features-panel"></a>

<a id="mt8390_genio_700_evk-mt8390_genio_700_evk/mt8188/a55-hw-features-memory"></a>

该开发板目标的片上存储容量：8 MiB RAM、N/A Flash。

<a id="mt8390_genio_700_evk-mt8390_genio_700_evk/mt8188/a55-hw-features-table"></a>

<table>
<tr>
<th>类型（Type）</th>
<th>位置（Location）</th>
<th>说明（Description）</th>
<th>兼容字符串（Compatible）</th>
</tr>
<tr>
<td rowspan="1">中央处理器（CPU）</td>
<td>片上（On-Chip）</td>
<td>Arm Cortex-A55 CPU（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/mediatek/mt8188.dtsi?plain=1#L37">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/mediatek/mt8188.dtsi?plain=1#L19">已禁用：5</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P009_arm_cortex-a55.md#std-dtcompatible-arm-cortex-a55"><code>arm,cortex-a55</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>MediaTek MT8188基础设施常开时钟控制器（Infra Always-On Clock Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/mediatek/mt8188.dtsi?plain=1#L74">已启用：1</a>）</td>
<td><a href="../clock_esp_infineon_microchip_binding_reference/P016_mediatek_mt8188-infracfg-ao.md#std-dtcompatible-mediatek-mt8188-infracfg-ao"><code>mediatek,mt8188-infracfg-ao</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/mediatek/mt8188.dtsi?plain=1#L65">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>MediaTek MT8188引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/mediatek/mt8188.dtsi?plain=1#L80">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P005_mediatek_mt8188-pinctrl.md#std-dtcompatible-mediatek-mt8188-pinctrl"><code>mediatek,mt8188-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>MediaTek MT8188 UART（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/mediatek/mt8188.dtsi?plain=1#L96">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/mediatek/mt8188.dtsi?plain=1#L86">已禁用：3</a>）</td>
<td><a href="../uart_espressif_infineon_microchip_binding_reference/P016_mediatek_mt8188-uart.md#std-dtcompatible-mediatek-mt8188-uart"><code>mediatek,mt8188-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/mediatek/mt8188.dtsi?plain=1#L56">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
</table>

Zephyr支持分配给客户系统分区（Inmate Cell）的外设。其余硬件仍属于Linux根分区（Root Cell），在开发板设备树中保持禁用。

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

<a id="serial-port"></a>

#### 串口（Serial Port）

Zephyr控制台使用UART1，设置为115200、8N1，复用到33脚UTXD1及34脚URXD1。

开发板引出三路UART，每路通过独立Micro-USB连接器上的USB转UART桥连接：

<table>
<tr>
<th>通用异步收发器（UART）</th>
<th>连接器（Connector）</th>
</tr>
<tr>
<td>UART0</td>
<td>CN3200</td>
</tr>
<tr>
<td>UART1</td>
<td>CN3201</td>
</tr>
<tr>
<td>UART2</td>
<td>CN3202</td>
</tr>
</table>

UART0为Linux控制台，保留在Root Cell，因此Zephyr使用CN3201上的UART1。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

Zephyr通过[Jailhouse](https://github.com/siemens/jailhouse)虚拟机监控器（Hypervisor）运行。Jailhouse从Linux收回一个Cortex-A55内核，分配给Zephyr。

此处需要理解三个Jailhouse概念：


- 分区（Cell）：分配给某个操作系统的一组硬件资源。
- 根分区（Root Cell）：Linux运行的分区，包含Linux使用的资源；客户系统资源从该分区中划出。
- 客户系统（Inmate）：与Linux同时运行的其他操作系统，此处为Zephyr。

Linux和Zephyr都不感知对方，各自只看到所属Cell描述的内核及内存。虚拟机监控器通过第二阶段地址转换（Second-Stage Translation）强制隔离；若Inmate访问未包含在其Cell配置中的资源，会触发故障。

Zephyr分得一个Cortex-A55内核及8 MB DRAM窗口，Cell将该窗口映射到Inmate自身地址空间的0x8000。其他内核及剩余外设留给Linux。

<a id="prerequisites"></a>

### 前置条件（Prerequisites）

目标设备需运行[IoT Yocto](https://genio.mediatek.com/doc/iot-yocto/latest/)镜像。Jailhouse、其内核模块及此板Cell配置都已包含在镜像中，无需单独构建。

原文步骤在IoT Yocto 26.0-release、Jailhouse 0.12及Linux 6.6内核组合上验证。

<a id="building"></a>

### 构建（Building）

```text
# From the root of the zephyr repository
west build -b mt8390_genio_700_evk/mt8188/a55 samples/hello_world
```

加载产物为原始二进制文件build/zephyr/zephyr.bin，不能使用ELF。可通过scp等方式复制到目标设备。

<a id="loading"></a>

### 加载（Loading）

在目标设备上，将Zephyr二进制文件放在当前目录，然后执行：

```text
modprobe jailhouse
jailhouse enable      /usr/share/jailhouse/cells/genio-700-evk.cell
jailhouse cell create /usr/share/jailhouse/cells/genio-700-evk-zephyr.cell
jailhouse cell load   zephyr zephyr.bin -a 0x8000
jailhouse cell start  zephyr
```

镜像不会自行启动虚拟机监控器，因此每次目标设备启动后，创建Inmate前都需执行一次jailhouse enable。此后重复运行只需最后三条命令。

重要提示（Important）

传给jailhouse cell load的加载地址必须为0x8000，同时匹配虚拟机监控器配置的Inmate基址，以及开发板设备树的memory@8000节点。若不匹配，镜像将被放到与Zephyr链接运行地址不同的位置，而构建过程不会发现此错误。

输出会出现在连接及I/O章节所述控制台：（[连接与输入输出（Connections and IOs）](#connections-and-ios)）

```text
*** Booting Zephyr OS build v4.4.0 ***
Hello World! mt8390_genio_700_evk/mt8188/a55
```

停止并卸载Inmate：

```text
jailhouse cell shutdown zephyr
jailhouse cell destroy  zephyr
```

<a id="debugging"></a>

### 调试（Debugging）

此板不提供Zephyr烧录或调试运行工具（Runner）。镜像由Linux中的虚拟机监控器加载，因此west flash及west debug不适用于此板。

<a id="references"></a>

## 参考资料（References）

Genio 700产品页面：

[https://genio.mediatek.com/genio-700](https://genio.mediatek.com/genio-700)

Genio 700 EVK硬件文档：

[https://genio.mediatek.com/doc/iot-yocto/latest/hw/g700-evk.html](https://genio.mediatek.com/doc/iot-yocto/latest/hw/g700-evk.html)

IoT Yocto文档：

[https://genio.mediatek.com/doc/iot-yocto/latest/](https://genio.mediatek.com/doc/iot-yocto/latest/)

## 译注

物理SoC为MT8390，构建目标仍使用mt8188/a55。Jailhouse客户系统与Linux根分区的资源边界、UART1控制台及每次目标启动后需启用监控器的步骤完整保留。

---

[上一章](P014_Genio_510_EVK.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md)
