---
id: learning.zephyr-docs.boards-atmel.page-3
title: SAM4L-EK
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/atmel/sam/sam4l_ek/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="sam4l_ek"></a>

# 第3章\_SAM4L-EK

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/atmel/sam/sam4l_ek/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../../_images/atmel-sam4l-ek-callouts.jpg](images/atmel-sam4l-ek-callouts.jpg)](images/atmel-sam4l-ek-callouts.jpg)

SAM4L-EK

名称（Name）：

`sam4l_ek`

厂商（Vendor）：

[Atmel公司（Atmel Corporation）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=atmel)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[sam4lc4c](https://docs.zephyrproject.org/latest/boards/index.html#soc=sam4lc4c)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/atmel/sam/sam4l_ek/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

SAM4L系列集成picoPower技术以降低功耗。多种电源控制技术结合后，活动电流可降至90 μA/MHz。器件提供丰富配置，便于在最低功耗与应用所需功能之间取舍。等待模式（WAIT）及保持模式（RETENTION）可保留全部逻辑和RAM，唤醒时间小于1.5 μs，功耗分别低至3 μA和1.5 μA；WAIT还支持睡眠行走（SleepWalking）。备份模式（BACKUP）关闭CPU、外设及RAM供电，消耗低于0.9 μA，并支持外部中断唤醒。

<a id="id3"></a>

SAM4L-EK是面向Atmel SAM4L SoC系列的完整开发设计，配备丰富外设，可作为ATSAM4L-EK评估平台。更多细节见[SAM4L-EK在线用户指南](http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-42026-ATSAM4L-EK-User-Guide_ApplicationNote_AVR32850.pdf)[注1](#id2)。

<a id="hardware"></a>

## 硬件（Hardware）


- ATSAM4LC4C ARM Cortex-M4处理器
- 12 MHz晶体振荡器（Crystal Oscillator）
- 32.768 kHz晶体振荡器（Crystal Oscillator）
- 一个Micro-AB USB OTG主机／设备接口
- 一个AT86RF2xx IEEE 802.15.4收发器连接器
- 一路RS-485全双工接口（Full Duplex）
- 一个Sensor Xplained扩展板连接器
- 一个3.5 mm音频插孔（Audio Jack）
- 一个专用开发板监控MCU（Board Monitor）


  - 功耗测量（Power Measurement）：VDDIN、VDDIO、VDDANA
  - 一个128 × 64有机发光二极管显示屏（OLED）
  - 五个LED
  - 一个操纵杆（Joystick）
  - 一路USART
  - 一路双线接口（TWI）
- 一个40 × 4段式液晶显示屏（LCD Segment Display）
- 一个用户触摸按键及一个用户机械按键
- 一个用户LED
- 一个QTouch滑条（Slider）
- 一个QTouch按键
- 一个TEMT6000光传感器（Light Sensor）
- 一片AT25DF641A串行NOR闪存

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`sam4l_ek`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="sam4l_ek-hw-features"></a>

<a id="sam4l_ek-sam4l_ek/sam4lc4c-hw-features-section"></a>

#### `sam4l_ek/sam4lc4c`目标（Target）

<a id="sam4l_ek-sam4l_ek/sam4lc4c-hw-features-panel"></a>

<a id="sam4l_ek-sam4l_ek/sam4lc4c-hw-features-memory"></a>

该开发板目标的片上存储容量：32 KiB RAM、256 KiB Flash。

<a id="sam4l_ek-sam4l_ek/sam4lc4c-hw-features-table"></a>

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
<td>ARM Cortex-M4 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L27">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P024_arm_cortex-m4.md#std-dtcompatible-arm-cortex-m4"><code>arm,cortex-m4</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Atmel电源管理控制器（PMC / Power Management Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L58">已启用：1</a>）</td>
<td><a href="../clock_adi_atmel_bflb_binding_reference/P009_atmel_sam-pmc.md#std-dtcompatible-atmel-sam-pmc"><code>atmel,sam-pmc</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM定时器／计数器（TC / Timer Counter）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L224">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L234">已禁用：1</a>）</td>
<td><a href="../counter_binding_reference/P010_atmel_sam-tc.md#std-dtcompatible-atmel-sam-tc"><code>atmel,sam-tc</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM4L双字闪存控制器（FLASHCALW / Flash Controller Double Word）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L66">已禁用：1</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P008_atmel_sam4l-flashcalw-controller.md#std-dtcompatible-atmel-sam4l-flashcalw-controller"><code>atmel,sam4l-flashcalw-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>SAM4L通用输入输出端口（GPIO Port）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L193">已启用：3</a>）</td>
<td><a href="../gpio_connectors_bflb_esp_binding_reference/P001_atmel_sam4l-gpio.md#std-dtcompatible-atmel-sam4l-gpio"><code>atmel,sam4l-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>ATMEL SAM4L唯一120位序列号（Unique Serial Number）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L252">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P002_atmel_sam4l-uid.md#std-dtcompatible-atmel-sam4l-uid"><code>atmel,sam4l-uid</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM4L系列I2C主机双线接口（TWIM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L90">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L101">已禁用：3</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P010_atmel_sam-i2c-twim.md#std-dtcompatible-atmel-sam-i2c-twim"><code>atmel,sam-i2c-twim</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam/sam4l_ek/sam4l_ek.dts?plain=1#L38">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam/sam4l_ek/sam4l_ek.dts?plain=1#L29">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L34">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P005_arm_armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu"><code>arm,armv7m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L74">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM引脚控制容器（Pinctrl Container）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L187">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P013_atmel_sam-pinctrl.md#std-dtcompatible-atmel-sam-pinctrl"><code>atmel,sam-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM随机数发生器（RNG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L244">已启用：1</a>）</td>
<td><a href="../rng_binding_reference/P004_atmel_sam-trng.md#std-dtcompatible-atmel-sam-trng"><code>atmel,sam-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM系列通用同步／异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L160">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L144">已禁用：3</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P011_atmel_sam-usart.md#std-dtcompatible-atmel-sam-usart"><code>atmel,sam-usart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L134">已启用：1</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P008_atmel_sam-spi.md#std-dtcompatible-atmel-sam-spi"><code>atmel,sam-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L41">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td rowspan="1">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>Atmel SAM系列USB控制器（USBC），设备模式（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L176">已启用：1</a>）</td>
<td><a href="../usb_controller_binding_reference/P004_atmel_sam-usbc.md#std-dtcompatible-atmel-sam-usbc"><code>atmel,sam-usbc</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>ATMEL SAM4L看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L258">已启用：1</a>）</td>
<td><a href="../watchdog_binding_reference/P009_atmel_sam4l-watchdog.md#std-dtcompatible-atmel-sam4l-watchdog"><code>atmel,sam4l-watchdog</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

<a id="id5"></a>

<a id="id6"></a>

[SAM4L-EK设计文档](http://ww1.microchip.com/downloads/en/DeviceDoc/doc42027_SAM4L-EK_Design_Documentation.PDF)[注2](#id4)提供开发板连接的详细信息。更多细节可下载[SAM4L-EK设计文档](http://ww1.microchip.com/downloads/en/DeviceDoc/doc42027_SAM4L-EK_Design_Documentation.PDF)[注2](#id4)查看。

<a id="system-clock"></a>

### 系统时钟（System Clock）

SAM4L MCU使用板上的12 MHz内部振荡器，经片上PLL生成48 MHz系统时钟（振荡器类型依原文保留）。

<a id="serial-port"></a>

### 串口（Serial Port）

ATSAM4LC4C MCU有四路USART。USART2连接嵌入式调试单元，可作为控制台；USART0在其他排针和RS-485端口之间共用。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`sam4l_ek`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-jlink"><code>jlink</code></a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

SAM4L-EK配有SEGGER板载嵌入式调试单元[J-Link OB](https://www.segger.com/jlink-ob.html)，为SAM4LC4C提供调试接口。可使用Ozone或JLink与芯片通信。

<a id="flashing"></a>

### 烧录（Flashing）


1. <a id="id8"></a>

  从SEGGER [JLink下载页面](https://www.segger.com/downloads/jlink)[注3](#id7)获取JLink，在“J-Link Software and Documentation Pack”一节安装Linux版软件及文档包。应确保`JLinkExe`可通过`PATH`找到。
2. 运行你惯用的终端程序，监听输出。Linux下的终端设备应为`/dev/ttyACM0`，例如：

  ```text
  $ minicom -D /dev/ttyACM0 -o
  ```

  `-o`选项让`minicom`不发送调制解调器初始化字符串（Modem Initialization String）。连接参数应配置如下：


  - 速率（Speed）：115200波特率
  - 数据位（Data）：8位
  - 奇偶校验（Parity）：无（None）
  - 停止位（Stop Bits）：1位
3. 通过USB调试端口将SAM4L-EK连接到主机，然后构建并烧录[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用。

  ```text
  # From the root of the zephyr repository
  west build -b sam4l_ek samples/hello_world
  west flash
  ```

  终端应显示`Hello World! sam4l_ek`。

<a id="debugging"></a>

### 调试（Debugging）

可以按常规方式调试应用。下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例。

```text
# From the root of the zephyr repository
west build -b sam4l_ek samples/hello_world
west debug
```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-42026-ATSAM4L-EK-User-Guide_ApplicationNote_AVR32850.pdf](http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-42026-ATSAM4L-EK-User-Guide_ApplicationNote_AVR32850.pdf)

<a id="id4"></a>

〔2〕 ([1](#id5),[2](#id6)) [http://ww1.microchip.com/downloads/en/DeviceDoc/doc42027_SAM4L-EK_Design_Documentation.PDF](http://ww1.microchip.com/downloads/en/DeviceDoc/doc42027_SAM4L-EK_Design_Documentation.PDF)

<a id="id7"></a>

〔[3](#id8)〕 [https://www.segger.com/downloads/jlink](https://www.segger.com/downloads/jlink)

## 译注

原文时钟段落将板上的12 MHz振荡器称为internal oscillator，部分硬件列表也将32.768 kHz晶体称为internal；这里保留原始表述，不自行按器件资料改写。

---

[上一章](P002_SAM4E_Xplained_Pro.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P004_SAM4S_Xplained.md)
