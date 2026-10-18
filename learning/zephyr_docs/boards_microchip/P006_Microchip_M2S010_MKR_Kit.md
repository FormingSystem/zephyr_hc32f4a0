---
id: learning.zephyr-docs.boards-microchip.page-6
title: Microchip M2S010 MKR Kit
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/microchip/m2s010_mkr_kit/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="m2s010_mkr_kit"></a>

# 第6章\_Microchip M2S010 MKR套件（Kit）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/microchip/m2s010_mkr_kit/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`m2s010_mkr_kit`

厂商（Vendor）：

[微芯科技（Microchip Technology Inc.）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=microchip)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[m2s010](https://docs.zephyrproject.org/latest/boards/index.html#soc=m2s010)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/microchip/m2s010_mkr_kit/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

Microchip M2S010-MKR-KIT是基于M2S010器件的SmartFusion2 FPGA开发套件，集成Arm Cortex-M3子系统。此移植的Zephyr目标为m2s010_mkr_kit/m2s010。

套件参考资料见Microchip M2S010-MKR-KIT快速入门指南。（[Microchip M2S010-MKR-KIT快速入门指南（Quick Start Guide）](https://ww1.microchip.com/downloads/aemdocuments/documents/fpga/ProductDocuments/UserGuides/microsemi_digikey_quick_start_guide_120x180mm.pdf)）

<a id="programming-and-debugging"></a>

## 编程与调试（Programming and Debugging）

`m2s010_mkr_kit`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

<a id="building"></a>

### 构建（Building）

m2s010_mkr_kit/m2s010目标应用可按通常方式构建：

```text
west build -b m2s010_mkr_kit/m2s010
```

<a id="clock-configuration"></a>

### 时钟配置（Clock Configuration）

当前SmartFusion2移植不会由Zephyr编程微控制器子系统（MSS）时钟树。实际CPU及外设时钟必须预先在SmartFusion2硬件设计中配置，例如在生成开发板镜像所用的MSS／Libero配置中设置。

Zephyr中软件可见的CPU频率来自设备树CPU节点：


- `&cpu0 { clock-frequency = <...>; }`

该数值用于推导：


- `CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC`
- SmartFusion2 SoC移植使用的SystemCoreClock变量

SmartFusion2专用时钟控制器节点目前用于UART时钟，其余外设仍使用各自设备树频率属性。硬件时钟配置改变后，必须同步更新设备树，使其匹配真实硬件。例如，可通过应用设备树覆盖文件修改CPU及外设时钟描述值：

```text
&cpu0 {
   clock-frequency = <80000000>;
};

&clkc {
   clock-frequencies = <80000000 40000000>;
};
```

设备树中的数值必须描述真实硬件时钟。只修改Zephyr中的这些数值，并不会重新编程SmartFusion2时钟硬件。

<a id="flashing"></a>

### 烧录（Flashing）

开发板使用board.cmake及support/openocd.cfg中的OpenOCD运行配置。主机具备该套件所需CMSIS-DAP／OpenOCD环境后，通常执行：

```text
west flash --runner openocd
west debug --runner openocd
```

<a id="helpful-documentation"></a>

## 参考文档（Helpful Documentation）

扩展开发板支持或向上游提交时，以下Microchip文档很有帮助。

<a id="board-documentation"></a>

### 开发板文档（Board Documentation）


- [M2S010-MKR-KIT快速入门指南（Quick Start Guide）](https://ww1.microchip.com/downloads/aemdocuments/documents/fpga/ProductDocuments/UserGuides/microsemi_digikey_quick_start_guide_120x180mm.pdf)

<a id="soc-documentation"></a>

### SoC文档（Documentation）


- [IGLOO 2 FPGA及SmartFusion 2 SoC FPGA数据手册，DS00004750](https://ww1.microchip.com/downloads/aemDocuments/documents/FPGA/ProductDocuments/DataSheets/IGLOO-2-FPGA-And-SmartFusion-2-SoC-FPGA-Data-Sheet-DS00004750.pdf)
- [SmartFusion2及IGLOO2编程用户指南，UG0451](https://ww1.microchip.com/downloads/aemdocuments/documents/FPGA/ProductDocuments/SoC/microsemi_smartfusion2_igloo2_programming_user_guide_ug0451_v9.pdf)

快速入门指南适用于开发板初次启动、连接器概览及套件内容。器件数据手册更适合作为封装选项、存储器容量、硬IP清单及电气能力的总体参考。编程指南则适合查阅闪存编程、器件配置流程、启动／编程模式及调试设置。

<a id="hardware"></a>

## 硬件（Hardware）

当前板级支持包（BSP）对以下已验证平台模块建模：


- ARM Cortex-M3处理器（CPU）
- 嵌套向量中断控制器（NVIC）
- 用于代码存储的256 KB嵌入式非易失性存储器（eNVM）
- 64 KB静态随机存储器（SRAM）
- MSS UART0作为Zephyr控制台
- MSS GPIO，其中GPIO0的0号引脚连接一个用户LED

设备树还枚举其他SmartFusion2外设模块，以便相应Zephyr驱动进入上游后逐步启用：


- SPI0及SPI1
- I2C0及I2C1
- PDMA
- 定时器及看门狗（Timers and Watchdog）
- CAN及实时时钟（RTC）

<table>
<tr>
<th>接口（Interface）</th>
<th>控制器（Controller）</th>
<th>驱动／组件（Driver/Component）</th>
</tr>
<tr>
<td>嵌套向量中断控制器（NVIC）</td>
<td>片上（On-Chip）</td>
<td>嵌套向量中断控制器（Nested Vectored Interrupt Controller）。</td>
</tr>
<tr>
<td>系统节拍（SYSTICK）</td>
<td>片上（On-Chip）</td>
<td>systick</td>
</tr>
<tr>
<td>通用异步收发器（UART）</td>
<td>MSS UART0</td>
<td><code>ns16550</code></td>
</tr>
<tr>
<td>通用输入输出（GPIO）</td>
<td>MSS GPIO</td>
<td>通用输入输出（gpio）</td>
</tr>
<tr>
<td>闪存（FLASH）</td>
<td>eNVM</td>
<td><code>soc-nv-flash</code></td>
</tr>
</table>

其他片上外设虽在设备树描述，但会保持禁用，直至相应Zephyr驱动可用且已在开发板验证。

<a id="pin-and-interface-mapping"></a>

## 引脚及接口映射（Pin and Interface Mapping）

下表汇总原文从套件附带的DIGIKEY MAKER KIT REVA1_0_20170606.pdf原理图提取的板级接线。信号名称采用原理图网络名称及SmartFusion2封装球位名称。

<a id="user-leds-and-buttons"></a>

### 用户LED及按键（User LEDs and Buttons）

<table>
<tr>
<th>开发板功能（Board Function）</th>
<th>SmartFusion2信号（Signal）</th>
<th>备注（Notes）</th>
</tr>
<tr>
<td><code>led0</code></td>
<td><code>DDRIO47PB0</code></td>
<td>在Zephyr中表示为LED0</td>
</tr>
<tr>
<td><code>LED1</code></td>
<td><code>DDRIO47NB0</code></td>
<td>板载红色LED</td>
</tr>
<tr>
<td>LED2／LED3</td>
<td>DDRIO44PB0及DDRIO44NB0</td>
<td>八LED阵列中间的一对</td>
</tr>
<tr>
<td>LED4</td>
<td><code>DDRIO43PB0</code></td>
<td>板载红色LED</td>
</tr>
<tr>
<td>LED5</td>
<td><code>DDRIO43NB0</code></td>
<td>板载红色LED</td>
</tr>
<tr>
<td>LED6</td>
<td><code>DDRIO37PB0</code></td>
<td>板载红色LED</td>
</tr>
<tr>
<td><code>LED7</code></td>
<td><code>DDRIO37NB0</code></td>
<td>板载红色LED</td>
</tr>
<tr>
<td>USER_PB1</td>
<td><code>DDRIO59PB0/GB0</code></td>
<td>用户按键SW1</td>
</tr>
<tr>
<td>USER_PB2</td>
<td><code>DDRIO63PB0</code></td>
<td>用户按键SW2</td>
</tr>
<tr>
<td><code>SF2_RST_N</code></td>
<td>专用复位网络（Dedicated Reset Net）</td>
<td>复位按键SW3</td>
</tr>
</table>

原理图将分立LED标为D2至D9。当前启用的Zephyr LED对应LED0网络，连接到DDRIO47PB0。

<a id="debug-clock-and-console-routing"></a>

### 调试、时钟及控制台走线（Routing）

<table>
<tr>
<th>功能（Function）</th>
<th>SmartFusion2信号（Signal）</th>
<th>外部器件（External Device）</th>
</tr>
<tr>
<td>主振荡器（Main Oscillator）</td>
<td><code>XTLOSC_MAIN_XTAL/EXTAL</code></td>
<td>32.768 kHz晶体</td>
</tr>
<tr>
<td>辅助振荡器（Auxiliary Oscillator）</td>
<td><code>XTLOSC_AUX_XTAL/EXTAL</code></td>
<td>原理图标注不安装（DNI）</td>
</tr>
<tr>
<td>JTAG选择（Select）</td>
<td><code>JTAGSEL</code></td>
<td>排针／跳线网络（Header / Jumper Network）</td>
</tr>
<tr>
<td>JTAG测试数据输出（TDO）</td>
<td><code>JTAG_TDO/M3_TDO/M3_SWO</code></td>
<td>FT4232H JTAG桥接器</td>
</tr>
<tr>
<td>JTAG测试时钟（TCK）</td>
<td><code>JTAG_TCK/M3_TCK</code></td>
<td>FT4232H JTAG桥接器</td>
</tr>
<tr>
<td>JTAG测试复位（TRST）</td>
<td><code>JTAG_TRSTB/M3_TRSTB</code></td>
<td>FT4232H JTAG桥接器</td>
</tr>
<tr>
<td>JTAG测试模式选择（TMS）／串行线调试数据（SWDIO）</td>
<td><code>JTAG_TMS/M3_TMS/M3_SWDIO</code></td>
<td>FT4232H JTAG桥接器</td>
</tr>
<tr>
<td>JTAG测试数据输入（TDI）</td>
<td><code>JTAG_TDI/M3_TDI</code></td>
<td>FT4232H JTAG桥接器</td>
</tr>
<tr>
<td>MSS UART发送（TX）</td>
<td><code>UART_TXD_OUT</code></td>
<td>FT4232H USB串口（UART）</td>
</tr>
<tr>
<td>MSS UART接收（RX）</td>
<td><code>UART_RXD_IN</code></td>
<td>FT4232H USB串口（UART）</td>
</tr>
<tr>
<td>USB UART发送网络（TX Net）</td>
<td><code>USB_UART_TXD</code></td>
<td>连接到FT4232H</td>
</tr>
<tr>
<td>USB UART接收网络（RX Net）</td>
<td><code>USB_UART_RXD</code></td>
<td>连接到FT4232H</td>
</tr>
</table>

<a id="on-board-spi-flash-and-light-sensor"></a>

### 板载SPI闪存及光传感器（Light Sensor）

<table>
<tr>
<th>外设信号（Peripheral Signal）</th>
<th>SmartFusion2信号（Signal）</th>
<th>连接的器件（Connected Device）</th>
</tr>
<tr>
<td><code>SPI_0_SS0</code></td>
<td><code>MSIO13NB2 / GPIO_7_A</code></td>
<td>AT25SF161片选（CS）</td>
</tr>
<tr>
<td><code>SPI_0_SDI</code></td>
<td><code>MSIO12NB2 / GPIO_5_A</code></td>
<td>AT25SF161串行输入（SI）</td>
</tr>
<tr>
<td><code>SPI_0_SDO</code></td>
<td><code>MSIO13PB2 / GPIO_6_A</code></td>
<td>AT25SF161串行输出（SO）</td>
</tr>
<tr>
<td><code>SPI_0_CLK</code></td>
<td><code>MSIO12PB2</code></td>
<td>AT25SF161串行时钟（SCK）</td>
</tr>
<tr>
<td><code>SPI_0_WP_N</code></td>
<td><code>MSIO2PB2 / USB_STP_B</code></td>
<td>AT25SF161低电平写保护（WP#）</td>
</tr>
<tr>
<td><code>SPI_0_HOLD_N</code></td>
<td><code>MSIO2NB2 / USB_NXT_B</code></td>
<td>AT25SF161低电平保持（HOLD#）</td>
</tr>
<tr>
<td><code>LIGHT_SDA</code></td>
<td><code>MSIO4NB2 / USB_DATA3_B</code></td>
<td>LTR-329ALS串行数据（SDA）</td>
</tr>
<tr>
<td><code>LIGHT_SCL</code></td>
<td><code>MSIO4PB2 / USB_DATA2_B</code></td>
<td>LTR-329ALS串行时钟（SCL）</td>
</tr>
</table>

<a id="optional-esp8266-footprint"></a>

### 可选ESP8266封装焊盘（Footprint）

原理图包含标为未安装的可选ESP8266模块焊盘，其走线仍可供扩展板级支持时参考：

<table>
<tr>
<th>ESP8266信号（Signal）</th>
<th>SmartFusion2信号（Signal）</th>
<th>备注（Notes）</th>
</tr>
<tr>
<td><code>MOD1_TX</code></td>
<td><code>MSIO1PB2 / USB_XCLK_B</code></td>
<td>ESP8266发送输出（TXO）</td>
</tr>
<tr>
<td><code>MOD1_RX</code></td>
<td><code>MSIO1NB2 / USB_DIR_B</code></td>
<td>ESP8266接收输入（RXI）</td>
</tr>
<tr>
<td><code>MOD1_CE</code></td>
<td><code>MSIO3NB2 / USB_DATA1_B</code></td>
<td>ESP8266 CHPD</td>
</tr>
<tr>
<td><code>MOD1_RST</code></td>
<td><code>MSIO3PB2 / USB_DATA0_B</code></td>
<td>ESP8266复位（Reset）</td>
</tr>
<tr>
<td><code>MOD1_GPIO2</code></td>
<td><code>MSIO0NB2 / USB_DATA7_B</code></td>
<td>ESP8266 GPIO2</td>
</tr>
<tr>
<td><code>MOD1_GPIO0</code></td>
<td><code>MSIO5NB2 / USB_DATA5_B</code></td>
<td>ESP8266 GPIO0</td>
</tr>
<tr>
<td>备用走线（Spare Routing）</td>
<td><code>MSIO5PB2 / USB_DATA4_B</code></td>
<td>标为BANK2_UNUSED1</td>
</tr>
<tr>
<td>备用走线（Spare Routing）</td>
<td><code>MSIO6PB2 / USB_DATA6_B</code></td>
<td>标为BANK2_UNUSED2</td>
</tr>
</table>

<a id="optional-esp-wroom-32-header"></a>

### 可选ESP-WROOM-32排针（Header）

原理图第6页还在Bank 7引出一组未安装的ESP-WROOM-32／Wi-Fi-BT-BLE排针走线：

<table>
<tr>
<th>排针／网络（Header/net）</th>
<th>SmartFusion2信号（Signal）</th>
<th>备注（Notes）</th>
</tr>
<tr>
<td><code>USB_UART_TXD</code></td>
<td><code>MSIO64NB7</code></td>
<td>模块UART</td>
</tr>
<tr>
<td><code>USB_UART_RXD</code></td>
<td><code>MSIO64PB7</code></td>
<td>模块UART</td>
</tr>
<tr>
<td><code>BT_TX</code></td>
<td><code>MSIO67NB7</code></td>
<td>模块串行接口（Serial）</td>
</tr>
<tr>
<td><code>BT_RX</code></td>
<td><code>MSIO67PB7</code></td>
<td>模块串行接口（Serial）</td>
</tr>
<tr>
<td><code>BT_BOOT</code></td>
<td><code>MSIO71NB7</code></td>
<td>启动配置引脚（Boot Strap）</td>
</tr>
<tr>
<td><code>BT_IO34</code></td>
<td><code>MSIO71PB7</code></td>
<td>通用输入输出（GPIO）</td>
</tr>
<tr>
<td><code>BT_IO35</code></td>
<td><code>MSIO72NB7</code></td>
<td>通用输入输出（GPIO）</td>
</tr>
<tr>
<td><code>BT_IO18</code></td>
<td><code>MSIO73NB7</code></td>
<td>通用输入输出（GPIO）</td>
</tr>
<tr>
<td><code>BT_IO22</code></td>
<td><code>MSIO76NB7</code></td>
<td>通用输入输出（GPIO）</td>
</tr>
<tr>
<td><code>BT_IO23</code></td>
<td><code>MSIO77NB7</code></td>
<td>通用输入输出（GPIO）</td>
</tr>
<tr>
<td><code>BT_EN</code></td>
<td><code>MSIO79NB7</code></td>
<td>使能（Enable）</td>
</tr>
<tr>
<td><code>BT_IO2</code></td>
<td><code>MSIO79PB7/GB1</code></td>
<td>通用输入输出（GPIO）</td>
</tr>
<tr>
<td>J12第1脚</td>
<td><code>ESP32_SCS</code></td>
<td>SPI片选（Chip Select）</td>
</tr>
<tr>
<td>J12第2脚</td>
<td><code>ESP32_SCK</code></td>
<td>SPI时钟（Clock）</td>
</tr>
<tr>
<td>J12第3脚</td>
<td><code>ESP32_SDO</code></td>
<td>SPI主机输入从机输出（MISO）</td>
</tr>
<tr>
<td>J12第4脚</td>
<td><code>ESP32_SDI</code></td>
<td>SPI主机输出从机输入（MOSI）</td>
</tr>
</table>

<a id="ethernet-phy-wiring"></a>

### 以太网PHY接线（Wiring）

VSC8541 PHY直接连接SmartFusion2可编程逻辑（Fabric）的Bank 4及Bank 6。原文明确提取出的信号分配如下：

<table>
<tr>
<th>PHY／千兆媒体独立接口（GMII）信号</th>
<th>SmartFusion2信号（Signal）</th>
<th>引脚组（Bank）</th>
</tr>
<tr>
<td><code>CLK_50MHZ_SF2</code></td>
<td><code>MSIOD84PB6/CCC_NE1_CLKI2</code></td>
<td>Bank 6引脚组</td>
</tr>
<tr>
<td><code>GMII_TX_CLK</code></td>
<td><code>MSIOD85PB6/CCC_NE1_CLKI1</code></td>
<td>Bank 6引脚组</td>
</tr>
<tr>
<td><code>GMII_MDIO</code></td>
<td><code>MSIOD90NB6</code></td>
<td>Bank 6引脚组</td>
</tr>
<tr>
<td><code>GMII_MDC</code></td>
<td><code>MSIOD90PB6</code></td>
<td>Bank 6引脚组</td>
</tr>
<tr>
<td><code>GMII_TXD7</code></td>
<td><code>MSIOD93NB6</code></td>
<td>Bank 6引脚组</td>
</tr>
<tr>
<td><code>GMII_TXD6</code></td>
<td><code>MSIOD93PB6</code></td>
<td>Bank 6引脚组</td>
</tr>
<tr>
<td><code>GMII_TXD5</code></td>
<td><code>MSIOD96PB6</code></td>
<td>Bank 6引脚组</td>
</tr>
<tr>
<td><code>GMII_TXD4</code></td>
<td><code>MSIOD96NB6</code></td>
<td>Bank 6引脚组</td>
</tr>
<tr>
<td><code>GMII_TXD3</code></td>
<td><code>MSIOD98NB6</code></td>
<td>Bank 6引脚组</td>
</tr>
<tr>
<td><code>GMII_TXD2</code></td>
<td><code>MSIOD99PB6</code></td>
<td>Bank 6引脚组</td>
</tr>
<tr>
<td><code>GMII_TXD1</code></td>
<td><code>MSIOD99NB6</code></td>
<td>Bank 6引脚组</td>
</tr>
<tr>
<td><code>GMII_GTX_CLK</code></td>
<td><code>MSIO102NB4/CCC_NE1_CLKI0</code></td>
<td>Bank 4引脚组</td>
</tr>
<tr>
<td><code>GMII_RXD7</code></td>
<td><code>MSIO113NB4</code></td>
<td>Bank 4引脚组</td>
</tr>
<tr>
<td><code>GMII_RXD6</code></td>
<td><code>MSIO113PB4</code></td>
<td>Bank 4引脚组</td>
</tr>
<tr>
<td><code>GMII_RX_DV</code></td>
<td><code>MSIO105NB4</code></td>
<td>Bank 4引脚组</td>
</tr>
<tr>
<td><code>GMII_RX_CLK</code></td>
<td><code>MSIO105PB4/CCC_NE0_CLKI0</code></td>
<td>Bank 4引脚组</td>
</tr>
<tr>
<td><code>GMII_RXD1</code></td>
<td><code>MSIO106NB4</code></td>
<td>Bank 4引脚组</td>
</tr>
<tr>
<td><code>GMII_RXD0</code></td>
<td><code>MSIO106PB4</code></td>
<td>Bank 4引脚组</td>
</tr>
<tr>
<td><code>GMII_RXD3</code></td>
<td><code>MSIO108NB4</code></td>
<td>Bank 4引脚组</td>
</tr>
</table>

其余VSC8541接收及状态网络也在同一原理图页面上，但原文说明，只有上表分配能通过机器文本提取得到较高置信度结果。在向上游提交以太网支持之前，仍需对照原始原理图PDF完整核验GMII映射。

## 译注

硬件连接、原理图提取及GMII表格均来自本页官方正文，不是本仓库实验补充。Zephyr设备树描述实际硬件时钟，不能替代MSS／Libero的时钟配置；原文对机器提取的GMII连接要求进一步核实，译文保留。

---

[上一章](P005_M2GL025_Mi-V.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P007_Microchip_M2S_Hello_FPGA_Kit.md)
