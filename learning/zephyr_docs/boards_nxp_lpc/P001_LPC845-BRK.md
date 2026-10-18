---
id: learning.zephyr-docs.boards-nxp-lpc.page-1
title: LPC845-BRK
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/nxp/lpc845brk/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="lpc845brk"></a>

# 第1章\_LPC845-BRK

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/nxp/lpc845brk/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/lpc845brk.webp](images/lpc845brk.webp)](images/lpc845brk.webp)

LPC845-BRK

名称（Name）：

`lpc845brk`

厂商（Vendor）：

[恩智浦半导体（NXP Semiconductors）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=nxp)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[lpc845](https://docs.zephyrproject.org/latest/boards/index.html#soc=lpc845)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/lpc845brk/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

NXP开发的LPC845引出板（Breakout Board）用于LPC84x微控制器系列的快速评估与原型开发。

LPC84x是基于Arm Cortex-M0+架构的低成本32位MCU系列，CPU最高30 MHz，最多支持64 KB闪存及16 KB SRAM，并通过开关矩阵（Switch Matrix）提供灵活的外设配置。

<a id="hardware"></a>

## 硬件（Hardware）

LPC845-BRK基于NXP LPC845 MCU，提供以下功能：


- Arm Cortex-M0+处理器，最高30 MHz
- 64 KB片上闪存及16 KB SRAM
- 提供多种频率选项的内部自由运行振荡器（FRO）
- 5路USART，支持开关矩阵路由及分数波特率（Fractional Baud Rate）
- 2路SPI控制器，支持开关矩阵路由
- 4路I2C，其中一路支持1 Mbit/s快速模式增强版（Fast-mode Plus）
- 一个12位模数转换器（ADC）及两个10位数模转换器（DAC）
- 状态可配置定时器／脉宽调制（SCTimer/PWM）及多个通用定时器
- 25通道直接存储器访问（DMA）控制器及循环冗余校验（CRC）引擎
- 最多54个GPIO，支持灵活的开关矩阵配置
- 最多8个引脚，即8个IRQ槽位，支持引脚中断及模式匹配引擎（Pattern Match Engine）
- 串行线调试（SWD）接口
- 电容触摸接口（Capacitive Touch Interface）

`lpc845brk`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="lpc845brk-hw-features"></a>

<a id="lpc845brk-lpc845brk/lpc845-hw-features-section"></a>

### `lpc845brk/lpc845`目标（Target）

<a id="lpc845brk-lpc845brk/lpc845-hw-features-panel"></a>

<a id="lpc845brk-lpc845brk/lpc845-hw-features-memory"></a>

该开发板目标的片上存储容量：16 KiB RAM、64 KiB Flash。

<a id="lpc845brk-lpc845brk/lpc845-hw-features-table"></a>

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
<td>ARM Cortex-M0+处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc84x/nxp_lpc84x.dtsi?plain=1#L16">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P017_arm_cortex-m0+.md#std-dtcompatible-arm-cortex-m0"><code>arm,cortex-m0+</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC84x时钟控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc84x/nxp_lpc84x.dtsi?plain=1#L57">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P009_nxp_lpc84x-clock.md#std-dtcompatible-nxp-lpc84x-clock"><code>nxp,lpc84x-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC84x片上闪存控制器，使用ROM在应用编程（IAP）及闪存控制器（FMC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc84x/nxp_lpc84x.dtsi?plain=1#L36">已启用：1</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P013_nxp_iap-fmc84x.md#std-dtcompatible-nxp-iap-fmc84x"><code>nxp,iap-fmc84x</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P001_ARMv6_M_NVIC.md#std-dtcompatible-arm-v6m-nvic"><code>arm,v6m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc84x/nxp_lpc84x.dtsi?plain=1#L46">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC84x开关矩阵（SWM）引脚控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc84x/nxp_lpc84x.dtsi?plain=1#L66">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P010_nxp_lpc84x-swm.md#std-dtcompatible-nxp-lpc84x-swm"><code>nxp,lpc84x-swm</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP LPC84x输入输出配置（IOCON）引脚控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc84x/nxp_lpc84x.dtsi?plain=1#L73">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P009_nxp_lpc84x-iocon.md#std-dtcompatible-nxp-lpc84x-iocon"><code>nxp,lpc84x-iocon</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC84x通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc84x/nxp_lpc84x.dtsi?plain=1#L80">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc84x/nxp_lpc84x.dtsi?plain=1#L88">已禁用：4</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P016_nxp_lpc84x-uart.md#std-dtcompatible-nxp-lpc84x-uart"><code>nxp,lpc84x-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/lpc/lpc84x/nxp_lpc84x.dtsi?plain=1#L27">已启用：1</a>）</td>
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

LPC845通过开关矩阵（SWM）及IOCON模块配置引脚功能。

默认引脚配置如下：

<table>
<tr>
<th>名称（Name）</th>
<th>功能（Function）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>PIO0_24</td>
<td>UART0发送数据（TXD）</td>
<td>控制台发送（Console TX）</td>
</tr>
<tr>
<td>PIO0_25</td>
<td>UART0接收数据（RXD）</td>
<td>控制台接收（Console RX）</td>
</tr>
<tr>
<td>PIO1_0</td>
<td>通用输入输出（GPIO）</td>
<td>绿色LED（GREEN LED）</td>
</tr>
<tr>
<td>PIO1_1</td>
<td>通用输入输出（GPIO）</td>
<td>蓝色LED（BLUE LED）</td>
</tr>
<tr>
<td>PIO1_2</td>
<td>通用输入输出（GPIO）</td>
<td>红色LED（RED LED）</td>
</tr>
<tr>
<td>PIO0_11</td>
<td>集成电路间总线（I2C）</td>
<td>I2C0串行数据（SDA）</td>
</tr>
<tr>
<td>PIO0_10</td>
<td>集成电路间总线（I2C）</td>
<td>I2C0串行时钟（SCL）</td>
</tr>
<tr>
<td>PIO0_31</td>
<td>CAPT</td>
<td>CAPT_X0</td>
</tr>
<tr>
<td>PIO1_8</td>
<td>CAPT</td>
<td>CAPT_YL</td>
</tr>
<tr>
<td>PIO1_9</td>
<td>CAPT</td>
<td>CAPT_YH</td>
</tr>
<tr>
<td>PIO0_2</td>
<td>SWD</td>
<td>SWD调试端口</td>
</tr>
<tr>
<td>PIO0_3</td>
<td>SWD</td>
<td>SWD调试端口</td>
</tr>
<tr>
<td>PIO0_4</td>
<td>通用输入输出（GPIO）</td>
<td>用户开关（User SW）</td>
</tr>
<tr>
<td>PIO0_5</td>
<td>通用输入输出（GPIO）</td>
<td>复位开关（Reset SW）</td>
</tr>
<tr>
<td>PIO0_7</td>
<td>模数转换器（ADC）</td>
<td>电位器（Potentiometer）</td>
</tr>
<tr>
<td>PIO0_12</td>
<td>通用输入输出（GPIO）</td>
<td>ISP启动开关（ISP Booting SW）</td>
</tr>
</table>

注意（Note）

LPC845开关矩阵提供高度灵活的引脚路由。上表列出默认及固定引脚连接；SPI、PWM、USART等可移动功能可通过设备树配置，路由到几乎任意可用GPIO引脚。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`lpc845brk`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
<th>连接调试会话（attach）</th>
<th>实时传输（rtt）</th>
<th>复位（reset）</th>
<th>调试服务器（debugserver）</th>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-pyocd">pyocd</a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

<a id="building"></a>

### 构建（Building）

以下以构建[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)示例应用为例。

```text
# From the root of the zephyr repository
west build -b lpc845brk samples/hello_world
```

<a id="flashing"></a>

### 烧录（Flashing）

构建完成后，可使用以下命令烧录：

```text
west flash
```

<a id="debugging"></a>

### 调试（Debugging）

使用以下命令调试应用：

```text
west debug
```

<a id="references"></a>

## 参考资料（References）


- [NXP LPC845引出板网站](https://www.nxp.com/design/design-center/development-boards-and-designs/LPC845-BRK)
- [LPC84X数据手册（Data Sheet）](https://www.nxp.com/docs/en/data-sheet/LPC84x.pdf)
- [LPC845 BRK用户手册（User Manual）](https://community.nxp.com/pwmxy87654/attachments/pwmxy87654/lpc/35244/1/UM11181.pdf)

<a id="support-resources-for-zephyr"></a>

### Zephyr支持资源（Support Resources）


- [NXP开发板支持状态（Board Support Status）](https://github.com/nxp-zephyr/nxp-zsdk/blob/main/doc/releases/Board-Support-Status.md)
- [NXP Zephyr下游软件开发工具包（Downstream SDK）](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code文档](https://mcuxpresso.nxp.com/mcux-vscode)及[Zephyr实验指南](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)
- [NXP Zephyr知识中心（Knowledge Hub）](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- NXP Zephyr主页，包含培训资源（[NXP的Zephyr专题页面](https://nxp.com/zephyr)）
- [NXP Zephyr支持社区论坛（Support Community）](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

## 译注

保留官方lpc845brk.webp原件。文件末尾存在1字节换行，重复下载的SHA-256完全一致，RIFF数据块及664×187图像均可完整解码；未裁剪或重编码。SWM可移动功能与固定引脚连接按原文区分。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)：HTTP Error 403: Forbidden。
- [Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)：HTTP Error 403: Forbidden。
- [Training-Zephyr-Getting-Started.html](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)：HTTP Error 404: Not Found。
- [zephyr](https://nxp.com/zephyr)：HTTP Error 404: Not Found。
- [LPC845-BRK](https://www.nxp.com/design/design-center/development-boards-and-designs/LPC845-BRK)：HTTP Error 404: Not Found。
- [LPC84x.pdf](https://www.nxp.com/docs/en/data-sheet/LPC84x.pdf)：HTTP Error 404: Not Found。

---

[返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P002_LPCXpresso11U68.md)
