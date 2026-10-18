---
id: learning.zephyr-docs.boards-microchip.page-15
title: PIC32CK SG01 Curiosity Ultra
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/microchip/pic32c/pic32ck_sg01_cult/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="pic32ck_sg01_cult"></a>

# 第15章\_PIC32CK SG01 Curiosity Ultra

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/microchip/pic32c/pic32ck_sg01_cult/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../../_images/pic32ck_sg01_cult.webp](images/pic32ck_sg01_cult.webp)](images/pic32ck_sg01_cult.webp)

PIC32CK SG01 Curiosity Ultra

名称（Name）：

`pic32ck_sg01_cult`

厂商（Vendor）：

[微芯科技（Microchip Technology Inc.）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=microchip)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[pic32ck2051sg01144](https://docs.zephyrproject.org/latest/boards/index.html#soc=pic32ck2051sg01144)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/microchip/pic32c/pic32ck_sg01_cult/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

PIC32CK SG01 Curiosity Ultra评估套件用于评估Microchip PIC32CK SG微控制器，料号按原文为EV44P93A。套件提供完整功能，方便探索PIC32CK SG外设并了解如何将器件集成到自己的设计。

<a id="hardware"></a>

## 硬件（Hardware）


- 144引脚TQFP封装的PIC32CK2051SG01144微控制器
- Arm® Cortex®-M33微控制器
- 支持TrustZone®技术的硬件安全模块（HSM）
- 32.768 kHz晶体振荡器（Crystal Oscillator）
- 12 MHz晶体振荡器（Crystal Oscillator）
- 2048 KiB闪存及512 KiB RAM
- 两个用户LED，红色及绿色
- 一个绿色开发板电源LED
- 两个机械用户按键
- 1个复位按键（Reset Button）
- 板载温度传感器（Temperature Sensor）
- 两个USB接口，Type-C及Micro-B
- 虚拟COM端口（VCOM）
- 通过串行线调试（SWD）及板载PKoB4调试器，对板上PIC32CK SG编程和调试
- Arduino Uno连接器
- MikroBUS™插座
- Xplained Pro扩展排针
- 图形接口（Graphics Interface）
- 10/100 MB以太网接口，单位按原文保留
- 两个CAN FD接口
- SD卡槽
- QSPI闪存及串行EEPROM
- 一个电机控制位置解码器（PDEC）接口

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`pic32ck_sg01_cult`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="pic32ck_sg01_cult-hw-features"></a>

<a id="pic32ck_sg01_cult-pic32ck_sg01_cult/pic32ck2051sg01144-hw-features-section"></a>

#### `pic32ck_sg01_cult/pic32ck2051sg01144`目标（Target）

<a id="pic32ck_sg01_cult-pic32ck_sg01_cult/pic32ck2051sg01144-hw-features-panel"></a>

<a id="pic32ck_sg01_cult-pic32ck_sg01_cult/pic32ck2051sg01144-hw-features-memory"></a>

该开发板目标的片上存储容量：512 KiB RAM、2 MiB Flash。

<a id="pic32ck_sg01_cult-pic32ck_sg01_cult/pic32ck2051sg01144-hw-features-table"></a>

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
<td>ARM Cortex-M33处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32ck_sg_gc/common/pic32ck_sg_gc.dtsi?plain=1#L16">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P022_arm_cortex-m33.md#std-dtcompatible-arm-cortex-m33"><code>arm,cortex-m33</code></a></td>
</tr>
<tr>
<td rowspan="10">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Microchip PIC32CK SG／GC时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32ck_sg_gc/common/pic32ck_sg_gc.dtsi?plain=1#L54">已启用：1</a>）</td>
<td><a href="../clock_esp_infineon_microchip_binding_reference/P022_microchip_pic32ck-sg-gc-clock.md#std-dtcompatible-microchip-pic32ck-sg-gc-clock"><code>microchip,pic32ck-sg-gc-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>PIC32CK_SG_GC晶体振荡器（XOSC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32ck_sg_gc/common/pic32ck_sg_gc.dtsi?plain=1#L67">已启用：1</a>）</td>
<td><a href="../clock_microchip_pic32_binding_reference/P005_microchip_pic32ck-sg-gc-xosc.md#std-dtcompatible-microchip-pic32ck-sg-gc-xosc"><code>microchip,pic32ck-sg-gc-xosc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>PIC32CK_SG_GC内部振荡器（OSC48M）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32ck_sg_gc/common/pic32ck_sg_gc.dtsi?plain=1#L71">已启用：1</a>）</td>
<td><a href="../clock_esp_infineon_microchip_binding_reference/P023_microchip_pic32ck-sg-gc-dfll48m.md#std-dtcompatible-microchip-pic32ck-sg-gc-dfll48m"><code>microchip,pic32ck-sg-gc-dfll48m</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>PIC32CK_SG_GC PLL时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32ck_sg_gc/common/pic32ck_sg_gc.dtsi?plain=1#L75">已启用：1</a>）</td>
<td><a href="../clock_microchip_pic32_binding_reference/P003_microchip_pic32ck-sg-gc-pll.md#std-dtcompatible-microchip-pic32ck-sg-gc-pll"><code>microchip,pic32ck-sg-gc-pll</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>PIC32CK_SG_GC RTC时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32ck_sg_gc/common/pic32ck_sg_gc.dtsi?plain=1#L107">已启用：1</a>）</td>
<td><a href="../clock_microchip_pic32_binding_reference/P004_microchip_pic32ck-sg-gc-rtc.md#std-dtcompatible-microchip-pic32ck-sg-gc-rtc"><code>microchip,pic32ck-sg-gc-rtc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>PIC32CK_SG_GC外部晶体振荡器（XOSC32K）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32ck_sg_gc/common/pic32ck_sg_gc.dtsi?plain=1#L112">已启用：1</a>）</td>
<td><a href="../clock_microchip_pic32_binding_reference/P006_microchip_pic32ck-sg-gc-xosc32k.md#std-dtcompatible-microchip-pic32ck-sg-gc-xosc32k"><code>microchip,pic32ck-sg-gc-xosc32k</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>PIC32CK_SG_GC通用时钟发生器（Generic Clock Generator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32ck_sg_gc/common/pic32ck_sg_gc.dtsi?plain=1#L116">已启用：1</a>）</td>
<td><a href="../clock_esp_infineon_microchip_binding_reference/P024_microchip_pic32ck-sg-gc-gclkgen.md#std-dtcompatible-microchip-pic32ck-sg-gc-gclkgen"><code>microchip,pic32ck-sg-gc-gclkgen</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>PIC32CK_SG_GC通用时钟外设（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32ck_sg_gc/common/pic32ck_sg_gc.dtsi?plain=1#L120">已启用：1</a>）</td>
<td><a href="../clock_esp_infineon_microchip_binding_reference/P025_microchip_pic32ck-sg-gc-gclkperiph.md#std-dtcompatible-microchip-pic32ck-sg-gc-gclkperiph"><code>microchip,pic32ck-sg-gc-gclkperiph</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>PIC32CK_SG_GC主时钟域（Main Clock Domains）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32ck_sg_gc/common/pic32ck_sg_gc.dtsi?plain=1#L125">已启用：1</a>）</td>
<td><a href="../clock_microchip_pic32_binding_reference/P001_microchip_pic32ck-sg-gc-mclkcpu.md#std-dtcompatible-microchip-pic32ck-sg-gc-mclkcpu"><code>microchip,pic32ck-sg-gc-mclkcpu</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>PIC32CK_SG_GC MCLK外设（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32ck_sg_gc/common/pic32ck_sg_gc.dtsi?plain=1#L129">已启用：1</a>）</td>
<td><a href="../clock_microchip_pic32_binding_reference/P002_microchip_pic32ck-sg-gc-mclkperiph.md#std-dtcompatible-microchip-pic32ck-sg-gc-mclkperiph"><code>microchip,pic32ck-sg-gc-mclkperiph</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Microchip Port G1 GPIO（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32ck_sg_gc/common/pic32ck_sg_gc.dtsi?plain=1#L151">已启用：2</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32ck_sg_gc/common/pic32ck_sg_gc.dtsi?plain=1#L142">已禁用：2</a>）</td>
<td><a href="../gpio_microchip_nordic_nuvoton_binding_reference/P001_microchip_port-g1-gpio.md#std-dtcompatible-microchip-port-g1-gpio"><code>microchip,port-g1-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/microchip/pic32c/pic32ck_sg01_cult/pic32ck_sg01_cult.dts?plain=1#L42">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P003_ARMv8_M_NVIC.md#std-dtcompatible-arm-v8m-nvic"><code>arm,v8m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/microchip/pic32c/pic32ck_sg01_cult/pic32ck_sg01_cult.dts?plain=1#L28">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32ck_sg_gc/common/pic32ck_sg_gc.dtsi?plain=1#L23">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P007_arm_armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu"><code>arm,armv8m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32ck_sg_gc/common/pic32ck_sg_gc.dtsi?plain=1#L37">已启用：2</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Microchip PORT引脚控制（Pinctrl）容器节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32ck_sg_gc/common/pic32ck_sg.dtsi?plain=1#L9">已启用：1</a>）</td>
<td><a href="../pinctrl_infineon_nordic_nxp_binding_reference/P006_microchip_port-g1-pinctrl.md#std-dtcompatible-microchip-port-g1-pinctrl"><code>microchip,port-g1-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/microchip/pic32c/pic32ck_sg_gc/common/pic32ck_sg_gc.dtsi?plain=1#L50">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

PIC32CK SG01 Curiosity Ultra用户指南提供开发板连接详情。（[PIC32CK SG01 Curiosity Ultra用户指南（User Guide）](https://ww1.microchip.com/downloads/aemDocuments/documents/MCU32/ProductDocuments/UserGuides/PIC32CK-SG01-SG01-Curiosity-Ultra-User-Guide-DS70005529.pdf)）

<a id="programming-debugging"></a>

## 编程与调试（Programming & Debugging）

`pic32ck_sg01_cult`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td>✅</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>mplab_ipe</td>
<td>✅（默认 / default）</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>

<a id="flash-using-mplab-ipe"></a>

### 使用MPLAB IPE烧录（Flash）

使用MPLAB IPE烧录的方法见“使用Microchip MPLAB IPE烧录”。（[使用Microchip MPLAB IPE烧录（Flashing）](P001_Flashing_with_Microchip_MPLAB_IPE.md#microchip-mplab-ipe-flashing)）

<a id="flash-using-j-link"></a>

### 使用J-Link烧录（Flash Using J-Link）

使用J-Link调试器烧录开发板时，请按以下步骤操作：


1. 安装J-Link软件（Install J-Link Software）


  - 从Segger下载并安装[J-Link软件](https://www.segger.com/downloads/jlink)工具。
  - 确认已安装的J-Link可执行文件，例如JLink及JLinkGDBServer，已加入系统PATH。
2. 连接开发板（Connect the Board）


  - 将J32调试探针连接到开发板的CORTEX DEBUG排针。（[J32调试探针（Debug Probe）](https://www.microchip.com/en-us/development-tool/dv164232)）
  - 通过USB将J32调试探针另一端连接到主机PC。
  - 将开发板DEBUG USB端口连接主机，为开发板供电。
3. 构建应用（Build the Application）

  可用west工具构建Blinky等Zephyr示例应用。从Zephyr工作区执行以下命令：

  ```text
  west build -b pic32ck_sg01_cult -p samples/basic/blinky
  ```

  这将为pic32ck_sg01_cult开发板构建Blinky应用。
4. 烧录设备（Flash the Device）

  构建完成后，用以下命令烧录固件：

  ```text
  west flash --runner jlink
  ```

  该命令使用`jlink`运行器（Runner）将应用烧录到开发板。
5. 观察结果（Observe the Result）

  烧录后LED0应开始闪烁，表明应用成功运行。

<a id="debug-using-j-link-gdb-command-line"></a>

### 使用J-Link调试：GDB命令行（Command-Line）

使用J-Link调试器调试开发板时，按以下步骤操作：


1. 构建应用（Build the Application）

  可用west工具构建Blinky等Zephyr示例应用。从Zephyr工作区执行以下命令：

  ```text
  west build -b pic32ck_sg01_cult -p samples/basic/blinky
  ```

  这将为pic32ck_sg01_cult开发板构建Blinky应用。
2. 调试应用（Debug the Application）

  从Zephyr工作区执行以下命令调试应用：

  ```text
  west debug
  ```

  注意（Note）

  `Debugging with J-Link GDB Server: Halting at `main` and Setting Breakpoints`

  ```text
  (gdb) break main
  (gdb) break main.c:42         # Optional: set breakpoint at line 42 in main.c
  (gdb) continue                # Start execution, halts at first breakpoint
  (gdb) info breakpoints        # List all breakpoints
  (gdb) delete 1                # Delete breakpoint number 1
  (gdb) delete                  # Delete all breakpoints
  (gdb) clear main.c:42         # Clear breakpoint at specific location
  (gdb) continue                # Resume execution
  ```

<a id="debug-using-j-link-vscode"></a>

### 使用J-Link调试：VSCode

使用VSCode调试时，在项目目录创建或编辑`.vscode/launch.json`，配置如下：

```text
{
   "version": "0.2.0",
   "configurations": [
      {
            "name": "Debug (J-Link, PIC32CK2051SG01144)",
            "type": "cortex-debug",
            "request": "launch",
            "servertype": "jlink",
            "device": "PIC32CK2051SG01144",
            "interface": "swd",
            "runToEntryPoint": "main",
            "showDevDebugOutput": "none",
            "cwd": "${workspaceFolder}",
            "executable": "${workspaceFolder}/zephyr/build/zephyr/zephyr.elf",

            /* J-Link settings */
            "serverpath": "C:/Program Files/SEGGER/JLink_Vxxx/JLinkGDBServerCL.exe",
            "serverArgs": [
               "-singlerun",
               "-if", "swd",
               "-speed", "4000",
               "-device", "PIC32CK2051SG",
               "-port", "50000"
            ],

             /* Zephyr SDK toolchain paths */
            "gdbPath": "***/zephyr-sdk-x.xx.x/arm-zephyr-eabi/bin/arm-zephyr-eabi-gdb.exe",
            "objdumpPath": "***/zephyr-sdk-x.xx.x/arm-zephyr-eabi/bin/arm-zephyr-eabi-objdump.exe",
      }
   ]
}
```

注意（Note）


- serverpath：若系统PATH中没有J-Link GDB Server可执行文件，指定其完整路径。
- gdbPath：若系统PATH中没有GDB可执行文件，指定其完整路径。
- objdumpPath：若系统PATH中没有objdump可执行文件，指定其完整路径。

<a id="debugging-steps-in-vscode"></a>

#### VSCode调试步骤（Debugging Steps）


1. 按上述方式启动J-Link GDB Server。
2. 在VSCode中打开samples/basic/blinky/src/main.c。
3. 单击源码行号旁的位置设置断点。
4. 按F5或单击VSCode的绿色“开始调试（Start Debugging）”按钮。
5. 调试器连接后加载程序，并在main处暂停。
6. 使用VSCode调试控件继续运行、单步执行或检查变量。

<a id="references"></a>

## 参考资料（References）

PIC32CK SG产品页面：

[https://www.microchip.com/en-us/product/pic32ck2051sg01144](https://www.microchip.com/en-us/product/pic32ck2051sg01144)

PIC32CK SG／SG产品系列页面，名称按原文保留：

[https://www.microchip.com/en-us/products/microcontrollers/32-bit-mcus/pic32-sam/pic32ck-sg-sg](https://www.microchip.com/en-us/products/microcontrollers/32-bit-mcus/pic32-sam/pic32ck-sg-sg)

## 译注

原文套件料号与GC页同为EV44P93A，产品系列标签写SG/SG；保留原文差异。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [PIC32CK-SG01-SG01-Curiosity-Ultra-User-Guide-DS70005529.pdf](https://ww1.microchip.com/downloads/aemDocuments/documents/MCU32/ProductDocuments/UserGuides/PIC32CK-SG01-SG01-Curiosity-Ultra-User-Guide-DS70005529.pdf)：HTTP Error 403: Forbidden。
- [dv164232](https://www.microchip.com/en-us/development-tool/dv164232)：HTTP Error 403: Forbidden。
- [pic32ck2051sg01144](https://www.microchip.com/en-us/product/pic32ck2051sg01144)：HTTP Error 403: Forbidden。
- [pic32ck-sg-sg](https://www.microchip.com/en-us/products/microcontrollers/32-bit-mcus/pic32-sam/pic32ck-sg-sg)：HTTP Error 403: Forbidden。

---

[上一章](P014_PIC32CK_GC01_Curiosity_Ultra.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P016_PIC32CM_GC00_Curiosity_Pro.md)
