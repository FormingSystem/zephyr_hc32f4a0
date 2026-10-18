---
id: learning.zephyr-docs.hardware.mipi-0
title: MIPI显示接口定义
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第244章\_MIPI显示接口定义

原文：[group__mipi__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html)。读取日期：2026-10-13，`latest`。

## 244.1\_范围与术语

本页收录 MIPI 联盟（MIPI Alliance）的显示设备常量定义，来自官方头文件 `zephyr/display/mipi_display.h`。**显示串行接口（Display Serial Interface，DSI）**的 **显示命令集（Display Command Set，DCS）**、地址模式寄存器字段和处理器到外设的事务类型均列在下面。

常用名称包括空操作（No Operation，NOP）、查找表（Look-Up Table，LUT）、垂直/水平同步（Vertical/Horizontal Synchronization，VSync/HSync）、传输结束包（End of Transmission Packet，EoTp）以及蓝绿红分量顺序（Blue, Green, Red，BGR）。YCbCr 是亮度 Y 与蓝/红色差 Cb/Cr（Luma, Blue-Difference Chroma, Red-Difference Chroma）的分量命名。`BIT(n)` 是第 n 位掩码宏。

> 译注：内容自适应亮度控制（Content Adaptive Brightness Control，CABC）的展开可对照[显示控制器原厂数据手册第8节](https://community.nxp.com/pwmxy87654/attachments/pwmxy87654/lpcxpresso-ide/2792/1/ILI9488_Preliminary_DS_V090.pdf)；设备描述符块（Device Descriptor Block，DDB）的展开可对照[ST官方术语表](https://wiki.st.com/stm32mpu/wiki/Glossary)。这些资料仅用于补足本页缩写释义，不改变 Zephyr 宏值。

## 244.2\_显示命令集与像素格式常量

以下每行都是宏定义，保留原值及英文命令说明。像素格式的数值是命令参数常量。

| 宏 | 值 | 中文说明与原英文 |
| --- | --- | --- |
| [`MIPI_DCS_NOP`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gadcaf06472d3e281e425bd2d71c5beaed) | `0x00U` | 空操作（NOP）。 |
| [`MIPI_DCS_SOFT_RESET`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gab8c88ef2d316b783d5222a85d0e118ea) | `0x01U` | 软复位（Soft Reset）。 |
| [`MIPI_DCS_GET_COMPRESSION_MODE`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga6d88c902f9d07c1fff0d1e92fe966fad) | `0x03U` | 取得压缩模式（Get Compression Mode）。 |
| [`MIPI_DCS_GET_DISPLAY_ID`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga94cb2e4ce1ae29871de780301d4d59d0) | `0x04U` | 取得显示器标识（Get Display ID）。 |
| [`MIPI_DCS_GET_RED_CHANNEL`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga5007b2e6e6e7750d13cb8421ff06d8e7) | `0x06U` | 取得红色通道（Get Red Channel）。 |
| [`MIPI_DCS_GET_GREEN_CHANNEL`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaa40f1c03dca04961a28dd19754212f06) | `0x07U` | 取得绿色通道（Get Green Channel）。 |
| [`MIPI_DCS_GET_BLUE_CHANNEL`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaf1091bc7718eb7aa3a2c72c5c025ab4d) | `0x08U` | 取得蓝色通道（Get Blue Channel）。 |
| [`MIPI_DCS_GET_DISPLAY_STATUS`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaca8b503fdca34456ca68ced074873424) | `0x09U` | 取得显示状态（Get Display Status）。 |
| [`MIPI_DCS_GET_POWER_MODE`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga48669397e8ea5a7c6e0cb09ea9d4fd5c) | `0x0AU` | 取得电源模式（Get Power Mode）。 |
| [`MIPI_DCS_GET_ADDRESS_MODE`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga9da041d715731d8d67caad967e5d6002) | `0x0BU` | 取得地址模式（Get Address Mode）。 |
| [`MIPI_DCS_GET_PIXEL_FORMAT`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gae7088fe2f1351d534262d111692a1bfa) | `0x0CU` | 取得像素格式（Get Pixel Format）。 |
| [`MIPI_DCS_GET_DISPLAY_MODE`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaf752f812f791e805fbfed0d3ab9b89de) | `0x0DU` | 取得显示模式（Get Display Mode）。 |
| [`MIPI_DCS_GET_SIGNAL_MODE`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaa80bc31f551b39eff6625e80c211f16a) | `0x0EU` | 取得信号模式（Get Signal Mode）。 |
| [`MIPI_DCS_GET_DIAGNOSTIC_RESULT`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga8ec1590be25764411567933943b77869) | `0x0FU` | 取得诊断结果（Get Diagnostic Result）。 |
| [`MIPI_DCS_ENTER_SLEEP_MODE`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga06f9b8e87b6f1f6f41a139db370f236b) | `0x10U` | 进入睡眠模式（Enter Sleep Mode）。 |
| [`MIPI_DCS_EXIT_SLEEP_MODE`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga276231424603f027583ffd2a1bdd6089) | `0x11U` | 退出睡眠模式（Exit Sleep Mode）。 |
| [`MIPI_DCS_ENTER_PARTIAL_MODE`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga219bb0ba9e91812f4ab372adaa9afd07) | `0x12U` | 进入局部模式（Enter Partial Mode）。 |
| [`MIPI_DCS_ENTER_NORMAL_MODE`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaedb3b5fa815593d3fa1ae247383d8a8e) | `0x13U` | 进入正常模式（Enter Normal Mode）。 |
| [`MIPI_DCS_EXIT_INVERT_MODE`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga41a4fd226d8f86ba2efa34403b4033f8) | `0x20U` | 退出反相模式（Exit Invert Mode）。 |
| [`MIPI_DCS_ENTER_INVERT_MODE`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gad1041d71940752f1c1121cf392a3b2d3) | `0x21U` | 进入反相模式（Enter Invert Mode）。 |
| [`MIPI_DCS_SET_GAMMA_CURVE`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga14771de93ba08dffabafffcedc85b54e) | `0x26U` | 设置伽马曲线（Set Gamma Curve）。 |
| [`MIPI_DCS_SET_DISPLAY_OFF`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaf50a5539c89552512ffcd04ece5b7fe0) | `0x28U` | 关闭显示（Set Display Off）。 |
| [`MIPI_DCS_SET_DISPLAY_ON`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gabdbee428ef6d48009a5795e384665c8f) | `0x29U` | 开启显示（Set Display On）。 |
| [`MIPI_DCS_SET_COLUMN_ADDRESS`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga2d08791d990c2e4d9c6c9800ad2d8c1b) | `0x2AU` | 设置列地址（Set Column Address）。 |
| [`MIPI_DCS_SET_PAGE_ADDRESS`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga63334f8e1458151197a35c7d5cf781a5) | `0x2BU` | 设置页地址（Set Page Address）。 |
| [`MIPI_DCS_WRITE_MEMORY_START`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga9a31b4772025e2046816057b74d2e7cd) | `0x2CU` | 开始写存储器（Write Memory Start）。 |
| [`MIPI_DCS_WRITE_LUT`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga6f94b4db07db5a287cd50ed87197a9c2) | `0x2DU` | 写入查找表（Write LUT）。 |
| [`MIPI_DCS_READ_MEMORY_START`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga860180f5477caadae3857b4c93f04281) | `0x2EU` | 开始读存储器（Read Memory Start）。 |
| [`MIPI_DCS_SET_PARTIAL_ROWS`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga18fe9e1cf30da71c18bebce1960095c3) | `0x30U` | 设置局部行（Set Partial Rows）。 |
| [`MIPI_DCS_SET_PARTIAL_COLUMNS`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga359a43a0bb277b8f09fa1120bb2c3b09) | `0x31U` | 设置局部列（Set Partial Columns）。 |
| [`MIPI_DCS_SET_SCROLL_AREA`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga36aa83afeed02df37cb2bb295915c92d) | `0x33U` | 设置滚动区域（Set Scroll Area）。 |
| [`MIPI_DCS_SET_TEAR_OFF`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gadcd4fd3ea6ccbb63ebecb290c00c660f) | `0x34U` | 关闭撕裂同步输出（Set Tear Off）。 |
| [`MIPI_DCS_SET_TEAR_ON`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gad85387743db362579b788fd28ecd2fbf) | `0x35U` | 开启撕裂同步输出（Set Tear On）。 |
| [`MIPI_DCS_SET_ADDRESS_MODE`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga1d7e5a77666d13f4a8a435db202f4323) | `0x36U` | 设置地址模式（Set Address Mode）。 |
| [`MIPI_DCS_SET_SCROLL_START`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaee29e37b0cb4b10920211048e0d95756) | `0x37U` | 设置滚动起点（Set Scroll Start）。 |
| [`MIPI_DCS_EXIT_IDLE_MODE`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaf0a1f7ede08492751141cf52235808b3) | `0x38U` | 退出空闲模式（Exit Idle Mode）。 |
| [`MIPI_DCS_ENTER_IDLE_MODE`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga7f1dfc0645ab456b38ac2caae783b709) | `0x39U` | 进入空闲模式（Enter Idle Mode）。 |
| [`MIPI_DCS_SET_PIXEL_FORMAT`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga1165d0835844eb0bd86fa6d30db7a84d) | `0x3AU` | 设置像素格式（Set Pixel Format）。 |
| [`MIPI_DCS_WRITE_MEMORY_CONTINUE`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga532122daccbd1370332fd9c26569c11f) | `0x3CU` | 继续写存储器（Write Memory Continue）。 |
| [`MIPI_DCS_SET_3D_CONTROL`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaf9210d3033c2b09a7da608e9aeb88ad1) | `0x3DU` | 设置三维控制（Set 3D Control）。 |
| [`MIPI_DCS_READ_MEMORY_CONTINUE`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga6d3fcf5c050b45d8afe3af4ec98adadc) | `0x3EU` | 继续读存储器（Read Memory Continue）。 |
| [`MIPI_DCS_GET_3D_CONTROL`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaace0882d961807760db2ed7693ab760a) | `0x3FU` | 取得三维控制（Get 3D Control）。 |
| [`MIPI_DCS_SET_VSYNC_TIMING`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga9597f72175b99376f7119b95cf425c1c) | `0x40U` | 设置垂直同步时序（Set VSync Timing）。 |
| [`MIPI_DCS_SET_TEAR_SCANLINE`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaaac44d1367419dc395332712b0427458) | `0x44U` | 设置撕裂同步扫描行（Set Tear Scanline）。 |
| [`MIPI_DCS_GET_SCANLINE`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga7933493853f9ef2dd28b31ea2fbb492f) | `0x45U` | 取得扫描行（Get Scanline）。 |
| [`MIPI_DCS_SET_DISPLAY_BRIGHTNESS`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gac8dec8303a247b56a513628645d67f2b) | `0x51U` | 设置显示亮度（Set Display Brightness）。 |
| [`MIPI_DCS_GET_DISPLAY_BRIGHTNESS`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga4df917017e27912a343731b350e8d02e) | `0x52U` | 取得显示亮度（Get Display Brightness）。 |
| [`MIPI_DCS_WRITE_CONTROL_DISPLAY`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gad47f873520b505e3463ad1f85d617787) | `0x53U` | 写入显示控制（Write Control Display）。 |
| [`MIPI_DCS_GET_CONTROL_DISPLAY`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga9f83f0b2412084ab2ac3edd36b41fc11) | `0x54U` | 取得显示控制（Get Control Display）。 |
| [`MIPI_DCS_WRITE_POWER_SAVE`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga2655d637a53b1b5e805ab3d69bc9fe9e) | `0x55U` | 写入节能设置（Write Power Save）。 |
| [`MIPI_DCS_GET_POWER_SAVE`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga518ba3d308b6c453850e5168b26d1024) | `0x56U` | 取得节能设置（Get Power Save）。 |
| [`MIPI_DCS_SET_CABC_MIN_BRIGHTNESS`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gab0d27051994aa70c8baf12a103080e80) | `0x5EU` | 设置内容自适应亮度控制的最低亮度（Set CABC Min Brightness）。 |
| [`MIPI_DCS_GET_CABC_MIN_BRIGHTNESS`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga2d56066851a38acf38323cd2327820c4) | `0x5FU` | 取得内容自适应亮度控制的最低亮度（Get CABC Min Brightness）。 |
| [`MIPI_DCS_READ_DDB_START`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga6cccd95a6bc9c007bb648b70d664c34d) | `0xA1U` | 开始读取设备描述符块（Read DDB Start）。 |
| [`MIPI_DCS_READ_DDB_CONTINUE`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga26b4f0111aee93b8ad01448d7b4af368) | `0xA8U` | 继续读取设备描述符块（Read DDB Continue）。 |
| [`MIPI_DCS_PIXEL_FORMAT_24BIT`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga2772b5432484431573d092447c12e005) | `0x77` | 24 位像素格式（24-bit Pixel Format）。 |
| [`MIPI_DCS_PIXEL_FORMAT_18BIT`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gab2d74d3cc0ce8036b57d5aec073b5b6b) | `0x66` | 18 位像素格式（18-bit Pixel Format）。 |
| [`MIPI_DCS_PIXEL_FORMAT_16BIT`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga171be8bd1a5551ffc129c14e0d829e61) | `0x55` | 16 位像素格式（16-bit Pixel Format）。 |
| [`MIPI_DCS_PIXEL_FORMAT_12BIT`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga77944b2fd7f59be6698bd414cbeedcac) | `0x33` | 12 位像素格式（12-bit Pixel Format）。 |
| [`MIPI_DCS_PIXEL_FORMAT_8BIT`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gac3e18d2d9d4bcfb98d99518021bf98bd) | `0x22` | 8 位像素格式（8-bit Pixel Format）。 |
| [`MIPI_DCS_PIXEL_FORMAT_3BIT`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga5a14ff4ebc8e81b9bc92e87069ad7466) | `0x11` | 3 位像素格式（3-bit Pixel Format）。 |

## 244.3\_地址模式寄存器字段

以下宏定义地址模式（Address Mode）的位字段，镜像（Mirror）与翻转（Flip）按原文区分。

| 宏 | 值 | 中文说明与原英文 |
| --- | --- | --- |
| [`MIPI_DCS_ADDRESS_MODE_MIRROR_Y`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga549bdf77bc40cc4a5cc81004b3f91775) | `BIT(7)` | Y 镜像（Mirror Y）。 |
| [`MIPI_DCS_ADDRESS_MODE_MIRROR_X`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaa9c5f1e04806ef4dd672a6169136d07c) | `BIT(6)` | X 镜像（Mirror X）。 |
| [`MIPI_DCS_ADDRESS_MODE_SWAP_XY`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gadfce4431c308f186479af4d15c83187b) | `BIT(5)` | 交换 X/Y（Swap XY）。 |
| [`MIPI_DCS_ADDRESS_MODE_REFRESH_BT`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gad8591d77dafcb2d1ccc2ce971b012761) | `BIT(4)` | 从下向上刷新（Refresh Bottom to Top）。 |
| [`MIPI_DCS_ADDRESS_MODE_BGR`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga5320efc9a396b1cdfe89c5cfc87d8c11) | `BIT(3)` | 蓝绿红顺序（BGR Order）。 |
| [`MIPI_DCS_ADDRESS_MODE_LATCH_RL`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaa32acf97423f4491b27b2d9cb7d49a3c) | `BIT(2)` | 从右向左锁存（Latch Right to Left）。 |
| [`MIPI_DCS_ADDRESS_MODE_FLIP_X`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga75df1e79cde793c01c47103bf683f3aa) | `BIT(1)` | X 翻转（Flip X）。 |
| [`MIPI_DCS_ADDRESS_MODE_FLIP_Y`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga72cf84630b55cd8dfe762eb84272692f) | `BIT(0)` | Y 翻转（Flip Y）。 |

## 244.4\_处理器到外设的事务类型

以下为处理器到外设（Processor-to-Peripheral）的事务类型宏；短包（Short Packet）、长包（Long Packet）与像素流（Pixel Stream）的说明和参数数目按原文保留。

| 宏 | 值 | 中文说明与原英文 |
| --- | --- | --- |
| [`MIPI_DSI_V_SYNC_START`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gad58c27d600a73e38f33669a3ae743f01) | `0x01U` | 同步事件：垂直同步开始（Sync Event, V Sync Start）。 |
| [`MIPI_DSI_V_SYNC_END`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaf85ef5c73d29fec41460de8b752cef39) | `0x11U` | 同步事件：垂直同步结束（Sync Event, V Sync End）。 |
| [`MIPI_DSI_H_SYNC_START`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga6852f3d6bfb77101d64b10a2b48a91c5) | `0x21U` | 同步事件：水平同步开始（Sync Event, H Sync Start）。 |
| [`MIPI_DSI_H_SYNC_END`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaa8cc494ce41880ec765701ee4beffe97) | `0x31U` | 同步事件：水平同步结束（Sync Event, H Sync End）。 |
| [`MIPI_DSI_COLOR_MODE_OFF`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gad713fb809d6012db370ef23601c81619) | `0x02U` | 关闭颜色模式命令（Color Mode Off Command）。 |
| [`MIPI_DSI_COLOR_MODE_ON`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga1987975c9389ec9570c5ff05e3e1a9b1) | `0x12U` | 开启颜色模式命令（Color Mode On Command）。 |
| [`MIPI_DSI_SHUTDOWN_PERIPHERAL`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gafac7d0f045d77fed0ff35f3a3503f6a5) | `0x22U` | 关闭外设命令（Shutdown Peripheral Command）。 |
| [`MIPI_DSI_TURN_ON_PERIPHERAL`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga56292f7b60a0e7b55cd5118c1641c3ba) | `0x32U` | 开启外设命令（Turn On Peripheral Command）。 |
| [`MIPI_DSI_GENERIC_SHORT_WRITE_0_PARAM`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga639170a23fa7b28e6bf3726c8d54ead0) | `0x03U` | 带 0 个参数的通用短写包（Generic Short WRITE Packet with 0 parameters）。 |
| [`MIPI_DSI_GENERIC_SHORT_WRITE_1_PARAM`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaa0e596feb47e6eada0217fa7a81a0278) | `0x13U` | 带 1 个参数的通用短写包（Generic Short WRITE Packet with 1 parameter）。 |
| [`MIPI_DSI_GENERIC_SHORT_WRITE_2_PARAM`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaea2acb4489552a159a19278018122ce6) | `0x23U` | 带 2 个参数的通用短写包（Generic Short WRITE Packet with 2 parameters）。 |
| [`MIPI_DSI_GENERIC_READ_REQUEST_0_PARAM`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga9d541d3e054b1fa75fd7f1b0ffa3883a) | `0x04U` | 带 0 个参数的通用读请求（Generic READ Request with 0 parameters）。 |
| [`MIPI_DSI_GENERIC_READ_REQUEST_1_PARAM`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gabff929d8285415c0d3edb95748bf2686) | `0x14U` | 带 1 个参数的通用读请求（Generic READ Request with 1 parameter）。 |
| [`MIPI_DSI_GENERIC_READ_REQUEST_2_PARAM`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga9ea3c57a021879863097edc3f275ea60) | `0x24U` | 带 2 个参数的通用读请求（Generic READ Request with 2 parameters）。 |
| [`MIPI_DSI_DCS_SHORT_WRITE`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga51191c76ceca6f0e79cdb4f0e58013a3) | `0x05U` | 无参数 DCS 短写命令（DCS Short Write Command with 0 parameters）。 |
| [`MIPI_DSI_DCS_SHORT_WRITE_PARAM`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga5e0e1bf73a04668617e46cb0392bac8d) | `0x15U` | 带 1 个参数的 DCS 短写命令（DCS Short Write Command with 1 parameter）。 |
| [`MIPI_DSI_DCS_READ`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga60acd68f9c3271b2cd306f6bb5e4af94) | `0x06U` | 无参数 DCS 读请求（DCS Read Request with 0 parameters）。 |
| [`MIPI_DSI_SET_MAXIMUM_RETURN_PACKET_SIZE`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gab07bcea365f9835c5df3c37d15f3073c) | `0x37U` | 设置最大返回包大小命令（Set Maximum Return Packet Size Command）。 |
| [`MIPI_DSI_END_OF_TRANSMISSION`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga575957d9fd4de559cd938b332f1eff05) | `0x08U` | 传输结束包（End of Transmission Packet (EoTp)）。 |
| [`MIPI_DSI_NULL_PACKET`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gabcd142889c213edb8a7e7e95bb138b08) | `0x09U` | 空包，长包（Null Packet (Long)）。 |
| [`MIPI_DSI_BLANKING_PACKET`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga66550282423b364aed89c6ed2c202329) | `0x19U` | 消隐包，长包（Blanking Packet (Long)）。 |
| [`MIPI_DSI_GENERIC_LONG_WRITE`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gadb6e6683462c4b8eaeda3a77b86f3e1d) | `0x29U` | 通用长写（Generic Long Write）。 |
| [`MIPI_DSI_DCS_LONG_WRITE`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga141eda8b32761dc7a275524c04e45535) | `0x39U` | DCS 长写/写查找表命令（DCS Long Write / write_LUT Command）。 |
| [`MIPI_DSI_LOOSELY_PACKED_PIXEL_STREAM_YCBCR20`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga933521f6a7f2f8ebad1569a0e8320d41) | `0x0CU` | 松散打包像素流，20 位 YCbCr 4:2:2（Loosely Packed Pixel Stream, 20-bit YCbCr 4:2:2 Format）。 |
| [`MIPI_DSI_PACKED_PIXEL_STREAM_YCBCR24`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga858695ed8e1f5234d25f44b59a4f270d) | `0x1CU` | 打包像素流，24 位 YCbCr 4:2:2（Packed Pixel Stream, 24-bit YCbCr 4:2:2 Format）。 |
| [`MIPI_DSI_PACKED_PIXEL_STREAM_YCBCR16`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga928d1364d635cb892f5992f7cdda7905) | `0x2CU` | 打包像素流，16 位 YCbCr 4:2:2（Packed Pixel Stream, 16-bit YCbCr 4:2:2 Format）。 |
| [`MIPI_DSI_PACKED_PIXEL_STREAM_30`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga09da8d6976e18b7ac074f9e10cc8c52f) | `0x0DU` | 打包像素流，30 位格式（Packed Pixel Stream, 30-bit Format）。 |
| [`MIPI_DSI_PACKED_PIXEL_STREAM_36`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga0015e0c7df4f3688e5567099f9d0ea11) | `0x1DU` | 打包像素流，36 位格式（Packed Pixel Stream, 36-bit Format）。 |
| [`MIPI_DSI_PACKED_PIXEL_STREAM_YCBCR12`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga999976bf03f40c56ccb9272f99334cdf) | `0x3DU` | 打包像素流，12 位 YCbCr 4:2:0（Packed Pixel Stream, 12-bit YCbCr 4:2:0 Format）。 |
| [`MIPI_DSI_PACKED_PIXEL_STREAM_16`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga93db7cc5b15cd5683ba8b9358731e151) | `0x0EU` | 打包像素流，16 位格式（Packed Pixel Stream, 16-bit Format）。 |
| [`MIPI_DSI_PACKED_PIXEL_STREAM_18`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga3bf54b5ef30c94f863c353ac8a68f0f0) | `0x1EU` | 打包像素流，18 位格式（Packed Pixel Stream, 18-bit Format）。 |
| [`MIPI_DSI_PIXEL_STREAM_3BYTE_18`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaeee3817bcc554f3c04cb737e03649733) | `0x2EU` | 三字节承载的 18 位像素流（Pixel Stream, 18-bit Format in Three Bytes）。 |
| [`MIPI_DSI_PACKED_PIXEL_STREAM_24`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga0956384d8db5940cc6ffe3a4569a2fb2) | `0x3EU` | 打包像素流，24 位格式（Packed Pixel Stream, 24-bit Format）。 |

---

[上一章：Trinamic斜坡发生器参数](P243_Trinamic斜坡发生器参数.md) · [下一章：MIPI显示总线接口](P245_MIPI显示总线接口.md) · [返回大纲](大纲.md)
