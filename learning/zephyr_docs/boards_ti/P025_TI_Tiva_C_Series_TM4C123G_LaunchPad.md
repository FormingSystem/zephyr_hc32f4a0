---
id: learning.zephyr-docs.boards-ti.page-25
title: TI Tiva C Series TM4C123G LaunchPad
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/ti/tm4c123gxl/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="tm4c123gxl"></a>

# 第25章\_TI Tiva C系列TM4C123G LaunchPad

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/ti/tm4c123gxl/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/tm4c123gxl.webp](images/tm4c123gxl.webp)](images/tm4c123gxl.webp)

TI Tiva C系列TM4C123G LaunchPad

名称（Name）：

`tm4c123gxl`

厂商（Vendor）：

[德州仪器（Texas Instruments）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=ti)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[ti_tm4c123gh6pm](https://docs.zephyrproject.org/latest/boards/index.html#soc=ti_tm4c123gh6pm)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ti/tm4c123gxl/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

TM4C123GXL LaunchPad评估套件是用于TI Tiva C系列TM4C123GH6PM微控制器的低成本开发平台，采用80 MHz高性能Arm Cortex-M4F核，具有256 KB闪存及32 KB SRAM。

TM4C123GH6PM微控制器包含：


- 处理器核（Core）


  - 80 MHz Arm Cortex-M4F，带浮点单元（FPU）
  - 嵌套向量中断控制器（NVIC）
  - 存储器保护单元（MPU）
- 存储器（Memory）


  - 256 KB单周期访问闪存，最高40 MHz
  - 32 KB单周期访问SRAM
  - 2 KB电可擦除可编程只读存储器（EEPROM）
- 通信接口（Communication）


  - 八路UART
  - 四个同步串行接口／SPI模块（SSI/SPI）
  - 四个I2C模块
  - 两个CAN 2.0 A／B控制器
  - USB 2.0 OTG／主机／设备，全速（Full-speed）
- 定时器（Timers）


  - 原文列六个64位通用定时器，也可作为十二个32位定时器
  - 六个宽定时器（Wide Timer）
  - 两个看门狗定时器
- 其他（Other）


  - 16路PWM输出
  - 带锁相环（PLL）的系统控制及时钟

![官方原图：TM4C123GXL LaunchPad development board](images/tm4c123gxl1.webp)

<a id="hardware"></a>

## 硬件（Hardware）

TM4C123GXL LaunchPad具有：


- 板载在线调试接口（In-Circuit Debug Interface，ICDI），用于编程及调试
- USB Micro-B连接器，用于调试及供电
- 两个用户开关：SW1接PF4，SW2接PF0
- RGB LED：红色接PF1，蓝色接PF2，绿色接PF3
- 复位开关
- 兼容BoosterPack的排针，引出多数微控制器引脚

TM4C123GXL LaunchPad详情见[TI TM4C123GXL产品页](https://www.ti.com/tool/EK-TM4C123GXL)。

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`tm4c123gxl`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="tm4c123gxl-hw-features"></a>

<a id="tm4c123gxl-tm4c123gxl/ti_tm4c123gh6pm-hw-features-section"></a>

#### `tm4c123gxl/ti_tm4c123gh6pm`目标（Target）

<a id="tm4c123gxl-tm4c123gxl/ti_tm4c123gh6pm-hw-features-panel"></a>

<a id="tm4c123gxl-tm4c123gxl/ti_tm4c123gh6pm-hw-features-memory"></a>

该开发板目标的片上存储容量：32 KiB RAM、256 KiB Flash。

<a id="tm4c123gxl-tm4c123gxl/ti_tm4c123gh6pm-hw-features-table"></a>

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
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/tm4c123gh6pm.dtsi?plain=1#L22">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/tm4c123gh6pm.dtsi?plain=1#L34">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>TI Stellaris闪存控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/tm4c123gh6pm.dtsi?plain=1#L46">已启用：1</a>）</td>
<td><a href="../flash_renesas_st_ti_binding_reference/P033_ti_stellaris-flash-controller.md#std-dtcompatible-ti-stellaris-flash-controller"><code>ti,stellaris-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/tm4c123gh6pm.dtsi?plain=1#L53">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>TI Tiva C系列引脚控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/tm4c123gh6pm.dtsi?plain=1#L41">已启用：1</a>）</td>
<td><a href="../pinctrl_stm32_ti_xilinx_binding_reference/P015_ti_tiva-c-pinctrl.md#std-dtcompatible-ti-tiva-c-pinctrl"><code>ti,tiva-c-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>TI Tiva C系列UART（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/tm4c123gh6pm.dtsi?plain=1#L64">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/tm4c123gh6pm.dtsi?plain=1#L82">已禁用：6</a>）</td>
<td><a href="../uart_ti_wch_virtual_binding_reference/P004_ti_tiva-c-uart.md#std-dtcompatible-ti-tiva-c-uart"><code>ti,tiva-c-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/tm4c123gh6pm.dtsi?plain=1#L29">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

<a id="uart"></a>

#### 通用异步收发器（UART）

TM4C123GXL具有8个UART模块，UART0通过PA0（RX）及PA1（TX）连接板载ICDI虚拟COM端口。

<table>
<tr>
<th>通用异步收发器（UART）</th>
<th>接收引脚（RX Pin）</th>
<th>发送引脚（TX Pin）</th>
</tr>
<tr>
<td>UART0</td>
<td>PA0</td>
<td>PA1</td>
</tr>
<tr>
<td>UART1</td>
<td>PB0</td>
<td>PB1</td>
</tr>
</table>

<a id="building-and-flashing"></a>

## 构建与烧录（Building and Flashing）

<a id="building"></a>

### 构建（Building）

Zephyr应用开发请遵循[入门指南](../getting_started/P002_入门指南.md#getting-started)。

例如，为TM4C123GXL LaunchPad构建Hello World应用：

```text
# From the root of the zephyr repository
west build -b tm4c123gxl samples/hello_world
```

<a id="flashing"></a>

### 烧录（Flashing）

TM4C123GXL通过板载TI ICDI接口及OpenOCD烧录。

```text
# From the root of the zephyr repository
west build -b tm4c123gxl samples/hello_world
west flash
```

<a id="debugging"></a>

### 调试（Debugging）

```text
# From the root of the zephyr repository
west build -b tm4c123gxl samples/hello_world
west debug
```

<a id="console"></a>

### 控制台（Console）

UART0控制台通过板载ICDI虚拟COM端口提供，以115200、8N1连接串口。

Linux下：

```text
$ screen /dev/ttyACM0 115200
```

<a id="references"></a>

## 参考资料（References）


- [TM4C123GH6PM数据手册](https://www.ti.com/lit/ds/symlink/tm4c123gh6pm.pdf)
- [TM4C123GXL LaunchPad用户指南](https://www.ti.com/lit/ug/spmu296/spmu296.pdf)
- [TivaWare外设驱动库（Peripheral Driver Library）](https://www.ti.com/tool/SW-TM4C)

## 译注

TM4C123GXL通过ICDI及OpenOCD烧录，UART0经PA0／PA1连接虚拟串口。原文通用定时器列表的位宽与随后wide timers表述均保留，未据译者推测改写硬件规格。

---

[上一章](P024_SK-AM64.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md)
