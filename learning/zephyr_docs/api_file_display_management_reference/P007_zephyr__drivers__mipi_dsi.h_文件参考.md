---
id: learning.zephyr-docs.api-file-display-management-reference.page-7
title: zephyr__drivers__mipi_dsi.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mipi__dsi_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_drivers\_\_mipi\_dsi.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mipi__dsi_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MIPI显示串行接口（Display Serial Interface，MIPI-DSI）驱动API的主头文件。

<a id="details"></a>

```c
#include <errno.h>
#include <sys/types.h>
#include <zephyr/device.h>
#include <zephyr/display/mipi_display.h>
#include <zephyr/dt-bindings/mipi_dsi/mipi_dsi.h>
```

查看此文件的源码。

MIPI显示串行接口（Display Serial Interface，MIPI-DSI）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.1\_数据结构（Data Structures）

<a id="r_mipi_5Fdsi_5Ftimings"></a>

```c
struct mipi_dsi_timings
```

相关声明：[mipi_dsi_timings](../hardware/P248_MIPI显示串行时序.md)。

MIPI显示串行接口（MIPI-DSI）的显示时序。

<a id="r_mipi_5Fdsi_5Fdevice"></a>

```c
struct mipi_dsi_device
```

相关声明：[mipi_dsi_device](../hardware/P249_MIPI显示串行设备.md)。

MIPI显示串行接口（MIPI-DSI）设备。

<a id="r_mipi_5Fdsi_5Fmsg"></a>

```c
struct mipi_dsi_msg
```

相关声明：[mipi_dsi_msg](../hardware/P250_MIPI显示串行消息.md)。

MIPI显示串行接口（MIPI-DSI）的读写消息。

<a id="r_mipi_5Fdsi_5Fdriver_5Fapi"></a>

```c
struct mipi_dsi_driver_api
```

相关声明：[mipi_dsi_driver_api](../hardware/P254_MIPI显示串行函数表.md)。

驱动操作（Driver Operations）：MIPI显示串行接口（MIPI-DSI）驱动操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.2\_宏定义（Macros）

<a id="r_gaaf7954dcd5644e3ff332f5fab8fe48ef"></a>

```c
#define MIPI_DSI_MSG_USE_LPM BIT(0x0)
```

相关声明：[MIPI_DSI_MSG_USE_LPM](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gaaf7954dcd5644e3ff332f5fab8fe48ef)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="define-members-0"></a>

### MIPI-DSI 设备模式标志（Device Mode Flags）

<a id="r_ga2b4ff0fda3d00061b06e576a98628e7b"></a>

```c
#define MIPI_DSI_MODE_VIDEO BIT(0)
```

相关声明：[MIPI_DSI_MODE_VIDEO](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga2b4ff0fda3d00061b06e576a98628e7b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

视频模式（Video Mode）。

<a id="r_gaabfe30e5981efc1a73f4f9bf2def1610"></a>

```c
#define MIPI_DSI_MODE_VIDEO_BURST BIT(1)
```

相关声明：[MIPI_DSI_MODE_VIDEO_BURST](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gaabfe30e5981efc1a73f4f9bf2def1610)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

视频突发模式（Video Burst Mode）。

<a id="r_ga75709f3a91b803598d9d772f3c5b9eed"></a>

```c
#define MIPI_DSI_MODE_VIDEO_SYNC_PULSE BIT(2)
```

相关声明：[MIPI_DSI_MODE_VIDEO_SYNC_PULSE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga75709f3a91b803598d9d772f3c5b9eed)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

视频脉冲模式（Video Pulse Mode）。

<a id="r_ga5871aadda35ece0944217053f5c6c6fe"></a>

```c
#define MIPI_DSI_MODE_VIDEO_AUTO_VERT BIT(3)
```

相关声明：[MIPI_DSI_MODE_VIDEO_AUTO_VERT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga5871aadda35ece0944217053f5c6c6fe)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

使能自动垂直计数模式（Auto Vertical Count Mode）。

<a id="r_ga21d9620a4986884bbe2ac3a11b311337"></a>

```c
#define MIPI_DSI_MODE_VIDEO_HSE BIT(4)
```

相关声明：[MIPI_DSI_MODE_VIDEO_HSE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga21d9620a4986884bbe2ac3a11b311337)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

在垂直同步脉冲（vsync-pulse）和垂直消隐前后沿区域（v-porch）中，使能水平同步结束数据包（hsync-end Packets）。

<a id="r_ga625d1738ae1cfd25aef5772729c0aae8"></a>

```c
#define MIPI_DSI_MODE_VIDEO_HFP BIT(5)
```

相关声明：[MIPI_DSI_MODE_VIDEO_HFP](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga625d1738ae1cfd25aef5772729c0aae8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

禁用水平前沿区域（hfront-porch Area）。

<a id="r_ga90e09b889a1dbac1e2b7b9ae84f38ee4"></a>

```c
#define MIPI_DSI_MODE_VIDEO_HBP BIT(6)
```

相关声明：[MIPI_DSI_MODE_VIDEO_HBP](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga90e09b889a1dbac1e2b7b9ae84f38ee4)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

禁用水平后沿区域（hback-porch Area）。

<a id="r_ga395bb9085f92a1927e3cc317196ab353"></a>

```c
#define MIPI_DSI_MODE_VIDEO_HSA BIT(7)
```

相关声明：[MIPI_DSI_MODE_VIDEO_HSA](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga395bb9085f92a1927e3cc317196ab353)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

禁用水平同步有效区域（hsync-active Area）。

<a id="r_gacdc35d8e6726accc88c2e2e82c88d46d"></a>

```c
#define MIPI_DSI_MODE_VSYNC_FLUSH BIT(8)
```

相关声明：[MIPI_DSI_MODE_VSYNC_FLUSH](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gacdc35d8e6726accc88c2e2e82c88d46d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

在垂直同步脉冲（vsync Pulse）时清空显示先进先出缓冲区（FIFO）。

<a id="r_ga4bbcabcb84af1a2bd715b0bd8be78db3"></a>

```c
#define MIPI_DSI_MODE_EOT_PACKET BIT(9)
```

相关声明：[MIPI_DSI_MODE_EOT_PACKET](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga4bbcabcb84af1a2bd715b0bd8be78db3)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

在高速模式（HS Mode）中禁用传输结束数据包（EoT Packets）。

<a id="r_ga75c0e183f1235e37245cf890aa4a656b"></a>

```c
#define MIPI_DSI_CLOCK_NON_CONTINUOUS BIT(10)
```

相关声明：[MIPI_DSI_CLOCK_NON_CONTINUOUS](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga75c0e183f1235e37245cf890aa4a656b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

设备支持非连续时钟行为（Non-continuous Clock Behavior），参见 DSI 规范 5.6.1。

<a id="r_ga1f8923811fc5d704e28362e72a1f1633"></a>

```c
#define MIPI_DSI_MODE_LPM BIT(11)
```

相关声明：[MIPI_DSI_MODE_LPM](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga1f8923811fc5d704e28362e72a1f1633)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

以低功耗方式（Low Power）传输数据。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 7.3\_类型定义（Typedefs）

<a id="r_ga9abb63e5c7cdb7597376a237a420c2b5"></a>

```c
typedef int(* mipi_dsi_api_attach_t) (const struct device *dev, uint8_t channel, const struct mipi_dsi_device *mdev)
```

相关声明：[mipi_dsi_api_attach_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface__backend.html#ga9abb63e5c7cdb7597376a237a420c2b5)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mipi_dsi_device](../hardware/P249_MIPI显示串行设备.md)。

向 MIPI 显示串行接口（MIPI-DSI）总线挂接新设备。

<a id="r_ga9ebc67e63c629c75ff61fa220a2787a0"></a>

```c
typedef ssize_t(* mipi_dsi_api_transfer_t) (const struct device *dev, uint8_t channel, struct mipi_dsi_msg *msg)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[mipi_dsi_api_transfer_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface__backend.html#ga9ebc67e63c629c75ff61fa220a2787a0)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mipi_dsi_msg](../hardware/P250_MIPI显示串行消息.md)。

与挂接到 MIPI-DSI 总线的设备进行双向数据传输（Transfer）。

<a id="r_gaf5e12800d2a80e8a78da16cb5a71b008"></a>

```c
typedef int(* mipi_dsi_api_detach_t) (const struct device *dev, uint8_t channel, const struct mipi_dsi_device *mdev)
```

相关声明：[mipi_dsi_api_detach_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface__backend.html#gaf5e12800d2a80e8a78da16cb5a71b008)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mipi_dsi_device](../hardware/P249_MIPI显示串行设备.md)。

从 MIPI-DSI 总线分离设备（Detach）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.4\_函数（Functions）

<a id="r_ga18689fac223fddc10b23b6bc6712944e"></a>

```c
static int mipi_dsi_attach (const struct device *dev, uint8_t channel, const struct mipi_dsi_device *mdev)
```

相关声明：[mipi_dsi_attach](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga18689fac223fddc10b23b6bc6712944e)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mipi_dsi_device](../hardware/P249_MIPI显示串行设备.md)。

向 MIPI 显示串行接口（MIPI-DSI）总线挂接新设备。

<a id="r_gace5bb52f483634baa185f46ac61efb71"></a>

```c
static ssize_t mipi_dsi_transfer (const struct device *dev, uint8_t channel, struct mipi_dsi_msg *msg)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[mipi_dsi_transfer](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gace5bb52f483634baa185f46ac61efb71)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mipi_dsi_msg](../hardware/P250_MIPI显示串行消息.md)。

与挂接到 MIPI-DSI 总线的设备进行双向数据传输（Transfer）。

<a id="r_ga121633e8e379e7d1ebd749328f2014fd"></a>

```c
ssize_t mipi_dsi_generic_read (const struct device *dev, uint8_t channel, const void *params, size_t nparams, void *buf, size_t len)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[mipi_dsi_generic_read](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga121633e8e379e7d1ebd749328f2014fd)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

MIPI-DSI 通用读取（Generic Read）。

<a id="r_ga5442f45c7c827d1dd8c3fa21da49c560"></a>

```c
ssize_t mipi_dsi_generic_write (const struct device *dev, uint8_t channel, const void *buf, size_t len)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[mipi_dsi_generic_write](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga5442f45c7c827d1dd8c3fa21da49c560)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

MIPI-DSI 通用写入（Generic Write）。

<a id="r_ga7b5f52bcd51821bf120c5ac67b4c2fa5"></a>

```c
ssize_t mipi_dsi_dcs_read (const struct device *dev, uint8_t channel, uint8_t cmd, void *buf, size_t len)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[mipi_dsi_dcs_read](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga7b5f52bcd51821bf120c5ac67b4c2fa5)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)。

MIPI-DSI 显示命令集读取（DCS Read）。

<a id="r_gad0f324e32191469bc0d24ba203286237"></a>

```c
ssize_t mipi_dsi_dcs_write (const struct device *dev, uint8_t channel, uint8_t cmd, const void *buf, size_t len)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[mipi_dsi_dcs_write](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gad0f324e32191469bc0d24ba203286237)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)。

MIPI-DSI 显示命令集写入（DCS Write）。

<a id="r_gace728ac82d30e15868298facd6df0228"></a>

```c
static int mipi_dsi_detach (const struct device *dev, uint8_t channel, const struct mipi_dsi_device *mdev)
```

相关声明：[mipi_dsi_detach](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gace728ac82d30e15868298facd6df0228)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mipi_dsi_device](../hardware/P249_MIPI显示串行设备.md)。

从 MIPI-DSI 总线分离设备（Detach）。


## 7.5\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [sys/types.h](../api_source_runtime_reference/P038_types.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/display/mipi_display.h](../api_source_reference/P531_mipi_display.h_源码浏览.md)
- [zephyr/dt-bindings/mipi_dsi/mipi_dsi.h](../api_source_reference/P192_mipi_dsi.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P043_mipi_dsi.h_源码浏览.md)
- [mipi_dsi_timings](../hardware/P248_MIPI显示串行时序.md)
- [mipi_dsi_device](../hardware/P249_MIPI显示串行设备.md)
- [mipi_dsi_msg](../hardware/P250_MIPI显示串行消息.md)
- [mipi_dsi_driver_api](../hardware/P254_MIPI显示串行函数表.md)
- [MIPI_DSI_MSG_USE_LPM](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gaaf7954dcd5644e3ff332f5fab8fe48ef)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [MIPI_DSI_MODE_VIDEO](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga2b4ff0fda3d00061b06e576a98628e7b)
- [MIPI_DSI_MODE_VIDEO_BURST](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gaabfe30e5981efc1a73f4f9bf2def1610)
- [MIPI_DSI_MODE_VIDEO_SYNC_PULSE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga75709f3a91b803598d9d772f3c5b9eed)
- [MIPI_DSI_MODE_VIDEO_AUTO_VERT](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga5871aadda35ece0944217053f5c6c6fe)
- [MIPI_DSI_MODE_VIDEO_HSE](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga21d9620a4986884bbe2ac3a11b311337)
- [MIPI_DSI_MODE_VIDEO_HFP](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga625d1738ae1cfd25aef5772729c0aae8)
- [MIPI_DSI_MODE_VIDEO_HBP](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga90e09b889a1dbac1e2b7b9ae84f38ee4)
- [MIPI_DSI_MODE_VIDEO_HSA](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga395bb9085f92a1927e3cc317196ab353)
- [MIPI_DSI_MODE_VSYNC_FLUSH](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gacdc35d8e6726accc88c2e2e82c88d46d)
- [MIPI_DSI_MODE_EOT_PACKET](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga4bbcabcb84af1a2bd715b0bd8be78db3)
- [MIPI_DSI_CLOCK_NON_CONTINUOUS](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga75c0e183f1235e37245cf890aa4a656b)
- [MIPI_DSI_MODE_LPM](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga1f8923811fc5d704e28362e72a1f1633)
- [mipi_dsi_api_attach_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface__backend.html#ga9abb63e5c7cdb7597376a237a420c2b5)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)
- [mipi_dsi_api_transfer_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface__backend.html#ga9ebc67e63c629c75ff61fa220a2787a0)
- [mipi_dsi_api_detach_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface__backend.html#gaf5e12800d2a80e8a78da16cb5a71b008)
- [mipi_dsi_attach](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga18689fac223fddc10b23b6bc6712944e)
- [mipi_dsi_transfer](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gace5bb52f483634baa185f46ac61efb71)
- [mipi_dsi_generic_read](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga121633e8e379e7d1ebd749328f2014fd)
- [mipi_dsi_generic_write](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga5442f45c7c827d1dd8c3fa21da49c560)
- [mipi_dsi_dcs_read](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#ga7b5f52bcd51821bf120c5ac67b4c2fa5)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [mipi_dsi_dcs_write](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gad0f324e32191469bc0d24ba203286237)
- [mipi_dsi_detach](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface.html#gace728ac82d30e15868298facd6df0228)

<a id="header-details"></a>

---

[上一章](P006_zephyr__drivers__firmware__scmi__util.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P008_zephyr__dt-bindings__mipi_dbi__mipi_dbi.h_文件参考.md)
