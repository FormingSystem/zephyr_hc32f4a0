---
id: learning.zephyr-docs.boards-ti.page-10
title: CC3235SF LaunchXL
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/ti/cc3235sf_launchxl/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="cc3235sf_launchxl"></a>

# 第10章\_CC3235SF LaunchXL

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/ti/cc3235sf_launchxl/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`cc3235sf_launchxl`

厂商（Vendor）：

[德州仪器（Texas Instruments）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=ti)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[cc3235sf](https://docs.zephyrproject.org/latest/boards/index.html#soc=cc3235sf)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ti/cc3235sf_launchxl/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

SimpleLink Wi-Fi CC3235SF LaunchPad开发套件（CC3235SF-LAUNCHXL）搭载CC3235SF单芯片无线微控制器，具有1 MB内部闪存、4 MB外部串行闪存、256 KB RAM及增强安全功能，支持2.4 GHz及5 GHz的802.11 a/b/g/n。

<a id="id2"></a>

详情见[TI CC3235产品页](http://www.ti.com/product/cc3235SF)[注1](#id1)。

<a id="features"></a>

### 功能（Features）：


- 两个独立执行环境：专用于用户应用的Arm Cortex-M4微控制器，以及运行全部Wi-Fi及互联网逻辑层的网络处理微控制器
- 40引脚LaunchPad标准，兼容BoosterPack生态
- 板载加速度计及温度传感器
- 两个按键及一个RGB LED，用于用户交互
- UART通过USB连接电脑
- BoosterPack插接模块可添加图形显示、音频编解码器、天线选择、环境感知等功能
- 通过USB为LaunchPad及可选外部BoosterPack供电
- 基于XDS110的JTAG仿真，配有用于闪存编程的串口

<a id="id15"></a>

CC3235SF LaunchXL开发板详情见《[CC3235SF LaunchPad Dev Kit Hardware User’s Guide](http://www.ti.com/lit/pdf/swru539)》硬件用户指南[注6](#id14)。

<a id="hardware"></a>

## 硬件（Hardware）

CC3235SF SoC具有两个微控制器：


1. 应用微控制器（Applications MCU）：80 MHz Arm Cortex-M4核，RAM在此段原文写作256 Kb，可访问外部4 MB串行闪存，ROM内含引导加载器及外设驱动。
2. 网络协处理器（Network Coprocessor，NWP）：专用Arm微控制器，完全接管应用微控制器的Wi-Fi及互联网协议处理。

<a id="id4"></a>

CC3235SF SoC完整信息见[CC3235技术参考手册（TRM）](http://www.ti.com/lit/pdf/swru543)[注2](#id3)。

<a id="supported-features"></a>

### 支持的功能（Supported Features）

Zephyr已移植到应用微控制器，并提供基本外设驱动支持。

`cc3235sf_launchxl`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="cc3235sf_launchxl-hw-features"></a>

<a id="cc3235sf_launchxl-cc3235sf_launchxl/cc3235sf-hw-features-section"></a>

#### `cc3235sf_launchxl/cc3235sf`目标（Target）

<a id="cc3235sf_launchxl-cc3235sf_launchxl/cc3235sf-hw-features-panel"></a>

<a id="cc3235sf_launchxl-cc3235sf_launchxl/cc3235sf-hw-features-memory"></a>

此开发板目标可用存储器：256 KiB RAM、1 MiB 闪存。

<a id="cc3235sf_launchxl-cc3235sf_launchxl/cc3235sf-hw-features-table"></a>

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
<td>ARM Cortex-M4 处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc32xx.dtsi?plain=1#L40">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P024_arm_cortex-m4.md#std-dtcompatible-arm-cortex-m4"><code>arm,cortex-m4</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>CC32xx模数转换器（ADC）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc32xx.dtsi?plain=1#L121">已启用：1</a>）</td>
<td><a href="../hardware/P907_TICC32xx模数转换器绑定.md#dtbinding-ti-cc32xx-adc"><code>ti,cc32xx-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc32xx.dtsi?plain=1#L55">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>TI CC32XX通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc32xx.dtsi?plain=1#L89">已启用：4</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P012_ti_cc32xx-gpio.md#std-dtcompatible-ti-cc32xx-gpio"><code>ti,cc32xx-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>TI CC32XX I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc32xx.dtsi?plain=1#L78">已启用：1</a>）</td>
<td><a href="../i2c_stm32_ti_mux_binding_reference/P012_ti_cc32xx-i2c.md#std-dtcompatible-ti-cc32xx-i2c"><code>ti,cc32xx-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ti/cc3235sf_launchxl/cc3235sf_launchxl.dts?plain=1#L56">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ti/cc3235sf_launchxl/cc3235sf_launchxl.dts?plain=1#L37">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc3235sf.dtsi?plain=1#L19">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>TI CC32XX引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc32xx.dtsi?plain=1#L136">已启用：1</a>）</td>
<td><a href="../pinctrl_stm32_ti_xilinx_binding_reference/P012_ti_cc32xx-pinctrl.md#std-dtcompatible-ti-cc32xx-pinctrl"><code>ti,cc32xx-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>TI CC32XX通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc32xx.dtsi?plain=1#L62">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc32xx.dtsi?plain=1#L70">已禁用：1</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P020_ti_cc32xx-uart.md#std-dtcompatible-ti-cc32xx-uart"><code>ti,cc32xx-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc32xx.dtsi?plain=1#L47">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>CC32xx看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc32xx.dtsi?plain=1#L129">已启用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_watchdog_binding_reference/P005_ti_cc32xx-watchdog.md#std-dtcompatible-ti-cc32xx-watchdog"><code>ti,cc32xx-watchdog</code></a></td>
</tr>
</table>

注意（Note）

为与TI SimpleLink SDK及BoosterPack示例保持一致，I2C驱动启动时默认使用I2C_BITRATE_FAST模式，即400 kHz总线速度。

目前不支持可通过BoosterPack访问的加速度计、温度传感器及其他外设。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`cc3235sf_launchxl`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

<a id="id13"></a>

<a id="id10"></a>

TI官方支持在Windows及Linux上通过TI [CC32xx SDK](http://www.ti.com/tool/download/SIMPLELINK-CC32xx-SDK/2.40.01.01) [注5](#id12)开发，使用Code Composer Studio调试，使用[UniFlash](http://processors.wiki.ti.com/index.php/Category:CCS_UniFlash) [注4](#id9)烧录。

<a id="id7"></a>

Windows开发者可参阅[CC32xx快速入门指南](http://dev.ti.com/tirex/content/simplelink_cc32xx_sdk_2_40_01_01/docs/simplelink_mcu_sdk/Quick_Start_Guide.html)[注3](#id6)，了解工具安装及UniFlash烧录步骤。

Zephyr SDK生成的zephyr.bin可能无法通过UniFlash加载。若遇到问题，请改用zephyr.elf及下述OpenOCD流程。

以下步骤面向偏好命令行工具而非集成开发环境的Linux开发者。

烧录及调试前，需要完成几项一次性板卡设置。

<a id="prerequisites"></a>

### 前提条件（Prerequisites）：


1. <a id="id11"></a>

  下载并安装最新版本[UniFlash](http://processors.wiki.ti.com/index.php/Category:CCS_UniFlash) [注4](#id9)。
2. 将SOP[2..0]，即J15跳线，设为[010]，再通过USB连接电脑。

  应在/dev/ttyACM1及/dev/ttyACM0出现名为“Texas Instruments XDS110 Embed with CMSIS-DAP”的新设备。
3. 更新服务包（Service Pack），并将开发板设为开发模式（Development Mode）。

  开发模式会启用JTAG接口，这是后续使用OpenOCD及更新XDS110固件的前提。

  <a id="id8"></a>

  按[CC32xx快速入门指南](http://dev.ti.com/tirex/content/simplelink_cc32xx_sdk_2_40_01_01/docs/simplelink_mcu_sdk/Quick_Start_Guide.html)[注3](#id6)第2.4节“Download the Application”操作，但跳过第2.4.1节中选择MCU镜像的第5及第6步。
4. 确认XDS110仿真固件已更新。

  <a id="id17"></a>

  下载并安装最新[XDS110仿真软件包](http://processors.wiki.ti.com/index.php/XDS_Emulation_Software_Package#XDS_Emulation_Software_.28emupack.29_Download)[注7](#id16)。

  按照[XDS110固件更新说明](http://software-dl.ti.com/ccs/esd/documents/xdsdebugprobes/emu_xds110.html#updating-the-xds110-firmware)操作。

  仿真软件包可能将xdsdfu工具安装到<install_dir>/ccs_base/common/uscif/xds110/。
5. 将SOP[2..0]，即J15跳线，切回[001]。

  切换跳线前先断电，即拔下USB线。
6. 安装OpenOCD

  可按[安装最新Zephyr SDK的说明](../toolchains/P002_ZephyrSDK.md#toolchain-zephyr-sdk)获取OpenOCD。

  安装后，将OpenOCD可执行文件所在目录加入环境变量PATH。例如，Linux中可使用以下命令：

  ```text
  export PATH=$ZEPHYR_SDK_INSTALL_DIR/sysroots/x86_64-pokysdk-linux/usr/bin/openocd:$PATH
  ```

  若之前安装过TI OpenOCD，可直接切换使用Zephyr SDK版本。若仍希望使用TI OpenOCD，可在[boards/ti/cc3220sf_launchxl/board.cmake](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ti/cc3220sf_launchxl/board.cmake)包含通用openocd.board.cmake文件之前，设置OPENOCD及OPENOCD_DEFAULT_PATH，分别指向OpenOCD可执行文件及脚本位置：

  ```text
  set(OPENOCD "/usr/local/bin/openocd" CACHE FILEPATH "" FORCE)
  set(OPENOCD_DEFAULT_PATH /usr/local/share/openocd/scripts)
  include(${ZEPHYR_BASE}/boards/common/openocd.board.cmake)
  ```
7. 确认启用CONFIG_XIP=y，此为默认值。

  这会将程序放入闪存，并设置CONFIG_CC3235SF_DEBUG=y；后者在镜像前添加调试头，绕过引导加载器的闪存签名验证，使已写入内容在后续重启后仍可使用。

  <a id="id5"></a>

  安全闪存启动流程详情见CC3235技术参考手册[注2](#id3)第21.10节“Debugging Flash User Application Using JTAG”。（[CC3235技术参考手册（TRM）](http://www.ti.com/lit/pdf/swru543)）

满足以上条件后，可按Zephyr应用开发指南，用OpenOCD及GDB构建、烧录和调试_cc3235sf_launchxl板级配置的应用，见“构建应用”及“运行应用”；原文在此板名之前多一个下划线。（[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)；[运行应用（Run an Application）](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)）

<a id="flashing"></a>

### 烧录（Flashing）

针对<my_app>执行以下命令，构建并烧录应用：

```text
west build -b cc3235sf_launchxl <my_app>
west flash
```

这会将镜像加载到闪存。

另开终端连接UART0，查看程序输出：

```text
% screen /dev/ttyACM0 115200 8N1
```

随后按下开发板复位键SW1运行程序。

使用Zephyr SDK中的OpenOCD烧录时，若应用使用网络处理器，可能在启动该处理器时挂起。原文指出该版本OpenOCD复位网络处理器存在已知问题，烧录后需手动按开发板复位键，使设备正确复位。

<a id="debugging"></a>

### 调试（Debugging）

调试已烧录镜像时，先复位开发板，再使用debug构建目标：

```text
west build -b cc3235sf_launchxl <my_app>
west debug
```

<a id="wi-fi-support"></a>

## Wi-Fi支持（Wi-Fi Support）

从SimpleLink SDK引入的SimpleLink主机驱动已移植到Zephyr，通过专用SPI与网络协处理器通信。对应Zephyr Wi-Fi设备驱动位于[drivers/wifi/simplelink](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/simplelink)。

<a id="usage"></a>

### 用法（Usage）：

将[CONFIG_WIFI_SIMPLELINK](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_SIMPLELINK)及[CONFIG_WIFI](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)设为y以启用Wi-Fi，参见[samples/net/wifi/shell/boards/cc3235sf_launchxl.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/wifi/shell/boards/cc3235sf_launchxl.conf)。

<a id="provisioning"></a>

### 配置准备（Provisioning）：

SimpleLink提供多种较复杂的Wi-Fi配网（Provisioning）方式。为简化Zephyr开发及演示，启用了单次扫描的快速连接（Fast Connect）策略，使cc3235sf_launchxl自动重连上次成功使用的接入点（AP），无需再次扫描或重新指定SSID及密码。

连接AP前，先运行Zephyr Wi-Fi shell示例，通过SSID及密码连接已知AP。

参见[Wi-Fi shell](../networking/P169_WiFi命令行示例.md#wifi-shell)。

连接成功后，网络协处理器将AP标识保存在持久存储器中。新加载的Wi-Fi应用无需显式执行扫描或连接，直到需要切换到新的AP。

<a id="secure-socket-offload"></a>

## 安全套接字卸载（Secure Socket Offload）

SimpleLink Wi-Fi驱动向Zephyr套接字卸载接口提供socket操作。将[CONFIG_NET_SOCKETS_OFFLOAD](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_OFFLOAD)设为y，可将Zephyr BSD套接字API调用交由SimpleLink Wi-Fi驱动处理。

安全套接字TLS通信作为套接字API的一部分处理，启用方式为：


- 将[CONFIG_NET_SOCKETS_SOCKOPT_TLS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_SOCKOPT_TLS)及[CONFIG_TLS_CREDENTIAL_FILENAMES](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TLS_CREDENTIAL_FILENAMES)都设为y；
- 使用TI UniFlash将所需证书及密钥写入安全闪存文件系统，并启用TI受信任根证书目录（Trusted Root-Certificate Catalog）。

示例见“[HTTP GET using plain sockets](../networking/P051_普通套接字HTTP_GET示例.md#sockets-http-get)”及[samples/net/sockets/http_get/boards/cc3235sf_launchxl.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/http_get/boards/cc3235sf_launchxl.conf)。

<a id="id19"></a>

使用TI UniFlash写入证书的详情见《[Simplelink Wi-Fi Certificates Handling](http://www.ti.com/lit/pdf/swpu332)》[注8](#id18)。

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [http://www.ti.com/product/cc3235SF](http://www.ti.com/product/cc3235SF)

<a id="id3"></a>

〔2〕 ([1](#id4),[2](#id5)) [http://www.ti.com/lit/pdf/swru543](http://www.ti.com/lit/pdf/swru543)

<a id="id6"></a>

〔3〕 ([1](#id7),[2](#id8)) [http://dev.ti.com/tirex/content/simplelink_cc32xx_sdk_2_40_01_01/docs/simplelink_mcu_sdk/Quick_Start_Guide.html](http://dev.ti.com/tirex/content/simplelink_cc32xx_sdk_2_40_01_01/docs/simplelink_mcu_sdk/Quick_Start_Guide.html)

<a id="id9"></a>

〔4〕 ([1](#id10),[2](#id11)) [http://processors.wiki.ti.com/index.php/Category:CCS_UniFlash](http://processors.wiki.ti.com/index.php/Category:CCS_UniFlash)

<a id="id12"></a>

〔[5](#id13)〕 [http://www.ti.com/tool/download/SIMPLELINK-CC32xx-SDK/2.40.01.01](http://www.ti.com/tool/download/SIMPLELINK-CC32xx-SDK/2.40.01.01)

<a id="id14"></a>

〔[6](#id15)〕 [http://www.ti.com/lit/pdf/swru539](http://www.ti.com/lit/pdf/swru539)

<a id="id16"></a>

〔[7](#id17)〕 [http://processors.wiki.ti.com/index.php/XDS_Emulation_Software_Package#XDS_Emulation_Software_.28emupack.29_Download](http://processors.wiki.ti.com/index.php/XDS_Emulation_Software_Package#XDS_Emulation_Software_.28emupack.29_Download)

<a id="id18"></a>

〔[8](#id19)〕 [http://www.ti.com/lit/pdf/swpu332](http://www.ti.com/lit/pdf/swpu332)

TI SimpleLink微控制器（MCU）：

[http://www.ti.com/microcontrollers/simplelink-mcus/overview.html](http://www.ti.com/microcontrollers/simplelink-mcus/overview.html)

## 译注

CC3235SF支持2.4 GHz及5 GHz，独立保留CONFIG_CC3235SF_DEBUG及板级配置。Wi-Fi Fast Connect保存上次AP，TLS卸载还需UniFlash写入证书与密钥。原文历史Wiki链接保留并报告外链检查结果。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [Category:CCS_UniFlash](http://processors.wiki.ti.com/index.php/Category:CCS_UniFlash)：HTTP Error 421: Misdirected Request。
- [XDS_Emulation_Software_Package](http://processors.wiki.ti.com/index.php/XDS_Emulation_Software_Package#XDS_Emulation_Software_.28emupack.29_Download)：HTTP Error 421: Misdirected Request。
- [emu_xds110.html](http://software-dl.ti.com/ccs/esd/documents/xdsdebugprobes/emu_xds110.html#updating-the-xds110-firmware)：页面可访问，但未确认目标片段。

---

[上一章](P009_CC3220SF_LaunchXL.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P011_The_AM64x_AM243x_bootflow.md)
