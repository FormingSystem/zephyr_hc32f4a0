---
id: learning.zephyr-docs.boards-ti.page-22
title: MSP-EXP432P401R LaunchXL
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/ti/msp_exp432p401r_launchxl/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="msp_exp432p401r_launchxl"></a>

# 第22章\_MSP-EXP432P401R LaunchXL

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/ti/msp_exp432p401r_launchxl/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/msp_exp432p401r_launchxl.jpg](images/msp_exp432p401r_launchxl.jpg)](images/msp_exp432p401r_launchxl.jpg)

MSP-EXP432P401R LaunchXL

名称（Name）：

`msp_exp432p401r_launchxl`

厂商（Vendor）：

[德州仪器（Texas Instruments）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=ti)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[msp432p401r](https://docs.zephyrproject.org/latest/boards/index.html#soc=msp432p401r)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ti/msp_exp432p401r_launchxl/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

SimpleLink MSP-EXP432P401R LaunchPad开发套件是易用的MSP432P401R评估模块，提供开始开发所需的组件。目标芯片为兼顾低功耗与性能的SimpleLink MSP432 Arm 32位Cortex-M4F微控制器。

<a id="features"></a>

### 功能（Features）：


- 低功耗Arm Cortex-M4F MSP432P401R
- 40引脚LaunchPad开发套件标准，兼容BoosterPack插接模块生态
- XDS110-ET开源板载调试探针，提供EnergyTrace+技术及应用UART
- 两个按键及两个LED，用于用户交互
- 反向通道UART（Backchannel UART）通过USB连接电脑

MSP-EXP432P401R LaunchXL开发板详情见对应用户指南。

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`msp_exp432p401r_launchxl`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="msp_exp432p401r_launchxl-hw-features"></a>

<a id="msp_exp432p401r_launchxl-msp_exp432p401r_launchxl/msp432p401r-hw-features-section"></a>

#### `msp_exp432p401r_launchxl/msp432p401r`目标（Target）

<a id="msp_exp432p401r_launchxl-msp_exp432p401r_launchxl/msp432p401r-hw-features-panel"></a>

<a id="msp_exp432p401r_launchxl-msp_exp432p401r_launchxl/msp432p401r-hw-features-memory"></a>

该开发板目标的片上存储容量：64 KiB RAM、256 KiB Flash。

<a id="msp_exp432p401r_launchxl-msp_exp432p401r_launchxl/msp432p401r-hw-features-table"></a>

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
<td>ARM Cortex-M4F 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/msp432p4xx.dtsi?plain=1#L12">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P025_arm_cortex-m4f.md#std-dtcompatible-arm-cortex-m4f"><code>arm,cortex-m4f</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/msp432p4xx.dtsi?plain=1#L26">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>TI MSP432P4XX UART（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/msp432p4xx.dtsi?plain=1#L33">已启用：1</a>）</td>
<td><a href="../uart_ti_wch_virtual_binding_reference/P001_ti_msp432p4xx-uart.md#std-dtcompatible-ti-msp432p4xx-uart"><code>ti,msp432p4xx-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/msp432p4xx.dtsi?plain=1#L18">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
</table>


- 与默认内部32 kHz REFOCLK相比，板载32 kHz晶体可降低LPM3睡眠电流并提供更高精度时钟，因此可使用全部低功耗模式。
- 板载48 MHz晶体允许MCLK及HSMCLK按器件最高工作速度运行。

受支持外设的更多信息见MSP432P4XX技术参考手册。

<a id="building-and-flashing"></a>

## 构建与烧录（Building and Flashing）

`msp_exp432p401r_launchxl`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

<a id="prerequisites"></a>

### 前提条件（Prerequisites）：


1. 确认XDS110仿真固件已更新。

  <a id="id3"></a>

  下载并安装最新[XDS110仿真软件包](http://processors.wiki.ti.com/index.php/XDS_Emulation_Software_Package#XDS_Emulation_Software_.28emupack.29_Download)[注1](#id2)。

  按照[XDS110固件更新说明](http://software-dl.ti.com/ccs/esd/documents/xdsdebugprobes/emu_xds110.html#updating-the-xds110-firmware)操作。

  仿真软件包可能将xdsdfu工具安装到<install_dir>/ccs_base/common/uscif/xds110/。
2. 安装OpenOCD

  可按[安装最新Zephyr SDK的说明](../toolchains/P002_ZephyrSDK.md#toolchain-zephyr-sdk)获取OpenOCD。

  安装后，将OpenOCD可执行文件所在目录加入环境变量PATH。例如，Linux中可使用以下命令：

  ```text
  export PATH=$ZEPHYR_SDK_INSTALL_DIR/sysroots/x86_64-pokysdk-linux/usr/bin/openocd:$PATH
  ```

  若之前安装过TI OpenOCD，可直接切换使用Zephyr SDK版本。若仍希望使用TI OpenOCD，可在[boards/ti/msp_exp432p401r_launchxl/board.cmake](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ti/msp_exp432p401r_launchxl/board.cmake)包含通用openocd.board.cmake文件之前，设置OPENOCD及OPENOCD_DEFAULT_PATH，分别指向OpenOCD可执行文件及脚本位置：

  ```text
  set(OPENOCD "/usr/local/bin/openocd" CACHE FILEPATH "" FORCE)
  set(OPENOCD_DEFAULT_PATH /usr/local/share/openocd/scripts)
  include(${ZEPHYR_BASE}/boards/common/openocd.board.cmake)
  ```

<a id="flashing"></a>

### 烧录（Flashing）

Zephyr应用开发请遵循[入门指南](../getting_started/P002_入门指南.md#getting-started)。

例如，为MSP-EXP432P401R LaunchXL构建并烧录[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用：

```text
# From the root of the zephyr repository
west build -b msp_exp432p401r_launchxl samples/hello_world
west flash
```

这会将镜像加载到闪存。

另开终端连接UART0，查看程序输出：

```text
% screen /dev/ttyACM0 115200 8N1
```

随后按开发板复位键S3运行程序。

<a id="debugging"></a>

### 调试（Debugging）

调试已烧录镜像时，先复位开发板，再使用debug构建目标：

```text
# From the root of the zephyr repository
west build -b msp_exp432p401r_launchxl samples/hello_world
west debug
```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [http://processors.wiki.ti.com/index.php/XDS_Emulation_Software_Package#XDS_Emulation_Software_.28emupack.29_Download](http://processors.wiki.ti.com/index.php/XDS_Emulation_Software_Package#XDS_Emulation_Software_.28emupack.29_Download)

TI MSP432 Wiki：

[https://en.wikipedia.org/wiki/TI_MSP432](https://en.wikipedia.org/wiki/TI_MSP432)

TI MSP432P401R产品页：

[http://www.ti.com/product/msp432p401r](http://www.ti.com/product/msp432p401r)

TI MSP432 SDK：

[http://www.ti.com/tool/SIMPLELINK-MSP432-SDK](http://www.ti.com/tool/SIMPLELINK-MSP432-SDK)

## 译注

MSP432P401R的32 kHz晶体支持全部低功耗模式，48 MHz晶体用于MCLK及HSMCLK最高运行速度；板上复位键为S3。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [XDS_Emulation_Software_Package](http://processors.wiki.ti.com/index.php/XDS_Emulation_Software_Package#XDS_Emulation_Software_.28emupack.29_Download)：HTTP Error 421: Misdirected Request。
- [emu_xds110.html](http://software-dl.ti.com/ccs/esd/documents/xdsdebugprobes/emu_xds110.html#updating-the-xds110-firmware)：页面可访问，但未确认目标片段。
- [TI_MSP432](https://en.wikipedia.org/wiki/TI_MSP432)：HTTP Error 403: Too Many Reqs (1862a4b)。

---

[上一章](P021_MSPM33C321A_Launchpad.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P023_SK-AM62_Evaluation_board.md)
