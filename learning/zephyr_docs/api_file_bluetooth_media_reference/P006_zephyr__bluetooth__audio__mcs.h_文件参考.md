---
id: learning.zephyr-docs.api-file-bluetooth-media-reference.page-6
title: zephyr__bluetooth__audio__mcs.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mcs_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_bluetooth\_\_audio\_\_mcs.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mcs_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙媒体控制服务（Media Control Service，MCS）的API。

<a id="details"></a>

```c
#include <zephyr/sys/util.h>
#include <zephyr/sys/util_macro.h>
```

查看此文件的源码。

蓝牙媒体控制服务（Media Control Service，MCS）的API。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.1\_宏定义（Macros）

<a id="r_gab0c40404b2cd37d0a729504aa270e697"></a>

```c
#define BT_MCS_ERR_LONG_VAL_CHANGED 0x80U
```

相关声明：[BT_MCS_ERR_LONG_VAL_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gab0c40404b2cd37d0a729504aa270e697)。

读取长特征值子过程（Read Long Value Characteristic Sub-procedure）进行期间，某个特征值发生了变化。

<a id="r_ga4ae0b32e4192ba36b3ad4d6d8354929a"></a>

```c
#define BT_MCS_OPCODES_SUPPORTED_LEN 4U
```

相关声明：[BT_MCS_OPCODES_SUPPORTED_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga4ae0b32e4192ba36b3ad4d6d8354929a)。

媒体控制点（Media Control Point）支持的操作码字段长度。

<a id="r_gaff47bc210fdd2d4d80a0ce822ca29a67"></a>

```c
#define SEARCH_LEN_MIN 2U
```

相关声明：[SEARCH_LEN_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaff47bc210fdd2d4d80a0ce822ca29a67)。

搜索控制点（Search Control Point）最小长度。

<a id="r_gaf771b17acd202a20450b6ea939ddee3b"></a>

```c
#define SEARCH_LEN_MAX 64U
```

相关声明：[SEARCH_LEN_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaf771b17acd202a20450b6ea939ddee3b)。

搜索控制点（Search Control Point）最大长度。

<a id="r_gab1fad64b6a1edfefce90cd4692576a5d"></a>

```c
#define SEARCH_SCI_LEN_MIN
```

相关声明：[SEARCH_SCI_LEN_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gab1fad64b6a1edfefce90cd4692576a5d)。

搜索控制点项（Search Control Point Item，SCI）最小长度。

<a id="r_ga81665fd87487cbaf1c0f90f1e0b2126a"></a>

```c
#define SEARCH_PARAM_MAX 62U
```

相关声明：[SEARCH_PARAM_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga81665fd87487cbaf1c0f90f1e0b2126a)。

搜索参数（Search Parameters）最大长度。

<a id="define-members-0"></a>

### 播放速度（Playback speeds）

播放速度（Playback Speed）s 由 2 的 p/64 次幂计算，即 `s = 2^(p/64)`。

允许 -128 到 127 的所有值，这里只定义部分示例。

<a id="r_ga5d450ac222a491b7d544cc4d3f3ffcf0"></a>

```c
#define BT_MCS_PLAYBACK_SPEED_MIN -128
```

相关声明：[BT_MCS_PLAYBACK_SPEED_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga5d450ac222a491b7d544cc4d3f3ffcf0)。

最低播放速度（Minimum Playback Speed），对应 25% 速度。

<a id="r_ga90e55b0230a11f752b111750e94ace4c"></a>

```c
#define BT_MCS_PLAYBACK_SPEED_QUARTER -128
```

相关声明：[BT_MCS_PLAYBACK_SPEED_QUARTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga90e55b0230a11f752b111750e94ace4c)。

四分之一播放速度（Quarter Playback Speed），对应 25% 速度。

<a id="r_ga3bff45add6fbf602ad6bb07b0e64b335"></a>

```c
#define BT_MCS_PLAYBACK_SPEED_HALF -64
```

相关声明：[BT_MCS_PLAYBACK_SPEED_HALF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga3bff45add6fbf602ad6bb07b0e64b335)。

半速播放（Half Playback Speed），对应 50% 速度。

<a id="r_ga68c0eaa632ca581a1ab5ab144b3d7693"></a>

```c
#define BT_MCS_PLAYBACK_SPEED_UNITY 0
```

相关声明：[BT_MCS_PLAYBACK_SPEED_UNITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga68c0eaa632ca581a1ab5ab144b3d7693)。

一倍播放速度（Unity Playback Speed），对应 100% 速度。

<a id="r_ga05ec8bf9ae813c8a3755b1383030bdf0"></a>

```c
#define BT_MCS_PLAYBACK_SPEED_DOUBLE 64
```

相关声明：[BT_MCS_PLAYBACK_SPEED_DOUBLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga05ec8bf9ae813c8a3755b1383030bdf0)。

双倍播放速度（Double Playback Speed），对应 200% 速度。

<a id="r_gaa3299c597471a809033ec45b2c6f5b3d"></a>

```c
#define BT_MCS_PLAYBACK_SPEED_MAX 127
```

相关声明：[BT_MCS_PLAYBACK_SPEED_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaa3299c597471a809033ec45b2c6f5b3d)。

最高播放速度（Max Playback Speed），对应 395.7% 速度，接近 400%。

<a id="define-members-1"></a>

### 搜寻速度（Seeking speed）

搜寻速度（Seeking Speed）的允许值为 -64 到 -4（含端点）、0，以及 4 到 64（含端点）。

<a id="r_ga22c0b457d8c6e9ec119fff38205786d3"></a>

```c
#define BT_MCS_SEEKING_SPEED_FACTOR_MAX 64
```

相关声明：[BT_MCS_SEEKING_SPEED_FACTOR_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga22c0b457d8c6e9ec119fff38205786d3)。

最大搜寻速度（Maximum Seeking Speed），可取负值。

<a id="r_gaf912dcbc70c81a023f8b93a4d4b0e745"></a>

```c
#define BT_MCS_SEEKING_SPEED_FACTOR_MIN 4
```

相关声明：[BT_MCS_SEEKING_SPEED_FACTOR_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaf912dcbc70c81a023f8b93a4d4b0e745)。

最小搜寻速度（Minimum Seeking Speed），可取负值。

<a id="r_ga16bdf755d07c99895fa8698f9bd637a0"></a>

```c
#define BT_MCS_SEEKING_SPEED_FACTOR_ZERO 0
```

相关声明：[BT_MCS_SEEKING_SPEED_FACTOR_ZERO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga16bdf755d07c99895fa8698f9bd637a0)。

不搜寻（No Seeking）。

<a id="define-members-2"></a>

### 播放顺序（Playing orders）

<a id="r_ga1c25a91795472a553286def379fe943b"></a>

```c
#define BT_MCS_PLAYING_ORDER_SINGLE_ONCE 0x01U
```

相关声明：[BT_MCS_PLAYING_ORDER_SINGLE_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga1c25a91795472a553286def379fe943b)。

单个音轨（Track）播放一次，没有下一音轨。

<a id="r_ga4698529b5268ff1c5099f4cc9d8e9966"></a>

```c
#define BT_MCS_PLAYING_ORDER_SINGLE_REPEAT 0x02U
```

相关声明：[BT_MCS_PLAYING_ORDER_SINGLE_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga4698529b5268ff1c5099f4cc9d8e9966)。

重复播放单个音轨（Track），下一音轨就是当前音轨。

<a id="r_ga8b8023d46c3ce402a07c9146494ada60"></a>

```c
#define BT_MCS_PLAYING_ORDER_INORDER_ONCE 0x03U
```

相关声明：[BT_MCS_PLAYING_ORDER_INORDER_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga8b8023d46c3ce402a07c9146494ada60)。

按音轨顺序（Track Order）将组内音轨播放一次。

<a id="r_gaaccf440eb5df01eaa0a255e09cf7b996"></a>

```c
#define BT_MCS_PLAYING_ORDER_INORDER_REPEAT 0x04U
```

相关声明：[BT_MCS_PLAYING_ORDER_INORDER_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaaccf440eb5df01eaa0a255e09cf7b996)。

按音轨顺序（Track Order）重复播放组内音轨。

<a id="r_ga260b73c14b35ee596cacca082b5dc865"></a>

```c
#define BT_MCS_PLAYING_ORDER_OLDEST_ONCE 0x05U
```

相关声明：[BT_MCS_PLAYING_ORDER_OLDEST_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga260b73c14b35ee596cacca082b5dc865)。

从最旧音轨开始，将组内音轨播放一次（Oldest First）。

<a id="r_ga2fb92d553aed2f680321db68ef28035f"></a>

```c
#define BT_MCS_PLAYING_ORDER_OLDEST_REPEAT 0x06U
```

相关声明：[BT_MCS_PLAYING_ORDER_OLDEST_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga2fb92d553aed2f680321db68ef28035f)。

从最旧音轨开始，重复播放组内音轨（Oldest First）。

<a id="r_gaaa06525a5d53d4bf2312304208dda311"></a>

```c
#define BT_MCS_PLAYING_ORDER_NEWEST_ONCE 0x07U
```

相关声明：[BT_MCS_PLAYING_ORDER_NEWEST_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaaa06525a5d53d4bf2312304208dda311)。

从最新音轨开始，将组内音轨播放一次（Newest First）。

<a id="r_ga28a19c78f96b51f0e048395eb4378d61"></a>

```c
#define BT_MCS_PLAYING_ORDER_NEWEST_REPEAT 0x08U
```

相关声明：[BT_MCS_PLAYING_ORDER_NEWEST_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga28a19c78f96b51f0e048395eb4378d61)。

从最新音轨开始，重复播放组内音轨（Newest First）。

<a id="r_gaa33a02e34f65021b1b7290edc76b166e"></a>

```c
#define BT_MCS_PLAYING_ORDER_SHUFFLE_ONCE 0x09U
```

相关声明：[BT_MCS_PLAYING_ORDER_SHUFFLE_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaa33a02e34f65021b1b7290edc76b166e)。

以随机顺序（Random Order）将组内音轨播放一次。

<a id="r_gaa231c007f0448a5ba3bd61e8528c5b1e"></a>

```c
#define BT_MCS_PLAYING_ORDER_SHUFFLE_REPEAT 0x0AU
```

相关声明：[BT_MCS_PLAYING_ORDER_SHUFFLE_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaa231c007f0448a5ba3bd61e8528c5b1e)。

以随机顺序（Random Order）重复播放组内音轨。

<a id="define-members-3"></a>

### 支持的播放顺序（Playing orders supported）

位图（Bitmap），其顺序与上文的播放顺序相同。

注意，播放顺序（Playing Order）1 对应位 0，依此类推。

<a id="r_ga7102f1909baea2320827ea6b47522bd8"></a>

```c
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_SINGLE_ONCE BIT(0U)
```

相关声明：[BT_MCS_PLAYING_ORDERS_SUPPORTED_SINGLE_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga7102f1909baea2320827ea6b47522bd8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

单个音轨（Track）播放一次，没有下一音轨。

<a id="r_gafecb7edde06dfb97939af93034690cbc"></a>

```c
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_SINGLE_REPEAT BIT(1U)
```

相关声明：[BT_MCS_PLAYING_ORDERS_SUPPORTED_SINGLE_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gafecb7edde06dfb97939af93034690cbc)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

重复播放单个音轨（Track），下一音轨就是当前音轨。

<a id="r_ga594daa869c6696a4cdd961f8786134a6"></a>

```c
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_INORDER_ONCE BIT(2U)
```

相关声明：[BT_MCS_PLAYING_ORDERS_SUPPORTED_INORDER_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga594daa869c6696a4cdd961f8786134a6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

按音轨顺序（Track Order）将组内音轨播放一次。

<a id="r_gac4bcd9b84e28a47dd23d073dd942a9c8"></a>

```c
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_INORDER_REPEAT BIT(3U)
```

相关声明：[BT_MCS_PLAYING_ORDERS_SUPPORTED_INORDER_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gac4bcd9b84e28a47dd23d073dd942a9c8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

按音轨顺序（Track Order）重复播放组内音轨。

<a id="r_gae1d8c34c8f9ea9fadc4da56d0d127712"></a>

```c
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_OLDEST_ONCE BIT(4U)
```

相关声明：[BT_MCS_PLAYING_ORDERS_SUPPORTED_OLDEST_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gae1d8c34c8f9ea9fadc4da56d0d127712)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

从最旧音轨开始，将组内音轨播放一次（Oldest First）。

<a id="r_ga38bb3aa9a388fa3ae0230cb78cf2d3a5"></a>

```c
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_OLDEST_REPEAT BIT(5U)
```

相关声明：[BT_MCS_PLAYING_ORDERS_SUPPORTED_OLDEST_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga38bb3aa9a388fa3ae0230cb78cf2d3a5)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

从最旧音轨开始，重复播放组内音轨（Oldest First）。

<a id="r_gabd77af4da60d1b7531d35bd543cb4df2"></a>

```c
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_NEWEST_ONCE BIT(6U)
```

相关声明：[BT_MCS_PLAYING_ORDERS_SUPPORTED_NEWEST_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gabd77af4da60d1b7531d35bd543cb4df2)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

从最新音轨开始，将组内音轨播放一次（Newest First）。

<a id="r_ga9bb22c2c7d08032ab1d5c3ae64ce01a8"></a>

```c
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_NEWEST_REPEAT BIT(7U)
```

相关声明：[BT_MCS_PLAYING_ORDERS_SUPPORTED_NEWEST_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga9bb22c2c7d08032ab1d5c3ae64ce01a8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

从最新音轨开始，重复播放组内音轨（Newest First）。

<a id="r_ga2c245ad4f76937b366770aa7afe7b684"></a>

```c
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_SHUFFLE_ONCE BIT(8U)
```

相关声明：[BT_MCS_PLAYING_ORDERS_SUPPORTED_SHUFFLE_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga2c245ad4f76937b366770aa7afe7b684)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

以随机顺序（Random Order）将组内音轨播放一次。

<a id="r_gae5d972a834c1b568f39df91df0febb81"></a>

```c
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_SHUFFLE_REPEAT BIT(9U)
```

相关声明：[BT_MCS_PLAYING_ORDERS_SUPPORTED_SHUFFLE_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gae5d972a834c1b568f39df91df0febb81)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

以随机顺序（Random Order）重复播放组内音轨。

<a id="define-members-4"></a>

### 媒体状态（Media states）

<a id="r_gaa9c7d92a8aa79b1020c8b593b0edc088"></a>

```c
#define BT_MCS_MEDIA_STATE_INACTIVE 0x00U
```

相关声明：[BT_MCS_MEDIA_STATE_INACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaa9c7d92a8aa79b1020c8b593b0edc088)。

当前音轨无效，且未选择任何音轨（Track）。

<a id="r_gaa33b1ba9ebfd0d226df869cdc35e964c"></a>

```c
#define BT_MCS_MEDIA_STATE_PLAYING 0x01U
```

相关声明：[BT_MCS_MEDIA_STATE_PLAYING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaa33b1ba9ebfd0d226df869cdc35e964c)。

媒体播放器（Media Player）正在播放当前音轨。

<a id="r_gaa5a2768a288fe8058818b5f965c0d8b3"></a>

```c
#define BT_MCS_MEDIA_STATE_PAUSED 0x02U
```

相关声明：[BT_MCS_MEDIA_STATE_PAUSED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaa5a2768a288fe8058818b5f965c0d8b3)。

当前音轨已暂停（Paused）。

<a id="r_ga689e83131b6db63fa3a76f428a93714b"></a>

```c
#define BT_MCS_MEDIA_STATE_SEEKING 0x03U
```

相关声明：[BT_MCS_MEDIA_STATE_SEEKING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga689e83131b6db63fa3a76f428a93714b)。

当前音轨正在快进或快退（Fast Forwarding / Fast Rewinding）。

<a id="define-members-5"></a>

### 媒体控制点操作码（Media control point opcodes）

<a id="r_ga79c4cf8292a4548bc7b9b06b1ce0f60a"></a>

```c
#define BT_MCS_OPC_PLAY 0x01U
```

相关声明：[BT_MCS_OPC_PLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga79c4cf8292a4548bc7b9b06b1ce0f60a)。

开始播放当前音轨（Track）。

<a id="r_ga8b15cb7a8a1429f83e8d1619c37becc6"></a>

```c
#define BT_MCS_OPC_PAUSE 0x02U
```

相关声明：[BT_MCS_OPC_PAUSE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga8b15cb7a8a1429f83e8d1619c37becc6)。

暂停播放当前音轨（Track）。

<a id="r_ga6d49190bae54e66695ea3c856d558049"></a>

```c
#define BT_MCS_OPC_FAST_REWIND 0x03U
```

相关声明：[BT_MCS_OPC_FAST_REWIND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga6d49190bae54e66695ea3c856d558049)。

快退（Fast Rewind）当前音轨。

<a id="r_ga9ce0d00b1cfc0d3a33762aaed3c1bb75"></a>

```c
#define BT_MCS_OPC_FAST_FORWARD 0x04U
```

相关声明：[BT_MCS_OPC_FAST_FORWARD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga9ce0d00b1cfc0d3a33762aaed3c1bb75)。

快进（Fast Forward）当前音轨。

<a id="r_gade874bf59dc08ddb682280b644821e11"></a>

```c
#define BT_MCS_OPC_STOP 0x05U
```

相关声明：[BT_MCS_OPC_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gade874bf59dc08ddb682280b644821e11)。

停止当前活动，回到暂停状态（Paused State），并将当前音轨位置设为当前音轨起点。

<a id="r_gada25cc85988f5988887eab0cf66e4190"></a>

```c
#define BT_MCS_OPC_MOVE_RELATIVE 0x10U
```

相关声明：[BT_MCS_OPC_MOVE_RELATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gada25cc85988f5988887eab0cf66e4190)。

相对于当前音轨位置（Current Track Position），设置新的当前位置。

<a id="r_ga454775706fe60ccd12e5ab44e6ddacba"></a>

```c
#define BT_MCS_OPC_PREV_SEGMENT 0x20U
```

相关声明：[BT_MCS_OPC_PREV_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga454775706fe60ccd12e5ab44e6ddacba)。

将当前音轨位置设为当前音轨上一段（Previous Segment）的起始位置。

<a id="r_ga9cc7b813b933b56b1f60ef0ddf8e39df"></a>

```c
#define BT_MCS_OPC_NEXT_SEGMENT 0x21U
```

相关声明：[BT_MCS_OPC_NEXT_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga9cc7b813b933b56b1f60ef0ddf8e39df)。

将当前音轨位置设为当前音轨下一段（Next Segment）的起始位置。

<a id="r_ga6148011e40389bbed998a971f44f834a"></a>

```c
#define BT_MCS_OPC_FIRST_SEGMENT 0x22U
```

相关声明：[BT_MCS_OPC_FIRST_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga6148011e40389bbed998a971f44f834a)。

将当前音轨位置设为当前音轨第一段（First Segment）的起始位置。

<a id="r_ga08421e4d26d54fe3d40edeb08fd44aac"></a>

```c
#define BT_MCS_OPC_LAST_SEGMENT 0x23U
```

相关声明：[BT_MCS_OPC_LAST_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga08421e4d26d54fe3d40edeb08fd44aac)。

将当前音轨位置设为当前音轨最后一段（Last Segment）的起始位置。

<a id="r_ga4b91b6e3e3f92619d45ecc2066e97e74"></a>

```c
#define BT_MCS_OPC_GOTO_SEGMENT 0x24U
```

相关声明：[BT_MCS_OPC_GOTO_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga4b91b6e3e3f92619d45ecc2066e97e74)。

将当前音轨位置设为当前音轨第 n 段（Nth Segment）的起始位置。

<a id="r_ga88e09cd634c2dd3068f746cc978c1568"></a>

```c
#define BT_MCS_OPC_PREV_TRACK 0x30U
```

相关声明：[BT_MCS_OPC_PREV_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga88e09cd634c2dd3068f746cc978c1568)。

按播放顺序（Playing Order）将当前音轨设为上一音轨。

<a id="r_ga06df0d77c7a678ca8f4f01ec64c88de7"></a>

```c
#define BT_MCS_OPC_NEXT_TRACK 0x31U
```

相关声明：[BT_MCS_OPC_NEXT_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga06df0d77c7a678ca8f4f01ec64c88de7)。

按播放顺序（Playing Order）将当前音轨设为下一音轨。

<a id="r_gaed893751ae2ceae3a1d5c764b9411ecc"></a>

```c
#define BT_MCS_OPC_FIRST_TRACK 0x32U
```

相关声明：[BT_MCS_OPC_FIRST_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaed893751ae2ceae3a1d5c764b9411ecc)。

按播放顺序（Playing Order）将当前音轨设为第一音轨。

<a id="r_gacd2e15226d20eb65962d6441c2b7d565"></a>

```c
#define BT_MCS_OPC_LAST_TRACK 0x33U
```

相关声明：[BT_MCS_OPC_LAST_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gacd2e15226d20eb65962d6441c2b7d565)。

按播放顺序（Playing Order）将当前音轨设为最后一音轨。

<a id="r_ga4d5124b9ffc125e31c45c06a12fcc85c"></a>

```c
#define BT_MCS_OPC_GOTO_TRACK 0x34U
```

相关声明：[BT_MCS_OPC_GOTO_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga4d5124b9ffc125e31c45c06a12fcc85c)。

按播放顺序（Playing Order）将当前音轨设为第 n 个音轨。

<a id="r_gab7efc1fb17cc53c376f6f84bf31ef85c"></a>

```c
#define BT_MCS_OPC_PREV_GROUP 0x40U
```

相关声明：[BT_MCS_OPC_PREV_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gab7efc1fb17cc53c376f6f84bf31ef85c)。

将当前组设为组序列（Sequence of Groups）中的上一组。

<a id="r_ga4feb6b16975ae123bc77c08509e0c809"></a>

```c
#define BT_MCS_OPC_NEXT_GROUP 0x41U
```

相关声明：[BT_MCS_OPC_NEXT_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga4feb6b16975ae123bc77c08509e0c809)。

将当前组设为组序列（Sequence of Groups）中的下一组。

<a id="r_ga0b6075379c9abf0911c8a1f2b8d11923"></a>

```c
#define BT_MCS_OPC_FIRST_GROUP 0x42U
```

相关声明：[BT_MCS_OPC_FIRST_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga0b6075379c9abf0911c8a1f2b8d11923)。

将当前组设为组序列（Sequence of Groups）中的第一组。

<a id="r_gad234093556575ac31985944a483597e8"></a>

```c
#define BT_MCS_OPC_LAST_GROUP 0x43U
```

相关声明：[BT_MCS_OPC_LAST_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gad234093556575ac31985944a483597e8)。

将当前组设为组序列（Sequence of Groups）中的最后一组。

<a id="r_ga1911ae5e1285041a77bbd1db773c33b5"></a>

```c
#define BT_MCS_OPC_GOTO_GROUP 0x44U
```

相关声明：[BT_MCS_OPC_GOTO_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga1911ae5e1285041a77bbd1db773c33b5)。

将当前组设为组序列（Sequence of Groups）中的第 n 组。

<a id="define-members-6"></a>

### 媒体控制点支持的操作码值（Media control point supported opcodes values）

<a id="r_ga82d1bbc5cd67ab30960bca6992116a8f"></a>

```c
#define BT_MCS_OPC_SUP_PLAY BIT(0U)
```

相关声明：[BT_MCS_OPC_SUP_PLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga82d1bbc5cd67ab30960bca6992116a8f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持播放操作码（Play Opcode）。

<a id="r_gabdca574666b964d506d96e01562875f4"></a>

```c
#define BT_MCS_OPC_SUP_PAUSE BIT(1U)
```

相关声明：[BT_MCS_OPC_SUP_PAUSE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gabdca574666b964d506d96e01562875f4)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持暂停操作码（Pause Opcode）。

<a id="r_gaaa3b553dc8eb2de610b545f1ce88b067"></a>

```c
#define BT_MCS_OPC_SUP_FAST_REWIND BIT(2U)
```

相关声明：[BT_MCS_OPC_SUP_FAST_REWIND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaaa3b553dc8eb2de610b545f1ce88b067)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持快退操作码（Fast Rewind Opcode）。

<a id="r_gaa24785ccc713cb2421a55ff48f5f2c45"></a>

```c
#define BT_MCS_OPC_SUP_FAST_FORWARD BIT(3U)
```

相关声明：[BT_MCS_OPC_SUP_FAST_FORWARD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaa24785ccc713cb2421a55ff48f5f2c45)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持快进操作码（Fast Forward Opcode）。

<a id="r_gaec507c502c53413e510cc30f179befec"></a>

```c
#define BT_MCS_OPC_SUP_STOP BIT(4U)
```

相关声明：[BT_MCS_OPC_SUP_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaec507c502c53413e510cc30f179befec)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持停止操作码（Stop Opcode）。

<a id="r_ga3024e1b5a5175d2f45cdc7650bb9f66a"></a>

```c
#define BT_MCS_OPC_SUP_MOVE_RELATIVE BIT(5U)
```

相关声明：[BT_MCS_OPC_SUP_MOVE_RELATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga3024e1b5a5175d2f45cdc7650bb9f66a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持相对移动操作码（Move Relative Opcode）。

<a id="r_gae074d9404aa5c8722678d6805fb7636d"></a>

```c
#define BT_MCS_OPC_SUP_PREV_SEGMENT BIT(6U)
```

相关声明：[BT_MCS_OPC_SUP_PREV_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gae074d9404aa5c8722678d6805fb7636d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持上一段操作码（Previous Segment Opcode）。

<a id="r_ga416c45a7a2ac8c744c42c19a454d6363"></a>

```c
#define BT_MCS_OPC_SUP_NEXT_SEGMENT BIT(7U)
```

相关声明：[BT_MCS_OPC_SUP_NEXT_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga416c45a7a2ac8c744c42c19a454d6363)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持下一段操作码（Next Segment Opcode）。

<a id="r_ga5434b6409f4300cd86df1f75cb699ad8"></a>

```c
#define BT_MCS_OPC_SUP_FIRST_SEGMENT BIT(8U)
```

相关声明：[BT_MCS_OPC_SUP_FIRST_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga5434b6409f4300cd86df1f75cb699ad8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持第一段操作码（First Segment Opcode）。

<a id="r_ga9c4e53c88ea8ea9eb056e9ff37b58dd1"></a>

```c
#define BT_MCS_OPC_SUP_LAST_SEGMENT BIT(9U)
```

相关声明：[BT_MCS_OPC_SUP_LAST_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga9c4e53c88ea8ea9eb056e9ff37b58dd1)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持最后一段操作码（Last Segment Opcode）。

<a id="r_ga9c576ae9a0ad2200a4b29059e88c6c28"></a>

```c
#define BT_MCS_OPC_SUP_GOTO_SEGMENT BIT(10U)
```

相关声明：[BT_MCS_OPC_SUP_GOTO_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga9c576ae9a0ad2200a4b29059e88c6c28)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持转到指定段操作码（Goto Segment Opcode）。

<a id="r_ga59794af43d1b78a1f1a52fb48769be9c"></a>

```c
#define BT_MCS_OPC_SUP_PREV_TRACK BIT(11U)
```

相关声明：[BT_MCS_OPC_SUP_PREV_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga59794af43d1b78a1f1a52fb48769be9c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持上一音轨操作码（Previous Track Opcode）。

<a id="r_gae213edc6b714f0a1adc744e8ff779ee6"></a>

```c
#define BT_MCS_OPC_SUP_NEXT_TRACK BIT(12U)
```

相关声明：[BT_MCS_OPC_SUP_NEXT_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gae213edc6b714f0a1adc744e8ff779ee6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持下一音轨操作码（Next Track Opcode）。

<a id="r_ga7d79bde3dbc9044667fa2bc54cc7cec4"></a>

```c
#define BT_MCS_OPC_SUP_FIRST_TRACK BIT(13U)
```

相关声明：[BT_MCS_OPC_SUP_FIRST_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga7d79bde3dbc9044667fa2bc54cc7cec4)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持第一音轨操作码（First Track Opcode）。

<a id="r_ga8752a8b6ee27919025bb3e5fb4a77c46"></a>

```c
#define BT_MCS_OPC_SUP_LAST_TRACK BIT(14U)
```

相关声明：[BT_MCS_OPC_SUP_LAST_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga8752a8b6ee27919025bb3e5fb4a77c46)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持最后音轨操作码（Last Track Opcode）。

<a id="r_gaf8573ac7d802252076ef759575baef2f"></a>

```c
#define BT_MCS_OPC_SUP_GOTO_TRACK BIT(15U)
```

相关声明：[BT_MCS_OPC_SUP_GOTO_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaf8573ac7d802252076ef759575baef2f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持转到指定音轨操作码（Goto Track Opcode）。

<a id="r_ga4443a0f87750c537a6a39544bbf63111"></a>

```c
#define BT_MCS_OPC_SUP_PREV_GROUP BIT(16U)
```

相关声明：[BT_MCS_OPC_SUP_PREV_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga4443a0f87750c537a6a39544bbf63111)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持上一组操作码（Previous Group Opcode）。

<a id="r_gaeeeff1f344202619794af0de0cda199b"></a>

```c
#define BT_MCS_OPC_SUP_NEXT_GROUP BIT(17U)
```

相关声明：[BT_MCS_OPC_SUP_NEXT_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaeeeff1f344202619794af0de0cda199b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持下一组操作码（Next Group Opcode）。

<a id="r_ga57508e39d5a32ebefb0b103f805ec047"></a>

```c
#define BT_MCS_OPC_SUP_FIRST_GROUP BIT(18U)
```

相关声明：[BT_MCS_OPC_SUP_FIRST_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga57508e39d5a32ebefb0b103f805ec047)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持第一组操作码（First Group Opcode）。

<a id="r_ga80bf605e90dee5841d14fdbb9b39f96a"></a>

```c
#define BT_MCS_OPC_SUP_LAST_GROUP BIT(19U)
```

相关声明：[BT_MCS_OPC_SUP_LAST_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga80bf605e90dee5841d14fdbb9b39f96a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持最后一组操作码（Last Group Opcode）。

<a id="r_ga158df3fd1ae39fc3405e25ba7d056d80"></a>

```c
#define BT_MCS_OPC_SUP_GOTO_GROUP BIT(20U)
```

相关声明：[BT_MCS_OPC_SUP_GOTO_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga158df3fd1ae39fc3405e25ba7d056d80)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持转到指定组操作码（Goto Group Opcode）。

<a id="define-members-7"></a>

### 媒体控制点通知结果码（Media control point notification result codes）

<a id="r_ga7507062e3fe2df221cd47546713a0d28"></a>

```c
#define BT_MCS_OPC_NTF_SUCCESS 0x01U
```

相关声明：[BT_MCS_OPC_NTF_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga7507062e3fe2df221cd47546713a0d28)。

写入操作码（Opcode Write）所请求的动作已成功完成。

<a id="r_ga72e92f172f03a64d2d4641bcdbdb614f"></a>

```c
#define BT_MCS_OPC_NTF_NOT_SUPPORTED 0x02U
```

相关声明：[BT_MCS_OPC_NTF_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga72e92f172f03a64d2d4641bcdbdb614f)。

写入媒体控制点（Media Control Point）时使用了无效或不支持的操作码。

<a id="r_ga740d7278a770b215ae185441fb43c85b"></a>

```c
#define BT_MCS_OPC_NTF_PLAYER_INACTIVE 0x03U
```

相关声明：[BT_MCS_OPC_NTF_PLAYER_INACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga740d7278a770b215ae185441fb43c85b)。

收到操作码时，媒体播放器状态（Media Player State）特征值为非活动（Inactive）；或执行该操作码所请求动作的结果，使该特征值变为 Inactive。

<a id="r_gafe5d0665ae8b33428bce16c427eabcc1"></a>

```c
#define BT_MCS_OPC_NTF_CANNOT_BE_COMPLETED 0x04U
```

相关声明：[BT_MCS_OPC_NTF_CANNOT_BE_COMPLETED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gafe5d0665ae8b33428bce16c427eabcc1)。

由于播放器内部的某种条件，无法成功完成任何媒体控制点写入（Media Control Point Write）所请求的动作。

<a id="define-members-8"></a>

### 搜索控制点类型值（Search control point type values）

参考：《媒体控制服务规范》（Media Control Service Specification）v1.0 第 3.20.2 节。

<a id="r_ga5a53ce79494a2ec935a43e2cabb6496c"></a>

```c
#define BT_MCS_SEARCH_TYPE_TRACK_NAME 0x01U
```

相关声明：[BT_MCS_SEARCH_TYPE_TRACK_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga5a53ce79494a2ec935a43e2cabb6496c)。

按音轨名称（Track Name）搜索。

<a id="r_ga3bbf3a3393fa08a8f797e7e286f4b06f"></a>

```c
#define BT_MCS_SEARCH_TYPE_ARTIST_NAME 0x02U
```

相关声明：[BT_MCS_SEARCH_TYPE_ARTIST_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga3bbf3a3393fa08a8f797e7e286f4b06f)。

按艺人名称（Artist Name）搜索。

<a id="r_gade2b66ace813a9bf91b497fbc1dfb885"></a>

```c
#define BT_MCS_SEARCH_TYPE_ALBUM_NAME 0x03U
```

相关声明：[BT_MCS_SEARCH_TYPE_ALBUM_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gade2b66ace813a9bf91b497fbc1dfb885)。

按专辑名称（Album Name）搜索。

<a id="r_gaf98145eae298cca9e3df1dbcca9118a7"></a>

```c
#define BT_MCS_SEARCH_TYPE_GROUP_NAME 0x04U
```

相关声明：[BT_MCS_SEARCH_TYPE_GROUP_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaf98145eae298cca9e3df1dbcca9118a7)。

按组名称（Group Name）搜索。

<a id="r_ga2befe4b4b22125a9e24ab4af6eb08f95"></a>

```c
#define BT_MCS_SEARCH_TYPE_EARLIEST_YEAR 0x05U
```

相关声明：[BT_MCS_SEARCH_TYPE_EARLIEST_YEAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga2befe4b4b22125a9e24ab4af6eb08f95)。

按最早年份（Earliest Year）搜索。

<a id="r_gad120d8a4f7130762568b7c6f87a34cd4"></a>

```c
#define BT_MCS_SEARCH_TYPE_LATEST_YEAR 0x06U
```

相关声明：[BT_MCS_SEARCH_TYPE_LATEST_YEAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gad120d8a4f7130762568b7c6f87a34cd4)。

按最晚年份（Latest Year）搜索。

<a id="r_gae4d30046fb1f4d6ffc554fdd95946bf0"></a>

```c
#define BT_MCS_SEARCH_TYPE_GENRE 0x07U
```

相关声明：[BT_MCS_SEARCH_TYPE_GENRE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gae4d30046fb1f4d6ffc554fdd95946bf0)。

按流派（Genre）搜索。

<a id="r_gaa99d74ce6f523185a3522f257647edce"></a>

```c
#define BT_MCS_SEARCH_TYPE_ONLY_TRACKS 0x08U
```

相关声明：[BT_MCS_SEARCH_TYPE_ONLY_TRACKS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaa99d74ce6f523185a3522f257647edce)。

仅搜索音轨（Tracks）。

<a id="r_gab6f6fb41e61f5b4c257e36cba71f98a2"></a>

```c
#define BT_MCS_SEARCH_TYPE_ONLY_GROUPS 0x09U
```

相关声明：[BT_MCS_SEARCH_TYPE_ONLY_GROUPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gab6f6fb41e61f5b4c257e36cba71f98a2)。

仅搜索组（Groups）。

<a id="define-members-9"></a>

### 搜索通知结果码（Search notification result codes）

参考：《媒体控制服务规范》（Media Control Service Specification）v1.0 第 3.20.2 节。

<a id="r_gaa292c3bb4b5eeb62d5e8e6cb72e69908"></a>

```c
#define BT_MCS_SCP_NTF_SUCCESS 0x01U
```

相关声明：[BT_MCS_SCP_NTF_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaa292c3bb4b5eeb62d5e8e6cb72e69908)。

搜索请求（Search Request）已接受，搜索已开始。

<a id="r_ga0a7769ba43b5b5b20cdbce71a129fcef"></a>

```c
#define BT_MCS_SCP_NTF_FAILURE 0x02U
```

相关声明：[BT_MCS_SCP_NTF_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga0a7769ba43b5b5b20cdbce71a129fcef)。

搜索请求（Search Request）无效，未开始搜索。

<a id="define-members-10"></a>

### 组对象的对象类型（Group object object types）

参考：《媒体控制服务规范》（Media Control Service Specification）v1.0 第 4.4.1 节。

<a id="r_gab6f895d3001c6e896c0d9aa9fb11bbc1"></a>

```c
#define BT_MCS_GROUP_OBJECT_TRACK_TYPE 0x00U
```

相关声明：[BT_MCS_GROUP_OBJECT_TRACK_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gab6f895d3001c6e896c0d9aa9fb11bbc1)。

组对象类型（Group Object Type）为音轨（Track）。

<a id="r_gad7a15680dcf289dfe68b3d8c5f8c9d91"></a>

```c
#define BT_MCS_GROUP_OBJECT_GROUP_TYPE 0x01U
```

相关声明：[BT_MCS_GROUP_OBJECT_GROUP_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gad7a15680dcf289dfe68b3d8c5f8c9d91)。

组对象类型（Group Object Type）为组（Group）。


## 6.2\_原页交叉引用（Cross References）

- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P108_mcs.h_源码浏览.md)
- [BT_MCS_ERR_LONG_VAL_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gab0c40404b2cd37d0a729504aa270e697)
- [BT_MCS_OPCODES_SUPPORTED_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga4ae0b32e4192ba36b3ad4d6d8354929a)
- [SEARCH_LEN_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaff47bc210fdd2d4d80a0ce822ca29a67)
- [SEARCH_LEN_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaf771b17acd202a20450b6ea939ddee3b)
- [SEARCH_SCI_LEN_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gab1fad64b6a1edfefce90cd4692576a5d)
- [SEARCH_PARAM_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga81665fd87487cbaf1c0f90f1e0b2126a)
- [BT_MCS_PLAYBACK_SPEED_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga5d450ac222a491b7d544cc4d3f3ffcf0)
- [BT_MCS_PLAYBACK_SPEED_QUARTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga90e55b0230a11f752b111750e94ace4c)
- [BT_MCS_PLAYBACK_SPEED_HALF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga3bff45add6fbf602ad6bb07b0e64b335)
- [BT_MCS_PLAYBACK_SPEED_UNITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga68c0eaa632ca581a1ab5ab144b3d7693)
- [BT_MCS_PLAYBACK_SPEED_DOUBLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga05ec8bf9ae813c8a3755b1383030bdf0)
- [BT_MCS_PLAYBACK_SPEED_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaa3299c597471a809033ec45b2c6f5b3d)
- [BT_MCS_SEEKING_SPEED_FACTOR_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga22c0b457d8c6e9ec119fff38205786d3)
- [BT_MCS_SEEKING_SPEED_FACTOR_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaf912dcbc70c81a023f8b93a4d4b0e745)
- [BT_MCS_SEEKING_SPEED_FACTOR_ZERO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga16bdf755d07c99895fa8698f9bd637a0)
- [BT_MCS_PLAYING_ORDER_SINGLE_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga1c25a91795472a553286def379fe943b)
- [BT_MCS_PLAYING_ORDER_SINGLE_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga4698529b5268ff1c5099f4cc9d8e9966)
- [BT_MCS_PLAYING_ORDER_INORDER_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga8b8023d46c3ce402a07c9146494ada60)
- [BT_MCS_PLAYING_ORDER_INORDER_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaaccf440eb5df01eaa0a255e09cf7b996)
- [BT_MCS_PLAYING_ORDER_OLDEST_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga260b73c14b35ee596cacca082b5dc865)
- [BT_MCS_PLAYING_ORDER_OLDEST_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga2fb92d553aed2f680321db68ef28035f)
- [BT_MCS_PLAYING_ORDER_NEWEST_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaaa06525a5d53d4bf2312304208dda311)
- [BT_MCS_PLAYING_ORDER_NEWEST_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga28a19c78f96b51f0e048395eb4378d61)
- [BT_MCS_PLAYING_ORDER_SHUFFLE_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaa33a02e34f65021b1b7290edc76b166e)
- [BT_MCS_PLAYING_ORDER_SHUFFLE_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaa231c007f0448a5ba3bd61e8528c5b1e)
- [BT_MCS_PLAYING_ORDERS_SUPPORTED_SINGLE_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga7102f1909baea2320827ea6b47522bd8)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_MCS_PLAYING_ORDERS_SUPPORTED_SINGLE_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gafecb7edde06dfb97939af93034690cbc)
- [BT_MCS_PLAYING_ORDERS_SUPPORTED_INORDER_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga594daa869c6696a4cdd961f8786134a6)
- [BT_MCS_PLAYING_ORDERS_SUPPORTED_INORDER_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gac4bcd9b84e28a47dd23d073dd942a9c8)
- [BT_MCS_PLAYING_ORDERS_SUPPORTED_OLDEST_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gae1d8c34c8f9ea9fadc4da56d0d127712)
- [BT_MCS_PLAYING_ORDERS_SUPPORTED_OLDEST_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga38bb3aa9a388fa3ae0230cb78cf2d3a5)
- [BT_MCS_PLAYING_ORDERS_SUPPORTED_NEWEST_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gabd77af4da60d1b7531d35bd543cb4df2)
- [BT_MCS_PLAYING_ORDERS_SUPPORTED_NEWEST_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga9bb22c2c7d08032ab1d5c3ae64ce01a8)
- [BT_MCS_PLAYING_ORDERS_SUPPORTED_SHUFFLE_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga2c245ad4f76937b366770aa7afe7b684)
- [BT_MCS_PLAYING_ORDERS_SUPPORTED_SHUFFLE_REPEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gae5d972a834c1b568f39df91df0febb81)
- [BT_MCS_MEDIA_STATE_INACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaa9c7d92a8aa79b1020c8b593b0edc088)
- [BT_MCS_MEDIA_STATE_PLAYING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaa33b1ba9ebfd0d226df869cdc35e964c)
- [BT_MCS_MEDIA_STATE_PAUSED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaa5a2768a288fe8058818b5f965c0d8b3)
- [BT_MCS_MEDIA_STATE_SEEKING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga689e83131b6db63fa3a76f428a93714b)
- [BT_MCS_OPC_PLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga79c4cf8292a4548bc7b9b06b1ce0f60a)
- [BT_MCS_OPC_PAUSE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga8b15cb7a8a1429f83e8d1619c37becc6)
- [BT_MCS_OPC_FAST_REWIND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga6d49190bae54e66695ea3c856d558049)
- [BT_MCS_OPC_FAST_FORWARD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga9ce0d00b1cfc0d3a33762aaed3c1bb75)
- [BT_MCS_OPC_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gade874bf59dc08ddb682280b644821e11)
- [BT_MCS_OPC_MOVE_RELATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gada25cc85988f5988887eab0cf66e4190)
- [BT_MCS_OPC_PREV_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga454775706fe60ccd12e5ab44e6ddacba)
- [BT_MCS_OPC_NEXT_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga9cc7b813b933b56b1f60ef0ddf8e39df)
- [BT_MCS_OPC_FIRST_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga6148011e40389bbed998a971f44f834a)
- [BT_MCS_OPC_LAST_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga08421e4d26d54fe3d40edeb08fd44aac)
- [BT_MCS_OPC_GOTO_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga4b91b6e3e3f92619d45ecc2066e97e74)
- [BT_MCS_OPC_PREV_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga88e09cd634c2dd3068f746cc978c1568)
- [BT_MCS_OPC_NEXT_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga06df0d77c7a678ca8f4f01ec64c88de7)
- [BT_MCS_OPC_FIRST_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaed893751ae2ceae3a1d5c764b9411ecc)
- [BT_MCS_OPC_LAST_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gacd2e15226d20eb65962d6441c2b7d565)
- [BT_MCS_OPC_GOTO_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga4d5124b9ffc125e31c45c06a12fcc85c)
- [BT_MCS_OPC_PREV_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gab7efc1fb17cc53c376f6f84bf31ef85c)
- [BT_MCS_OPC_NEXT_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga4feb6b16975ae123bc77c08509e0c809)
- [BT_MCS_OPC_FIRST_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga0b6075379c9abf0911c8a1f2b8d11923)
- [BT_MCS_OPC_LAST_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gad234093556575ac31985944a483597e8)
- [BT_MCS_OPC_GOTO_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga1911ae5e1285041a77bbd1db773c33b5)
- [BT_MCS_OPC_SUP_PLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga82d1bbc5cd67ab30960bca6992116a8f)
- [BT_MCS_OPC_SUP_PAUSE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gabdca574666b964d506d96e01562875f4)
- [BT_MCS_OPC_SUP_FAST_REWIND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaaa3b553dc8eb2de610b545f1ce88b067)
- [BT_MCS_OPC_SUP_FAST_FORWARD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaa24785ccc713cb2421a55ff48f5f2c45)
- [BT_MCS_OPC_SUP_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaec507c502c53413e510cc30f179befec)
- [BT_MCS_OPC_SUP_MOVE_RELATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga3024e1b5a5175d2f45cdc7650bb9f66a)
- [BT_MCS_OPC_SUP_PREV_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gae074d9404aa5c8722678d6805fb7636d)
- [BT_MCS_OPC_SUP_NEXT_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga416c45a7a2ac8c744c42c19a454d6363)
- [BT_MCS_OPC_SUP_FIRST_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga5434b6409f4300cd86df1f75cb699ad8)
- [BT_MCS_OPC_SUP_LAST_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga9c4e53c88ea8ea9eb056e9ff37b58dd1)
- [BT_MCS_OPC_SUP_GOTO_SEGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga9c576ae9a0ad2200a4b29059e88c6c28)
- [BT_MCS_OPC_SUP_PREV_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga59794af43d1b78a1f1a52fb48769be9c)
- [BT_MCS_OPC_SUP_NEXT_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gae213edc6b714f0a1adc744e8ff779ee6)
- [BT_MCS_OPC_SUP_FIRST_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga7d79bde3dbc9044667fa2bc54cc7cec4)
- [BT_MCS_OPC_SUP_LAST_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga8752a8b6ee27919025bb3e5fb4a77c46)
- [BT_MCS_OPC_SUP_GOTO_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaf8573ac7d802252076ef759575baef2f)
- [BT_MCS_OPC_SUP_PREV_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga4443a0f87750c537a6a39544bbf63111)
- [BT_MCS_OPC_SUP_NEXT_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaeeeff1f344202619794af0de0cda199b)
- [BT_MCS_OPC_SUP_FIRST_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga57508e39d5a32ebefb0b103f805ec047)
- [BT_MCS_OPC_SUP_LAST_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga80bf605e90dee5841d14fdbb9b39f96a)
- [BT_MCS_OPC_SUP_GOTO_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga158df3fd1ae39fc3405e25ba7d056d80)
- [BT_MCS_OPC_NTF_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga7507062e3fe2df221cd47546713a0d28)
- [BT_MCS_OPC_NTF_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga72e92f172f03a64d2d4641bcdbdb614f)
- [BT_MCS_OPC_NTF_PLAYER_INACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga740d7278a770b215ae185441fb43c85b)
- [BT_MCS_OPC_NTF_CANNOT_BE_COMPLETED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gafe5d0665ae8b33428bce16c427eabcc1)
- [BT_MCS_SEARCH_TYPE_TRACK_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga5a53ce79494a2ec935a43e2cabb6496c)
- [BT_MCS_SEARCH_TYPE_ARTIST_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga3bbf3a3393fa08a8f797e7e286f4b06f)
- [BT_MCS_SEARCH_TYPE_ALBUM_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gade2b66ace813a9bf91b497fbc1dfb885)
- [BT_MCS_SEARCH_TYPE_GROUP_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaf98145eae298cca9e3df1dbcca9118a7)
- [BT_MCS_SEARCH_TYPE_EARLIEST_YEAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga2befe4b4b22125a9e24ab4af6eb08f95)
- [BT_MCS_SEARCH_TYPE_LATEST_YEAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gad120d8a4f7130762568b7c6f87a34cd4)
- [BT_MCS_SEARCH_TYPE_GENRE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gae4d30046fb1f4d6ffc554fdd95946bf0)
- [BT_MCS_SEARCH_TYPE_ONLY_TRACKS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaa99d74ce6f523185a3522f257647edce)
- [BT_MCS_SEARCH_TYPE_ONLY_GROUPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gab6f6fb41e61f5b4c257e36cba71f98a2)
- [BT_MCS_SCP_NTF_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaa292c3bb4b5eeb62d5e8e6cb72e69908)
- [BT_MCS_SCP_NTF_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga0a7769ba43b5b5b20cdbce71a129fcef)
- [BT_MCS_GROUP_OBJECT_TRACK_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gab6f895d3001c6e896c0d9aa9fb11bbc1)
- [BT_MCS_GROUP_OBJECT_GROUP_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gad7a15680dcf289dfe68b3d8c5f8c9d91)

<a id="header-details"></a>

---

[上一章](P005_zephyr__dt-bindings__clock__ifx_clock_source_common.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__bluetooth__audio__media_proxy.h_文件参考.md)
