---
id: learning.zephyr-docs.api-file-bluetooth-media-reference.page-7
title: zephyr__bluetooth__audio__media_proxy.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/media__proxy_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_bluetooth\_\_audio\_\_media\_proxy.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/media__proxy_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙媒体代理（Media Proxy）的API。

<a id="details"></a>

```c
#include <stdint.h>
#include <stdbool.h>
#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/sys/util_macro.h>
#include "mcs.h"
```

查看此文件的源码。

蓝牙媒体代理（Media Proxy）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.1\_数据结构（Data Structures）

<a id="r_mpl_5Fcmd"></a>

```c
struct mpl_cmd
```

相关声明：[mpl_cmd](../audio_video_model_reference/P037_mpl_cmd_结构体.md)。

媒体播放器命令（Media Player Command）。

<a id="r_mpl_5Fcmd_5Fntf"></a>

```c
struct mpl_cmd_ntf
```

相关声明：[mpl_cmd_ntf](../audio_video_model_reference/P038_mpl_cmd_ntf_结构体.md)。

媒体命令通知（Media Command Notification）。

<a id="r_mpl_5Fsci"></a>

```c
struct mpl_sci
```

相关声明：[mpl_sci](../audio_video_model_reference/P039_mpl_sci_结构体.md)。

搜索控制项（Search Control Item）。

<a id="r_mpl_5Fsearch"></a>

```c
struct mpl_search
```

相关声明：[mpl_search](../audio_video_model_reference/P040_mpl_search_结构体.md)。

搜索（Search）。

<a id="r_media_5Fproxy_5Fctrl_5Fcbs"></a>

```c
struct media_proxy_ctrl_cbs
```

相关声明：[media_proxy_ctrl_cbs](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md)。

媒体代理（Media Proxy）对控制器的回调。

<a id="r_media_5Fproxy_5Fpl_5Fcalls"></a>

```c
struct media_proxy_pl_calls
```

相关声明：[media_proxy_pl_calls](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md)。

播放器中可由媒体代理（Media Proxy）调用的接口。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.2\_宏定义（Macros）

<a id="r_ga22c2599cd62a263a01c06c9bd9fff054"></a>

```c
#define MEDIA_PROXY_OPCODES_SUPPORTED_LEN 4U
```

相关声明：[MEDIA_PROXY_OPCODES_SUPPORTED_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga22c2599cd62a263a01c06c9bd9fff054)。

媒体播放器（Media Player）支持的操作码字段长度。

<a id="define-members-0"></a>

### 播放速度参数（Playback speed parameters）

允许 -128 到 127 的所有值，这里仅定义其中一部分。

<a id="r_ga61732644eecad1442d5cedbda8f8cc08"></a>

```c
#define MEDIA_PROXY_PLAYBACK_SPEED_MIN -128
```

相关声明：[MEDIA_PROXY_PLAYBACK_SPEED_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga61732644eecad1442d5cedbda8f8cc08)。

最低播放速度（Minimum Playback Speed），对应 25% 速度。

<a id="r_ga5462f8d5ce98cc33a131b2e7b5548c41"></a>

```c
#define MEDIA_PROXY_PLAYBACK_SPEED_QUARTER -128
```

相关声明：[MEDIA_PROXY_PLAYBACK_SPEED_QUARTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga5462f8d5ce98cc33a131b2e7b5548c41)。

四分之一播放速度（Quarter Playback Speed），对应 25% 速度。

<a id="r_ga4c765363c2a5b0d9800864859746ae33"></a>

```c
#define MEDIA_PROXY_PLAYBACK_SPEED_HALF -64
```

相关声明：[MEDIA_PROXY_PLAYBACK_SPEED_HALF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga4c765363c2a5b0d9800864859746ae33)。

半速播放（Half Playback Speed），对应 50% 速度。

<a id="r_ga6d8854bd54dcbb657f0ba545ec231368"></a>

```c
#define MEDIA_PROXY_PLAYBACK_SPEED_UNITY 0
```

相关声明：[MEDIA_PROXY_PLAYBACK_SPEED_UNITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga6d8854bd54dcbb657f0ba545ec231368)。

一倍播放速度（Unity Playback Speed），对应 100% 速度。

<a id="r_gaa53d906340c0b2adb314945f5299464e"></a>

```c
#define MEDIA_PROXY_PLAYBACK_SPEED_DOUBLE 64
```

相关声明：[MEDIA_PROXY_PLAYBACK_SPEED_DOUBLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaa53d906340c0b2adb314945f5299464e)。

双倍播放速度（Double Playback Speed），对应 200% 速度。

<a id="r_gaaccc9d75f96b5fe2de101b119a516d36"></a>

```c
#define MEDIA_PROXY_PLAYBACK_SPEED_MAX 127
```

相关声明：[MEDIA_PROXY_PLAYBACK_SPEED_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaaccc9d75f96b5fe2de101b119a516d36)。

最高播放速度（Max Playback Speed），对应 395.7% 速度，接近 400%。

<a id="define-members-1"></a>

### 搜寻速度因子（Seeking speed factors）

搜寻速度（Seeking Speed）的允许值为 -64 到 -4（含端点）、0，以及 4 到 64（含端点）。

<a id="r_gaa6aa7a6e98631152b4bd77b60c78d58a"></a>

```c
#define MEDIA_PROXY_SEEKING_SPEED_FACTOR_MAX 64
```

相关声明：[MEDIA_PROXY_SEEKING_SPEED_FACTOR_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaa6aa7a6e98631152b4bd77b60c78d58a)。

最大搜寻速度（Maximum Seeking Speed），可取负值。

<a id="r_ga67c1069fa01425ad6cd8f36438b71826"></a>

```c
#define MEDIA_PROXY_SEEKING_SPEED_FACTOR_MIN 4
```

相关声明：[MEDIA_PROXY_SEEKING_SPEED_FACTOR_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga67c1069fa01425ad6cd8f36438b71826)。

最小搜寻速度（Minimum Seeking Speed），可取负值。

<a id="r_ga58495e58bf84235efcee89289fc992c2"></a>

```c
#define MEDIA_PROXY_SEEKING_SPEED_FACTOR_ZERO 0
```

相关声明：[MEDIA_PROXY_SEEKING_SPEED_FACTOR_ZERO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga58495e58bf84235efcee89289fc992c2)。

不搜寻（No Seeking）。

<a id="define-members-2"></a>

### 播放顺序（Playing orders）

<a id="r_ga8e721b49c361d2395bd8eb740d43e282"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDER_SINGLE_ONCE 0x01U
```

相关声明：[MEDIA_PROXY_PLAYING_ORDER_SINGLE_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga8e721b49c361d2395bd8eb740d43e282)。

单个音轨（Track）播放一次，没有下一音轨。

<a id="r_gadf5f0c15cb88cd92f49db1b57dbd2c18"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDER_SINGLE_REPEAT 0x02U
```

相关声明：[MEDIA_PROXY_PLAYING_ORDER_SINGLE_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gadf5f0c15cb88cd92f49db1b57dbd2c18)。

重复播放单个音轨（Track），下一音轨就是当前音轨。

<a id="r_ga63055a150b93f06e076b97abb6f6f682"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDER_INORDER_ONCE 0x03U
```

相关声明：[MEDIA_PROXY_PLAYING_ORDER_INORDER_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga63055a150b93f06e076b97abb6f6f682)。

按音轨顺序（Track Order）将组内音轨播放一次。

<a id="r_ga437068b9d90404cc68d41faaedfac9a8"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDER_INORDER_REPEAT 0x04U
```

相关声明：[MEDIA_PROXY_PLAYING_ORDER_INORDER_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga437068b9d90404cc68d41faaedfac9a8)。

按音轨顺序（Track Order）重复播放组内音轨。

<a id="r_ga48a33dd8fbb8a8ab162c18bc0e9b7531"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDER_OLDEST_ONCE 0x05U
```

相关声明：[MEDIA_PROXY_PLAYING_ORDER_OLDEST_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga48a33dd8fbb8a8ab162c18bc0e9b7531)。

从最旧音轨开始，将组内音轨播放一次（Oldest First）。

<a id="r_ga63a33c4e3267ab39ab5892fb5b0bbe89"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDER_OLDEST_REPEAT 0x06U
```

相关声明：[MEDIA_PROXY_PLAYING_ORDER_OLDEST_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga63a33c4e3267ab39ab5892fb5b0bbe89)。

从最旧音轨开始，重复播放组内音轨（Oldest First）。

<a id="r_gac344111e2b043cdfbcb9ac272622b16f"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDER_NEWEST_ONCE 0x07U
```

相关声明：[MEDIA_PROXY_PLAYING_ORDER_NEWEST_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gac344111e2b043cdfbcb9ac272622b16f)。

从最新音轨开始，将组内音轨播放一次（Newest First）。

<a id="r_gaf10b815dc579dc67b1f092e0a85c51d9"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDER_NEWEST_REPEAT 0x08U
```

相关声明：[MEDIA_PROXY_PLAYING_ORDER_NEWEST_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaf10b815dc579dc67b1f092e0a85c51d9)。

从最新音轨开始，重复播放组内音轨（Newest First）。

<a id="r_gae152374af5d567cf65d6d7b236b792a4"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDER_SHUFFLE_ONCE 0x09U
```

相关声明：[MEDIA_PROXY_PLAYING_ORDER_SHUFFLE_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gae152374af5d567cf65d6d7b236b792a4)。

以随机顺序（Random Order）将组内音轨播放一次。

<a id="r_ga45161ec08b67e4d3bd59efa45027f3aa"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDER_SHUFFLE_REPEAT 0x0AU
```

相关声明：[MEDIA_PROXY_PLAYING_ORDER_SHUFFLE_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga45161ec08b67e4d3bd59efa45027f3aa)。

以随机顺序（Random Order）重复播放组内音轨。

<a id="define-members-3"></a>

### 支持的播放顺序（Playing orders supported）

位图（Bitmap），其顺序与上文的播放顺序相同。

注意，播放顺序（Playing Order）1 对应位 0，依此类推。

<a id="r_ga55b5a00ea9ec849e7c495463e5f1869d"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_SINGLE_ONCE BIT(0U)
```

相关声明：[MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_SINGLE_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga55b5a00ea9ec849e7c495463e5f1869d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

单个音轨（Track）播放一次，没有下一音轨。

<a id="r_ga465a82ace21a0e88356eccaf038f58e9"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_SINGLE_REPEAT BIT(1U)
```

相关声明：[MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_SINGLE_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga465a82ace21a0e88356eccaf038f58e9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

重复播放单个音轨（Track），下一音轨就是当前音轨。

<a id="r_ga8fee464b8e17fffc4361972df15062af"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_INORDER_ONCE BIT(2U)
```

相关声明：[MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_INORDER_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga8fee464b8e17fffc4361972df15062af)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

按音轨顺序（Track Order）将组内音轨播放一次。

<a id="r_ga7faeff14de245ea670ca447b0adc4820"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_INORDER_REPEAT BIT(3U)
```

相关声明：[MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_INORDER_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga7faeff14de245ea670ca447b0adc4820)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

按音轨顺序（Track Order）重复播放组内音轨。

<a id="r_gae3d848fc0b9117fe9bc51327627ac635"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_OLDEST_ONCE BIT(4U)
```

相关声明：[MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_OLDEST_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gae3d848fc0b9117fe9bc51327627ac635)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

从最旧音轨开始，将组内音轨播放一次（Oldest First）。

<a id="r_ga7fa415d845dd1fefc8bdb74532878131"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_OLDEST_REPEAT BIT(5U)
```

相关声明：[MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_OLDEST_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga7fa415d845dd1fefc8bdb74532878131)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

从最旧音轨开始，重复播放组内音轨（Oldest First）。

<a id="r_ga334f9e16ea7a52bfb6357ad619e3601b"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_NEWEST_ONCE BIT(6U)
```

相关声明：[MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_NEWEST_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga334f9e16ea7a52bfb6357ad619e3601b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

从最新音轨开始，将组内音轨播放一次（Newest First）。

<a id="r_gaaf5f08e2dd624e2bb1bd9b72ab4b2b33"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_NEWEST_REPEAT BIT(7U)
```

相关声明：[MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_NEWEST_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaaf5f08e2dd624e2bb1bd9b72ab4b2b33)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

从最新音轨开始，重复播放组内音轨（Newest First）。

<a id="r_ga3e998cda3e91f1c9fbb8496a748bcf12"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_SHUFFLE_ONCE BIT(8U)
```

相关声明：[MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_SHUFFLE_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga3e998cda3e91f1c9fbb8496a748bcf12)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

以随机顺序（Random Order）将组内音轨播放一次。

<a id="r_ga4f0689fe1fc0ac2b3f9b9ef4ed1afb8b"></a>

```c
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_SHUFFLE_REPEAT BIT(9U)
```

相关声明：[MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_SHUFFLE_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga4f0689fe1fc0ac2b3f9b9ef4ed1afb8b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

以随机顺序（Random Order）重复播放组内音轨。

<a id="define-members-4"></a>

### 媒体播放器状态（Media player states）

<a id="r_gab8c465e0e63898e53c39171b89d668c9"></a>

```c
#define MEDIA_PROXY_STATE_INACTIVE 0x00U
```

相关声明：[MEDIA_PROXY_STATE_INACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gab8c465e0e63898e53c39171b89d668c9)。

当前音轨无效，且未选择任何音轨（Track）。

<a id="r_ga1967c76b290f1d20515740cf7139f49c"></a>

```c
#define MEDIA_PROXY_STATE_PLAYING 0x01U
```

相关声明：[MEDIA_PROXY_STATE_PLAYING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga1967c76b290f1d20515740cf7139f49c)。

媒体播放器（Media Player）正在播放当前音轨。

<a id="r_ga85325d7ff75ec05275a875d7d5540a6c"></a>

```c
#define MEDIA_PROXY_STATE_PAUSED 0x02U
```

相关声明：[MEDIA_PROXY_STATE_PAUSED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga85325d7ff75ec05275a875d7d5540a6c)。

当前音轨已暂停（Paused）。

<a id="r_gaa207ee7666ab18c40e5b1d2a6ed7f034"></a>

```c
#define MEDIA_PROXY_STATE_SEEKING 0x03U
```

相关声明：[MEDIA_PROXY_STATE_SEEKING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaa207ee7666ab18c40e5b1d2a6ed7f034)。

当前音轨正在快进或快退（Fast Forwarding / Fast Rewinding）。

<a id="r_gab0c8f3510109f18ef6445f035b27cbe9"></a>

```c
#define MEDIA_PROXY_STATE_LAST 0x04U
```

相关声明：[MEDIA_PROXY_STATE_LAST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gab0c8f3510109f18ef6445f035b27cbe9)。

内部用作最后一个状态值（Last State Value）。

<a id="define-members-5"></a>

### 媒体播放器命令操作码（Media player command opcodes）

<a id="r_gadd400bc6900abe1956d4de4efb212683"></a>

```c
#define MEDIA_PROXY_OP_PLAY 0x01U
```

相关声明：[MEDIA_PROXY_OP_PLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gadd400bc6900abe1956d4de4efb212683)。

开始播放当前音轨（Track）。

<a id="r_ga69bcb42294e8cd1eb062bbe19399a3df"></a>

```c
#define MEDIA_PROXY_OP_PAUSE 0x02U
```

相关声明：[MEDIA_PROXY_OP_PAUSE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga69bcb42294e8cd1eb062bbe19399a3df)。

暂停播放当前音轨（Track）。

<a id="r_gabc2b497b95728325208e28db6d5cf4f8"></a>

```c
#define MEDIA_PROXY_OP_FAST_REWIND 0x03U
```

相关声明：[MEDIA_PROXY_OP_FAST_REWIND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gabc2b497b95728325208e28db6d5cf4f8)。

快退（Fast Rewind）当前音轨。

<a id="r_gac0c0730bcf6592c5d2c61d21d09efb2b"></a>

```c
#define MEDIA_PROXY_OP_FAST_FORWARD 0x04U
```

相关声明：[MEDIA_PROXY_OP_FAST_FORWARD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gac0c0730bcf6592c5d2c61d21d09efb2b)。

快进（Fast Forward）当前音轨。

<a id="r_gaf3707d44c7a3305ba896c0257b2109b3"></a>

```c
#define MEDIA_PROXY_OP_STOP 0x05U
```

相关声明：[MEDIA_PROXY_OP_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaf3707d44c7a3305ba896c0257b2109b3)。

停止当前活动，回到暂停状态（Paused State），并将当前音轨位置设为当前音轨起点。

<a id="r_gaceb240f7f21074b6b7f9ed1e9d645cb0"></a>

```c
#define MEDIA_PROXY_OP_MOVE_RELATIVE 0x10U
```

相关声明：[MEDIA_PROXY_OP_MOVE_RELATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaceb240f7f21074b6b7f9ed1e9d645cb0)。

相对于当前音轨位置（Current Track Position），设置新的当前位置。

<a id="r_ga7846fa5da200e0d921056b410e60677e"></a>

```c
#define MEDIA_PROXY_OP_PREV_SEGMENT 0x20U
```

相关声明：[MEDIA_PROXY_OP_PREV_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga7846fa5da200e0d921056b410e60677e)。

将当前音轨位置设为当前音轨上一段（Previous Segment）的起始位置。

<a id="r_gada5e3114b2b00f4ea27adf884f49429e"></a>

```c
#define MEDIA_PROXY_OP_NEXT_SEGMENT 0x21U
```

相关声明：[MEDIA_PROXY_OP_NEXT_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gada5e3114b2b00f4ea27adf884f49429e)。

将当前音轨位置设为当前音轨下一段（Next Segment）的起始位置。

<a id="r_gac2e5c8e2cadd05092fa186f05ae74e57"></a>

```c
#define MEDIA_PROXY_OP_FIRST_SEGMENT 0x22U
```

相关声明：[MEDIA_PROXY_OP_FIRST_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gac2e5c8e2cadd05092fa186f05ae74e57)。

将当前音轨位置设为当前音轨第一段（First Segment）的起始位置。

<a id="r_ga3f317208b9d8495c498325a4d37d41ad"></a>

```c
#define MEDIA_PROXY_OP_LAST_SEGMENT 0x23U
```

相关声明：[MEDIA_PROXY_OP_LAST_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga3f317208b9d8495c498325a4d37d41ad)。

将当前音轨位置设为当前音轨最后一段（Last Segment）的起始位置。

<a id="r_gab3bbf7eb7c562bc6a5148c75eb99ada5"></a>

```c
#define MEDIA_PROXY_OP_GOTO_SEGMENT 0x24U
```

相关声明：[MEDIA_PROXY_OP_GOTO_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gab3bbf7eb7c562bc6a5148c75eb99ada5)。

将当前音轨位置设为当前音轨第 n 段（Nth Segment）的起始位置。

<a id="r_ga1b7db568fc3153c29ed4e951d95bee8e"></a>

```c
#define MEDIA_PROXY_OP_PREV_TRACK 0x30U
```

相关声明：[MEDIA_PROXY_OP_PREV_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga1b7db568fc3153c29ed4e951d95bee8e)。

按播放顺序（Playing Order）将当前音轨设为上一音轨。

<a id="r_gaae4cc32663f02bf96d1dcbbc8453e40b"></a>

```c
#define MEDIA_PROXY_OP_NEXT_TRACK 0x31U
```

相关声明：[MEDIA_PROXY_OP_NEXT_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaae4cc32663f02bf96d1dcbbc8453e40b)。

按播放顺序（Playing Order）将当前音轨设为下一音轨。

<a id="r_ga5c272e2e9b24ce92a7df7373d1b002cc"></a>

```c
#define MEDIA_PROXY_OP_FIRST_TRACK 0x32U
```

相关声明：[MEDIA_PROXY_OP_FIRST_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga5c272e2e9b24ce92a7df7373d1b002cc)。

按播放顺序（Playing Order）将当前音轨设为第一音轨。

<a id="r_ga72614d9a2fa4c938f1c7055bc219c8bc"></a>

```c
#define MEDIA_PROXY_OP_LAST_TRACK 0x33U
```

相关声明：[MEDIA_PROXY_OP_LAST_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga72614d9a2fa4c938f1c7055bc219c8bc)。

按播放顺序（Playing Order）将当前音轨设为最后一音轨。

<a id="r_gaf2f100d41413b14c5dbd8f2641a13bb0"></a>

```c
#define MEDIA_PROXY_OP_GOTO_TRACK 0x34U
```

相关声明：[MEDIA_PROXY_OP_GOTO_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaf2f100d41413b14c5dbd8f2641a13bb0)。

按播放顺序（Playing Order）将当前音轨设为第 n 个音轨。

<a id="r_gae15386adcfe1c5ca56eac7d0292dffd0"></a>

```c
#define MEDIA_PROXY_OP_PREV_GROUP 0x40U
```

相关声明：[MEDIA_PROXY_OP_PREV_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gae15386adcfe1c5ca56eac7d0292dffd0)。

将当前组设为组序列（Sequence of Groups）中的上一组。

<a id="r_ga3cf10acf1ef8b7d3252eb37cb4e35f97"></a>

```c
#define MEDIA_PROXY_OP_NEXT_GROUP 0x41U
```

相关声明：[MEDIA_PROXY_OP_NEXT_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga3cf10acf1ef8b7d3252eb37cb4e35f97)。

将当前组设为组序列（Sequence of Groups）中的下一组。

<a id="r_ga5eb0a22c257e370cd76d73f7fa9e342c"></a>

```c
#define MEDIA_PROXY_OP_FIRST_GROUP 0x42U
```

相关声明：[MEDIA_PROXY_OP_FIRST_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga5eb0a22c257e370cd76d73f7fa9e342c)。

将当前组设为组序列（Sequence of Groups）中的第一组。

<a id="r_gaa6ac8f8bf674c0ffec22bd061e9be3dc"></a>

```c
#define MEDIA_PROXY_OP_LAST_GROUP 0x43U
```

相关声明：[MEDIA_PROXY_OP_LAST_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaa6ac8f8bf674c0ffec22bd061e9be3dc)。

将当前组设为组序列（Sequence of Groups）中的最后一组。

<a id="r_ga139d2ced243a6ff47d8335583974a0da"></a>

```c
#define MEDIA_PROXY_OP_GOTO_GROUP 0x44U
```

相关声明：[MEDIA_PROXY_OP_GOTO_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga139d2ced243a6ff47d8335583974a0da)。

将当前组设为组序列（Sequence of Groups）中的第 n 组。

<a id="define-members-6"></a>

<a id="r_gafe30bb1287b9a44655d76364d4832eac"></a>

```c
#define MEDIA_PROXY_OP_SUP_PLAY BIT(0U)
```

相关声明：[MEDIA_PROXY_OP_SUP_PLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gafe30bb1287b9a44655d76364d4832eac)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

媒体播放器支持的命令操作码（Supported Command Opcodes）。

<a id="r_gaec37a692c28ca90c8053db9de2a6c44f"></a>

```c
#define MEDIA_PROXY_OP_SUP_PAUSE BIT(1U)
```

相关声明：[MEDIA_PROXY_OP_SUP_PAUSE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaec37a692c28ca90c8053db9de2a6c44f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持暂停操作码（Pause Opcode）。

<a id="r_ga99952473bafd76f6ceaf141307510f28"></a>

```c
#define MEDIA_PROXY_OP_SUP_FAST_REWIND BIT(2U)
```

相关声明：[MEDIA_PROXY_OP_SUP_FAST_REWIND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga99952473bafd76f6ceaf141307510f28)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持快退操作码（Fast Rewind Opcode）。

<a id="r_ga05453105bc3d1579110e908b794e3ac5"></a>

```c
#define MEDIA_PROXY_OP_SUP_FAST_FORWARD BIT(3U)
```

相关声明：[MEDIA_PROXY_OP_SUP_FAST_FORWARD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga05453105bc3d1579110e908b794e3ac5)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持快进操作码（Fast Forward Opcode）。

<a id="r_ga060ff676a0b2f249a26aaf61147b68e8"></a>

```c
#define MEDIA_PROXY_OP_SUP_STOP BIT(4U)
```

相关声明：[MEDIA_PROXY_OP_SUP_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga060ff676a0b2f249a26aaf61147b68e8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持停止操作码（Stop Opcode）。

<a id="r_ga03c393a29c68529e4dd9038e3947468b"></a>

```c
#define MEDIA_PROXY_OP_SUP_MOVE_RELATIVE BIT(5U)
```

相关声明：[MEDIA_PROXY_OP_SUP_MOVE_RELATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga03c393a29c68529e4dd9038e3947468b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持相对移动操作码（Move Relative Opcode）。

<a id="r_ga3d39700e21cbdf2906321c8899e0b626"></a>

```c
#define MEDIA_PROXY_OP_SUP_PREV_SEGMENT BIT(6U)
```

相关声明：[MEDIA_PROXY_OP_SUP_PREV_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga3d39700e21cbdf2906321c8899e0b626)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持上一段操作码（Previous Segment Opcode）。

<a id="r_ga26ae64ece06a1f6f8dd7eb2c9965a4b6"></a>

```c
#define MEDIA_PROXY_OP_SUP_NEXT_SEGMENT BIT(7U)
```

相关声明：[MEDIA_PROXY_OP_SUP_NEXT_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga26ae64ece06a1f6f8dd7eb2c9965a4b6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持下一段操作码（Next Segment Opcode）。

<a id="r_ga916ce95086dfeb127e124a8c5d530371"></a>

```c
#define MEDIA_PROXY_OP_SUP_FIRST_SEGMENT BIT(8U)
```

相关声明：[MEDIA_PROXY_OP_SUP_FIRST_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga916ce95086dfeb127e124a8c5d530371)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持第一段操作码（First Segment Opcode）。

<a id="r_gaf193ea0b4a34e3981f2f45d3b9c228a2"></a>

```c
#define MEDIA_PROXY_OP_SUP_LAST_SEGMENT BIT(9U)
```

相关声明：[MEDIA_PROXY_OP_SUP_LAST_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaf193ea0b4a34e3981f2f45d3b9c228a2)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持最后一段操作码（Last Segment Opcode）。

<a id="r_ga7af591de387958f5c187ba8d0e834247"></a>

```c
#define MEDIA_PROXY_OP_SUP_GOTO_SEGMENT BIT(10U)
```

相关声明：[MEDIA_PROXY_OP_SUP_GOTO_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga7af591de387958f5c187ba8d0e834247)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持转到指定段操作码（Goto Segment Opcode）。

<a id="r_gafe8bab8f90281e5894e5f79f32449e63"></a>

```c
#define MEDIA_PROXY_OP_SUP_PREV_TRACK BIT(11U)
```

相关声明：[MEDIA_PROXY_OP_SUP_PREV_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gafe8bab8f90281e5894e5f79f32449e63)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持上一音轨操作码（Previous Track Opcode）。

<a id="r_gafc061bc953b0338aded4cef681f9e963"></a>

```c
#define MEDIA_PROXY_OP_SUP_NEXT_TRACK BIT(12U)
```

相关声明：[MEDIA_PROXY_OP_SUP_NEXT_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gafc061bc953b0338aded4cef681f9e963)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持下一音轨操作码（Next Track Opcode）。

<a id="r_ga6e1d53fedf09bd95bcf112495dcfd64f"></a>

```c
#define MEDIA_PROXY_OP_SUP_FIRST_TRACK BIT(13U)
```

相关声明：[MEDIA_PROXY_OP_SUP_FIRST_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga6e1d53fedf09bd95bcf112495dcfd64f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持第一音轨操作码（First Track Opcode）。

<a id="r_gaf43188bb438b9a766d07cd2fa900e079"></a>

```c
#define MEDIA_PROXY_OP_SUP_LAST_TRACK BIT(14U)
```

相关声明：[MEDIA_PROXY_OP_SUP_LAST_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaf43188bb438b9a766d07cd2fa900e079)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持最后音轨操作码（Last Track Opcode）。

<a id="r_gad2364a0ef8c54bd9fa3372edddae32b0"></a>

```c
#define MEDIA_PROXY_OP_SUP_GOTO_TRACK BIT(15U)
```

相关声明：[MEDIA_PROXY_OP_SUP_GOTO_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gad2364a0ef8c54bd9fa3372edddae32b0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持转到指定音轨操作码（Goto Track Opcode）。

<a id="r_ga496060d673b48e045a5a2a57aa82bddc"></a>

```c
#define MEDIA_PROXY_OP_SUP_PREV_GROUP BIT(16U)
```

相关声明：[MEDIA_PROXY_OP_SUP_PREV_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga496060d673b48e045a5a2a57aa82bddc)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持上一组操作码（Previous Group Opcode）。

<a id="r_ga324dae538f28e818eea79c83aaa0b22c"></a>

```c
#define MEDIA_PROXY_OP_SUP_NEXT_GROUP BIT(17U)
```

相关声明：[MEDIA_PROXY_OP_SUP_NEXT_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga324dae538f28e818eea79c83aaa0b22c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持下一组操作码（Next Group Opcode）。

<a id="r_ga716af4c6eb702729ec4f9ff9ccc49b32"></a>

```c
#define MEDIA_PROXY_OP_SUP_FIRST_GROUP BIT(18U)
```

相关声明：[MEDIA_PROXY_OP_SUP_FIRST_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga716af4c6eb702729ec4f9ff9ccc49b32)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持第一组操作码（First Group Opcode）。

<a id="r_gac944825600367a41e8213dfd9de569a3"></a>

```c
#define MEDIA_PROXY_OP_SUP_LAST_GROUP BIT(19U)
```

相关声明：[MEDIA_PROXY_OP_SUP_LAST_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gac944825600367a41e8213dfd9de569a3)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持最后一组操作码（Last Group Opcode）。

<a id="r_gaec8b6d2d684c81b9da9fee870e0258c2"></a>

```c
#define MEDIA_PROXY_OP_SUP_GOTO_GROUP BIT(20U)
```

相关声明：[MEDIA_PROXY_OP_SUP_GOTO_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaec8b6d2d684c81b9da9fee870e0258c2)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持转到指定组操作码（Goto Group Opcode）。

<a id="define-members-7"></a>

### 媒体播放器命令结果码（Media player command result codes）

<a id="r_gaa56458b11f4cb78f1265ea8538774108"></a>

```c
#define MEDIA_PROXY_CMD_SUCCESS 0x01U
```

相关声明：[MEDIA_PROXY_CMD_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaa56458b11f4cb78f1265ea8538774108)。

写入操作码（Opcode Write）所请求的动作已成功完成。

<a id="r_ga1637459cd6eaf9d4d63a04d1facc29b7"></a>

```c
#define MEDIA_PROXY_CMD_NOT_SUPPORTED 0x02U
```

相关声明：[MEDIA_PROXY_CMD_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga1637459cd6eaf9d4d63a04d1facc29b7)。

写入媒体控制点（Media Control Point）时使用了无效或不支持的操作码。

<a id="r_ga7d0595796a80348b570add74c6dfa14e"></a>

```c
#define MEDIA_PROXY_CMD_PLAYER_INACTIVE 0x03U
```

相关声明：[MEDIA_PROXY_CMD_PLAYER_INACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga7d0595796a80348b570add74c6dfa14e)。

收到操作码时，媒体播放器状态（Media Player State）特征值为非活动（Inactive）；或执行该操作码所请求动作的结果，使该特征值变为 Inactive。

<a id="r_gaf2c68cb2ac32973b85594660d43688dd"></a>

```c
#define MEDIA_PROXY_CMD_CANNOT_BE_COMPLETED 0x04U
```

相关声明：[MEDIA_PROXY_CMD_CANNOT_BE_COMPLETED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaf2c68cb2ac32973b85594660d43688dd)。

由于播放器内部的某种条件，无法成功完成任何媒体控制点写入（Media Control Point Write）所请求的动作。

<a id="define-members-8"></a>

### 搜索操作类型值（Search operation type values）

<a id="r_ga8be6fd8d9bb08836bea1c3f0d2e577ea"></a>

```c
#define MEDIA_PROXY_SEARCH_TYPE_TRACK_NAME 0x01U
```

相关声明：[MEDIA_PROXY_SEARCH_TYPE_TRACK_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga8be6fd8d9bb08836bea1c3f0d2e577ea)。

按音轨名称（Track Name）搜索。

<a id="r_gaf0dbc19f843a444076d8886b1a05709b"></a>

```c
#define MEDIA_PROXY_SEARCH_TYPE_ARTIST_NAME 0x02U
```

相关声明：[MEDIA_PROXY_SEARCH_TYPE_ARTIST_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaf0dbc19f843a444076d8886b1a05709b)。

按艺人名称（Artist Name）搜索。

<a id="r_ga1f0fb19dea467e90afd670ed9af0c092"></a>

```c
#define MEDIA_PROXY_SEARCH_TYPE_ALBUM_NAME 0x03U
```

相关声明：[MEDIA_PROXY_SEARCH_TYPE_ALBUM_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga1f0fb19dea467e90afd670ed9af0c092)。

按专辑名称（Album Name）搜索。

<a id="r_gaca10de7253c1cdcf5e0c6544de33c116"></a>

```c
#define MEDIA_PROXY_SEARCH_TYPE_GROUP_NAME 0x04U
```

相关声明：[MEDIA_PROXY_SEARCH_TYPE_GROUP_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaca10de7253c1cdcf5e0c6544de33c116)。

按组名称（Group Name）搜索。

<a id="r_ga28b1d7de2174e3714786cb369232f339"></a>

```c
#define MEDIA_PROXY_SEARCH_TYPE_EARLIEST_YEAR 0x05U
```

相关声明：[MEDIA_PROXY_SEARCH_TYPE_EARLIEST_YEAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga28b1d7de2174e3714786cb369232f339)。

按最早年份（Earliest Year）搜索。

<a id="r_ga01fb087af00bf492d19cc19adcaa9dea"></a>

```c
#define MEDIA_PROXY_SEARCH_TYPE_LATEST_YEAR 0x06U
```

相关声明：[MEDIA_PROXY_SEARCH_TYPE_LATEST_YEAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga01fb087af00bf492d19cc19adcaa9dea)。

按最晚年份（Latest Year）搜索。

<a id="r_ga55c3a003881a75ce964e23fc3b0cea8e"></a>

```c
#define MEDIA_PROXY_SEARCH_TYPE_GENRE 0x07U
```

相关声明：[MEDIA_PROXY_SEARCH_TYPE_GENRE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga55c3a003881a75ce964e23fc3b0cea8e)。

按流派（Genre）搜索。

<a id="r_gad758e14fbe978ffd95364a6fb27eab40"></a>

```c
#define MEDIA_PROXY_SEARCH_TYPE_ONLY_TRACKS 0x08U
```

相关声明：[MEDIA_PROXY_SEARCH_TYPE_ONLY_TRACKS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gad758e14fbe978ffd95364a6fb27eab40)。

仅搜索音轨（Tracks）。

<a id="r_ga25270f6c90daaace6a80f3255aaaf7fd"></a>

```c
#define MEDIA_PROXY_SEARCH_TYPE_ONLY_GROUPS 0x09U
```

相关声明：[MEDIA_PROXY_SEARCH_TYPE_ONLY_GROUPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga25270f6c90daaace6a80f3255aaaf7fd)。

仅搜索组（Groups）。

<a id="define-members-9"></a>

### 搜索通知结果码（Search notification result codes）

<a id="r_ga2627f632efab868adddeebb59243497c"></a>

```c
#define MEDIA_PROXY_SEARCH_SUCCESS 0x01U
```

相关声明：[MEDIA_PROXY_SEARCH_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga2627f632efab868adddeebb59243497c)。

搜索请求（Search Request）已接受，搜索已开始。

<a id="r_gaf406225a87c697d784c5a429e89d2354"></a>

```c
#define MEDIA_PROXY_SEARCH_FAILURE 0x02U
```

相关声明：[MEDIA_PROXY_SEARCH_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaf406225a87c697d784c5a429e89d2354)。

搜索请求（Search Request）无效，未开始搜索。

<a id="define-members-10"></a>

### 组对象的对象类型（Group object object types）

<a id="r_ga7412b20ea355713443b7165f077b0a0d"></a>

```c
#define MEDIA_PROXY_GROUP_OBJECT_TRACK_TYPE 0x00U
```

相关声明：[MEDIA_PROXY_GROUP_OBJECT_TRACK_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga7412b20ea355713443b7165f077b0a0d)。

组对象类型（Group Object Type）为音轨（Track）。

<a id="r_ga63abba926894a45e187e3f4e4610cb35"></a>

```c
#define MEDIA_PROXY_GROUP_OBJECT_GROUP_TYPE 0x01U
```

相关声明：[MEDIA_PROXY_GROUP_OBJECT_GROUP_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga63abba926894a45e187e3f4e4610cb35)。

组对象类型（Group Object Type）为组（Group）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.3\_函数（Functions）

<a id="r_ga352228fb77498b61205a22b0f3a75c8e"></a>

```c
int media_proxy_ctrl_register (struct media_proxy_ctrl_cbs *ctrl_cbs)
```

相关声明：[media_proxy_ctrl_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga352228fb77498b61205a22b0f3a75c8e)、[media_proxy_ctrl_cbs](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md)。

向媒体代理（media_proxy）注册控制器（Controller）。

<a id="r_ga5aaa486e0c3663e21477984e54642ed1"></a>

```c
int media_proxy_ctrl_discover_player (struct bt_conn *conn)
```

相关声明：[media_proxy_ctrl_discover_player](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga5aaa486e0c3663e21477984e54642ed1)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

发现远端媒体播放器（Remote Media Player）。

<a id="r_ga2261222d8581ed86e91a276b13359126"></a>

```c
int media_proxy_ctrl_get_player_name (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_player_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga2261222d8581ed86e91a276b13359126)。

读取媒体播放器名称（Media Player Name）。

<a id="r_gae077bc84648137460a9aeb6cfd4acb4c"></a>

```c
int media_proxy_ctrl_set_player_name (struct media_player *player, const char *name)
```

相关声明：[media_proxy_ctrl_set_player_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gae077bc84648137460a9aeb6cfd4acb4c)。

设置媒体播放器名称。

<a id="r_ga5efccb39cdb97eed476e0c0bff461ec1"></a>

```c
int media_proxy_ctrl_get_icon_id (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_icon_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga5efccb39cdb97eed476e0c0bff461ec1)。

读取图标对象 ID（Icon Object ID）。

<a id="r_gab6df6fe71c8273eca855eb3be27290dd"></a>

```c
int media_proxy_ctrl_get_icon_url (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_icon_url](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gab6df6fe71c8273eca855eb3be27290dd)。

读取图标 URL。

<a id="r_gabfbb49e79204130cb004f217af771b80"></a>

```c
int media_proxy_ctrl_get_track_title (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_track_title](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gabfbb49e79204130cb004f217af771b80)。

读取曲目标题（Track Title）。

<a id="r_ga488441418a8f2d358092019bbfe16788"></a>

```c
int media_proxy_ctrl_get_track_duration (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_track_duration](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga488441418a8f2d358092019bbfe16788)。

读取曲目时长（Track Duration）。

<a id="r_gae0bb75feb49a68b495150c6fba2f21a7"></a>

```c
int media_proxy_ctrl_get_track_position (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_track_position](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gae0bb75feb49a68b495150c6fba2f21a7)。

读取曲目位置（Track Position）。

<a id="r_ga776bb5f16cf1f4f6cc3842aabd86b781"></a>

```c
int media_proxy_ctrl_set_track_position (struct media_player *player, int32_t position)
```

相关声明：[media_proxy_ctrl_set_track_position](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga776bb5f16cf1f4f6cc3842aabd86b781)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置曲目位置。

<a id="r_ga2d64a23b3f881579a603a04baeb64088"></a>

```c
int media_proxy_ctrl_get_playback_speed (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_playback_speed](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga2d64a23b3f881579a603a04baeb64088)。

获取播放速度（Playback Speed）。

<a id="r_gabafbc857c3e6befe98e339acb58f17fb"></a>

```c
int media_proxy_ctrl_set_playback_speed (struct media_player *player, int8_t speed)
```

相关声明：[media_proxy_ctrl_set_playback_speed](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gabafbc857c3e6befe98e339acb58f17fb)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

设置播放速度。

<a id="r_ga817ca4ab611e214493fbc918036def0f"></a>

```c
int media_proxy_ctrl_get_seeking_speed (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_seeking_speed](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga817ca4ab611e214493fbc918036def0f)。

获取搜索播放位置速度（Seeking Speed）。

<a id="r_ga1afcc097cb36c4f11141b82ce28e8126"></a>

```c
int media_proxy_ctrl_get_track_segments_id (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_track_segments_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga1afcc097cb36c4f11141b82ce28e8126)。

读取当前曲目片段对象 ID（Current Track Segments Object ID）。

<a id="r_gaebe7e3683041e28bef40df75cc991dea"></a>

```c
int media_proxy_ctrl_get_current_track_id (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_current_track_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaebe7e3683041e28bef40df75cc991dea)。

读取当前曲目对象 ID（Current Track Object ID）。

<a id="r_gaea6adacedaded10f7c2c0f91b7159f74"></a>

```c
int media_proxy_ctrl_set_current_track_id (struct media_player *player, uint64_t id)
```

相关声明：[media_proxy_ctrl_set_current_track_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaea6adacedaded10f7c2c0f91b7159f74)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

设置当前曲目对象 ID。

<a id="r_gae32da32bd504061801730805729242e1"></a>

```c
int media_proxy_ctrl_get_next_track_id (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_next_track_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gae32da32bd504061801730805729242e1)。

读取下一曲目对象 ID（Next Track Object ID）。

<a id="r_ga43b797717fb9b36b94a606dfabeb0fa7"></a>

```c
int media_proxy_ctrl_set_next_track_id (struct media_player *player, uint64_t id)
```

相关声明：[media_proxy_ctrl_set_next_track_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga43b797717fb9b36b94a606dfabeb0fa7)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

设置下一曲目对象 ID。

<a id="r_ga12dc878be39814660900ba875e13e537"></a>

```c
int media_proxy_ctrl_get_parent_group_id (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_parent_group_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga12dc878be39814660900ba875e13e537)。

读取父分组对象 ID（Parent Group Object ID）。

<a id="r_ga2ae50a1988305b4247ff0af796b6d93e"></a>

```c
int media_proxy_ctrl_get_current_group_id (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_current_group_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga2ae50a1988305b4247ff0af796b6d93e)。

读取当前分组对象 ID（Current Group Object ID）。

<a id="r_gae496885d0124f4e3fc2c0f203fcff118"></a>

```c
int media_proxy_ctrl_set_current_group_id (struct media_player *player, uint64_t id)
```

相关声明：[media_proxy_ctrl_set_current_group_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gae496885d0124f4e3fc2c0f203fcff118)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

设置当前分组对象 ID。

<a id="r_ga2f93bcde2460c6638880f8e6631eb68e"></a>

```c
int media_proxy_ctrl_get_playing_order (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_playing_order](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga2f93bcde2460c6638880f8e6631eb68e)。

读取播放顺序（Playing Order）。

<a id="r_gaa4040e97100f6e70527e6ad201309bbe"></a>

```c
int media_proxy_ctrl_set_playing_order (struct media_player *player, uint8_t order)
```

相关声明：[media_proxy_ctrl_set_playing_order](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaa4040e97100f6e70527e6ad201309bbe)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置播放顺序。

<a id="r_ga030899757b79251f1d5a1055f65fe989"></a>

```c
int media_proxy_ctrl_get_playing_orders_supported (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_playing_orders_supported](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga030899757b79251f1d5a1055f65fe989)。

读取支持的播放顺序（Playing Orders Supported）。

<a id="r_ga9433aaf24776c30557ea694795e75b3e"></a>

```c
int media_proxy_ctrl_get_media_state (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_media_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga9433aaf24776c30557ea694795e75b3e)。

读取媒体状态（Media State）。

<a id="r_ga590762e7272b99fb8ac50a7841424670"></a>

```c
int media_proxy_ctrl_send_command (struct media_player *player, const struct mpl_cmd *command)
```

相关声明：[media_proxy_ctrl_send_command](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga590762e7272b99fb8ac50a7841424670)、[mpl_cmd](../audio_video_model_reference/P037_mpl_cmd_结构体.md)。

发送命令。

<a id="r_ga15804287093b20d4a1616380729b33c8"></a>

```c
int media_proxy_ctrl_get_commands_supported (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_commands_supported](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga15804287093b20d4a1616380729b33c8)。

读取支持的命令（Commands Supported）。

<a id="r_ga052c3fabac4a44ee2802ddd4a6c5c9ac"></a>

```c
int media_proxy_ctrl_send_search (struct media_player *player, const struct mpl_search *search)
```

相关声明：[media_proxy_ctrl_send_search](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga052c3fabac4a44ee2802ddd4a6c5c9ac)、[mpl_search](../audio_video_model_reference/P040_mpl_search_结构体.md)。

设置搜索（Search）。

<a id="r_ga580a0c9fa47460be59f0571ee11a41b4"></a>

```c
int media_proxy_ctrl_get_search_results_id (struct media_player *player)
```

相关声明：[media_proxy_ctrl_get_search_results_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga580a0c9fa47460be59f0571ee11a41b4)。

读取搜索结果对象 ID（Search Results Object ID）。

<a id="r_ga23488e77985a04216ec7c7fa785f09fc"></a>

```c
uint8_t media_proxy_ctrl_get_content_ctrl_id (struct media_player *player)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[media_proxy_ctrl_get_content_ctrl_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga23488e77985a04216ec7c7fa785f09fc)。

读取内容控制 ID（Content Control ID）。

<a id="r_gac75e27a4a5e169481723cd6b39678274"></a>

```c
int media_proxy_pl_register (struct media_proxy_pl_calls *pl_calls)
```

相关声明：[media_proxy_pl_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gac75e27a4a5e169481723cd6b39678274)、[media_proxy_pl_calls](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md)。

向媒体代理（Media Proxy）注册播放器（Player）。

<a id="r_gab0b10b3de5674f2172e1a2f779cbe8d5"></a>

```c
int media_proxy_pl_init (void)
```

相关声明：[media_proxy_pl_init](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gab0b10b3de5674f2172e1a2f779cbe8d5)。

初始化播放器（Player）。

<a id="r_gaf535f1ab028407432ef890d278d936e0"></a>

```c
struct bt_ots * bt_mcs_get_ots (void)
```

相关声明：[bt_ots](../bluetooth_service_model_reference/P135_bt_ots_结构体.md)、[bt_mcs_get_ots](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaf535f1ab028407432ef890d278d936e0)。

获取媒体控制服务（Media Control Service）使用的对象传输服务（Object Transfer Service）指针。

<a id="r_ga0a70dc60a4d6acbcc58e220b75dad92a"></a>

```c
void media_proxy_pl_name_cb (const char *name)
```

相关声明：[media_proxy_pl_name_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga0a70dc60a4d6acbcc58e220b75dad92a)。

播放器名称变化回调（Player Name Changed Callback）。

<a id="r_gadd348a8d5aff193f7a9113a759e85b1d"></a>

```c
void media_proxy_pl_icon_url_cb (const char *url)
```

相关声明：[media_proxy_pl_icon_url_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gadd348a8d5aff193f7a9113a759e85b1d)。

播放器图标 URL 变化回调（Player Icon URL Changed Callback）。

<a id="r_ga4a93a18cb0b75cb16828243f0d37b4b4"></a>

```c
void media_proxy_pl_track_changed_cb (void)
```

相关声明：[media_proxy_pl_track_changed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga4a93a18cb0b75cb16828243f0d37b4b4)。

音轨变化回调（Track Changed Callback）。

<a id="r_ga9489b517e4baa215f0b7b59243cee11c"></a>

```c
void media_proxy_pl_track_title_cb (char *title)
```

相关声明：[media_proxy_pl_track_title_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga9489b517e4baa215f0b7b59243cee11c)。

音轨标题回调（Track Title Callback）。

<a id="r_ga7b0f9633a5322557b91ea97eafac9f34"></a>

```c
void media_proxy_pl_track_duration_cb (int32_t duration)
```

相关声明：[media_proxy_pl_track_duration_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga7b0f9633a5322557b91ea97eafac9f34)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

音轨时长回调（Track Duration Callback）。

<a id="r_ga61d494d7e149cfa2c3f9546c1e3b99bd"></a>

```c
void media_proxy_pl_track_position_cb (int32_t position)
```

相关声明：[media_proxy_pl_track_position_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga61d494d7e149cfa2c3f9546c1e3b99bd)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

音轨位置回调（Track Position Callback）。

<a id="r_ga17c2ca149050e1382eb556f6dcccad21"></a>

```c
void media_proxy_pl_playback_speed_cb (int8_t speed)
```

相关声明：[media_proxy_pl_playback_speed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga17c2ca149050e1382eb556f6dcccad21)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

播放速度回调（Playback Speed Callback）。

<a id="r_gaeaf89f4b760870896ed42687562971ca"></a>

```c
void media_proxy_pl_seeking_speed_cb (int8_t speed)
```

相关声明：[media_proxy_pl_seeking_speed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaeaf89f4b760870896ed42687562971ca)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

搜寻速度回调（Seeking Speed Callback）。

<a id="r_gadcad4efdd714159d5d9611bbf74d5fae"></a>

```c
void media_proxy_pl_current_track_id_cb (uint64_t id)
```

相关声明：[media_proxy_pl_current_track_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gadcad4efdd714159d5d9611bbf74d5fae)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

当前音轨对象 ID 回调（Current Track Object ID Callback）。

<a id="r_gaf0bd3447e64b6128710c07461766a0c9"></a>

```c
void media_proxy_pl_next_track_id_cb (uint64_t id)
```

相关声明：[media_proxy_pl_next_track_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaf0bd3447e64b6128710c07461766a0c9)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

下一音轨对象 ID 回调（Next Track Object ID Callback）。

<a id="r_ga64730f46b87cf9089aff65b6be12f42d"></a>

```c
void media_proxy_pl_parent_group_id_cb (uint64_t id)
```

相关声明：[media_proxy_pl_parent_group_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga64730f46b87cf9089aff65b6be12f42d)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

父组对象 ID 回调（Parent Group Object ID Callback）。

<a id="r_gad02f2924e1aa765c04cbbc6441e7d063"></a>

```c
void media_proxy_pl_current_group_id_cb (uint64_t id)
```

相关声明：[media_proxy_pl_current_group_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gad02f2924e1aa765c04cbbc6441e7d063)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

当前组对象 ID 回调（Current Group Object ID Callback）。

<a id="r_ga96e8156b0267f3d55ee52ab307d81985"></a>

```c
void media_proxy_pl_playing_order_cb (uint8_t order)
```

相关声明：[media_proxy_pl_playing_order_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga96e8156b0267f3d55ee52ab307d81985)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

播放顺序回调（Playing Order Callback）。

<a id="r_ga842d7951a04702d6f819de44c47b9cac"></a>

```c
void media_proxy_pl_media_state_cb (uint8_t state)
```

相关声明：[media_proxy_pl_media_state_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga842d7951a04702d6f819de44c47b9cac)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

媒体状态回调（Media State Callback）。

<a id="r_ga694e83401835149833024cf094b98cd1"></a>

```c
void media_proxy_pl_command_cb (const struct mpl_cmd_ntf *cmd_ntf)
```

相关声明：[media_proxy_pl_command_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga694e83401835149833024cf094b98cd1)、[mpl_cmd_ntf](../audio_video_model_reference/P038_mpl_cmd_ntf_结构体.md)。

命令回调（Command Callback）。

<a id="r_ga70ea8a24a4e853a191e0947e1c2d1145"></a>

```c
void media_proxy_pl_commands_supported_cb (uint32_t opcodes)
```

相关声明：[media_proxy_pl_commands_supported_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga70ea8a24a4e853a191e0947e1c2d1145)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

支持的命令回调（Commands Supported Callback）。

<a id="r_ga8c0d75f61120047bacd0b933534e1b41"></a>

```c
void media_proxy_pl_search_cb (uint8_t result_code)
```

相关声明：[media_proxy_pl_search_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga8c0d75f61120047bacd0b933534e1b41)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

搜索回调（Search Callback）。

<a id="r_ga35896de266f2a2bd101279e4ce9900c7"></a>

```c
void media_proxy_pl_search_results_id_cb (uint64_t id)
```

相关声明：[media_proxy_pl_search_results_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga35896de266f2a2bd101279e4ce9900c7)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

搜索结果对象 ID 回调（Search Results Object ID Callback）。


## 7.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/bluetooth/bluetooth.h](../api_source_system_reference/P003_bluetooth.h_源码浏览.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [mcs.h](../api_source_supplement_reference/P108_mcs.h_源码浏览.md)
- [查看此文件的源码。](../api_source_runtime_reference/P042_media_proxy.h_源码浏览.md)
- [mpl_cmd](../audio_video_model_reference/P037_mpl_cmd_结构体.md)
- [mpl_cmd_ntf](../audio_video_model_reference/P038_mpl_cmd_ntf_结构体.md)
- [mpl_sci](../audio_video_model_reference/P039_mpl_sci_结构体.md)
- [mpl_search](../audio_video_model_reference/P040_mpl_search_结构体.md)
- [media_proxy_ctrl_cbs](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md)
- [media_proxy_pl_calls](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md)
- [MEDIA_PROXY_OPCODES_SUPPORTED_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga22c2599cd62a263a01c06c9bd9fff054)
- [MEDIA_PROXY_PLAYBACK_SPEED_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga61732644eecad1442d5cedbda8f8cc08)
- [MEDIA_PROXY_PLAYBACK_SPEED_QUARTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga5462f8d5ce98cc33a131b2e7b5548c41)
- [MEDIA_PROXY_PLAYBACK_SPEED_HALF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga4c765363c2a5b0d9800864859746ae33)
- [MEDIA_PROXY_PLAYBACK_SPEED_UNITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga6d8854bd54dcbb657f0ba545ec231368)
- [MEDIA_PROXY_PLAYBACK_SPEED_DOUBLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaa53d906340c0b2adb314945f5299464e)
- [MEDIA_PROXY_PLAYBACK_SPEED_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaaccc9d75f96b5fe2de101b119a516d36)
- [MEDIA_PROXY_SEEKING_SPEED_FACTOR_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaa6aa7a6e98631152b4bd77b60c78d58a)
- [MEDIA_PROXY_SEEKING_SPEED_FACTOR_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga67c1069fa01425ad6cd8f36438b71826)
- [MEDIA_PROXY_SEEKING_SPEED_FACTOR_ZERO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga58495e58bf84235efcee89289fc992c2)
- [MEDIA_PROXY_PLAYING_ORDER_SINGLE_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga8e721b49c361d2395bd8eb740d43e282)
- [MEDIA_PROXY_PLAYING_ORDER_SINGLE_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gadf5f0c15cb88cd92f49db1b57dbd2c18)
- [MEDIA_PROXY_PLAYING_ORDER_INORDER_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga63055a150b93f06e076b97abb6f6f682)
- [MEDIA_PROXY_PLAYING_ORDER_INORDER_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga437068b9d90404cc68d41faaedfac9a8)
- [MEDIA_PROXY_PLAYING_ORDER_OLDEST_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga48a33dd8fbb8a8ab162c18bc0e9b7531)
- [MEDIA_PROXY_PLAYING_ORDER_OLDEST_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga63a33c4e3267ab39ab5892fb5b0bbe89)
- [MEDIA_PROXY_PLAYING_ORDER_NEWEST_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gac344111e2b043cdfbcb9ac272622b16f)
- [MEDIA_PROXY_PLAYING_ORDER_NEWEST_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaf10b815dc579dc67b1f092e0a85c51d9)
- [MEDIA_PROXY_PLAYING_ORDER_SHUFFLE_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gae152374af5d567cf65d6d7b236b792a4)
- [MEDIA_PROXY_PLAYING_ORDER_SHUFFLE_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga45161ec08b67e4d3bd59efa45027f3aa)
- [MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_SINGLE_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga55b5a00ea9ec849e7c495463e5f1869d)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_SINGLE_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga465a82ace21a0e88356eccaf038f58e9)
- [MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_INORDER_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga8fee464b8e17fffc4361972df15062af)
- [MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_INORDER_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga7faeff14de245ea670ca447b0adc4820)
- [MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_OLDEST_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gae3d848fc0b9117fe9bc51327627ac635)
- [MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_OLDEST_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga7fa415d845dd1fefc8bdb74532878131)
- [MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_NEWEST_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga334f9e16ea7a52bfb6357ad619e3601b)
- [MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_NEWEST_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaaf5f08e2dd624e2bb1bd9b72ab4b2b33)
- [MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_SHUFFLE_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga3e998cda3e91f1c9fbb8496a748bcf12)
- [MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_SHUFFLE_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga4f0689fe1fc0ac2b3f9b9ef4ed1afb8b)
- [MEDIA_PROXY_STATE_INACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gab8c465e0e63898e53c39171b89d668c9)
- [MEDIA_PROXY_STATE_PLAYING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga1967c76b290f1d20515740cf7139f49c)
- [MEDIA_PROXY_STATE_PAUSED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga85325d7ff75ec05275a875d7d5540a6c)
- [MEDIA_PROXY_STATE_SEEKING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaa207ee7666ab18c40e5b1d2a6ed7f034)
- [MEDIA_PROXY_STATE_LAST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gab0c8f3510109f18ef6445f035b27cbe9)
- [MEDIA_PROXY_OP_PLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gadd400bc6900abe1956d4de4efb212683)
- [MEDIA_PROXY_OP_PAUSE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga69bcb42294e8cd1eb062bbe19399a3df)
- [MEDIA_PROXY_OP_FAST_REWIND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gabc2b497b95728325208e28db6d5cf4f8)
- [MEDIA_PROXY_OP_FAST_FORWARD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gac0c0730bcf6592c5d2c61d21d09efb2b)
- [MEDIA_PROXY_OP_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaf3707d44c7a3305ba896c0257b2109b3)
- [MEDIA_PROXY_OP_MOVE_RELATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaceb240f7f21074b6b7f9ed1e9d645cb0)
- [MEDIA_PROXY_OP_PREV_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga7846fa5da200e0d921056b410e60677e)
- [MEDIA_PROXY_OP_NEXT_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gada5e3114b2b00f4ea27adf884f49429e)
- [MEDIA_PROXY_OP_FIRST_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gac2e5c8e2cadd05092fa186f05ae74e57)
- [MEDIA_PROXY_OP_LAST_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga3f317208b9d8495c498325a4d37d41ad)
- [MEDIA_PROXY_OP_GOTO_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gab3bbf7eb7c562bc6a5148c75eb99ada5)
- [MEDIA_PROXY_OP_PREV_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga1b7db568fc3153c29ed4e951d95bee8e)
- [MEDIA_PROXY_OP_NEXT_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaae4cc32663f02bf96d1dcbbc8453e40b)
- [MEDIA_PROXY_OP_FIRST_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga5c272e2e9b24ce92a7df7373d1b002cc)
- [MEDIA_PROXY_OP_LAST_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga72614d9a2fa4c938f1c7055bc219c8bc)
- [MEDIA_PROXY_OP_GOTO_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaf2f100d41413b14c5dbd8f2641a13bb0)
- [MEDIA_PROXY_OP_PREV_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gae15386adcfe1c5ca56eac7d0292dffd0)
- [MEDIA_PROXY_OP_NEXT_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga3cf10acf1ef8b7d3252eb37cb4e35f97)
- [MEDIA_PROXY_OP_FIRST_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga5eb0a22c257e370cd76d73f7fa9e342c)
- [MEDIA_PROXY_OP_LAST_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaa6ac8f8bf674c0ffec22bd061e9be3dc)
- [MEDIA_PROXY_OP_GOTO_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga139d2ced243a6ff47d8335583974a0da)
- [MEDIA_PROXY_OP_SUP_PLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gafe30bb1287b9a44655d76364d4832eac)
- [MEDIA_PROXY_OP_SUP_PAUSE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaec37a692c28ca90c8053db9de2a6c44f)
- [MEDIA_PROXY_OP_SUP_FAST_REWIND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga99952473bafd76f6ceaf141307510f28)
- [MEDIA_PROXY_OP_SUP_FAST_FORWARD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga05453105bc3d1579110e908b794e3ac5)
- [MEDIA_PROXY_OP_SUP_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga060ff676a0b2f249a26aaf61147b68e8)
- [MEDIA_PROXY_OP_SUP_MOVE_RELATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga03c393a29c68529e4dd9038e3947468b)
- [MEDIA_PROXY_OP_SUP_PREV_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga3d39700e21cbdf2906321c8899e0b626)
- [MEDIA_PROXY_OP_SUP_NEXT_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga26ae64ece06a1f6f8dd7eb2c9965a4b6)
- [MEDIA_PROXY_OP_SUP_FIRST_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga916ce95086dfeb127e124a8c5d530371)
- [MEDIA_PROXY_OP_SUP_LAST_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaf193ea0b4a34e3981f2f45d3b9c228a2)
- [MEDIA_PROXY_OP_SUP_GOTO_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga7af591de387958f5c187ba8d0e834247)
- [MEDIA_PROXY_OP_SUP_PREV_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gafe8bab8f90281e5894e5f79f32449e63)
- [MEDIA_PROXY_OP_SUP_NEXT_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gafc061bc953b0338aded4cef681f9e963)
- [MEDIA_PROXY_OP_SUP_FIRST_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga6e1d53fedf09bd95bcf112495dcfd64f)
- [MEDIA_PROXY_OP_SUP_LAST_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaf43188bb438b9a766d07cd2fa900e079)
- [MEDIA_PROXY_OP_SUP_GOTO_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gad2364a0ef8c54bd9fa3372edddae32b0)
- [MEDIA_PROXY_OP_SUP_PREV_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga496060d673b48e045a5a2a57aa82bddc)
- [MEDIA_PROXY_OP_SUP_NEXT_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga324dae538f28e818eea79c83aaa0b22c)
- [MEDIA_PROXY_OP_SUP_FIRST_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga716af4c6eb702729ec4f9ff9ccc49b32)
- [MEDIA_PROXY_OP_SUP_LAST_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gac944825600367a41e8213dfd9de569a3)
- [MEDIA_PROXY_OP_SUP_GOTO_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaec8b6d2d684c81b9da9fee870e0258c2)
- [MEDIA_PROXY_CMD_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaa56458b11f4cb78f1265ea8538774108)
- [MEDIA_PROXY_CMD_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga1637459cd6eaf9d4d63a04d1facc29b7)
- [MEDIA_PROXY_CMD_PLAYER_INACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga7d0595796a80348b570add74c6dfa14e)
- [MEDIA_PROXY_CMD_CANNOT_BE_COMPLETED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaf2c68cb2ac32973b85594660d43688dd)
- [MEDIA_PROXY_SEARCH_TYPE_TRACK_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga8be6fd8d9bb08836bea1c3f0d2e577ea)
- [MEDIA_PROXY_SEARCH_TYPE_ARTIST_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaf0dbc19f843a444076d8886b1a05709b)
- [MEDIA_PROXY_SEARCH_TYPE_ALBUM_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga1f0fb19dea467e90afd670ed9af0c092)
- [MEDIA_PROXY_SEARCH_TYPE_GROUP_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaca10de7253c1cdcf5e0c6544de33c116)
- [MEDIA_PROXY_SEARCH_TYPE_EARLIEST_YEAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga28b1d7de2174e3714786cb369232f339)
- [MEDIA_PROXY_SEARCH_TYPE_LATEST_YEAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga01fb087af00bf492d19cc19adcaa9dea)
- [MEDIA_PROXY_SEARCH_TYPE_GENRE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga55c3a003881a75ce964e23fc3b0cea8e)
- [MEDIA_PROXY_SEARCH_TYPE_ONLY_TRACKS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gad758e14fbe978ffd95364a6fb27eab40)
- [MEDIA_PROXY_SEARCH_TYPE_ONLY_GROUPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga25270f6c90daaace6a80f3255aaaf7fd)
- [MEDIA_PROXY_SEARCH_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga2627f632efab868adddeebb59243497c)
- [MEDIA_PROXY_SEARCH_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaf406225a87c697d784c5a429e89d2354)
- [MEDIA_PROXY_GROUP_OBJECT_TRACK_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga7412b20ea355713443b7165f077b0a0d)
- [MEDIA_PROXY_GROUP_OBJECT_GROUP_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga63abba926894a45e187e3f4e4610cb35)
- [media_proxy_ctrl_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga352228fb77498b61205a22b0f3a75c8e)
- [media_proxy_ctrl_discover_player](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga5aaa486e0c3663e21477984e54642ed1)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [media_proxy_ctrl_get_player_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga2261222d8581ed86e91a276b13359126)
- [media_proxy_ctrl_set_player_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gae077bc84648137460a9aeb6cfd4acb4c)
- [media_proxy_ctrl_get_icon_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga5efccb39cdb97eed476e0c0bff461ec1)
- [media_proxy_ctrl_get_icon_url](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gab6df6fe71c8273eca855eb3be27290dd)
- [media_proxy_ctrl_get_track_title](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gabfbb49e79204130cb004f217af771b80)
- [media_proxy_ctrl_get_track_duration](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga488441418a8f2d358092019bbfe16788)
- [media_proxy_ctrl_get_track_position](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gae0bb75feb49a68b495150c6fba2f21a7)
- [media_proxy_ctrl_set_track_position](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga776bb5f16cf1f4f6cc3842aabd86b781)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [media_proxy_ctrl_get_playback_speed](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga2d64a23b3f881579a603a04baeb64088)
- [media_proxy_ctrl_set_playback_speed](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gabafbc857c3e6befe98e339acb58f17fb)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [media_proxy_ctrl_get_seeking_speed](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga817ca4ab611e214493fbc918036def0f)
- [media_proxy_ctrl_get_track_segments_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga1afcc097cb36c4f11141b82ce28e8126)
- [media_proxy_ctrl_get_current_track_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaebe7e3683041e28bef40df75cc991dea)
- [media_proxy_ctrl_set_current_track_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaea6adacedaded10f7c2c0f91b7159f74)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [media_proxy_ctrl_get_next_track_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gae32da32bd504061801730805729242e1)
- [media_proxy_ctrl_set_next_track_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga43b797717fb9b36b94a606dfabeb0fa7)
- [media_proxy_ctrl_get_parent_group_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga12dc878be39814660900ba875e13e537)
- [media_proxy_ctrl_get_current_group_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga2ae50a1988305b4247ff0af796b6d93e)
- [media_proxy_ctrl_set_current_group_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gae496885d0124f4e3fc2c0f203fcff118)
- [media_proxy_ctrl_get_playing_order](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga2f93bcde2460c6638880f8e6631eb68e)
- [media_proxy_ctrl_set_playing_order](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaa4040e97100f6e70527e6ad201309bbe)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [media_proxy_ctrl_get_playing_orders_supported](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga030899757b79251f1d5a1055f65fe989)
- [media_proxy_ctrl_get_media_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga9433aaf24776c30557ea694795e75b3e)
- [media_proxy_ctrl_send_command](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga590762e7272b99fb8ac50a7841424670)
- [media_proxy_ctrl_get_commands_supported](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga15804287093b20d4a1616380729b33c8)
- [media_proxy_ctrl_send_search](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga052c3fabac4a44ee2802ddd4a6c5c9ac)
- [media_proxy_ctrl_get_search_results_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga580a0c9fa47460be59f0571ee11a41b4)
- [media_proxy_ctrl_get_content_ctrl_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga23488e77985a04216ec7c7fa785f09fc)
- [media_proxy_pl_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gac75e27a4a5e169481723cd6b39678274)
- [media_proxy_pl_init](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gab0b10b3de5674f2172e1a2f779cbe8d5)
- [bt_ots](../bluetooth_service_model_reference/P135_bt_ots_结构体.md)
- [bt_mcs_get_ots](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaf535f1ab028407432ef890d278d936e0)
- [media_proxy_pl_name_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga0a70dc60a4d6acbcc58e220b75dad92a)
- [media_proxy_pl_icon_url_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gadd348a8d5aff193f7a9113a759e85b1d)
- [media_proxy_pl_track_changed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga4a93a18cb0b75cb16828243f0d37b4b4)
- [media_proxy_pl_track_title_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga9489b517e4baa215f0b7b59243cee11c)
- [media_proxy_pl_track_duration_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga7b0f9633a5322557b91ea97eafac9f34)
- [media_proxy_pl_track_position_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga61d494d7e149cfa2c3f9546c1e3b99bd)
- [media_proxy_pl_playback_speed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga17c2ca149050e1382eb556f6dcccad21)
- [media_proxy_pl_seeking_speed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaeaf89f4b760870896ed42687562971ca)
- [media_proxy_pl_current_track_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gadcad4efdd714159d5d9611bbf74d5fae)
- [media_proxy_pl_next_track_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaf0bd3447e64b6128710c07461766a0c9)
- [media_proxy_pl_parent_group_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga64730f46b87cf9089aff65b6be12f42d)
- [media_proxy_pl_current_group_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gad02f2924e1aa765c04cbbc6441e7d063)
- [media_proxy_pl_playing_order_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga96e8156b0267f3d55ee52ab307d81985)
- [media_proxy_pl_media_state_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga842d7951a04702d6f819de44c47b9cac)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [media_proxy_pl_command_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga694e83401835149833024cf094b98cd1)
- [media_proxy_pl_commands_supported_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga70ea8a24a4e853a191e0947e1c2d1145)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [media_proxy_pl_search_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga8c0d75f61120047bacd0b933534e1b41)
- [media_proxy_pl_search_results_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga35896de266f2a2bd101279e4ce9900c7)

<a id="header-details"></a>

---

[上一章](P006_zephyr__bluetooth__audio__mcs.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P008_zephyr__net__mii.h_文件参考.md)
