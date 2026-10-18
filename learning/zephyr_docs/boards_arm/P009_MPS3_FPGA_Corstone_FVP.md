---
id: learning.zephyr-docs.boards-arm.page-9
title: MPS3 FPGA Corstone FVP
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/arm/mps3/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mps3"></a>

# 第9章\_MPS3 FPGA／Corstone固定虚拟平台（FVP）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/arm/mps3/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/mps3.jpg](images/mps3.jpg)](images/mps3.jpg)

MPS3 FPGA／Corstone固定虚拟平台（FVP）

名称（Name）：

`mps3`

厂商（Vendor）：

[Arm公司（ARM Ltd.）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=arm)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

`[an536](https://docs.zephyrproject.org/latest/boards/index.html#soc=an536), [corstone300](https://docs.zephyrproject.org/latest/boards/index.html#soc=corstone300), [corstone310](https://docs.zephyrproject.org/latest/boards/index.html#soc=corstone310)`

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/arm/mps3/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

`mps3`配置用于运行在MPS3上的Zephyr应用，支持多种Arm FPGA镜像及仿真模型：


- AN536支持Arm Cortex-R52 CPU
- AN547及AN552支持Arm Cortex-M55 CPU
- AN555支持Arm Cortex-M85 CPU
- 部分Cortex-M配置支持Corstone-300及Corstone-310 FVP

根据所选目标，提供以下设备支持：


- 嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）
- 系统滴答系统时钟（SYSTICK / System Tick System Clock）
- 通用中断控制器v3（GICv3 / Generic Interrupt Controller v3）
- Arm架构定时器（Architectural Timer）
- Cortex-M系统设计套件（CMSDK）GPIO
- Cortex-M系统设计套件（CMSDK）UART
- Ethos-U55神经网络处理单元（NPU）

![官方原图：ARM MPS3](images/mps31.jpg)

[Corstone-300 FVP](https://developer.arm.com/tools-and-software/open-source-software/arm-platforms-software/arm-ecosystem-fvps)及[Corstone-310 FVP](https://developer.arm.com/tools-and-software/open-source-software/arm-platforms-software/arm-ecosystem-fvps)完整模拟Arm系统，包括处理器、存储器和外设，可在Linux及Windows系统上免费使用。选择FVP进行仿真，是因为它提供Ethos-U55 NPU访问能力，而QEMU及其他仿真平台没有这项能力。

AN536 Cortex-R52x2子系统可通过QEMU的`mps3-an536`机器模型运行。

<a id="zephyr-board-options"></a>

### Zephyr开发板选项（Board Options）

<a id="tab-0-0-0"></a>

<a id="tab-0-0-1"></a>

<a id="tab-0-0-2"></a>

<a id="tab-0-0-3"></a>

<a id="tab-0-0-4"></a>

<a id="tab-0-0-5"></a>

<a id="panel-0-0-0"></a>

**MPS3 Corstone-300（AN547）**

MPS3+ AN547是采用Cortex-M55架构的SoC。Zephyr支持构建安全及非安全固件。

`BOARD`选项汇总如下：

<table>
<tr>
<th>开发板目标（BOARD）</th>
<th>说明（Description）</th>
</tr>
<tr>
<td><code>mps3/corstone300/an547</code></td>
<td>构建安全固件，或仅安全态固件（Secure-Only）</td>
</tr>
<tr>
<td><code>mps3/corstone300/an547/ns</code></td>
<td>构建非安全固件（Non-Secure）</td>
</tr>
</table>

FPGA用法：


- 构建与烧录说明见编程与调试（[Programming and Debugging](#programming-and-debugging)）。

FVP用法：


- 此变体不支持FVP。

QEMU用法：


- 若要使用QEMU替代默认的FVP，可在构建时按以下方式覆盖仿真器选择：

```text
$ west build -b mps3/corstone300/an547 samples/hello_world -DEMU_PLATFORM=qemu -t run
```

<a id="panel-0-0-1"></a>

**MPS3 Corstone-300（AN552）**

MPS3+ AN552是采用Cortex-M55架构的SoC。Zephyr支持构建安全及非安全固件。

`BOARD`选项汇总如下：

<table>
<tr>
<th>开发板目标（BOARD）</th>
<th>说明（Description）</th>
</tr>
<tr>
<td><code>mps3/corstone300/an552</code></td>
<td>构建安全固件，或仅安全态固件（Secure-Only）</td>
</tr>
<tr>
<td><code>mps3/corstone300/an552/ns</code></td>
<td>构建非安全固件（Non-Secure）</td>
</tr>
</table>

FPGA用法：


- 构建与烧录说明见编程与调试（[Programming and Debugging](#programming-and-debugging)）。

FVP用法：


- 此变体不支持FVP。

QEMU用法：


- 此开发板变体不支持QEMU。

<a id="panel-0-0-2"></a>

**MPS3 Corstone-300固定虚拟平台（FVP）**

MPS3+ FVP是采用Cortex-M55架构的SoC。Zephyr支持构建安全及非安全固件。

`BOARD`选项汇总如下：

<table>
<tr>
<th>开发板目标（BOARD）</th>
<th>说明（Description）</th>
</tr>
<tr>
<td><code>mps3/corstone300/fvp</code></td>
<td>构建安全固件，或仅安全态固件（Secure-Only）</td>
</tr>
<tr>
<td><code>mps3/corstone300/fvp/ns</code></td>
<td>构建非安全固件（Non-Secure）</td>
</tr>
</table>

FPGA用法：


- N/A.

FVP用法：


- 使用FVP前，先设置环境变量`ARMFVP_BIN_PATH`，然后通过`west build -t run`运行。

```text
export ARMFVP_BIN_PATH=/path/to/fvp/directory
west build -b {BOARD qualifier from table above} samples/hello_world -t run
```

运行FVP仿真工具前，需要从Arm下载“FVP model for the Corstone-300 MPS3”并安装到主机。原文记录使用11.24.13版本（2024年1月4日）测试。

QEMU用法：


- N/A.

<a id="panel-0-0-3"></a>

**MPS3 Corstone-310（AN555）**

MPS3+ AN555是采用Cortex-M85架构的SoC。Zephyr支持构建安全及非安全固件。

`BOARD`选项汇总如下：

<table>
<tr>
<th>开发板目标（BOARD）</th>
<th>说明（Description）</th>
</tr>
<tr>
<td><code>mps3/corstone310/an555</code></td>
<td>构建安全固件，或仅安全态固件（Secure-Only）</td>
</tr>
<tr>
<td><code>mps3/corstone310/an555/ns</code></td>
<td>构建非安全固件（Non-Secure）</td>
</tr>
</table>

FPGA用法：


- 构建与烧录说明见编程与调试（[Programming and Debugging](#programming-and-debugging)）。

FVP用法：


- 此变体不支持FVP。

QEMU用法：


- 此开发板变体不支持QEMU。

<a id="panel-0-0-4"></a>

**MPS3 Corstone-310固定虚拟平台（FVP）**

MPS3+ FVP是采用Cortex-M85架构的SoC。Zephyr支持构建安全及非安全固件。

`BOARD`选项汇总如下：

<table>
<tr>
<th>开发板目标（BOARD）</th>
<th>说明（Description）</th>
</tr>
<tr>
<td><code>mps3/corstone310/fvp</code></td>
<td>构建安全固件，或仅安全态固件（Secure-Only）</td>
</tr>
<tr>
<td><code>mps3/corstone310/fvp/ns</code></td>
<td>构建非安全固件（Non-Secure）</td>
</tr>
</table>

FPGA用法：


- N/A.

FVP用法：


- 使用FVP前，先设置环境变量`ARMFVP_BIN_PATH`，然后通过`west build -t run`运行。

```text
export ARMFVP_BIN_PATH=/path/to/fvp/directory
west build -b {BOARD qualifier from table above} samples/hello_world -t run
```

运行FVP仿真工具前，需要从Arm下载“FVP model for the Corstone-310 MPS3”并安装到主机。原文记录使用11.24.13版本（2024年1月4日）测试。

QEMU用法：


- N/A.

<a id="panel-0-0-5"></a>

**MPS3 AN536**

MPS3 AN536是Cortex-R52x2子系统示例。Zephyr当前支持为CPU0构建。

`BOARD`选项汇总如下：

<table>
<tr>
<th>开发板目标（BOARD）</th>
<th>说明（Description）</th>
</tr>
<tr>
<td><code>mps3/an536/cpu0</code></td>
<td>为R52 CPU0构建固件</td>
</tr>
</table>

FPGA用法：


- N/A.

FVP用法：


- N/A.

QEMU用法：


- 使用QEMU运行：

```text
west build -b mps3/an536/cpu0 samples/hello_world -t run
```

注意（Note）

开发板限定符（Board Qualifier）必须包含上述完整名称，仅用`mps3/corstone300`、`mps3/corstone310`或`mps3/an536`无效。

<a id="hardware"></a>

## 硬件（Hardware）

ARM MPS3提供以下硬件组件：


- 中央处理器（CPU）


  - AN547与AN552支持Arm Cortex-M55 CPU，以及SSE-300子系统的软宏模型（SMM）实现
  - AN555支持Arm Cortex-M85 CPU，以及SSE-310子系统的软宏模型（SMM）实现
  - AN536支持Arm Cortex-R52 CPU及Cortex-R52x2子系统示例
- 存储器（Memory）


  - 8 MB块RAM（BRAM）
  - 默认4 GB DDR4小型双列直插内存模块（SODIMM），可升级到8 GB
  - 16 GB嵌入式多媒体卡存储器（eMMC）
  - 8 MB四线SPI闪存（QSPI Flash）
- 调试（Debug）


  - P-JTAG、F-JTAG、SWD、四位跟踪及16位跟踪（Trace）
  - 通过USB提供四个串口
- 接口（Interface）


  - AHB通用输入输出（GPIO）
  - 通用异步收发器（UART）
  - 串行外设接口（SPI）
  - 集成电路间总线（I2C）
  - 集成电路间音频总线（I2S）
  - 彩色液晶显示器串行接口（LCD Serial Interface）
  - 以太网（Ethernet）
  - 视频图形阵列接口（VGA）
- 板载外设（On-Board Peripherals）


  - 彩色液晶显示器（LCD）
  - 十个LED
  - 八个开关
  - 两个用户按键

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`mps3`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="mps3-hw-features"></a>

<a id="mps3-mps3/an536/cpu0-hw-features-section"></a>

#### `mps3/an536/cpu0`目标（Target）

<a id="mps3-mps3/an536/cpu0-hw-features-panel"></a>

<a id="mps3-mps3/an536/cpu0-hw-features-memory"></a>

该开发板目标的片上存储容量：512 KiB RAM、N/A Flash。

<a id="mps3-mps3/an536/cpu0-hw-features-table"></a>

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
<td>ARM Cortex-R52处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_an536.dtsi?plain=1#L21">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_an536.dtsi?plain=1#L27">已禁用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P011_arm_cortex-r52.md#std-dtcompatible-arm-cortex-r52"><code>arm,cortex-r52</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_an536.dtsi?plain=1#L97">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>板载（On-Board）</td>
<td>ARM CMSDK通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_an536.dtsi?plain=1#L132">已启用：4</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P027_arm_cmsdk-gpio.md#std-dtcompatible-arm-cmsdk-gpio"><code>arm,cmsdk-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>板载（On-Board）</td>
<td>ARM SBCon双线串行总线接口（Two-Wire Serial Bus Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_an536.dtsi?plain=1#L189">已禁用：5</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P006_arm_versatile-i2c.md#std-dtcompatible-arm-versatile-i2c"><code>arm,versatile-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>板载（On-Board）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_an536.dtsi?plain=1#L116">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>板载（On-Board）</td>
<td>Arm MPS3引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_an536.dtsi?plain=1#L103">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P009_arm_mps3-pinctrl.md#std-dtcompatible-arm-mps3-pinctrl"><code>arm,mps3-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>板载（On-Board）</td>
<td>ARM CMSDK通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_an536_cpu0.dts?plain=1#L26">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_an536.dtsi?plain=1#L275">已禁用：4</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P007_arm_cmsdk-uart.md#std-dtcompatible-arm-cmsdk-uart"><code>arm,cmsdk-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>板载（On-Board）</td>
<td>ARM PL022串行外设接口（SPI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_an536.dtsi?plain=1#L207">已禁用：3</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P007_arm_pl022.md#std-dtcompatible-arm-pl022"><code>arm,pl022</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_an536.dtsi?plain=1#L86">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_an536.dtsi?plain=1#L34">已禁用：8</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>板载（On-Board）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_an536.dtsi?plain=1#L70">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>板载（On-Board）</td>
<td>ARM CMSDK看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_an536.dtsi?plain=1#L172">已禁用：1</a>）</td>
<td><a href="../watchdog_binding_reference/P005_arm_cmsdk-watchdog.md#std-dtcompatible-arm-cmsdk-watchdog"><code>arm,cmsdk-watchdog</code></a></td>
</tr>
</table>

<a id="mps3-mps3/corstone300/an547-hw-features-section"></a>

#### `mps3/corstone300/an547`目标（Target）

<a id="mps3-mps3/corstone300/an547-hw-features-panel"></a>

<a id="mps3-mps3/corstone300/an547-hw-features-memory"></a>

该开发板目标的片上存储容量：512 KiB RAM、512 KiB Flash。

<a id="mps3-mps3/corstone300/an547-hw-features-table"></a>

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
<td>ARM Cortex-M55处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_corstone300_an547.dts?plain=1#L29">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P003_arm_cortex-m55.md#std-dtcompatible-arm-cortex-m55"><code>arm,cortex-m55</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>板载（On-Board）</td>
<td>Arm Ethos-U是一种微型神经网络处理单元（Micro NPU），可在嵌入式设备上对神经网络进行硬件加速（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_corstone300_an547.dts?plain=1#L48">已启用：1</a>）</td>
<td><a href="../arm_timing_ethosu_control_binding_reference/P004_arm_ethos-u.md#std-dtcompatible-arm-ethos-u"><code>arm,ethos-u</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L8">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">以太网（Ethernet）</td>
<td>板载（On-Board）</td>
<td>SMSC（现属Microchip）LAN9220以太网控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L46">已启用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P003_smsc_lan9220.md#std-dtcompatible-smsc-lan9220"><code>smsc,lan9220</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>板载（On-Board）</td>
<td>ARM CMSDK通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L14">已启用：4</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P027_arm_cmsdk-gpio.md#std-dtcompatible-arm-cmsdk-gpio"><code>arm,cmsdk-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ARM 32位内存映射输入输出GPIO（MMIO32 GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L132">已启用：3</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P028_arm_mmio32-gpio.md#std-dtcompatible-arm-mmio32-gpio"><code>arm,mmio32-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>板载（On-Board）</td>
<td>ARM SBCon双线串行总线接口（Two-Wire Serial Bus Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L54">已启用：5</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P006_arm_versatile-i2c.md#std-dtcompatible-arm-versatile-i2c"><code>arm,versatile-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common.dtsi?plain=1#L77">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8.1-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L17">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P004_ARMv8_1_M_NVIC.md#std-dtcompatible-arm-v8.1m-nvic"><code>arm,v8.1m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common.dtsi?plain=1#L23">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>板载（On-Board）</td>
<td>ARMv8.1-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_corstone300_an547.dts?plain=1#L36">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P006_arm_armv8.1m-mpu.md#std-dtcompatible-arm-armv8.1m-mpu"><code>arm,armv8.1m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>板载（On-Board）</td>
<td>Arm MPS3引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L219">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P009_arm_mps3-pinctrl.md#std-dtcompatible-arm-mps3-pinctrl"><code>arm,mps3-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>板载（On-Board）</td>
<td>ARM CMSDK通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L160">已启用：5</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L209">已禁用：1</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P007_arm_cmsdk-uart.md#std-dtcompatible-arm-cmsdk-uart"><code>arm,cmsdk-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>板载（On-Board）</td>
<td>ARM PL022串行外设接口（SPI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L70">已启用：3</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P007_arm_pl022.md#std-dtcompatible-arm-pl022"><code>arm,pl022</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8.1-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L25">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P008_ARMv8_1_M_SysTick.md#std-dtcompatible-arm-armv8.1m-systick"><code>arm,armv8.1m-systick</code></a></td>
</tr>
</table>

<a id="mps3-mps3/corstone300/an552-hw-features-section"></a>

#### `mps3/corstone300/an552`目标（Target）

<a id="mps3-mps3/corstone300/an552-hw-features-panel"></a>

<a id="mps3-mps3/corstone300/an552-hw-features-memory"></a>

该开发板目标的片上存储容量：512 KiB RAM、512 KiB Flash。

<a id="mps3-mps3/corstone300/an552-hw-features-table"></a>

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
<td>ARM Cortex-M55处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_corstone300_an552.dts?plain=1#L28">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P003_arm_cortex-m55.md#std-dtcompatible-arm-cortex-m55"><code>arm,cortex-m55</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>板载（On-Board）</td>
<td>Arm Ethos-U是一种微型神经网络处理单元（Micro NPU），可在嵌入式设备上对神经网络进行硬件加速（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_corstone300_an552.dts?plain=1#L47">已启用：1</a>）</td>
<td><a href="../arm_timing_ethosu_control_binding_reference/P004_arm_ethos-u.md#std-dtcompatible-arm-ethos-u"><code>arm,ethos-u</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L8">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">以太网（Ethernet）</td>
<td>板载（On-Board）</td>
<td>SMSC（现属Microchip）LAN9220以太网控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L46">已启用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P003_smsc_lan9220.md#std-dtcompatible-smsc-lan9220"><code>smsc,lan9220</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>板载（On-Board）</td>
<td>ARM CMSDK通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L14">已启用：4</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P027_arm_cmsdk-gpio.md#std-dtcompatible-arm-cmsdk-gpio"><code>arm,cmsdk-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ARM 32位内存映射输入输出GPIO（MMIO32 GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L132">已启用：3</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P028_arm_mmio32-gpio.md#std-dtcompatible-arm-mmio32-gpio"><code>arm,mmio32-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>板载（On-Board）</td>
<td>ARM SBCon双线串行总线接口（Two-Wire Serial Bus Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L54">已启用：5</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P006_arm_versatile-i2c.md#std-dtcompatible-arm-versatile-i2c"><code>arm,versatile-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common.dtsi?plain=1#L77">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8.1-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L17">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P004_ARMv8_1_M_NVIC.md#std-dtcompatible-arm-v8.1m-nvic"><code>arm,v8.1m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common.dtsi?plain=1#L23">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>板载（On-Board）</td>
<td>ARMv8.1-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_corstone300_an552.dts?plain=1#L35">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P006_arm_armv8.1m-mpu.md#std-dtcompatible-arm-armv8.1m-mpu"><code>arm,armv8.1m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>板载（On-Board）</td>
<td>Arm MPS3引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L219">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P009_arm_mps3-pinctrl.md#std-dtcompatible-arm-mps3-pinctrl"><code>arm,mps3-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>板载（On-Board）</td>
<td>ARM CMSDK通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L160">已启用：5</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L209">已禁用：1</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P007_arm_cmsdk-uart.md#std-dtcompatible-arm-cmsdk-uart"><code>arm,cmsdk-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>板载（On-Board）</td>
<td>ARM PL022串行外设接口（SPI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L70">已启用：3</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P007_arm_pl022.md#std-dtcompatible-arm-pl022"><code>arm,pl022</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8.1-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L25">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P008_ARMv8_1_M_SysTick.md#std-dtcompatible-arm-armv8.1m-systick"><code>arm,armv8.1m-systick</code></a></td>
</tr>
</table>

<a id="mps3-mps3/corstone300/fvp-hw-features-section"></a>

#### `mps3/corstone300/fvp`目标（Target）

<a id="mps3-mps3/corstone300/fvp-hw-features-panel"></a>

<a id="mps3-mps3/corstone300/fvp-hw-features-memory"></a>

该开发板目标的片上存储容量：512 KiB RAM、512 KiB Flash。

<a id="mps3-mps3/corstone300/fvp-hw-features-table"></a>

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
<td>ARM Cortex-M55处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_corstone300_fvp.dts?plain=1#L28">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P003_arm_cortex-m55.md#std-dtcompatible-arm-cortex-m55"><code>arm,cortex-m55</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>板载（On-Board）</td>
<td>Arm Ethos-U是一种微型神经网络处理单元（Micro NPU），可在嵌入式设备上对神经网络进行硬件加速（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_corstone300_fvp.dts?plain=1#L47">已启用：1</a>）</td>
<td><a href="../arm_timing_ethosu_control_binding_reference/P004_arm_ethos-u.md#std-dtcompatible-arm-ethos-u"><code>arm,ethos-u</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L8">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">以太网（Ethernet）</td>
<td>板载（On-Board）</td>
<td>SMSC（现属Microchip）LAN9220以太网控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L46">已启用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P003_smsc_lan9220.md#std-dtcompatible-smsc-lan9220"><code>smsc,lan9220</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>板载（On-Board）</td>
<td>ARM CMSDK通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L14">已启用：4</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P027_arm_cmsdk-gpio.md#std-dtcompatible-arm-cmsdk-gpio"><code>arm,cmsdk-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ARM 32位内存映射输入输出GPIO（MMIO32 GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L132">已启用：3</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P028_arm_mmio32-gpio.md#std-dtcompatible-arm-mmio32-gpio"><code>arm,mmio32-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>板载（On-Board）</td>
<td>ARM SBCon双线串行总线接口（Two-Wire Serial Bus Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L54">已启用：5</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P006_arm_versatile-i2c.md#std-dtcompatible-arm-versatile-i2c"><code>arm,versatile-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common.dtsi?plain=1#L77">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8.1-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L17">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P004_ARMv8_1_M_NVIC.md#std-dtcompatible-arm-v8.1m-nvic"><code>arm,v8.1m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common.dtsi?plain=1#L23">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>板载（On-Board）</td>
<td>ARMv8.1-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_corstone300_fvp.dts?plain=1#L35">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P006_arm_armv8.1m-mpu.md#std-dtcompatible-arm-armv8.1m-mpu"><code>arm,armv8.1m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>板载（On-Board）</td>
<td>Arm MPS3引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L219">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P009_arm_mps3-pinctrl.md#std-dtcompatible-arm-mps3-pinctrl"><code>arm,mps3-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>板载（On-Board）</td>
<td>ARM CMSDK通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L160">已启用：5</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L209">已禁用：1</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P007_arm_cmsdk-uart.md#std-dtcompatible-arm-cmsdk-uart"><code>arm,cmsdk-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>板载（On-Board）</td>
<td>ARM PL022串行外设接口（SPI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L70">已启用：3</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P007_arm_pl022.md#std-dtcompatible-arm-pl022"><code>arm,pl022</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8.1-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L25">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P008_ARMv8_1_M_SysTick.md#std-dtcompatible-arm-armv8.1m-systick"><code>arm,armv8.1m-systick</code></a></td>
</tr>
</table>

<a id="mps3-mps3/corstone310/an555-hw-features-section"></a>

#### `mps3/corstone310/an555`目标（Target）

<a id="mps3-mps3/corstone310/an555-hw-features-panel"></a>

<a id="mps3-mps3/corstone310/an555-hw-features-memory"></a>

该开发板目标的片上存储容量：2 MiB RAM、4 MiB Flash。

<a id="mps3-mps3/corstone310/an555-hw-features-table"></a>

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
<td>ARM Cortex-M85处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_corstone310_an555.dts?plain=1#L28">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P006_arm_cortex-m85.md#std-dtcompatible-arm-cortex-m85"><code>arm,cortex-m85</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>板载（On-Board）</td>
<td>Arm Ethos-U是一种微型神经网络处理单元（Micro NPU），可在嵌入式设备上对神经网络进行硬件加速（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_corstone310_an555.dts?plain=1#L47">已启用：1</a>）</td>
<td><a href="../arm_timing_ethosu_control_binding_reference/P004_arm_ethos-u.md#std-dtcompatible-arm-ethos-u"><code>arm,ethos-u</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L8">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">以太网（Ethernet）</td>
<td>板载（On-Board）</td>
<td>SMSC（现属Microchip）LAN9220以太网控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L46">已启用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P003_smsc_lan9220.md#std-dtcompatible-smsc-lan9220"><code>smsc,lan9220</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>板载（On-Board）</td>
<td>ARM CMSDK通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L14">已启用：4</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P027_arm_cmsdk-gpio.md#std-dtcompatible-arm-cmsdk-gpio"><code>arm,cmsdk-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ARM 32位内存映射输入输出GPIO（MMIO32 GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L132">已启用：3</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P028_arm_mmio32-gpio.md#std-dtcompatible-arm-mmio32-gpio"><code>arm,mmio32-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>板载（On-Board）</td>
<td>ARM SBCon双线串行总线接口（Two-Wire Serial Bus Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L54">已启用：5</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P006_arm_versatile-i2c.md#std-dtcompatible-arm-versatile-i2c"><code>arm,versatile-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common.dtsi?plain=1#L77">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8.1-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L17">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P004_ARMv8_1_M_NVIC.md#std-dtcompatible-arm-v8.1m-nvic"><code>arm,v8.1m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common.dtsi?plain=1#L23">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>板载（On-Board）</td>
<td>ARMv8.1-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_corstone310_an555.dts?plain=1#L35">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P006_arm_armv8.1m-mpu.md#std-dtcompatible-arm-armv8.1m-mpu"><code>arm,armv8.1m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>板载（On-Board）</td>
<td>Arm MPS3引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L219">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P009_arm_mps3-pinctrl.md#std-dtcompatible-arm-mps3-pinctrl"><code>arm,mps3-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>板载（On-Board）</td>
<td>ARM CMSDK通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L160">已启用：5</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L209">已禁用：1</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P007_arm_cmsdk-uart.md#std-dtcompatible-arm-cmsdk-uart"><code>arm,cmsdk-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>板载（On-Board）</td>
<td>ARM PL022串行外设接口（SPI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L70">已启用：3</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P007_arm_pl022.md#std-dtcompatible-arm-pl022"><code>arm,pl022</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8.1-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L25">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P008_ARMv8_1_M_SysTick.md#std-dtcompatible-arm-armv8.1m-systick"><code>arm,armv8.1m-systick</code></a></td>
</tr>
</table>

<a id="mps3-mps3/corstone310/fvp-hw-features-section"></a>

#### `mps3/corstone310/fvp`目标（Target）

<a id="mps3-mps3/corstone310/fvp-hw-features-panel"></a>

<a id="mps3-mps3/corstone310/fvp-hw-features-memory"></a>

该开发板目标的片上存储容量：2 MiB RAM、4 MiB Flash。

<a id="mps3-mps3/corstone310/fvp-hw-features-table"></a>

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
<td>ARM Cortex-M85处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_corstone310_fvp.dts?plain=1#L28">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P006_arm_cortex-m85.md#std-dtcompatible-arm-cortex-m85"><code>arm,cortex-m85</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>板载（On-Board）</td>
<td>Arm Ethos-U是一种微型神经网络处理单元（Micro NPU），可在嵌入式设备上对神经网络进行硬件加速（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_corstone310_fvp.dts?plain=1#L47">已启用：1</a>）</td>
<td><a href="../arm_timing_ethosu_control_binding_reference/P004_arm_ethos-u.md#std-dtcompatible-arm-ethos-u"><code>arm,ethos-u</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L8">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">以太网（Ethernet）</td>
<td>板载（On-Board）</td>
<td>SMSC（现属Microchip）LAN9220以太网控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L46">已启用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P003_smsc_lan9220.md#std-dtcompatible-smsc-lan9220"><code>smsc,lan9220</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>板载（On-Board）</td>
<td>ARM CMSDK通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L14">已启用：4</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P027_arm_cmsdk-gpio.md#std-dtcompatible-arm-cmsdk-gpio"><code>arm,cmsdk-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ARM 32位内存映射输入输出GPIO（MMIO32 GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L132">已启用：3</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P028_arm_mmio32-gpio.md#std-dtcompatible-arm-mmio32-gpio"><code>arm,mmio32-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>板载（On-Board）</td>
<td>ARM SBCon双线串行总线接口（Two-Wire Serial Bus Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L54">已启用：5</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P006_arm_versatile-i2c.md#std-dtcompatible-arm-versatile-i2c"><code>arm,versatile-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common.dtsi?plain=1#L77">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8.1-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L17">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P004_ARMv8_1_M_NVIC.md#std-dtcompatible-arm-v8.1m-nvic"><code>arm,v8.1m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common.dtsi?plain=1#L23">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>板载（On-Board）</td>
<td>ARMv8.1-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_corstone310_fvp.dts?plain=1#L35">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P006_arm_armv8.1m-mpu.md#std-dtcompatible-arm-armv8.1m-mpu"><code>arm,armv8.1m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>板载（On-Board）</td>
<td>Arm MPS3引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L219">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P009_arm_mps3-pinctrl.md#std-dtcompatible-arm-mps3-pinctrl"><code>arm,mps3-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>板载（On-Board）</td>
<td>ARM CMSDK通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L160">已启用：5</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L209">已禁用：1</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P007_arm_cmsdk-uart.md#std-dtcompatible-arm-cmsdk-uart"><code>arm,cmsdk-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>板载（On-Board）</td>
<td>ARM PL022串行外设接口（SPI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps3/mps3_common_soc_peripheral.dtsi?plain=1#L70">已启用：3</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P007_arm_pl022.md#std-dtcompatible-arm-pl022"><code>arm,pl022</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8.1-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L25">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P008_ARMv8_1_M_SysTick.md#std-dtcompatible-arm-armv8.1m-systick"><code>arm,armv8.1m-systick</code></a></td>
</tr>
</table>

<a id="serial-port"></a>

### 串口（Serial Port）

MPS3有六路UART。Zephyr控制台默认使用UART0，通过调试USB接口J8引出。

调试USB接口的串口0是主板配置控制器（MCC）的板级控制台。

调试USB接口的串口1连接UART0。

调试USB接口的串口2连接UART1。

调试USB接口的串口3连接UART2。

AN536 Cortex-R52x2子系统提供CPU私有的低延迟外设端口（LLPP）UART0和UART1，以及共享的CMSDK UART。`mps3/an536/cpu0`目标使用LLPP UART0作为Zephyr控制台。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

<a id="flashing"></a>

### 烧录（Flashing）

MPS3提供：


- 连接主机的USB接口，提供大容量存储设备（Mass Storage）、CMSIS-DAP及串口。

<a id="building-an-application-with-an547"></a>

#### 为AN547构建应用（Building an Application）

可按通常方式构建应用。以下以AN547上的[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b mps3/corstone300/an547 samples/hello_world
```

打开串口终端（如minicom或PuTTY），设置如下：


- 速率（Speed）：115200波特率
- 数据位（Data）：8位
- 奇偶校验（Parity）：无（None）
- 停止位（Stop Bits）：1位

复位开发板后，对应串口应显示以下消息：

```text
Hello World! mps3
```

<a id="uploading-an-application-to-mps3-an547"></a>

#### 向MPS3 AN547上传应用（Uploading an Application）

应用可使用ELF、HEX或BIN格式。开发板启动时，从板载Micro SD卡读取文件并烧录二进制程序。主板配置控制器（MCC / Motherboard Configuration Controller）负责加载FPGA镜像及二进制程序。

通过USB端口将MPS3连接到主机，应出现大容量存储设备，默认名称为`V2M-MPS3`。

更新需要三个步骤：


1. 将应用文件复制到`<MPS3 device name>/SOFTWARE/`。
2. 打开`<MPS3 device name>/MB/HBI0309C/AN547/images.txt`。
3. 按以下方式更新`images.txt`文件：

```text
TITLE: Versatile Express Images Configuration File

[IMAGES]
TOTALIMAGES: 1 ;Number of Images (Max: 32)

IMAGE0ADDRESS: 0x01000000 ;Please select the required executable program

IMAGE0FILE: \SOFTWARE\zephyr.elf
```

复位开发板后，对应串口应显示以下消息：

```text
Hello World! mps3
```

<a id="building-and-running-an-application-with-an536"></a>

#### 为AN536构建并运行应用（Building and Running）

可按通常方式构建应用。以下以AN536上的[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b mps3/an536/cpu0 samples/hello_world
```

通过QEMU运行应用：

```text
# From the root of the zephyr repository
west build -b mps3/an536/cpu0 samples/hello_world
west build -t run
```

应看到以下消息：

```text
Hello World! mps3/an536/cpu0
```

更多细节见：


- [MPS3 AN536应用说明（Application Note）](https://developer.arm.com/documentation/dai0536/latest)
- [MPS3 AN547技术参考手册（TRM）](https://developer.arm.com/-/media/Arm%20Developer%20Community/PDF/DAI0547B_SSE300_PLUS_U55_FPGA_for_mps3.pdf)
- [MPS3 AN552技术参考手册（TRM）](https://developer.arm.com/documentation/dai0552/latest)
- [MPS3 AN555技术参考手册（TRM）](https://developer.arm.com/documentation/107642/latest)
- [MPS3 FPGA原型验证板技术参考手册（TRM）](https://developer.arm.com/documentation/100765/latest)
- [Cortex R52技术参考手册（Technical Reference Manual）](https://developer.arm.com/documentation/100026/latest)
- [Cortex M55通用用户指南（Generic User Guide）](https://developer.arm.com/documentation/101051/latest)
- [Cortex M85通用用户指南（Generic User Guide）](https://developer.arm.com/documentation/101924/latest)
- [Corelink SSE-300示例子系统（Example Subsystem）](https://developer.arm.com/documentation/101772/latest)
- [Corelink SSE-310示例子系统（Example Subsystem）](https://developer.arm.com/documentation/102778/latest)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [DAI0547B_SSE300_PLUS_U55_FPGA_for_mps3.pdf](https://developer.arm.com/-/media/Arm%20Developer%20Community/PDF/DAI0547B_SSE300_PLUS_U55_FPGA_for_mps3.pdf)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。
- [latest](https://developer.arm.com/documentation/100026/latest)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。
- [latest](https://developer.arm.com/documentation/100765/latest)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。
- [latest](https://developer.arm.com/documentation/101051/latest)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。
- [latest](https://developer.arm.com/documentation/101772/latest)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。
- [latest](https://developer.arm.com/documentation/101924/latest)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。
- [latest](https://developer.arm.com/documentation/102778/latest)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。
- [latest](https://developer.arm.com/documentation/107642/latest)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。
- [latest](https://developer.arm.com/documentation/dai0536/latest)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。
- [latest](https://developer.arm.com/documentation/dai0552/latest)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。
- [arm-ecosystem-fvps](https://developer.arm.com/tools-and-software/open-source-software/arm-platforms-software/arm-ecosystem-fvps)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。

---

[上一章](P008_ARM_V2M_MPS2_Armv7-m_AN385_AN386_AN500.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P010_MPS4_Corstone_FVP.md)
