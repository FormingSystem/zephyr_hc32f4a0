---
id: learning.zephyr-docs.api-file-display-chat-reference.page-11
title: zephyr__drivers__i2s.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/i2s_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_zephyr\_\_drivers\_\_i2s.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/i2s_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

芯片间音频接口（Inter-IC Sound，I2S）驱动API的主头文件。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/syscalls/i2s.h>
```

查看此文件的源码。

芯片间音频接口（Inter-IC Sound，I2S）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 11.1\_数据结构（Data Structures）

<a id="r_i2s_5Fconfig"></a>

```c
struct i2s_config
```

相关声明：[i2s_config](../audio_video_model_reference/P008_i2s_config_结构体.md)。

接口配置选项（Interface Configuration Options）。

<a id="r_i2s_5Fdriver_5Fapi"></a>

```c
struct i2s_driver_api
```

相关声明：[i2s_driver_api](../audio_video_model_reference/P009_i2s_driver_api_结构体.md)。

驱动操作（Driver Operations）：I2S驱动操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.2\_宏定义（Macros）

<a id="r_gaa3f67c47874141782fbb7ec5a671b566"></a>

```c
#define I2S_FMT_DATA_FORMAT_SHIFT 0
```

相关声明：[I2S_FMT_DATA_FORMAT_SHIFT](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gaa3f67c47874141782fbb7ec5a671b566)。

数据格式（Data Format）位字段位置。

<a id="r_gaf3eb0116133dd3a041d9a80cb3397263"></a>

```c
#define I2S_FMT_DATA_FORMAT_MASK (0x7 << I2S_FMT_DATA_FORMAT_SHIFT)
```

相关声明：[I2S_FMT_DATA_FORMAT_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gaf3eb0116133dd3a041d9a80cb3397263)、[I2S_FMT_DATA_FORMAT_SHIFT](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gaa3f67c47874141782fbb7ec5a671b566)。

数据格式（Data Format）位字段掩码。

<a id="r_gaa1adc5e3b722e89f20f258b0fd53a2c5"></a>

```c
#define I2S_FMT_DATA_FORMAT_I2S (0 << I2S_FMT_DATA_FORMAT_SHIFT)
```

相关声明：[I2S_FMT_DATA_FORMAT_I2S](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gaa1adc5e3b722e89f20f258b0fd53a2c5)、[I2S_FMT_DATA_FORMAT_SHIFT](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gaa3f67c47874141782fbb7ec5a671b566)。

标准 I2S 数据格式（Standard I2S Data Format）。

<a id="r_ga70c7a19078a6f72e078b9c0488018b11"></a>

```c
#define I2S_FMT_DATA_FORMAT_PCM_SHORT (1 << I2S_FMT_DATA_FORMAT_SHIFT)
```

相关声明：[I2S_FMT_DATA_FORMAT_PCM_SHORT](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga70c7a19078a6f72e078b9c0488018b11)、[I2S_FMT_DATA_FORMAT_SHIFT](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gaa3f67c47874141782fbb7ec5a671b566)。

PCM 短帧同步数据格式（Short Frame Sync Data Format）。

<a id="r_ga7032b1894faded14a174593a3f10ca3c"></a>

```c
#define I2S_FMT_DATA_FORMAT_PCM_LONG (2 << I2S_FMT_DATA_FORMAT_SHIFT)
```

相关声明：[I2S_FMT_DATA_FORMAT_PCM_LONG](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga7032b1894faded14a174593a3f10ca3c)、[I2S_FMT_DATA_FORMAT_SHIFT](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gaa3f67c47874141782fbb7ec5a671b566)。

PCM 长帧同步数据格式（Long Frame Sync Data Format）。

<a id="r_gaabc5e62ed922b8c5834ed40c6af78022"></a>

```c
#define I2S_FMT_DATA_FORMAT_LEFT_JUSTIFIED (3 << I2S_FMT_DATA_FORMAT_SHIFT)
```

相关声明：[I2S_FMT_DATA_FORMAT_LEFT_JUSTIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gaabc5e62ed922b8c5834ed40c6af78022)、[I2S_FMT_DATA_FORMAT_SHIFT](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gaa3f67c47874141782fbb7ec5a671b566)。

左对齐数据格式（Left Justified Data Format）。

<a id="r_ga8ad25375c2f7344b2959bed2eec4be72"></a>

```c
#define I2S_FMT_DATA_FORMAT_RIGHT_JUSTIFIED (4 << I2S_FMT_DATA_FORMAT_SHIFT)
```

相关声明：[I2S_FMT_DATA_FORMAT_RIGHT_JUSTIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga8ad25375c2f7344b2959bed2eec4be72)、[I2S_FMT_DATA_FORMAT_SHIFT](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gaa3f67c47874141782fbb7ec5a671b566)。

右对齐数据格式（Right Justified Data Format）。

<a id="r_ga6a6c18e170333a56086f5bcf96e552a1"></a>

```c
#define I2S_FMT_DATA_ORDER_MSB (0 << 3)
```

相关声明：[I2S_FMT_DATA_ORDER_MSB](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga6a6c18e170333a56086f5bcf96e552a1)。

先发送最高有效位（MSB First）。

<a id="r_gacc2d0662903b2300b0e1009a8223ed7d"></a>

```c
#define I2S_FMT_DATA_ORDER_LSB BIT(3)
```

相关声明：[I2S_FMT_DATA_ORDER_LSB](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gacc2d0662903b2300b0e1009a8223ed7d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

先发送最低有效位（LSB First）。

<a id="r_ga052fa04f51ab96d90cdaf0d35f19a166"></a>

```c
#define I2S_FMT_DATA_ORDER_INV I2S_FMT_DATA_ORDER_LSB
```

相关声明：[I2S_FMT_DATA_ORDER_INV](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga052fa04f51ab96d90cdaf0d35f19a166)、[I2S_FMT_DATA_ORDER_LSB](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gacc2d0662903b2300b0e1009a8223ed7d)。

反转位顺序（Invert Bit Ordering），先发送最低有效位（LSB First）。

<a id="r_ga713fe1eb042953a315d1cb606a28d5ca"></a>

```c
#define I2S_FMT_CLK_FORMAT_SHIFT 4
```

相关声明：[I2S_FMT_CLK_FORMAT_SHIFT](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga713fe1eb042953a315d1cb606a28d5ca)。

数据格式（Data Format）位字段位置。

<a id="r_ga16e4b44cf7f4b2d11bbd2d50522d086d"></a>

```c
#define I2S_FMT_CLK_FORMAT_MASK (0x3 << I2S_FMT_CLK_FORMAT_SHIFT)
```

相关声明：[I2S_FMT_CLK_FORMAT_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga16e4b44cf7f4b2d11bbd2d50522d086d)、[I2S_FMT_CLK_FORMAT_SHIFT](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga713fe1eb042953a315d1cb606a28d5ca)。

数据格式（Data Format）位字段掩码。

<a id="r_ga1bbc3f0600b406691ce016bf7bf96a5f"></a>

```c
#define I2S_FMT_BIT_CLK_INV BIT(4)
```

相关声明：[I2S_FMT_BIT_CLK_INV](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga1bbc3f0600b406691ce016bf7bf96a5f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

反转位时钟（Invert Bit Clock）。

<a id="r_ga1cd356cbe68f622d0b3f5aee027d1f57"></a>

```c
#define I2S_FMT_FRAME_CLK_INV BIT(5)
```

相关声明：[I2S_FMT_FRAME_CLK_INV](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga1cd356cbe68f622d0b3f5aee027d1f57)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

反转帧时钟（Invert Frame Clock）。

<a id="r_gad555437f250801cbc8970cd02d7b7cde"></a>

```c
#define I2S_FMT_CLK_NF_NB (0 << I2S_FMT_CLK_FORMAT_SHIFT)
```

相关声明：[I2S_FMT_CLK_NF_NB](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gad555437f250801cbc8970cd02d7b7cde)、[I2S_FMT_CLK_FORMAT_SHIFT](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga713fe1eb042953a315d1cb606a28d5ca)。

帧时钟正常（Normal Frame）、位时钟正常（Normal Bit Clock）。

<a id="r_ga85714d803548509c6b41c2579b7f2a7f"></a>

```c
#define I2S_FMT_CLK_NF_IB (1 << I2S_FMT_CLK_FORMAT_SHIFT)
```

相关声明：[I2S_FMT_CLK_NF_IB](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga85714d803548509c6b41c2579b7f2a7f)、[I2S_FMT_CLK_FORMAT_SHIFT](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga713fe1eb042953a315d1cb606a28d5ca)。

帧时钟正常（Normal Frame）、位时钟反转（Inverted Bit Clock）。

<a id="r_ga5686ac4f8e3327d36f3f1293168330cd"></a>

```c
#define I2S_FMT_CLK_IF_NB (2 << I2S_FMT_CLK_FORMAT_SHIFT)
```

相关声明：[I2S_FMT_CLK_IF_NB](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga5686ac4f8e3327d36f3f1293168330cd)、[I2S_FMT_CLK_FORMAT_SHIFT](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga713fe1eb042953a315d1cb606a28d5ca)。

帧时钟反转（Inverted Frame）、位时钟正常（Normal Bit Clock）。

<a id="r_gaaaf186e3265d2fea6c8dc43a8030272c"></a>

```c
#define I2S_FMT_CLK_IF_IB (3 << I2S_FMT_CLK_FORMAT_SHIFT)
```

相关声明：[I2S_FMT_CLK_IF_IB](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gaaaf186e3265d2fea6c8dc43a8030272c)、[I2S_FMT_CLK_FORMAT_SHIFT](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga713fe1eb042953a315d1cb606a28d5ca)。

帧时钟反转（Inverted Frame）、位时钟反转（Inverted Bit Clock）。

<a id="r_ga039e7e244f7f1452dcd197c0a689d6e6"></a>

```c
#define I2S_OPT_BIT_CLK_CONT (0 << 0)
```

相关声明：[I2S_OPT_BIT_CLK_CONT](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga039e7e244f7f1452dcd197c0a689d6e6)。

连续运行位时钟（Bit Clock）。

<a id="r_ga4a68f73ee794684f68a02066ce1d632c"></a>

```c
#define I2S_OPT_BIT_CLK_GATED BIT(0)
```

相关声明：[I2S_OPT_BIT_CLK_GATED](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga4a68f73ee794684f68a02066ce1d632c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

仅在发送数据时运行位时钟（Bit Clock）。

<a id="r_ga36795543fd2423c7c0882e85b133f007"></a>

```c
#define I2S_OPT_BIT_CLK_CONTROLLER (0 << 1)
```

相关声明：[I2S_OPT_BIT_CLK_CONTROLLER](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga36795543fd2423c7c0882e85b133f007)。

I2S 驱动为位时钟控制端（Bit Clock Controller）。

<a id="r_ga040259ad09d059b0c2865287a53abbc3"></a>

```c
#define I2S_OPT_BIT_CLK_TARGET BIT(1)
```

相关声明：[I2S_OPT_BIT_CLK_TARGET](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga040259ad09d059b0c2865287a53abbc3)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

I2S 驱动为位时钟目标端（Bit Clock Target）。

<a id="r_ga28ed57b0bfceaf91d30aac12de9a4c47"></a>

```c
#define I2S_OPT_FRAME_CLK_CONTROLLER (0 << 2)
```

相关声明：[I2S_OPT_FRAME_CLK_CONTROLLER](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga28ed57b0bfceaf91d30aac12de9a4c47)。

I2S 驱动为帧时钟控制端（Frame Clock Controller）。

<a id="r_gacf77b7fc22301b426c8faa88d9e5eb30"></a>

```c
#define I2S_OPT_FRAME_CLK_TARGET BIT(2)
```

相关声明：[I2S_OPT_FRAME_CLK_TARGET](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gacf77b7fc22301b426c8faa88d9e5eb30)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

I2S 驱动为帧时钟目标端（Frame Clock Target）。

<a id="r_ga54aaaa7f0403e4f03574ffcc6141a67f"></a>

```c
#define I2S_OPT_BIT_CLK_MASTER I2S_OPT_BIT_CLK_CONTROLLER __DEPRECATED_MACRO
```

相关声明：[I2S_OPT_BIT_CLK_MASTER](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga54aaaa7f0403e4f03574ffcc6141a67f)、[I2S_OPT_BIT_CLK_CONTROLLER](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga36795543fd2423c7c0882e85b133f007)。

<a id="r_gaa76784ed4a645cb751b2c683bfa4be40"></a>

```c
#define I2S_OPT_BIT_CLK_SLAVE I2S_OPT_BIT_CLK_TARGET __DEPRECATED_MACRO
```

相关声明：[I2S_OPT_BIT_CLK_SLAVE](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gaa76784ed4a645cb751b2c683bfa4be40)、[I2S_OPT_BIT_CLK_TARGET](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga040259ad09d059b0c2865287a53abbc3)。

<a id="r_gaedfc35128aae5058a17ef5601bdc73d2"></a>

```c
#define I2S_OPT_FRAME_CLK_MASTER I2S_OPT_FRAME_CLK_CONTROLLER __DEPRECATED_MACRO
```

相关声明：[I2S_OPT_FRAME_CLK_MASTER](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gaedfc35128aae5058a17ef5601bdc73d2)、[I2S_OPT_FRAME_CLK_CONTROLLER](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga28ed57b0bfceaf91d30aac12de9a4c47)。

<a id="r_ga138640dfb430fe0565840078a7b23ace"></a>

```c
#define I2S_OPT_FRAME_CLK_SLAVE I2S_OPT_FRAME_CLK_TARGET __DEPRECATED_MACRO
```

相关声明：[I2S_OPT_FRAME_CLK_SLAVE](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga138640dfb430fe0565840078a7b23ace)、[I2S_OPT_FRAME_CLK_TARGET](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gacf77b7fc22301b426c8faa88d9e5eb30)。

<a id="r_ga093ed00a6081da8b4d958f80744fa09f"></a>

```c
#define I2S_OPT_LOOPBACK BIT(7)
```

相关声明：[I2S_OPT_LOOPBACK](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga093ed00a6081da8b4d958f80744fa09f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

回环模式（Loop Back Mode）。

<a id="r_gadcb20e201a0fef1fe10f4cf916ff4b72"></a>

```c
#define I2S_OPT_PINGPONG BIT(6)
```

相关声明：[I2S_OPT_PINGPONG](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gadcb20e201a0fef1fe10f4cf916ff4b72)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

乒乓模式（Ping Pong Mode）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 11.3\_类型定义（Typedefs）

<a id="r_ga0939a3ba04a233d9d637fba8a42b0bbb"></a>

```c
typedef uint8_t i2s_fmt_t
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[i2s_fmt_t](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga0939a3ba04a233d9d637fba8a42b0bbb)。

I2S 数据流格式选项（Data Stream Format Options）。

<a id="r_gad0ca475f9bf5edeecc7de65b4f56c119"></a>

```c
typedef uint8_t i2s_opt_t
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[i2s_opt_t](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gad0ca475f9bf5edeecc7de65b4f56c119)。

I2S 配置选项（Configuration Options）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 11.4\_枚举（Enumerations）

<a id="r_ga975a0f0901cadc789075078aa79f723f"></a>

```c
enum i2s_dir { I2S_DIR_RX , I2S_DIR_TX , I2S_DIR_BOTH }
```

相关声明：[i2s_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga975a0f0901cadc789075078aa79f723f)、[I2S_DIR_RX](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gga975a0f0901cadc789075078aa79f723fac9f71d312c5d5ad7ef64af4217091aca)、[I2S_DIR_TX](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gga975a0f0901cadc789075078aa79f723fab005c2cfee6206c2b5b596638e6c8443)、[I2S_DIR_BOTH](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gga975a0f0901cadc789075078aa79f723fa3cca349476d0dbe214111b9ef5d8b272)。

I2S 方向（Direction）。

<a id="r_ga975d09fe35ddf7942968155b62abc531"></a>

```c
enum i2s_state { I2S_STATE_NOT_READY , I2S_STATE_READY , I2S_STATE_RUNNING , I2S_STATE_STOPPING , I2S_STATE_ERROR }
```

相关声明：[i2s_state](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga975d09fe35ddf7942968155b62abc531)、[I2S_STATE_NOT_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gga975d09fe35ddf7942968155b62abc531a7151755b31bbb614e7b668141a7ef43a)、[I2S_STATE_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gga975d09fe35ddf7942968155b62abc531af6babeef999bfb034ea55366e9c59b13)、[I2S_STATE_RUNNING](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gga975d09fe35ddf7942968155b62abc531aa3d21ba793efa7d8f557774e8b330a42)、[I2S_STATE_STOPPING](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gga975d09fe35ddf7942968155b62abc531a972fd7e9da207b36e07731b996620a33)、[I2S_STATE_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gga975d09fe35ddf7942968155b62abc531a68c0a46589ae00045900a8f79675641a)。

接口状态（Interface State）。

<a id="r_gac994676a89f1ea676475712a84003de6"></a>

```c
enum i2s_trigger_cmd { I2S_TRIGGER_START , I2S_TRIGGER_STOP , I2S_TRIGGER_DRAIN , I2S_TRIGGER_DROP , I2S_TRIGGER_PREPARE }
```

相关声明：[i2s_trigger_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gac994676a89f1ea676475712a84003de6)、[I2S_TRIGGER_START](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ggac994676a89f1ea676475712a84003de6a6f4cacef6ee84256e6223a4bab3bc3ac)、[I2S_TRIGGER_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ggac994676a89f1ea676475712a84003de6a37caf001d6ee6a263f3487f27952688b)、[I2S_TRIGGER_DRAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ggac994676a89f1ea676475712a84003de6a7bdbdf37c5a6481faa1866be323bb9de)、[I2S_TRIGGER_DROP](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ggac994676a89f1ea676475712a84003de6ae8155a4d72875bd885dc987765d7628d)、[I2S_TRIGGER_PREPARE](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ggac994676a89f1ea676475712a84003de6a61943bd287840e33bffd74bbc4a59e88)。

触发命令（Trigger Command）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.5\_函数（Functions）

<a id="r_ga299003d72146c127f88d7c12c08889cc"></a>

```c
int i2s_configure (const struct device *dev, enum i2s_dir dir, const struct i2s_config *cfg)
```

相关声明：[i2s_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga299003d72146c127f88d7c12c08889cc)、[device](../device_reference/P002_设备对象结构.md)、[i2s_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga975a0f0901cadc789075078aa79f723f)、[i2s_config](../audio_video_model_reference/P008_i2s_config_结构体.md)。

配置主机 I2S 控制器（Host I2S Controller）的运行方式。

<a id="r_gacf4d51fcfd07573582858cd50a76785d"></a>

```c
static const struct i2s_config * i2s_config_get (const struct device *dev, enum i2s_dir dir)
```

相关声明：[i2s_config](../audio_video_model_reference/P008_i2s_config_结构体.md)、[i2s_config_get](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gacf4d51fcfd07573582858cd50a76785d)、[device](../device_reference/P002_设备对象结构.md)、[i2s_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga975a0f0901cadc789075078aa79f723f)。

获取主机 I2S 控制器（Host I2S Controller）的配置信息。

<a id="r_ga7f23b7959280e1c4075a4305c3edd655"></a>

```c
static int i2s_read (const struct device *dev, void **mem_block, size_t *size)
```

相关声明：[i2s_read](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga7f23b7959280e1c4075a4305c3edd655)、[device](../device_reference/P002_设备对象结构.md)。

从接收队列（RX Queue）读取数据。

<a id="r_ga5c8ca0bf6b394170ffbe031de8e37c28"></a>

```c
int i2s_buf_read (const struct device *dev, void *buf, size_t *size)
```

相关声明：[i2s_buf_read](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga5c8ca0bf6b394170ffbe031de8e37c28)、[device](../device_reference/P002_设备对象结构.md)。

将接收队列（RX Queue）的数据读入所提供的缓冲区。

<a id="r_ga01edf23acc6c16bbaf718dab8061a7a0"></a>

```c
static int i2s_write (const struct device *dev, void *mem_block, size_t size)
```

相关声明：[i2s_write](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga01edf23acc6c16bbaf718dab8061a7a0)、[device](../device_reference/P002_设备对象结构.md)。

向发送队列（TX Queue）写入数据。

<a id="r_ga98cbfe351a8dd5db361f4667959d0b58"></a>

```c
int i2s_buf_write (const struct device *dev, void *buf, size_t size)
```

相关声明：[i2s_buf_write](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga98cbfe351a8dd5db361f4667959d0b58)、[device](../device_reference/P002_设备对象结构.md)。

将所提供缓冲区中的数据写入发送队列（TX Queue）。

<a id="r_gaaa153e6c325f8f34f2fd5d550e4d3297"></a>

```c
int i2s_trigger (const struct device *dev, enum i2s_dir dir, enum i2s_trigger_cmd cmd)
```

相关声明：[i2s_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gaaa153e6c325f8f34f2fd5d550e4d3297)、[device](../device_reference/P002_设备对象结构.md)、[i2s_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga975a0f0901cadc789075078aa79f723f)、[i2s_trigger_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gac994676a89f1ea676475712a84003de6)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)。

发送触发命令（Trigger Command）。


## 11.6\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P089_i2s.h_源码浏览.md)
- [i2s_config](../audio_video_model_reference/P008_i2s_config_结构体.md)
- [i2s_driver_api](../audio_video_model_reference/P009_i2s_driver_api_结构体.md)
- [I2S_FMT_DATA_FORMAT_SHIFT](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gaa3f67c47874141782fbb7ec5a671b566)
- [I2S_FMT_DATA_FORMAT_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gaf3eb0116133dd3a041d9a80cb3397263)
- [I2S_FMT_DATA_FORMAT_I2S](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gaa1adc5e3b722e89f20f258b0fd53a2c5)
- [I2S_FMT_DATA_FORMAT_PCM_SHORT](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga70c7a19078a6f72e078b9c0488018b11)
- [I2S_FMT_DATA_FORMAT_PCM_LONG](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga7032b1894faded14a174593a3f10ca3c)
- [I2S_FMT_DATA_FORMAT_LEFT_JUSTIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gaabc5e62ed922b8c5834ed40c6af78022)
- [I2S_FMT_DATA_FORMAT_RIGHT_JUSTIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga8ad25375c2f7344b2959bed2eec4be72)
- [I2S_FMT_DATA_ORDER_MSB](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga6a6c18e170333a56086f5bcf96e552a1)
- [I2S_FMT_DATA_ORDER_LSB](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gacc2d0662903b2300b0e1009a8223ed7d)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [I2S_FMT_DATA_ORDER_INV](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga052fa04f51ab96d90cdaf0d35f19a166)
- [I2S_FMT_CLK_FORMAT_SHIFT](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga713fe1eb042953a315d1cb606a28d5ca)
- [I2S_FMT_CLK_FORMAT_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga16e4b44cf7f4b2d11bbd2d50522d086d)
- [I2S_FMT_BIT_CLK_INV](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga1bbc3f0600b406691ce016bf7bf96a5f)
- [I2S_FMT_FRAME_CLK_INV](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga1cd356cbe68f622d0b3f5aee027d1f57)
- [I2S_FMT_CLK_NF_NB](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gad555437f250801cbc8970cd02d7b7cde)
- [I2S_FMT_CLK_NF_IB](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga85714d803548509c6b41c2579b7f2a7f)
- [I2S_FMT_CLK_IF_NB](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga5686ac4f8e3327d36f3f1293168330cd)
- [I2S_FMT_CLK_IF_IB](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gaaaf186e3265d2fea6c8dc43a8030272c)
- [I2S_OPT_BIT_CLK_CONT](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga039e7e244f7f1452dcd197c0a689d6e6)
- [I2S_OPT_BIT_CLK_GATED](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga4a68f73ee794684f68a02066ce1d632c)
- [I2S_OPT_BIT_CLK_CONTROLLER](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga36795543fd2423c7c0882e85b133f007)
- [I2S_OPT_BIT_CLK_TARGET](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga040259ad09d059b0c2865287a53abbc3)
- [I2S_OPT_FRAME_CLK_CONTROLLER](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga28ed57b0bfceaf91d30aac12de9a4c47)
- [I2S_OPT_FRAME_CLK_TARGET](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gacf77b7fc22301b426c8faa88d9e5eb30)
- [I2S_OPT_BIT_CLK_MASTER](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga54aaaa7f0403e4f03574ffcc6141a67f)
- [I2S_OPT_BIT_CLK_SLAVE](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gaa76784ed4a645cb751b2c683bfa4be40)
- [I2S_OPT_FRAME_CLK_MASTER](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gaedfc35128aae5058a17ef5601bdc73d2)
- [I2S_OPT_FRAME_CLK_SLAVE](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga138640dfb430fe0565840078a7b23ace)
- [I2S_OPT_LOOPBACK](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga093ed00a6081da8b4d958f80744fa09f)
- [I2S_OPT_PINGPONG](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gadcb20e201a0fef1fe10f4cf916ff4b72)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [i2s_fmt_t](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga0939a3ba04a233d9d637fba8a42b0bbb)
- [i2s_opt_t](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gad0ca475f9bf5edeecc7de65b4f56c119)
- [i2s_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga975a0f0901cadc789075078aa79f723f)
- [I2S_DIR_RX](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gga975a0f0901cadc789075078aa79f723fac9f71d312c5d5ad7ef64af4217091aca)
- [I2S_DIR_TX](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gga975a0f0901cadc789075078aa79f723fab005c2cfee6206c2b5b596638e6c8443)
- [I2S_DIR_BOTH](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gga975a0f0901cadc789075078aa79f723fa3cca349476d0dbe214111b9ef5d8b272)
- [i2s_state](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga975d09fe35ddf7942968155b62abc531)
- [I2S_STATE_NOT_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gga975d09fe35ddf7942968155b62abc531a7151755b31bbb614e7b668141a7ef43a)
- [I2S_STATE_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gga975d09fe35ddf7942968155b62abc531af6babeef999bfb034ea55366e9c59b13)
- [I2S_STATE_RUNNING](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gga975d09fe35ddf7942968155b62abc531aa3d21ba793efa7d8f557774e8b330a42)
- [I2S_STATE_STOPPING](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gga975d09fe35ddf7942968155b62abc531a972fd7e9da207b36e07731b996620a33)
- [I2S_STATE_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gga975d09fe35ddf7942968155b62abc531a68c0a46589ae00045900a8f79675641a)
- [i2s_trigger_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gac994676a89f1ea676475712a84003de6)
- [I2S_TRIGGER_START](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ggac994676a89f1ea676475712a84003de6a6f4cacef6ee84256e6223a4bab3bc3ac)
- [I2S_TRIGGER_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ggac994676a89f1ea676475712a84003de6a37caf001d6ee6a263f3487f27952688b)
- [I2S_TRIGGER_DRAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ggac994676a89f1ea676475712a84003de6a7bdbdf37c5a6481faa1866be323bb9de)
- [I2S_TRIGGER_DROP](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ggac994676a89f1ea676475712a84003de6ae8155a4d72875bd885dc987765d7628d)
- [I2S_TRIGGER_PREPARE](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ggac994676a89f1ea676475712a84003de6a61943bd287840e33bffd74bbc4a59e88)
- [i2s_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga299003d72146c127f88d7c12c08889cc)
- [device](../device_reference/P002_设备对象结构.md)
- [i2s_config_get](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gacf4d51fcfd07573582858cd50a76785d)
- [i2s_read](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga7f23b7959280e1c4075a4305c3edd655)
- [i2s_buf_read](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga5c8ca0bf6b394170ffbe031de8e37c28)
- [i2s_write](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga01edf23acc6c16bbaf718dab8061a7a0)
- [i2s_buf_write](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga98cbfe351a8dd5db361f4667959d0b58)
- [i2s_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gaaa153e6c325f8f34f2fd5d550e4d3297)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)

<a id="header-details"></a>

---

[上一章](P010_zephyr__dt-bindings__pinctrl__em32f967-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P012_zephyr__net__ieee802154_mgmt.h_文件参考.md)
