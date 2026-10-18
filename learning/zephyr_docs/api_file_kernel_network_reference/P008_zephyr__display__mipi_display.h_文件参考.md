---
id: learning.zephyr-docs.api-file-kernel-network-reference.page-8
title: zephyr__display__mipi_display.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mipi__display_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_zephyr\_\_display\_\_mipi\_display.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mipi__display_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MIPI设备的显示定义（Display Definitions）。

查看此文件的源码。

<a id="details"></a>

MIPI设备的显示定义（Display Definitions）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 8.1\_宏定义（Macros）

<a id="define-members-0"></a>

### MIPI-DSI 显示命令集（MIPI-DSI DCS (Display Command Set)）

<a id="r_gadcaf06472d3e281e425bd2d71c5beaed"></a>

```c
#define MIPI_DCS_NOP 0x00U
```

相关声明：[MIPI_DCS_NOP](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gadcaf06472d3e281e425bd2d71c5beaed)。

空操作（NOP）。

<a id="r_gab8c88ef2d316b783d5222a85d0e118ea"></a>

```c
#define MIPI_DCS_SOFT_RESET 0x01U
```

相关声明：[MIPI_DCS_SOFT_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gab8c88ef2d316b783d5222a85d0e118ea)。

软件复位（Soft Reset）。

<a id="r_ga6d88c902f9d07c1fff0d1e92fe966fad"></a>

```c
#define MIPI_DCS_GET_COMPRESSION_MODE 0x03U
```

相关声明：[MIPI_DCS_GET_COMPRESSION_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga6d88c902f9d07c1fff0d1e92fe966fad)。

获取压缩模式（Get Compression Mode）。

<a id="r_ga94cb2e4ce1ae29871de780301d4d59d0"></a>

```c
#define MIPI_DCS_GET_DISPLAY_ID 0x04U
```

相关声明：[MIPI_DCS_GET_DISPLAY_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga94cb2e4ce1ae29871de780301d4d59d0)。

获取显示器标识符（Get Display ID）。

<a id="r_ga5007b2e6e6e7750d13cb8421ff06d8e7"></a>

```c
#define MIPI_DCS_GET_RED_CHANNEL 0x06U
```

相关声明：[MIPI_DCS_GET_RED_CHANNEL](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga5007b2e6e6e7750d13cb8421ff06d8e7)。

获取红色通道（Get Red Channel）。

<a id="r_gaa40f1c03dca04961a28dd19754212f06"></a>

```c
#define MIPI_DCS_GET_GREEN_CHANNEL 0x07U
```

相关声明：[MIPI_DCS_GET_GREEN_CHANNEL](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaa40f1c03dca04961a28dd19754212f06)。

获取绿色通道（Get Green Channel）。

<a id="r_gaf1091bc7718eb7aa3a2c72c5c025ab4d"></a>

```c
#define MIPI_DCS_GET_BLUE_CHANNEL 0x08U
```

相关声明：[MIPI_DCS_GET_BLUE_CHANNEL](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaf1091bc7718eb7aa3a2c72c5c025ab4d)。

获取蓝色通道（Get Blue Channel）。

<a id="r_gaca8b503fdca34456ca68ced074873424"></a>

```c
#define MIPI_DCS_GET_DISPLAY_STATUS 0x09U
```

相关声明：[MIPI_DCS_GET_DISPLAY_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaca8b503fdca34456ca68ced074873424)。

获取显示状态（Get Display Status）。

<a id="r_ga48669397e8ea5a7c6e0cb09ea9d4fd5c"></a>

```c
#define MIPI_DCS_GET_POWER_MODE 0x0AU
```

相关声明：[MIPI_DCS_GET_POWER_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga48669397e8ea5a7c6e0cb09ea9d4fd5c)。

获取电源模式（Get Power Mode）。

<a id="r_ga9da041d715731d8d67caad967e5d6002"></a>

```c
#define MIPI_DCS_GET_ADDRESS_MODE 0x0BU
```

相关声明：[MIPI_DCS_GET_ADDRESS_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga9da041d715731d8d67caad967e5d6002)。

获取地址模式（Get Address Mode）。

<a id="r_gae7088fe2f1351d534262d111692a1bfa"></a>

```c
#define MIPI_DCS_GET_PIXEL_FORMAT 0x0CU
```

相关声明：[MIPI_DCS_GET_PIXEL_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gae7088fe2f1351d534262d111692a1bfa)。

获取像素格式（Get Pixel Format）。

<a id="r_gaf752f812f791e805fbfed0d3ab9b89de"></a>

```c
#define MIPI_DCS_GET_DISPLAY_MODE 0x0DU
```

相关声明：[MIPI_DCS_GET_DISPLAY_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaf752f812f791e805fbfed0d3ab9b89de)。

获取显示模式（Get Display Mode）。

<a id="r_gaa80bc31f551b39eff6625e80c211f16a"></a>

```c
#define MIPI_DCS_GET_SIGNAL_MODE 0x0EU
```

相关声明：[MIPI_DCS_GET_SIGNAL_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaa80bc31f551b39eff6625e80c211f16a)。

获取信号模式（Get Signal Mode）。

<a id="r_ga8ec1590be25764411567933943b77869"></a>

```c
#define MIPI_DCS_GET_DIAGNOSTIC_RESULT 0x0FU
```

相关声明：[MIPI_DCS_GET_DIAGNOSTIC_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga8ec1590be25764411567933943b77869)。

获取诊断结果（Get Diagnostic Result）。

<a id="r_ga06f9b8e87b6f1f6f41a139db370f236b"></a>

```c
#define MIPI_DCS_ENTER_SLEEP_MODE 0x10U
```

相关声明：[MIPI_DCS_ENTER_SLEEP_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga06f9b8e87b6f1f6f41a139db370f236b)。

进入睡眠模式（Enter Sleep Mode）。

<a id="r_ga276231424603f027583ffd2a1bdd6089"></a>

```c
#define MIPI_DCS_EXIT_SLEEP_MODE 0x11U
```

相关声明：[MIPI_DCS_EXIT_SLEEP_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga276231424603f027583ffd2a1bdd6089)。

退出睡眠模式（Exit Sleep Mode）。

<a id="r_ga219bb0ba9e91812f4ab372adaa9afd07"></a>

```c
#define MIPI_DCS_ENTER_PARTIAL_MODE 0x12U
```

相关声明：[MIPI_DCS_ENTER_PARTIAL_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga219bb0ba9e91812f4ab372adaa9afd07)。

进入局部显示模式（Enter Partial Mode）。

<a id="r_gaedb3b5fa815593d3fa1ae247383d8a8e"></a>

```c
#define MIPI_DCS_ENTER_NORMAL_MODE 0x13U
```

相关声明：[MIPI_DCS_ENTER_NORMAL_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaedb3b5fa815593d3fa1ae247383d8a8e)。

进入正常模式（Enter Normal Mode）。

<a id="r_ga41a4fd226d8f86ba2efa34403b4033f8"></a>

```c
#define MIPI_DCS_EXIT_INVERT_MODE 0x20U
```

相关声明：[MIPI_DCS_EXIT_INVERT_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga41a4fd226d8f86ba2efa34403b4033f8)。

退出反色模式（Exit Invert Mode）。

<a id="r_gad1041d71940752f1c1121cf392a3b2d3"></a>

```c
#define MIPI_DCS_ENTER_INVERT_MODE 0x21U
```

相关声明：[MIPI_DCS_ENTER_INVERT_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gad1041d71940752f1c1121cf392a3b2d3)。

进入反色模式（Enter Invert Mode）。

<a id="r_ga14771de93ba08dffabafffcedc85b54e"></a>

```c
#define MIPI_DCS_SET_GAMMA_CURVE 0x26U
```

相关声明：[MIPI_DCS_SET_GAMMA_CURVE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga14771de93ba08dffabafffcedc85b54e)。

设置伽马曲线（Set Gamma Curve）。

<a id="r_gaf50a5539c89552512ffcd04ece5b7fe0"></a>

```c
#define MIPI_DCS_SET_DISPLAY_OFF 0x28U
```

相关声明：[MIPI_DCS_SET_DISPLAY_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaf50a5539c89552512ffcd04ece5b7fe0)。

关闭显示（Set Display Off）。

<a id="r_gabdbee428ef6d48009a5795e384665c8f"></a>

```c
#define MIPI_DCS_SET_DISPLAY_ON 0x29U
```

相关声明：[MIPI_DCS_SET_DISPLAY_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gabdbee428ef6d48009a5795e384665c8f)。

开启显示（Set Display On）。

<a id="r_ga2d08791d990c2e4d9c6c9800ad2d8c1b"></a>

```c
#define MIPI_DCS_SET_COLUMN_ADDRESS 0x2AU
```

相关声明：[MIPI_DCS_SET_COLUMN_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga2d08791d990c2e4d9c6c9800ad2d8c1b)。

设置列地址（Set Column Address）。

<a id="r_ga63334f8e1458151197a35c7d5cf781a5"></a>

```c
#define MIPI_DCS_SET_PAGE_ADDRESS 0x2BU
```

相关声明：[MIPI_DCS_SET_PAGE_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga63334f8e1458151197a35c7d5cf781a5)。

设置页地址（Set Page Address）。

<a id="r_ga9a31b4772025e2046816057b74d2e7cd"></a>

```c
#define MIPI_DCS_WRITE_MEMORY_START 0x2CU
```

相关声明：[MIPI_DCS_WRITE_MEMORY_START](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga9a31b4772025e2046816057b74d2e7cd)。

开始写存储器（Write Memory Start）。

<a id="r_ga6f94b4db07db5a287cd50ed87197a9c2"></a>

```c
#define MIPI_DCS_WRITE_LUT 0x2DU
```

相关声明：[MIPI_DCS_WRITE_LUT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga6f94b4db07db5a287cd50ed87197a9c2)。

写查找表（Write LUT）。

<a id="r_ga860180f5477caadae3857b4c93f04281"></a>

```c
#define MIPI_DCS_READ_MEMORY_START 0x2EU
```

相关声明：[MIPI_DCS_READ_MEMORY_START](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga860180f5477caadae3857b4c93f04281)。

开始读存储器（Read Memory Start）。

<a id="r_ga18fe9e1cf30da71c18bebce1960095c3"></a>

```c
#define MIPI_DCS_SET_PARTIAL_ROWS 0x30U
```

相关声明：[MIPI_DCS_SET_PARTIAL_ROWS](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga18fe9e1cf30da71c18bebce1960095c3)。

设置局部显示行（Set Partial Rows）。

<a id="r_ga359a43a0bb277b8f09fa1120bb2c3b09"></a>

```c
#define MIPI_DCS_SET_PARTIAL_COLUMNS 0x31U
```

相关声明：[MIPI_DCS_SET_PARTIAL_COLUMNS](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga359a43a0bb277b8f09fa1120bb2c3b09)。

设置局部显示列（Set Partial Columns）。

<a id="r_ga36aa83afeed02df37cb2bb295915c92d"></a>

```c
#define MIPI_DCS_SET_SCROLL_AREA 0x33U
```

相关声明：[MIPI_DCS_SET_SCROLL_AREA](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga36aa83afeed02df37cb2bb295915c92d)。

设置滚动区域（Set Scroll Area）。

<a id="r_gadcd4fd3ea6ccbb63ebecb290c00c660f"></a>

```c
#define MIPI_DCS_SET_TEAR_OFF 0x34U
```

相关声明：[MIPI_DCS_SET_TEAR_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gadcd4fd3ea6ccbb63ebecb290c00c660f)。

关闭撕裂效应信号（Set Tear Off）。

<a id="r_gad85387743db362579b788fd28ecd2fbf"></a>

```c
#define MIPI_DCS_SET_TEAR_ON 0x35U
```

相关声明：[MIPI_DCS_SET_TEAR_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gad85387743db362579b788fd28ecd2fbf)。

开启撕裂效应信号（Set Tear On）。

<a id="r_ga1d7e5a77666d13f4a8a435db202f4323"></a>

```c
#define MIPI_DCS_SET_ADDRESS_MODE 0x36U
```

相关声明：[MIPI_DCS_SET_ADDRESS_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga1d7e5a77666d13f4a8a435db202f4323)。

设置地址模式（Set Address Mode）。

<a id="r_gaee29e37b0cb4b10920211048e0d95756"></a>

```c
#define MIPI_DCS_SET_SCROLL_START 0x37U
```

相关声明：[MIPI_DCS_SET_SCROLL_START](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaee29e37b0cb4b10920211048e0d95756)。

设置滚动起始位置（Set Scroll Start）。

<a id="r_gaf0a1f7ede08492751141cf52235808b3"></a>

```c
#define MIPI_DCS_EXIT_IDLE_MODE 0x38U
```

相关声明：[MIPI_DCS_EXIT_IDLE_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaf0a1f7ede08492751141cf52235808b3)。

退出空闲模式（Exit Idle Mode）。

<a id="r_ga7f1dfc0645ab456b38ac2caae783b709"></a>

```c
#define MIPI_DCS_ENTER_IDLE_MODE 0x39U
```

相关声明：[MIPI_DCS_ENTER_IDLE_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga7f1dfc0645ab456b38ac2caae783b709)。

进入空闲模式（Enter Idle Mode）。

<a id="r_ga1165d0835844eb0bd86fa6d30db7a84d"></a>

```c
#define MIPI_DCS_SET_PIXEL_FORMAT 0x3AU
```

相关声明：[MIPI_DCS_SET_PIXEL_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga1165d0835844eb0bd86fa6d30db7a84d)。

设置像素格式（Set Pixel Format）。

<a id="r_ga532122daccbd1370332fd9c26569c11f"></a>

```c
#define MIPI_DCS_WRITE_MEMORY_CONTINUE 0x3CU
```

相关声明：[MIPI_DCS_WRITE_MEMORY_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga532122daccbd1370332fd9c26569c11f)。

继续写存储器（Write Memory Continue）。

<a id="r_gaf9210d3033c2b09a7da608e9aeb88ad1"></a>

```c
#define MIPI_DCS_SET_3D_CONTROL 0x3DU
```

相关声明：[MIPI_DCS_SET_3D_CONTROL](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaf9210d3033c2b09a7da608e9aeb88ad1)。

设置三维控制（Set 3D Control）。

<a id="r_ga6d3fcf5c050b45d8afe3af4ec98adadc"></a>

```c
#define MIPI_DCS_READ_MEMORY_CONTINUE 0x3EU
```

相关声明：[MIPI_DCS_READ_MEMORY_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga6d3fcf5c050b45d8afe3af4ec98adadc)。

继续读存储器（Read Memory Continue）。

<a id="r_gaace0882d961807760db2ed7693ab760a"></a>

```c
#define MIPI_DCS_GET_3D_CONTROL 0x3FU
```

相关声明：[MIPI_DCS_GET_3D_CONTROL](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaace0882d961807760db2ed7693ab760a)。

获取三维控制（Get 3D Control）。

<a id="r_ga9597f72175b99376f7119b95cf425c1c"></a>

```c
#define MIPI_DCS_SET_VSYNC_TIMING 0x40U
```

相关声明：[MIPI_DCS_SET_VSYNC_TIMING](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga9597f72175b99376f7119b95cf425c1c)。

设置垂直同步时序（Set VSync Timing）。

<a id="r_gaaac44d1367419dc395332712b0427458"></a>

```c
#define MIPI_DCS_SET_TEAR_SCANLINE 0x44U
```

相关声明：[MIPI_DCS_SET_TEAR_SCANLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaaac44d1367419dc395332712b0427458)。

设置撕裂效应扫描线（Set Tear Scanline）。

<a id="r_ga7933493853f9ef2dd28b31ea2fbb492f"></a>

```c
#define MIPI_DCS_GET_SCANLINE 0x45U
```

相关声明：[MIPI_DCS_GET_SCANLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga7933493853f9ef2dd28b31ea2fbb492f)。

获取扫描线（Get Scanline）。

<a id="r_gac8dec8303a247b56a513628645d67f2b"></a>

```c
#define MIPI_DCS_SET_DISPLAY_BRIGHTNESS 0x51U
```

相关声明：[MIPI_DCS_SET_DISPLAY_BRIGHTNESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gac8dec8303a247b56a513628645d67f2b)。

设置显示亮度（Set Display Brightness）。

<a id="r_ga4df917017e27912a343731b350e8d02e"></a>

```c
#define MIPI_DCS_GET_DISPLAY_BRIGHTNESS 0x52U
```

相关声明：[MIPI_DCS_GET_DISPLAY_BRIGHTNESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga4df917017e27912a343731b350e8d02e)。

获取显示亮度（Get Display Brightness）。

<a id="r_gad47f873520b505e3463ad1f85d617787"></a>

```c
#define MIPI_DCS_WRITE_CONTROL_DISPLAY 0x53U
```

相关声明：[MIPI_DCS_WRITE_CONTROL_DISPLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gad47f873520b505e3463ad1f85d617787)。

写显示控制（Write Control Display）。

<a id="r_ga9f83f0b2412084ab2ac3edd36b41fc11"></a>

```c
#define MIPI_DCS_GET_CONTROL_DISPLAY 0x54U
```

相关声明：[MIPI_DCS_GET_CONTROL_DISPLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga9f83f0b2412084ab2ac3edd36b41fc11)。

获取显示控制（Get Control Display）。

<a id="r_ga2655d637a53b1b5e805ab3d69bc9fe9e"></a>

```c
#define MIPI_DCS_WRITE_POWER_SAVE 0x55U
```

相关声明：[MIPI_DCS_WRITE_POWER_SAVE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga2655d637a53b1b5e805ab3d69bc9fe9e)。

写节能设置（Write Power Save）。

<a id="r_ga518ba3d308b6c453850e5168b26d1024"></a>

```c
#define MIPI_DCS_GET_POWER_SAVE 0x56U
```

相关声明：[MIPI_DCS_GET_POWER_SAVE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga518ba3d308b6c453850e5168b26d1024)。

获取节能设置（Get Power Save）。

<a id="r_gab0d27051994aa70c8baf12a103080e80"></a>

```c
#define MIPI_DCS_SET_CABC_MIN_BRIGHTNESS 0x5EU
```

相关声明：[MIPI_DCS_SET_CABC_MIN_BRIGHTNESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gab0d27051994aa70c8baf12a103080e80)。

设置内容自适应背光控制的最低亮度（Set CABC Min Brightness）。

<a id="r_ga2d56066851a38acf38323cd2327820c4"></a>

```c
#define MIPI_DCS_GET_CABC_MIN_BRIGHTNESS 0x5FU
```

相关声明：[MIPI_DCS_GET_CABC_MIN_BRIGHTNESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga2d56066851a38acf38323cd2327820c4)。

获取内容自适应背光控制的最低亮度（Get CABC Min Brightness）。

<a id="r_ga6cccd95a6bc9c007bb648b70d664c34d"></a>

```c
#define MIPI_DCS_READ_DDB_START 0xA1U
```

相关声明：[MIPI_DCS_READ_DDB_START](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga6cccd95a6bc9c007bb648b70d664c34d)。

开始读取设备描述块（Read DDB Start）。

<a id="r_ga26b4f0111aee93b8ad01448d7b4af368"></a>

```c
#define MIPI_DCS_READ_DDB_CONTINUE 0xA8U
```

相关声明：[MIPI_DCS_READ_DDB_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga26b4f0111aee93b8ad01448d7b4af368)。

继续读取设备描述块（Read DDB Continue）。

<a id="r_ga2772b5432484431573d092447c12e005"></a>

```c
#define MIPI_DCS_PIXEL_FORMAT_24BIT 0x77
```

相关声明：[MIPI_DCS_PIXEL_FORMAT_24BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga2772b5432484431573d092447c12e005)。

24 位像素格式（24-bit Pixel Format）。

<a id="r_gab2d74d3cc0ce8036b57d5aec073b5b6b"></a>

```c
#define MIPI_DCS_PIXEL_FORMAT_18BIT 0x66
```

相关声明：[MIPI_DCS_PIXEL_FORMAT_18BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gab2d74d3cc0ce8036b57d5aec073b5b6b)。

18 位像素格式（18-bit Pixel Format）。

<a id="r_ga171be8bd1a5551ffc129c14e0d829e61"></a>

```c
#define MIPI_DCS_PIXEL_FORMAT_16BIT 0x55
```

相关声明：[MIPI_DCS_PIXEL_FORMAT_16BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga171be8bd1a5551ffc129c14e0d829e61)。

16 位像素格式（16-bit Pixel Format）。

<a id="r_ga77944b2fd7f59be6698bd414cbeedcac"></a>

```c
#define MIPI_DCS_PIXEL_FORMAT_12BIT 0x33
```

相关声明：[MIPI_DCS_PIXEL_FORMAT_12BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga77944b2fd7f59be6698bd414cbeedcac)。

12 位像素格式（12-bit Pixel Format）。

<a id="r_gac3e18d2d9d4bcfb98d99518021bf98bd"></a>

```c
#define MIPI_DCS_PIXEL_FORMAT_8BIT 0x22
```

相关声明：[MIPI_DCS_PIXEL_FORMAT_8BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gac3e18d2d9d4bcfb98d99518021bf98bd)。

8 位像素格式（8-bit Pixel Format）。

<a id="r_ga5a14ff4ebc8e81b9bc92e87069ad7466"></a>

```c
#define MIPI_DCS_PIXEL_FORMAT_3BIT 0x11
```

相关声明：[MIPI_DCS_PIXEL_FORMAT_3BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga5a14ff4ebc8e81b9bc92e87069ad7466)。

3 位像素格式（3-bit Pixel Format）。

<a id="define-members-1"></a>

### MIPI-DSI 地址模式寄存器字段（MIPI-DSI Address mode register fields.）

<a id="r_ga549bdf77bc40cc4a5cc81004b3f91775"></a>

```c
#define MIPI_DCS_ADDRESS_MODE_MIRROR_Y BIT(7)
```

相关声明：[MIPI_DCS_ADDRESS_MODE_MIRROR_Y](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga549bdf77bc40cc4a5cc81004b3f91775)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

Y 轴镜像（Mirror Y）。

<a id="r_gaa9c5f1e04806ef4dd672a6169136d07c"></a>

```c
#define MIPI_DCS_ADDRESS_MODE_MIRROR_X BIT(6)
```

相关声明：[MIPI_DCS_ADDRESS_MODE_MIRROR_X](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaa9c5f1e04806ef4dd672a6169136d07c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

X 轴镜像（Mirror X）。

<a id="r_gadfce4431c308f186479af4d15c83187b"></a>

```c
#define MIPI_DCS_ADDRESS_MODE_SWAP_XY BIT(5)
```

相关声明：[MIPI_DCS_ADDRESS_MODE_SWAP_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gadfce4431c308f186479af4d15c83187b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

交换 X、Y 轴（Swap XY）。

<a id="r_gad8591d77dafcb2d1ccc2ce971b012761"></a>

```c
#define MIPI_DCS_ADDRESS_MODE_REFRESH_BT BIT(4)
```

相关声明：[MIPI_DCS_ADDRESS_MODE_REFRESH_BT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gad8591d77dafcb2d1ccc2ce971b012761)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

从底部向顶部刷新（Refresh Bottom to Top）。

<a id="r_ga5320efc9a396b1cdfe89c5cfc87d8c11"></a>

```c
#define MIPI_DCS_ADDRESS_MODE_BGR BIT(3)
```

相关声明：[MIPI_DCS_ADDRESS_MODE_BGR](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga5320efc9a396b1cdfe89c5cfc87d8c11)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

蓝绿红通道顺序（BGR Order）。

<a id="r_gaa32acf97423f4491b27b2d9cb7d49a3c"></a>

```c
#define MIPI_DCS_ADDRESS_MODE_LATCH_RL BIT(2)
```

相关声明：[MIPI_DCS_ADDRESS_MODE_LATCH_RL](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaa32acf97423f4491b27b2d9cb7d49a3c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

从右向左锁存（Latch Right to Left）。

<a id="r_ga75df1e79cde793c01c47103bf683f3aa"></a>

```c
#define MIPI_DCS_ADDRESS_MODE_FLIP_X BIT(1)
```

相关声明：[MIPI_DCS_ADDRESS_MODE_FLIP_X](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga75df1e79cde793c01c47103bf683f3aa)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

X 轴翻转（Flip X）。

<a id="r_ga72cf84630b55cd8dfe762eb84272692f"></a>

```c
#define MIPI_DCS_ADDRESS_MODE_FLIP_Y BIT(0)
```

相关声明：[MIPI_DCS_ADDRESS_MODE_FLIP_Y](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga72cf84630b55cd8dfe762eb84272692f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

Y 轴翻转（Flip Y）。

<a id="define-members-2"></a>

### MIPI-DSI 处理器到外设的事务类型（MIPI-DSI Processor-to-Peripheral transaction types.）

<a id="r_gad58c27d600a73e38f33669a3ae743f01"></a>

```c
#define MIPI_DSI_V_SYNC_START 0x01U
```

相关声明：[MIPI_DSI_V_SYNC_START](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gad58c27d600a73e38f33669a3ae743f01)。

同步事件：垂直同步开始（Sync Event, V Sync Start）。

<a id="r_gaf85ef5c73d29fec41460de8b752cef39"></a>

```c
#define MIPI_DSI_V_SYNC_END 0x11U
```

相关声明：[MIPI_DSI_V_SYNC_END](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaf85ef5c73d29fec41460de8b752cef39)。

同步事件：垂直同步结束（Sync Event, V Sync End）。

<a id="r_ga6852f3d6bfb77101d64b10a2b48a91c5"></a>

```c
#define MIPI_DSI_H_SYNC_START 0x21U
```

相关声明：[MIPI_DSI_H_SYNC_START](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga6852f3d6bfb77101d64b10a2b48a91c5)。

同步事件：水平同步开始（Sync Event, H Sync Start）。

<a id="r_gaa8cc494ce41880ec765701ee4beffe97"></a>

```c
#define MIPI_DSI_H_SYNC_END 0x31U
```

相关声明：[MIPI_DSI_H_SYNC_END](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaa8cc494ce41880ec765701ee4beffe97)。

同步事件：水平同步结束（Sync Event, H Sync End）。

<a id="r_gad713fb809d6012db370ef23601c81619"></a>

```c
#define MIPI_DSI_COLOR_MODE_OFF 0x02U
```

相关声明：[MIPI_DSI_COLOR_MODE_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gad713fb809d6012db370ef23601c81619)。

关闭颜色模式命令（Color Mode Off Command）。

<a id="r_ga1987975c9389ec9570c5ff05e3e1a9b1"></a>

```c
#define MIPI_DSI_COLOR_MODE_ON 0x12U
```

相关声明：[MIPI_DSI_COLOR_MODE_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga1987975c9389ec9570c5ff05e3e1a9b1)。

开启颜色模式命令（Color Mode On Command）。

<a id="r_gafac7d0f045d77fed0ff35f3a3503f6a5"></a>

```c
#define MIPI_DSI_SHUTDOWN_PERIPHERAL 0x22U
```

相关声明：[MIPI_DSI_SHUTDOWN_PERIPHERAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gafac7d0f045d77fed0ff35f3a3503f6a5)。

关闭外设命令（Shutdown Peripheral Command）。

<a id="r_ga56292f7b60a0e7b55cd5118c1641c3ba"></a>

```c
#define MIPI_DSI_TURN_ON_PERIPHERAL 0x32U
```

相关声明：[MIPI_DSI_TURN_ON_PERIPHERAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga56292f7b60a0e7b55cd5118c1641c3ba)。

开启外设命令（Turn On Peripheral Command）。

<a id="r_ga639170a23fa7b28e6bf3726c8d54ead0"></a>

```c
#define MIPI_DSI_GENERIC_SHORT_WRITE_0_PARAM 0x03U
```

相关声明：[MIPI_DSI_GENERIC_SHORT_WRITE_0_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga639170a23fa7b28e6bf3726c8d54ead0)。

带 0 个参数的通用短写数据包（Generic Short WRITE Packet with 0 parameters）。

<a id="r_gaa0e596feb47e6eada0217fa7a81a0278"></a>

```c
#define MIPI_DSI_GENERIC_SHORT_WRITE_1_PARAM 0x13U
```

相关声明：[MIPI_DSI_GENERIC_SHORT_WRITE_1_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaa0e596feb47e6eada0217fa7a81a0278)。

带 1 个参数的通用短写数据包（Generic Short WRITE Packet with 1 parameter）。

<a id="r_gaea2acb4489552a159a19278018122ce6"></a>

```c
#define MIPI_DSI_GENERIC_SHORT_WRITE_2_PARAM 0x23U
```

相关声明：[MIPI_DSI_GENERIC_SHORT_WRITE_2_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaea2acb4489552a159a19278018122ce6)。

带 2 个参数的通用短写数据包（Generic Short WRITE Packet with 2 parameters）。

<a id="r_ga9d541d3e054b1fa75fd7f1b0ffa3883a"></a>

```c
#define MIPI_DSI_GENERIC_READ_REQUEST_0_PARAM 0x04U
```

相关声明：[MIPI_DSI_GENERIC_READ_REQUEST_0_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga9d541d3e054b1fa75fd7f1b0ffa3883a)。

带 0 个参数的通用读请求（Generic READ Request with 0 parameters）。

<a id="r_gabff929d8285415c0d3edb95748bf2686"></a>

```c
#define MIPI_DSI_GENERIC_READ_REQUEST_1_PARAM 0x14U
```

相关声明：[MIPI_DSI_GENERIC_READ_REQUEST_1_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gabff929d8285415c0d3edb95748bf2686)。

带 1 个参数的通用读请求（Generic READ Request with 1 parameter）。

<a id="r_ga9ea3c57a021879863097edc3f275ea60"></a>

```c
#define MIPI_DSI_GENERIC_READ_REQUEST_2_PARAM 0x24U
```

相关声明：[MIPI_DSI_GENERIC_READ_REQUEST_2_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga9ea3c57a021879863097edc3f275ea60)。

带 2 个参数的通用读请求（Generic READ Request with 2 parameters）。

<a id="r_ga51191c76ceca6f0e79cdb4f0e58013a3"></a>

```c
#define MIPI_DSI_DCS_SHORT_WRITE 0x05U
```

相关声明：[MIPI_DSI_DCS_SHORT_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga51191c76ceca6f0e79cdb4f0e58013a3)。

带 0 个参数的显示命令集短写命令（DCS Short Write Command with 0 parameters）。

<a id="r_ga5e0e1bf73a04668617e46cb0392bac8d"></a>

```c
#define MIPI_DSI_DCS_SHORT_WRITE_PARAM 0x15U
```

相关声明：[MIPI_DSI_DCS_SHORT_WRITE_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga5e0e1bf73a04668617e46cb0392bac8d)。

带 1 个参数的显示命令集短写命令（DCS Short Write Command with 1 parameter）。

<a id="r_ga60acd68f9c3271b2cd306f6bb5e4af94"></a>

```c
#define MIPI_DSI_DCS_READ 0x06U
```

相关声明：[MIPI_DSI_DCS_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga60acd68f9c3271b2cd306f6bb5e4af94)。

带 0 个参数的显示命令集读请求（DCS Read Request with 0 parameters）。

<a id="r_gab07bcea365f9835c5df3c37d15f3073c"></a>

```c
#define MIPI_DSI_SET_MAXIMUM_RETURN_PACKET_SIZE 0x37U
```

相关声明：[MIPI_DSI_SET_MAXIMUM_RETURN_PACKET_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gab07bcea365f9835c5df3c37d15f3073c)。

设置最大返回数据包大小命令（Set Maximum Return Packet Size Command）。

<a id="r_ga575957d9fd4de559cd938b332f1eff05"></a>

```c
#define MIPI_DSI_END_OF_TRANSMISSION 0x08U
```

相关声明：[MIPI_DSI_END_OF_TRANSMISSION](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga575957d9fd4de559cd938b332f1eff05)。

传输结束数据包（End of Transmission Packet (EoTp)）。

<a id="r_gabcd142889c213edb8a7e7e95bb138b08"></a>

```c
#define MIPI_DSI_NULL_PACKET 0x09U
```

相关声明：[MIPI_DSI_NULL_PACKET](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gabcd142889c213edb8a7e7e95bb138b08)。

空数据包（长包）（Null Packet (Long)）。

<a id="r_ga66550282423b364aed89c6ed2c202329"></a>

```c
#define MIPI_DSI_BLANKING_PACKET 0x19U
```

相关声明：[MIPI_DSI_BLANKING_PACKET](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga66550282423b364aed89c6ed2c202329)。

消隐数据包（长包）（Blanking Packet (Long)）。

<a id="r_gadb6e6683462c4b8eaeda3a77b86f3e1d"></a>

```c
#define MIPI_DSI_GENERIC_LONG_WRITE 0x29U
```

相关声明：[MIPI_DSI_GENERIC_LONG_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gadb6e6683462c4b8eaeda3a77b86f3e1d)。

通用长写（Generic Long Write）。

<a id="r_ga141eda8b32761dc7a275524c04e45535"></a>

```c
#define MIPI_DSI_DCS_LONG_WRITE 0x39U
```

相关声明：[MIPI_DSI_DCS_LONG_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga141eda8b32761dc7a275524c04e45535)。

显示命令集长写／写查找表命令（DCS Long Write / write_LUT Command）。

<a id="r_ga933521f6a7f2f8ebad1569a0e8320d41"></a>

```c
#define MIPI_DSI_LOOSELY_PACKED_PIXEL_STREAM_YCBCR20 0x0CU
```

相关声明：[MIPI_DSI_LOOSELY_PACKED_PIXEL_STREAM_YCBCR20](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga933521f6a7f2f8ebad1569a0e8320d41)。

松散打包的像素流，20 位 YCbCr 4:2:2 格式（Loosely Packed Pixel Stream, 20-bit YCbCr 4:2:2 Format）。

<a id="r_ga858695ed8e1f5234d25f44b59a4f270d"></a>

```c
#define MIPI_DSI_PACKED_PIXEL_STREAM_YCBCR24 0x1CU
```

相关声明：[MIPI_DSI_PACKED_PIXEL_STREAM_YCBCR24](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga858695ed8e1f5234d25f44b59a4f270d)。

紧密打包的像素流，24 位 YCbCr 4:2:2 格式（Packed Pixel Stream, 24-bit YCbCr 4:2:2 Format）。

<a id="r_ga928d1364d635cb892f5992f7cdda7905"></a>

```c
#define MIPI_DSI_PACKED_PIXEL_STREAM_YCBCR16 0x2CU
```

相关声明：[MIPI_DSI_PACKED_PIXEL_STREAM_YCBCR16](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga928d1364d635cb892f5992f7cdda7905)。

紧密打包的像素流，16 位 YCbCr 4:2:2 格式（Packed Pixel Stream, 16-bit YCbCr 4:2:2 Format）。

<a id="r_ga09da8d6976e18b7ac074f9e10cc8c52f"></a>

```c
#define MIPI_DSI_PACKED_PIXEL_STREAM_30 0x0DU
```

相关声明：[MIPI_DSI_PACKED_PIXEL_STREAM_30](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga09da8d6976e18b7ac074f9e10cc8c52f)。

紧密打包的像素流，30 位格式（Packed Pixel Stream, 30-bit Format）。

<a id="r_ga0015e0c7df4f3688e5567099f9d0ea11"></a>

```c
#define MIPI_DSI_PACKED_PIXEL_STREAM_36 0x1DU
```

相关声明：[MIPI_DSI_PACKED_PIXEL_STREAM_36](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga0015e0c7df4f3688e5567099f9d0ea11)。

紧密打包的像素流，36 位格式（Packed Pixel Stream, 36-bit Format）。

<a id="r_ga999976bf03f40c56ccb9272f99334cdf"></a>

```c
#define MIPI_DSI_PACKED_PIXEL_STREAM_YCBCR12 0x3DU
```

相关声明：[MIPI_DSI_PACKED_PIXEL_STREAM_YCBCR12](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga999976bf03f40c56ccb9272f99334cdf)。

紧密打包的像素流，12 位 YCbCr 4:2:0 格式（Packed Pixel Stream, 12-bit YCbCr 4:2:0 Format）。

<a id="r_ga93db7cc5b15cd5683ba8b9358731e151"></a>

```c
#define MIPI_DSI_PACKED_PIXEL_STREAM_16 0x0EU
```

相关声明：[MIPI_DSI_PACKED_PIXEL_STREAM_16](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga93db7cc5b15cd5683ba8b9358731e151)。

紧密打包的像素流，16 位格式（Packed Pixel Stream, 16-bit Format）。

<a id="r_ga3bf54b5ef30c94f863c353ac8a68f0f0"></a>

```c
#define MIPI_DSI_PACKED_PIXEL_STREAM_18 0x1EU
```

相关声明：[MIPI_DSI_PACKED_PIXEL_STREAM_18](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga3bf54b5ef30c94f863c353ac8a68f0f0)。

紧密打包的像素流，18 位格式（Packed Pixel Stream, 18-bit Format）。

<a id="r_gaeee3817bcc554f3c04cb737e03649733"></a>

```c
#define MIPI_DSI_PIXEL_STREAM_3BYTE_18 0x2EU
```

相关声明：[MIPI_DSI_PIXEL_STREAM_3BYTE_18](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaeee3817bcc554f3c04cb737e03649733)。

像素流，以三个字节承载的 18 位格式（Pixel Stream, 18-bit Format in Three Bytes）。

<a id="r_ga0956384d8db5940cc6ffe3a4569a2fb2"></a>

```c
#define MIPI_DSI_PACKED_PIXEL_STREAM_24 0x3EU
```

相关声明：[MIPI_DSI_PACKED_PIXEL_STREAM_24](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga0956384d8db5940cc6ffe3a4569a2fb2)。

紧密打包的像素流，24 位格式（Packed Pixel Stream, 24-bit Format）。


## 8.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P531_mipi_display.h_源码浏览.md)
- [MIPI_DCS_NOP](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gadcaf06472d3e281e425bd2d71c5beaed)
- [MIPI_DCS_SOFT_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gab8c88ef2d316b783d5222a85d0e118ea)
- [MIPI_DCS_GET_COMPRESSION_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga6d88c902f9d07c1fff0d1e92fe966fad)
- [MIPI_DCS_GET_DISPLAY_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga94cb2e4ce1ae29871de780301d4d59d0)
- [MIPI_DCS_GET_RED_CHANNEL](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga5007b2e6e6e7750d13cb8421ff06d8e7)
- [MIPI_DCS_GET_GREEN_CHANNEL](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaa40f1c03dca04961a28dd19754212f06)
- [MIPI_DCS_GET_BLUE_CHANNEL](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaf1091bc7718eb7aa3a2c72c5c025ab4d)
- [MIPI_DCS_GET_DISPLAY_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaca8b503fdca34456ca68ced074873424)
- [MIPI_DCS_GET_POWER_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga48669397e8ea5a7c6e0cb09ea9d4fd5c)
- [MIPI_DCS_GET_ADDRESS_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga9da041d715731d8d67caad967e5d6002)
- [MIPI_DCS_GET_PIXEL_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gae7088fe2f1351d534262d111692a1bfa)
- [MIPI_DCS_GET_DISPLAY_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaf752f812f791e805fbfed0d3ab9b89de)
- [MIPI_DCS_GET_SIGNAL_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaa80bc31f551b39eff6625e80c211f16a)
- [MIPI_DCS_GET_DIAGNOSTIC_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga8ec1590be25764411567933943b77869)
- [MIPI_DCS_ENTER_SLEEP_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga06f9b8e87b6f1f6f41a139db370f236b)
- [MIPI_DCS_EXIT_SLEEP_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga276231424603f027583ffd2a1bdd6089)
- [MIPI_DCS_ENTER_PARTIAL_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga219bb0ba9e91812f4ab372adaa9afd07)
- [MIPI_DCS_ENTER_NORMAL_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaedb3b5fa815593d3fa1ae247383d8a8e)
- [MIPI_DCS_EXIT_INVERT_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga41a4fd226d8f86ba2efa34403b4033f8)
- [MIPI_DCS_ENTER_INVERT_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gad1041d71940752f1c1121cf392a3b2d3)
- [MIPI_DCS_SET_GAMMA_CURVE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga14771de93ba08dffabafffcedc85b54e)
- [MIPI_DCS_SET_DISPLAY_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaf50a5539c89552512ffcd04ece5b7fe0)
- [MIPI_DCS_SET_DISPLAY_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gabdbee428ef6d48009a5795e384665c8f)
- [MIPI_DCS_SET_COLUMN_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga2d08791d990c2e4d9c6c9800ad2d8c1b)
- [MIPI_DCS_SET_PAGE_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga63334f8e1458151197a35c7d5cf781a5)
- [MIPI_DCS_WRITE_MEMORY_START](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga9a31b4772025e2046816057b74d2e7cd)
- [MIPI_DCS_WRITE_LUT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga6f94b4db07db5a287cd50ed87197a9c2)
- [MIPI_DCS_READ_MEMORY_START](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga860180f5477caadae3857b4c93f04281)
- [MIPI_DCS_SET_PARTIAL_ROWS](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga18fe9e1cf30da71c18bebce1960095c3)
- [MIPI_DCS_SET_PARTIAL_COLUMNS](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga359a43a0bb277b8f09fa1120bb2c3b09)
- [MIPI_DCS_SET_SCROLL_AREA](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga36aa83afeed02df37cb2bb295915c92d)
- [MIPI_DCS_SET_TEAR_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gadcd4fd3ea6ccbb63ebecb290c00c660f)
- [MIPI_DCS_SET_TEAR_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gad85387743db362579b788fd28ecd2fbf)
- [MIPI_DCS_SET_ADDRESS_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga1d7e5a77666d13f4a8a435db202f4323)
- [MIPI_DCS_SET_SCROLL_START](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaee29e37b0cb4b10920211048e0d95756)
- [MIPI_DCS_EXIT_IDLE_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaf0a1f7ede08492751141cf52235808b3)
- [MIPI_DCS_ENTER_IDLE_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga7f1dfc0645ab456b38ac2caae783b709)
- [MIPI_DCS_SET_PIXEL_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga1165d0835844eb0bd86fa6d30db7a84d)
- [MIPI_DCS_WRITE_MEMORY_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga532122daccbd1370332fd9c26569c11f)
- [MIPI_DCS_SET_3D_CONTROL](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaf9210d3033c2b09a7da608e9aeb88ad1)
- [MIPI_DCS_READ_MEMORY_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga6d3fcf5c050b45d8afe3af4ec98adadc)
- [MIPI_DCS_GET_3D_CONTROL](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaace0882d961807760db2ed7693ab760a)
- [MIPI_DCS_SET_VSYNC_TIMING](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga9597f72175b99376f7119b95cf425c1c)
- [MIPI_DCS_SET_TEAR_SCANLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaaac44d1367419dc395332712b0427458)
- [MIPI_DCS_GET_SCANLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga7933493853f9ef2dd28b31ea2fbb492f)
- [MIPI_DCS_SET_DISPLAY_BRIGHTNESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gac8dec8303a247b56a513628645d67f2b)
- [MIPI_DCS_GET_DISPLAY_BRIGHTNESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga4df917017e27912a343731b350e8d02e)
- [MIPI_DCS_WRITE_CONTROL_DISPLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gad47f873520b505e3463ad1f85d617787)
- [MIPI_DCS_GET_CONTROL_DISPLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga9f83f0b2412084ab2ac3edd36b41fc11)
- [MIPI_DCS_WRITE_POWER_SAVE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga2655d637a53b1b5e805ab3d69bc9fe9e)
- [MIPI_DCS_GET_POWER_SAVE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga518ba3d308b6c453850e5168b26d1024)
- [MIPI_DCS_SET_CABC_MIN_BRIGHTNESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gab0d27051994aa70c8baf12a103080e80)
- [MIPI_DCS_GET_CABC_MIN_BRIGHTNESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga2d56066851a38acf38323cd2327820c4)
- [MIPI_DCS_READ_DDB_START](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga6cccd95a6bc9c007bb648b70d664c34d)
- [MIPI_DCS_READ_DDB_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga26b4f0111aee93b8ad01448d7b4af368)
- [MIPI_DCS_PIXEL_FORMAT_24BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga2772b5432484431573d092447c12e005)
- [MIPI_DCS_PIXEL_FORMAT_18BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gab2d74d3cc0ce8036b57d5aec073b5b6b)
- [MIPI_DCS_PIXEL_FORMAT_16BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga171be8bd1a5551ffc129c14e0d829e61)
- [MIPI_DCS_PIXEL_FORMAT_12BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga77944b2fd7f59be6698bd414cbeedcac)
- [MIPI_DCS_PIXEL_FORMAT_8BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gac3e18d2d9d4bcfb98d99518021bf98bd)
- [MIPI_DCS_PIXEL_FORMAT_3BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga5a14ff4ebc8e81b9bc92e87069ad7466)
- [MIPI_DCS_ADDRESS_MODE_MIRROR_Y](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga549bdf77bc40cc4a5cc81004b3f91775)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [MIPI_DCS_ADDRESS_MODE_MIRROR_X](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaa9c5f1e04806ef4dd672a6169136d07c)
- [MIPI_DCS_ADDRESS_MODE_SWAP_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gadfce4431c308f186479af4d15c83187b)
- [MIPI_DCS_ADDRESS_MODE_REFRESH_BT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gad8591d77dafcb2d1ccc2ce971b012761)
- [MIPI_DCS_ADDRESS_MODE_BGR](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga5320efc9a396b1cdfe89c5cfc87d8c11)
- [MIPI_DCS_ADDRESS_MODE_LATCH_RL](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaa32acf97423f4491b27b2d9cb7d49a3c)
- [MIPI_DCS_ADDRESS_MODE_FLIP_X](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga75df1e79cde793c01c47103bf683f3aa)
- [MIPI_DCS_ADDRESS_MODE_FLIP_Y](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga72cf84630b55cd8dfe762eb84272692f)
- [MIPI_DSI_V_SYNC_START](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gad58c27d600a73e38f33669a3ae743f01)
- [MIPI_DSI_V_SYNC_END](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaf85ef5c73d29fec41460de8b752cef39)
- [MIPI_DSI_H_SYNC_START](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga6852f3d6bfb77101d64b10a2b48a91c5)
- [MIPI_DSI_H_SYNC_END](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaa8cc494ce41880ec765701ee4beffe97)
- [MIPI_DSI_COLOR_MODE_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gad713fb809d6012db370ef23601c81619)
- [MIPI_DSI_COLOR_MODE_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga1987975c9389ec9570c5ff05e3e1a9b1)
- [MIPI_DSI_SHUTDOWN_PERIPHERAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gafac7d0f045d77fed0ff35f3a3503f6a5)
- [MIPI_DSI_TURN_ON_PERIPHERAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga56292f7b60a0e7b55cd5118c1641c3ba)
- [MIPI_DSI_GENERIC_SHORT_WRITE_0_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga639170a23fa7b28e6bf3726c8d54ead0)
- [MIPI_DSI_GENERIC_SHORT_WRITE_1_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaa0e596feb47e6eada0217fa7a81a0278)
- [MIPI_DSI_GENERIC_SHORT_WRITE_2_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaea2acb4489552a159a19278018122ce6)
- [MIPI_DSI_GENERIC_READ_REQUEST_0_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga9d541d3e054b1fa75fd7f1b0ffa3883a)
- [MIPI_DSI_GENERIC_READ_REQUEST_1_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gabff929d8285415c0d3edb95748bf2686)
- [MIPI_DSI_GENERIC_READ_REQUEST_2_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga9ea3c57a021879863097edc3f275ea60)
- [MIPI_DSI_DCS_SHORT_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga51191c76ceca6f0e79cdb4f0e58013a3)
- [MIPI_DSI_DCS_SHORT_WRITE_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga5e0e1bf73a04668617e46cb0392bac8d)
- [MIPI_DSI_DCS_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga60acd68f9c3271b2cd306f6bb5e4af94)
- [MIPI_DSI_SET_MAXIMUM_RETURN_PACKET_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gab07bcea365f9835c5df3c37d15f3073c)
- [MIPI_DSI_END_OF_TRANSMISSION](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga575957d9fd4de559cd938b332f1eff05)
- [MIPI_DSI_NULL_PACKET](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gabcd142889c213edb8a7e7e95bb138b08)
- [MIPI_DSI_BLANKING_PACKET](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga66550282423b364aed89c6ed2c202329)
- [MIPI_DSI_GENERIC_LONG_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gadb6e6683462c4b8eaeda3a77b86f3e1d)
- [MIPI_DSI_DCS_LONG_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga141eda8b32761dc7a275524c04e45535)
- [MIPI_DSI_LOOSELY_PACKED_PIXEL_STREAM_YCBCR20](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga933521f6a7f2f8ebad1569a0e8320d41)
- [MIPI_DSI_PACKED_PIXEL_STREAM_YCBCR24](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga858695ed8e1f5234d25f44b59a4f270d)
- [MIPI_DSI_PACKED_PIXEL_STREAM_YCBCR16](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga928d1364d635cb892f5992f7cdda7905)
- [MIPI_DSI_PACKED_PIXEL_STREAM_30](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga09da8d6976e18b7ac074f9e10cc8c52f)
- [MIPI_DSI_PACKED_PIXEL_STREAM_36](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga0015e0c7df4f3688e5567099f9d0ea11)
- [MIPI_DSI_PACKED_PIXEL_STREAM_YCBCR12](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga999976bf03f40c56ccb9272f99334cdf)
- [MIPI_DSI_PACKED_PIXEL_STREAM_16](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga93db7cc5b15cd5683ba8b9358731e151)
- [MIPI_DSI_PACKED_PIXEL_STREAM_18](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga3bf54b5ef30c94f863c353ac8a68f0f0)
- [MIPI_DSI_PIXEL_STREAM_3BYTE_18](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#gaeee3817bcc554f3c04cb737e03649733)
- [MIPI_DSI_PACKED_PIXEL_STREAM_24](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__interface.html#ga0956384d8db5940cc6ffe3a4569a2fb2)

<a id="header-details"></a>

---

[上一章](P007_zephyr__dt-bindings__clock__mchp_pic32cm_pl_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P009_zephyr__net__socket.h_文件参考.md)
