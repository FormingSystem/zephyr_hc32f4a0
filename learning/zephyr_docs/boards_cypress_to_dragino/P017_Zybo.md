---
id: learning.zephyr-docs.boards-cypress-to-dragino.page-17
title: Zybo
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/digilent/zybo/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="zybo"></a>

# 第17章\_Zybo

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/digilent/zybo/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id2"></a>

[![官方原图：../../../../_images/zybo-0.jpg](images/zybo-0.jpg)](images/zybo-0.jpg)

Zybo

名称（Name）：

`zybo`

厂商（Vendor）：

[Digilent, Inc.公司](https://docs.zephyrproject.org/latest/boards/index.html#vendor=digilent)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[xc7z010](https://docs.zephyrproject.org/latest/boards/index.html#soc=xc7z010)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/digilent/zybo/doc/index.rst/../..)<a id="digilent-zybo"></a>

## Digilent Zybo

<a id="overview"></a>

### 概述（Overview）

[Digilent Zybo](https://digilent.com/reference/programmable-logic/zybo/start)，即ZYnq BOard，是一款功能丰富、开箱即用的嵌入式软件与数字电路开发板。它基于采用Xilinx全可编程片上系统（AP SoC）架构的Zynq-7000系列，将双核ARM Cortex-A9处理器与Xilinx 7系列FPGA逻辑紧密集成。

<a id="id3"></a>

![官方原图：Digilent Zybo](images/zybo-01.jpg)

Digilent，图片来源（Credit）：Digilent

<a id="hardware"></a>

### 硬件（Hardware）

<a id="supported-features"></a>

#### 支持的功能（Supported Features）

`zybo`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="zybo-hw-features"></a>

<a id="zybo-zybo/xc7z010-hw-features-section"></a>

##### `zybo/xc7z010`目标（Target）

<a id="zybo-zybo/xc7z010-hw-features-panel"></a>

<a id="zybo-zybo/xc7z010-hw-features-memory"></a>

该开发板目标的片上存储容量：512 MiB RAM、N/A Flash。

<a id="zybo-zybo/xc7z010-hw-features-table"></a>

<table>
<tr>
<th>类型（Type）</th>
<th>位置（Location）</th>
<th>说明（Description）</th>
<th>兼容字符串（Compatible）</th>
</tr>
<tr>
<td rowspan="1">中央处理器（CPU）</td>
<td>板载（On-Board）</td>
<td>ARM Cortex-A9处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/digilent/zybo/zybo.dts?plain=1#L38">已启用：2</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P016_arm_cortex-a9.md#std-dtcompatible-arm-cortex-a9"><code>arm,cortex-a9</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynq7000.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="2">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>Xilinx千兆以太网媒体访问控制器（GEM Ethernet Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynq7000.dtsi?plain=1#L80">已禁用：2</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P022_xlnx_gem.md#std-dtcompatible-xlnx-gem"><code>xlnx,gem</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Xilinx GEM管理数据输入输出节点（MDIO Node）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynq7000.dtsi?plain=1#L102">已禁用：2</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P012_xlnx_gem-mdio.md#std-dtcompatible-xlnx-gem-mdio"><code>xlnx,gem-mdio</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Xilinx Zynq-7000/ZynqMP MIO/EMIO通用输入输出控制器（GPIO Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynq7000.dtsi?plain=1#L184">已启用：1</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P030_xlnx_ps-gpio.md#std-dtcompatible-xlnx-ps-gpio"><code>xlnx,ps-gpio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Xilinx Zynq-7000/ZynqMP MIO/EMIO GPIO控制器组（Bank）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynq7000.dtsi?plain=1#L195">已启用：4</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P029_xlnx_ps-gpio-bank.md#std-dtcompatible-xlnx-ps-gpio-bank"><code>xlnx,ps-gpio-bank</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Cadence I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynq7000.dtsi?plain=1#L58">已禁用：2</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P015_cdns_i2c.md#std-dtcompatible-cdns-i2c"><code>cdns,i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/digilent/zybo/zybo.dts?plain=1#L65">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v1（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynq7000.dtsi?plain=1#L49">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P002_arm_gic-v1.md#std-dtcompatible-arm-gic-v1"><code>arm,gic-v1</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/digilent/zybo/zybo.dts?plain=1#L56">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Xilinx Zynq-7000系列SoC引脚控制（Pinctrl）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynq7000.dtsi?plain=1#L258">已启用：1</a>）</td>
<td><a href="../pinctrl_stm32_ti_xilinx_binding_reference/P021_xlnx_pinctrl-zynq.md#std-dtcompatible-xlnx-pinctrl-zynq"><code>xlnx,pinctrl-zynq</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>Xilinx安全数字／嵌入式多媒体卡主机控制器（SD/EMMC Host Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynq7000.dtsi?plain=1#L232">已禁用：2</a>）</td>
<td><a href="../sdhc_binding_reference/P021_xlnx_versal-8.9a.md#std-dtcompatible-xlnx-versal-8.9a"><code>xlnx,versal-8.9a</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Xilinx处理系统通用异步收发器（PS UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynq7000.dtsi?plain=1#L149">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynq7000.dtsi?plain=1#L140">已禁用：1</a>）</td>
<td><a href="../uart_ti_wch_virtual_binding_reference/P011_xlnx_xuartps.md#std-dtcompatible-xlnx-xuartps"><code>xlnx,xuartps</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Cadence串行外设接口控制器（SPI Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynq7000.dtsi?plain=1#L158">已禁用：2</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P011_cdns_spi.md#std-dtcompatible-cdns-spi"><code>cdns,spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/digilent/zybo/zybo.dts?plain=1#L51">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">系统控制器（System Controller）</td>
<td>片上（On-Chip）</td>
<td>系统控制器寄存器读写（System Controller Registers R/W）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynq7000.dtsi?plain=1#L251">已启用：1</a>）</td>
<td><a href="../edac_syscon_binding_reference/P008_syscon.md#std-dtcompatible-syscon"><code>syscon</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynq7000.dtsi?plain=1#L34">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
</table>

<a id="programming-and-debugging"></a>

### 烧录与调试（Programming and Debugging）

运行Zephyr应用前，必须初始化Zynq-7000系列SoC。可以采用多种方式，例如Xilinx第一级引导加载程序（FSBL）、Xilinx Vivado生成的`ps_init.tcl` JTAG脚本，以及Das U-Boot次级程序加载器（SPL）等。

这里使用U-Boot SPL。关于Das U-Boot在Xilinx Zynq-7000系列SoC上的使用细节与步骤，见以下文档：


- [Das U-Boot网站](https://www.denx.de/wiki/U-Boot)
- [在Xilinx U-Boot中使用发行版启动（Distro Boot）](https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/749142017/Using+Distro+Boot+With+Xilinx+U-Boot)

<a id="building-das-u-boot"></a>

#### 构建Das U-Boot（Building Das U-Boot）

为Digilent Zybo克隆并构建Das U-Boot：

```text
git clone -b v2022.04 https://source.denx.de/u-boot/u-boot.git
cd u-boot
make distclean
make xilinx_zynq_virt_defconfig
export PATH=/path/to/zephyr-sdk/arm-zephyr-eabi/bin/:$PATH
export CROSS_COMPILE=arm-zephyr-eabi-
export DEVICE_TREE="zynq-zybo"
make
```

<a id="flashing"></a>

#### 烧录（Flashing）

以下示例通过JTAG运行[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用。

确保开发板配置为JTAG启动，打开串口终端，给开发板上电或按PS-SRST键复位；通过JTAG上传并运行U-Boot SPL，初始化Zynq-7000系列SoC。

随后上传并运行Zephyr应用：

```text
# From the root of the zephyr repository
west build -b zybo samples/hello_world
west flash
```

终端中应出现以下消息：

```text
*** Booting Zephyr OS vx.xx.x-xxx-gxxxxxxxxxxxx ***
Hello World! zybo
```

另一种方式是通过U-Boot加载并运行[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用。将`u-boot/spl/boot.bin`、`u-boot/u-boot.img`及`zephyr/zephyr.bin`复制到FAT32格式的microSD卡，插入Zybo的SD MICRO插槽，确保开发板配置为SD卡启动，然后上电。

U-Boot初始化完成后，加载并运行Zephyr应用：

```text
Zynq> fatload mmc 0 0x0 zephyr.bin
817120 bytes read in 56 ms (13.9 MiB/s)
Zynq> go 0x0
## Starting application at 0x00000000 ...
*** Booting Zephyr OS vx.xx.x-xxx-gxxxxxxxxxxxx ***
Hello World! zybo
```

<a id="debugging"></a>

#### 调试（Debugging）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

确保开发板配置为JTAG启动，打开串口终端，给开发板上电或按PS-SRST键复位；通过JTAG上传并运行U-Boot SPL，初始化Zynq-7000系列SoC。

随后上传并调试Zephyr应用：

```text
# From the root of the zephyr repository
west build -b zybo samples/hello_world
west debug
```

在调试器中单步执行应用，终端中应出现以下消息：

```text
*** Booting Zephyr OS vx.x.x-xxx-gxxxxxxxxxxxx ***
Hello World! zybo
```

## 译注

Zybo的JTAG与SD卡启动流程分别保留。SD卡段落给出的zephyr/zephyr.bin与ZedBoard页面的build/zephyr/zephyr.bin不同，按各自原文记录；复制前应确认实际构建产物位置。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [start](https://digilent.com/reference/programmable-logic/zybo/start)：HTTP Error 403: Forbidden。

---

[上一章](P016_ZedBoard.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P018_DT-BL10_coexistence_Module_Development_Kit.md)
