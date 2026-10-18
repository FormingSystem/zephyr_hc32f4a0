---
id: learning.zephyr-docs.boards-arm.page-10
title: MPS4 Corstone FVP
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/arm/mps4/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mps4"></a>

# 第10章\_MPS4 Corstone固定虚拟平台（FVP）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/arm/mps4/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`mps4`

厂商（Vendor）：

[Arm公司（ARM Ltd.）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=arm)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

`[corstone315](https://docs.zephyrproject.org/latest/boards/index.html#soc=corstone315), [corstone320](https://docs.zephyrproject.org/latest/boards/index.html#soc=corstone320)`

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/arm/mps4/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

MPS4开发板配置用于运行在MPS4上的Zephyr应用。

[Corstone-315 FVP](https://developer.arm.com/tools-and-software/open-source-software/arm-platforms-software/arm-ecosystem-fvps)及[Corstone-320 FVP](https://developer.arm.com/tools-and-software/open-source-software/arm-platforms-software/arm-ecosystem-fvps)是Arm面向安全SoC的参考子系统，包含Armv8.1-M Cortex-M85处理器、生命周期管理器（LCM）、密钥管理单元（KMU）及安全告警管理器（SAM）IP。Corstone-320 FVP包含Ethos-U85，Corstone-315 FVP包含Ethos-U65神经网络处理器。两者可在Linux和Windows系统免费使用。选择这些FVP进行仿真，是因为它们提供Ethos-U65／Ethos-U85 NPU访问能力，而QEMU及其他仿真平台没有这项能力。

<a id="zephyr-board-options"></a>

### Zephyr开发板选项（Board Options）

<a id="tab-0-0-0"></a>

<a id="tab-0-0-1"></a>

<a id="panel-0-0-0"></a>

**MPS4 Corstone-315固定虚拟平台（FVP）**

MPS4 FVP是采用Cortex-M85架构的SoC。Zephyr支持构建安全及非安全固件。

`BOARD`选项汇总如下：

<table>
<tr>
<th>开发板目标（BOARD）</th>
<th>说明（Description）</th>
</tr>
<tr>
<td><code>mps4/corstone315/fvp</code></td>
<td>构建安全固件，或仅安全态固件（Secure-Only）</td>
</tr>
<tr>
<td><code>mps4/corstone315/fvp/ns</code></td>
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

运行FVP仿真工具前，需要从Arm下载“FVP model for the Corstone-315 MPS4”并安装到主机。

QEMU用法：


- N/A.

<a id="panel-0-0-1"></a>

**MPS4 Corstone-320固定虚拟平台（FVP）**

MPS4 FVP是采用Cortex-M85架构的SoC。Zephyr支持构建安全及非安全固件。

`BOARD`选项汇总如下：

<table>
<tr>
<th>开发板目标（BOARD）</th>
<th>说明（Description）</th>
</tr>
<tr>
<td><code>mps4/corstone320/fvp</code></td>
<td>构建安全固件，或仅安全态固件（Secure-Only）</td>
</tr>
<tr>
<td><code>mps4/corstone320/fvp/ns</code></td>
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

运行FVP仿真工具前，需要从Arm下载“FVP model for the Corstone-320 MPS4”并安装到主机。原文记录使用11.27.25版本（2024年9月24日）测试。

QEMU用法：


- N/A.

注意（Note）


- 开发板限定符（Board Qualifier）必须包含上述变体名称，缺少变体名称的`mps4/corstone315/`或`mps4/corstone320`不是有效限定符。
- `mps4/corstone315/fvp/ns/`及`mps4/corstone320/fvp/ns`变体需要最新上游TF-M版本，因为原文所述Zephyr当前使用的TF-M尚不支持Corstone-315 FVP。

<a id="hardware"></a>

## 硬件（Hardware）

尚无可用硬件（H/W），目前仅支持ARMFVP仿真的开发板变体。

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`mps4`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="mps4-hw-features"></a>

<a id="mps4-mps4/corstone315/fvp-hw-features-section"></a>

#### `mps4/corstone315/fvp`目标（Target）

<a id="mps4-mps4/corstone315/fvp-hw-features-panel"></a>

<a id="mps4-mps4/corstone315/fvp-hw-features-memory"></a>

该开发板目标的片上存储容量：2 MiB RAM、4 MiB Flash。

<a id="mps4-mps4/corstone315/fvp-hw-features-table"></a>

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
<td>ARM Cortex-M85处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_corstone315_fvp.dts?plain=1#L28">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P006_arm_cortex-m85.md#std-dtcompatible-arm-cortex-m85"><code>arm,cortex-m85</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>板载（On-Board）</td>
<td>Arm Ethos-U是一种微型神经网络处理单元（Micro NPU），可在嵌入式设备上对神经网络进行硬件加速（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_corstone315_fvp.dts?plain=1#L47">已启用：1</a>）</td>
<td><a href="../arm_timing_ethosu_control_binding_reference/P004_arm_ethos-u.md#std-dtcompatible-arm-ethos-u"><code>arm,ethos-u</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L7">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">以太网（Ethernet）</td>
<td>板载（On-Board）</td>
<td>SMSC（现属Microchip）LAN9220以太网控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L45">已启用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P003_smsc_lan9220.md#std-dtcompatible-smsc-lan9220"><code>smsc,lan9220</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>板载（On-Board）</td>
<td>ARM CMSDK通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L13">已启用：4</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P027_arm_cmsdk-gpio.md#std-dtcompatible-arm-cmsdk-gpio"><code>arm,cmsdk-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ARM 32位内存映射输入输出GPIO（MMIO32 GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L131">已启用：3</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P028_arm_mmio32-gpio.md#std-dtcompatible-arm-mmio32-gpio"><code>arm,mmio32-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>板载（On-Board）</td>
<td>ARM SBCon双线串行总线接口（Two-Wire Serial Bus Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L53">已启用：5</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P006_arm_versatile-i2c.md#std-dtcompatible-arm-versatile-i2c"><code>arm,versatile-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common.dtsi?plain=1#L77">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common.dtsi?plain=1#L23">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>板载（On-Board）</td>
<td>ARMv8.1-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_corstone315_fvp.dts?plain=1#L35">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P006_arm_armv8.1m-mpu.md#std-dtcompatible-arm-armv8.1m-mpu"><code>arm,armv8.1m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>板载（On-Board）</td>
<td>Arm MPS4引脚控制器节点负责选择引脚功能及属性，例如将UART3 TX路由到引脚1（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L215">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P010_arm_mps4-pinctrl.md#std-dtcompatible-arm-mps4-pinctrl"><code>arm,mps4-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>板载（On-Board）</td>
<td>ARM CMSDK通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L156">已启用：5</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L205">已禁用：1</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P007_arm_cmsdk-uart.md#std-dtcompatible-arm-cmsdk-uart"><code>arm,cmsdk-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>板载（On-Board）</td>
<td>ARM PL022串行外设接口（SPI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L69">已启用：3</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P007_arm_pl022.md#std-dtcompatible-arm-pl022"><code>arm,pl022</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8.1-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L25">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P008_ARMv8_1_M_SysTick.md#std-dtcompatible-arm-armv8.1m-systick"><code>arm,armv8.1m-systick</code></a></td>
</tr>
</table>

<a id="mps4-mps4/corstone320/fvp-hw-features-section"></a>

#### `mps4/corstone320/fvp`目标（Target）

<a id="mps4-mps4/corstone320/fvp-hw-features-panel"></a>

<a id="mps4-mps4/corstone320/fvp-hw-features-memory"></a>

该开发板目标的片上存储容量：2 MiB RAM、4 MiB Flash。

<a id="mps4-mps4/corstone320/fvp-hw-features-table"></a>

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
<td>ARM Cortex-M85处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_corstone320_fvp.dts?plain=1#L28">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P006_arm_cortex-m85.md#std-dtcompatible-arm-cortex-m85"><code>arm,cortex-m85</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>板载（On-Board）</td>
<td>Arm Ethos-U是一种微型神经网络处理单元（Micro NPU），可在嵌入式设备上对神经网络进行硬件加速（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_corstone320_fvp.dts?plain=1#L47">已启用：1</a>）</td>
<td><a href="../arm_timing_ethosu_control_binding_reference/P004_arm_ethos-u.md#std-dtcompatible-arm-ethos-u"><code>arm,ethos-u</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L7">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">以太网（Ethernet）</td>
<td>板载（On-Board）</td>
<td>SMSC（现属Microchip）LAN9220以太网控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L45">已启用：1</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P003_smsc_lan9220.md#std-dtcompatible-smsc-lan9220"><code>smsc,lan9220</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>板载（On-Board）</td>
<td>ARM CMSDK通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L13">已启用：4</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P027_arm_cmsdk-gpio.md#std-dtcompatible-arm-cmsdk-gpio"><code>arm,cmsdk-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>ARM 32位内存映射输入输出GPIO（MMIO32 GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L131">已启用：3</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P028_arm_mmio32-gpio.md#std-dtcompatible-arm-mmio32-gpio"><code>arm,mmio32-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>板载（On-Board）</td>
<td>ARM SBCon双线串行总线接口（Two-Wire Serial Bus Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L53">已启用：5</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P006_arm_versatile-i2c.md#std-dtcompatible-arm-versatile-i2c"><code>arm,versatile-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common.dtsi?plain=1#L77">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common.dtsi?plain=1#L23">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>板载（On-Board）</td>
<td>ARMv8.1-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_corstone320_fvp.dts?plain=1#L35">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P006_arm_armv8.1m-mpu.md#std-dtcompatible-arm-armv8.1m-mpu"><code>arm,armv8.1m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>板载（On-Board）</td>
<td>Arm MPS4引脚控制器节点负责选择引脚功能及属性，例如将UART3 TX路由到引脚1（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L215">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P010_arm_mps4-pinctrl.md#std-dtcompatible-arm-mps4-pinctrl"><code>arm,mps4-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>板载（On-Board）</td>
<td>ARM CMSDK通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L156">已启用：5</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L205">已禁用：1</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P007_arm_cmsdk-uart.md#std-dtcompatible-arm-cmsdk-uart"><code>arm,cmsdk-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>板载（On-Board）</td>
<td>ARM PL022串行外设接口（SPI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps4/mps4_common_soc_peripheral.dtsi?plain=1#L69">已启用：3</a>）</td>
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

MPS4有六路UART，Zephyr控制台默认使用UART0。

调试USB接口的串口0是主板配置控制器（MCC）的板级控制台。

调试USB接口的串口1连接UART0。

调试USB接口的串口2连接UART1。

调试USB接口的串口3连接UART2。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

<a id="flashing"></a>

### 烧录（Flashing）


- 不适用（N/A），因为当前仅支持FVP。

<a id="building-an-application-with-corstone-315"></a>

#### 为Corstone-315构建应用

可按通常方式构建应用。以下以Corstone-315上的[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b mps4/corstone315/fvp samples/hello_world
west build -t run
```

使用FVP运行后，应看到以下消息：

```text
Hello World! mps4
```

<a id="building-an-application-with-corstone-320"></a>

#### 为Corstone-320构建应用

可按通常方式构建应用。以下以Corstone-320上的[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b mps4/corstone320/fvp samples/hello_world
west build -t run
```

使用FVP运行后，应看到以下消息：

```text
Hello World! mps4
```

更多细节见：


- [Corstone SSE-315参考指南（Reference Guide）](https://developer.arm.com/documentation/109395/0000)
- [Corstone SSE-320参考指南（Reference Guide）](https://developer.arm.com/documentation/109760/0000/)
- [Cortex M85通用用户指南（Generic User Guide）](https://developer.arm.com/documentation/101924/latest)
- [Arm Corstone-320参考包技术概述（Reference Package Technical Overview）](https://developer.arm.com/documentation/109761/0000/)
- [Arm MPS4 FPGA原型验证板技术参考手册](https://developer.arm.com/documentation/102577/0000/)

## 译注

原文分别描述Corstone-315与Corstone-320变体，并指出非安全变体需要较新的上游TF-M；此限制反映本页来源快照，不表示所有Zephyr内置TF-M版本均可直接运行。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [latest](https://developer.arm.com/documentation/101924/latest)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。
- [](https://developer.arm.com/documentation/102577/0000/)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。
- [0000](https://developer.arm.com/documentation/109395/0000)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。
- [](https://developer.arm.com/documentation/109760/0000/)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。
- [](https://developer.arm.com/documentation/109761/0000/)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。
- [arm-ecosystem-fvps](https://developer.arm.com/tools-and-software/open-source-software/arm-platforms-software/arm-ecosystem-fvps)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。

---

[上一章](P009_MPS3_FPGA_Corstone_FVP.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P011_V2M_Beetle.md)
