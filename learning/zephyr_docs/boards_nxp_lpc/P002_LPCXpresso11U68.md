---
id: learning.zephyr-docs.boards-nxp-lpc.page-2
title: LPCXpresso11U68
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/nxp/lpcxpresso11u68/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="lpcxpresso11u68"></a>

# 第2章\_LPCXpresso11U68

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/nxp/lpcxpresso11u68/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/lpcxpresso11u68.jpg](images/lpcxpresso11u68.jpg)](images/lpcxpresso11u68.jpg)

LPCXpresso11U68

名称（Name）：

`lpcxpresso11u68`

厂商（Vendor）：

[恩智浦半导体（NXP Semiconductors）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=nxp)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[lpc11u68](https://docs.zephyrproject.org/latest/boards/index.html#soc=lpc11u68)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/lpcxpresso11u68/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

LPCXpresso11U68开发板采用基于Arm Cortex-M0+内核的NXP LPC11U68 MCU。

<a id="hardware"></a>

## 硬件（Hardware）

LPCXpresso11U68提供以下硬件：


- 采用100引脚低矮四方扁平封装（LQFP100）的LPC11U68微控制器
- Arm Cortex-M0+处理器
- 存储器（Memory）：


  - 256 KB闪存
  - 32 KB SRAM
  - 额外两块2 KB SRAM
  - 4 KB电可擦可编程只读存储器（EEPROM）
- 通用串行总线（USB）：


  - USB 2.0全速设备控制器（Full-speed Device Controller）
- DMA控制器
- 5路USART
- 2路I2C总线
- 2路支持DMA的同步串行端口（SSP）
- 开发板供电：USB总线或外部3 V／5 V电源
- 兼容Arduino UNO平台的Arduino连接器
- 三色用户LED、电源指示LED及复位LED
- 3个按键：目标复位、ISP及用户按键

更多信息见以下资料：


- [LPC11UXX SoC网站](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc1100-cortex-m0-plus-m0/scalable-entry-level-32-bit-microcontroller-mcu-based-on-arm-cortex-m0-plus-and-cortex-m0-cores:LPC11U00)
- [LPC11U6X 数据手册（Datasheet）](https://www.nxp.com/docs/en/data-sheet/LPC11U6X.pdf)
- [LPC11U6X 参考手册（Reference Manual）](https://www.nxp.com/webapp/Download?colCode=UM10732)
- [LPCXPRESSO11U68 网站](https://www.nxp.com/design/microcontrollers-developer-resources/lpc-microcontroller-utilities/lpcxpresso-board-for-lpc11u68:OM13058)
- [LPCXPRESSO11U68 原理图（Schematics）](https://www.nxp.com/downloads/en/schematics/LPC11U68_Xpresso_v2_Schematic_RevC_1.pdf)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`lpcxpresso11u68`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="lpcxpresso11u68-hw-features"></a>

<a id="lpcxpresso11u68-lpcxpresso11u68/lpc11u68-hw-features-section"></a>

#### `lpcxpresso11u68/lpc11u68`目标（Target）

<a id="lpcxpresso11u68-lpcxpresso11u68/lpc11u68-hw-features-panel"></a>

<a id="lpcxpresso11u68-lpcxpresso11u68/lpc11u68-hw-features-memory"></a>

该开发板目标的片上存储容量：32 KiB RAM、256 KiB Flash。

<a id="lpcxpresso11u68-lpcxpresso11u68/lpc11u68-hw-features-table"></a>

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
<td>ARM Cortex-M0+处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc11u6x/nxp_lpc11u6x.dtsi?plain=1#L17">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P017_arm_cortex-m0+.md#std-dtcompatible-arm-cortex-m0"><code>arm,cortex-m0+</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>LPC11U6X时钟控制器节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc11u6x/nxp_lpc11u6x.dtsi?plain=1#L136">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P008_nxp_lpc11u6x-syscon.md#std-dtcompatible-nxp-lpc11u6x-syscon"><code>nxp,lpc11u6x-syscon</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC11U6X通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc11u6x/nxp_lpc11u6x.dtsi?plain=1#L86">已启用：3</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P007_nxp_lpc11u6x-gpio.md#std-dtcompatible-nxp-lpc11u6x-gpio"><code>nxp,lpc11u6x-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>引出到Arduino Uno R3排针（Headers）的GPIO引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/lpcxpresso11u68/lpcxpresso11u68.dts?plain=1#L70">已启用：1</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P023_arduino-header-r3.md#std-dtcompatible-arduino-header-r3"><code>arduino-header-r3</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>LPC11U6X I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc11u6x/nxp_lpc11u6x.dtsi?plain=1#L182">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc11u6x/nxp_lpc11u6x.dtsi?plain=1#L192">已禁用：1</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P004_nxp_lpc11u6x-i2c.md#std-dtcompatible-nxp-lpc11u6x-i2c"><code>nxp,lpc11u6x-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/lpcxpresso11u68/lpcxpresso11u68.dts?plain=1#L35">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P001_ARMv6_M_NVIC.md#std-dtcompatible-arm-v6m-nvic"><code>arm,v6m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/lpcxpresso11u68/lpcxpresso11u68.dts?plain=1#L51">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="2">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc11u6x/nxp_lpc11u6x.dtsi?plain=1#L40">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP LPC11U6X片上EEPROM节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc11u6x/nxp_lpc11u6x.dtsi?plain=1#L45">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P001_nxp_lpc11u6x-eeprom.md#std-dtcompatible-nxp-lpc11u6x-eeprom"><code>nxp,lpc11u6x-eeprom</code></a></td>
</tr>
<tr>
<td rowspan="3">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>LPC I/O引脚配置（IOCON）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc11u6x/nxp_lpc11u6x.dtsi?plain=1#L55">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P007_nxp_lpc-iocon.md#std-dtcompatible-nxp-lpc-iocon"><code>nxp,lpc-iocon</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>LPC引脚控制（Pinctrl）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc11u6x/nxp_lpc11u6x.dtsi?plain=1#L62">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P008_nxp_lpc11u6x-pinctrl.md#std-dtcompatible-nxp-lpc11u6x-pinctrl"><code>nxp,lpc11u6x-pinctrl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>LPC输入输出引脚配置（IOCON）的端口输入输出（PIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc11u6x/nxp_lpc11u6x.dtsi?plain=1#L67">已启用：3</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P006_nxp_lpc-iocon-pio.md#std-dtcompatible-nxp-lpc-iocon-pio"><code>nxp,lpc-iocon-pio</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>LPC11U6X通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc11u6x/nxp_lpc11u6x.dtsi?plain=1#L142">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc11u6x/nxp_lpc11u6x.dtsi?plain=1#L150">已禁用：3</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P015_nxp_lpc11u6x-uart.md#std-dtcompatible-nxp-lpc11u6x-uart"><code>nxp,lpc11u6x-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc11u6x/nxp_lpc11u6x.dtsi?plain=1#L23">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P005_ARMv6_M_SysTick.md#std-dtcompatible-arm-armv6m-systick"><code>arm,armv6m-systick</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

可通过IOCON控制器配置LPC11U68引脚。

<table>
<tr>
<th>名称（Name）</th>
<th>功能（Function）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>PIO2_11</td>
<td>通用异步收发器（UART）</td>
<td>USART接收（RX）</td>
</tr>
<tr>
<td>PIO2_12</td>
<td>通用异步收发器（UART）</td>
<td>USART发送（TX）</td>
</tr>
<tr>
<td>PIO2_16</td>
<td>通用输入输出（GPIO）</td>
<td>绿色LED（GREEN LED）</td>
</tr>
<tr>
<td>PIO2_17</td>
<td>通用输入输出（GPIO）</td>
<td>红色LED（RED LED）</td>
</tr>
<tr>
<td>PIO2_18</td>
<td>通用输入输出（GPIO）</td>
<td>BLUE_LED</td>
</tr>
<tr>
<td>PIO0_4</td>
<td>集成电路间总线（I2C）</td>
<td>I2C串行时钟（SCL）</td>
</tr>
<tr>
<td>PIO0_5</td>
<td>集成电路间总线（I2C）</td>
<td>I2C串行数据（SDA）</td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`lpcxpresso11u68`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-openocd">openocd</a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

<a id="flashing"></a>

### 烧录（Flashing）

LPCXpresso11U68可使用板载LPC-Link2调试探针烧录，探针基于NXP LPC43xx MCU。它根据所烧录的固件提供CMSIS-DAP或J-Link接口。默认OpenOCD配置支持CMSIS-DAP；若要切换至J-Link，需编辑[boards/nxp/lpcxpresso11u68/support/openocd.cfg](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/lpcxpresso11u68/support/openocd.cfg)，将以下内容替换：

```text
source [find interface/cmsis-dap.cfg]
```

替换为：

```text
source [find interface/jlink.cfg]
```

注意（Note）

可使用[LPCScrypt工具](https://www.nxp.com/design/microcontrollers-developer-resources/lpc-microcontroller-utilities/lpcscrypt-v2-1-1:LPCSCRYPT)更新LPC-Link2固件。

注意（Note）

[Mbed项目](https://os.mbed.com)也在此处提供固件镜像；除CMSIS-DAP接口外，这些固件还通过模拟USB磁盘提供便捷的更新机制。（[here](https://os.mbed.com/teams/NXP/wiki/Updating-LPCXpresso-firmware)）

把已构建固件写入LPCXpresso11U68的步骤如下：


1. 将“Link”Micro-B USB端口连接主机。
2. 随后运行west flash命令。

<a id="debugging"></a>

### 调试（Debugging）

请参考[烧录（Flashing）](#flashing)一节，并将`west flash`替换为`west debug`执行调试。

<a id="references"></a>

## 参考资料（References）


- [LPC11UXX SoC网站](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc1100-cortex-m0-plus-m0/scalable-entry-level-32-bit-microcontroller-mcu-based-on-arm-cortex-m0-plus-and-cortex-m0-cores:LPC11U00)
- [LPC11U6X 数据手册（Datasheet）](https://www.nxp.com/docs/en/data-sheet/LPC11U6X.pdf)
- [LPC11U6X 参考手册（Reference Manual）](https://www.nxp.com/webapp/Download?colCode=UM10732)
- [LPCXPRESSO11U68 网站](https://www.nxp.com/design/microcontrollers-developer-resources/lpc-microcontroller-utilities/lpcxpresso-board-for-lpc11u68:OM13058)
- [LPCXPRESSO11U68 原理图（Schematics）](https://www.nxp.com/downloads/en/schematics/LPC11U68_Xpresso_v2_Schematic_RevC_1.pdf)

<a id="support-resources-for-zephyr"></a>

### Zephyr支持资源（Support Resources）


- [NXP开发板支持状态（Board Support Status）](https://github.com/nxp-zephyr/nxp-zsdk/blob/main/doc/releases/Board-Support-Status.md)
- [NXP Zephyr下游软件开发工具包（Downstream SDK）](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code文档](https://mcuxpresso.nxp.com/mcux-vscode)及[Zephyr实验指南](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)
- [NXP Zephyr知识中心（Knowledge Hub）](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- NXP Zephyr主页，包含培训资源（[NXP的Zephyr专题页面](https://nxp.com/zephyr)）
- [NXP Zephyr支持社区论坛（Support Community）](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)：HTTP Error 403: Forbidden。
- [Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)：HTTP Error 403: Forbidden。
- [Training-Zephyr-Getting-Started.html](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)：HTTP Error 404: Not Found。
- [zephyr](https://nxp.com/zephyr)：HTTP Error 404: Not Found。
- [lpcscrypt-v2-1-1:LPCSCRYPT](https://www.nxp.com/design/microcontrollers-developer-resources/lpc-microcontroller-utilities/lpcscrypt-v2-1-1:LPCSCRYPT)：HTTP Error 404: Not Found。
- [lpcxpresso-board-for-lpc11u68:OM13058](https://www.nxp.com/design/microcontrollers-developer-resources/lpc-microcontroller-utilities/lpcxpresso-board-for-lpc11u68:OM13058)：HTTP Error 404: Not Found。
- [LPC11U6X.pdf](https://www.nxp.com/docs/en/data-sheet/LPC11U6X.pdf)：HTTP Error 404: Not Found。
- [LPC11U68_Xpresso_v2_Schematic_RevC_1.pdf](https://www.nxp.com/downloads/en/schematics/LPC11U68_Xpresso_v2_Schematic_RevC_1.pdf)：HTTP Error 404: Not Found。
- [scalable-entry-level-32-bit-microcontroller-mcu-based-on-arm-cortex-m0-plus-and-cortex-m0-cores:LPC11U00](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc1100-cortex-m0-plus-m0/scalable-entry-level-32-bit-microcontroller-mcu-based-on-arm-cortex-m0-plus-and-cortex-m0-cores:LPC11U00)：HTTP Error 404: Not Found。
- [Download?colCode=UM10732](https://www.nxp.com/webapp/Download?colCode=UM10732)：HTTP Error 404: Not Found。

---

[上一章](P001_LPC845-BRK.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P003_LPCXPRESSO51U68.md)
