---
id: learning.zephyr-docs.api-media-cellular-topic-reference.page-6
title: 媒体控制服务（Media Control Service，MCS）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_媒体控制服务（Media Control Service，MCS）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

媒体控制服务（Media Control Service，MCS）

<a id="details"></a>

媒体控制服务（Media Control Service，MCS）。自 3.0 引入，版本 0.8.0。与《媒体控制服务》和《媒体控制配置文件》（Media Control Profile）规范相关的定义和类型。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.1\_宏定义（Macros）

<a id="r_gab0c40404b2cd37d0a729504aa270e697"></a>

```c
#define BT_MCS_ERR_LONG_VAL_CHANGED 0x80U
```

相关声明：[BT_MCS_ERR_LONG_VAL_CHANGED](#gab0c40404b2cd37d0a729504aa270e697)。

读取长特征值子过程（Read Long Value Characteristic Sub-procedure）进行期间，某个特征值发生了变化。

<a id="r_ga4ae0b32e4192ba36b3ad4d6d8354929a"></a>

```c
#define BT_MCS_OPCODES_SUPPORTED_LEN 4U
```

相关声明：[BT_MCS_OPCODES_SUPPORTED_LEN](#ga4ae0b32e4192ba36b3ad4d6d8354929a)。

媒体控制点（Media Control Point）支持的操作码字段长度。

<a id="r_gaff47bc210fdd2d4d80a0ce822ca29a67"></a>

```c
#define SEARCH_LEN_MIN 2U
```

相关声明：[SEARCH_LEN_MIN](#gaff47bc210fdd2d4d80a0ce822ca29a67)。

搜索控制点（Search Control Point）最小长度。

<a id="r_gaf771b17acd202a20450b6ea939ddee3b"></a>

```c
#define SEARCH_LEN_MAX 64U
```

相关声明：[SEARCH_LEN_MAX](#gaf771b17acd202a20450b6ea939ddee3b)。

搜索控制点（Search Control Point）最大长度。

<a id="r_gab1fad64b6a1edfefce90cd4692576a5d"></a>

```c
#define SEARCH_SCI_LEN_MIN
```

相关声明：[SEARCH_SCI_LEN_MIN](#gab1fad64b6a1edfefce90cd4692576a5d)。

搜索控制点项（Search Control Point Item，SCI）最小长度。

<a id="r_ga81665fd87487cbaf1c0f90f1e0b2126a"></a>

```c
#define SEARCH_PARAM_MAX 62U
```

相关声明：[SEARCH_PARAM_MAX](#ga81665fd87487cbaf1c0f90f1e0b2126a)。

搜索参数（Search Parameters）最大长度。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 6.2\_播放速度（Playback speeds）

播放速度（Playback Speed）s 由 2 的 p/64 次幂计算，即 `s = 2^(p/64)`。

允许 -128 到 127 的所有值，这里只定义部分示例。

<a id="r_ga5d450ac222a491b7d544cc4d3f3ffcf0"></a>

```c
#define BT_MCS_PLAYBACK_SPEED_MIN -128
```

相关声明：[BT_MCS_PLAYBACK_SPEED_MIN](#ga5d450ac222a491b7d544cc4d3f3ffcf0)。

最低播放速度（Minimum Playback Speed），对应 25% 速度。

<a id="r_ga90e55b0230a11f752b111750e94ace4c"></a>

```c
#define BT_MCS_PLAYBACK_SPEED_QUARTER -128
```

相关声明：[BT_MCS_PLAYBACK_SPEED_QUARTER](#ga90e55b0230a11f752b111750e94ace4c)。

四分之一播放速度（Quarter Playback Speed），对应 25% 速度。

<a id="r_ga3bff45add6fbf602ad6bb07b0e64b335"></a>

```c
#define BT_MCS_PLAYBACK_SPEED_HALF -64
```

相关声明：[BT_MCS_PLAYBACK_SPEED_HALF](#ga3bff45add6fbf602ad6bb07b0e64b335)。

半速播放（Half Playback Speed），对应 50% 速度。

<a id="r_ga68c0eaa632ca581a1ab5ab144b3d7693"></a>

```c
#define BT_MCS_PLAYBACK_SPEED_UNITY 0
```

相关声明：[BT_MCS_PLAYBACK_SPEED_UNITY](#ga68c0eaa632ca581a1ab5ab144b3d7693)。

一倍播放速度（Unity Playback Speed），对应 100% 速度。

<a id="r_ga05ec8bf9ae813c8a3755b1383030bdf0"></a>

```c
#define BT_MCS_PLAYBACK_SPEED_DOUBLE 64
```

相关声明：[BT_MCS_PLAYBACK_SPEED_DOUBLE](#ga05ec8bf9ae813c8a3755b1383030bdf0)。

双倍播放速度（Double Playback Speed），对应 200% 速度。

<a id="r_gaa3299c597471a809033ec45b2c6f5b3d"></a>

```c
#define BT_MCS_PLAYBACK_SPEED_MAX 127
```

相关声明：[BT_MCS_PLAYBACK_SPEED_MAX](#gaa3299c597471a809033ec45b2c6f5b3d)。

最高播放速度（Max Playback Speed），对应 395.7% 速度，接近 400%。

## 6.3\_搜寻速度（Seeking speed）

搜寻速度（Seeking Speed）的允许值为 -64 到 -4（含端点）、0，以及 4 到 64（含端点）。

<a id="r_ga22c0b457d8c6e9ec119fff38205786d3"></a>

```c
#define BT_MCS_SEEKING_SPEED_FACTOR_MAX 64
```

相关声明：[BT_MCS_SEEKING_SPEED_FACTOR_MAX](#ga22c0b457d8c6e9ec119fff38205786d3)。

最大搜寻速度（Maximum Seeking Speed），可取负值。

<a id="r_gaf912dcbc70c81a023f8b93a4d4b0e745"></a>

```c
#define BT_MCS_SEEKING_SPEED_FACTOR_MIN 4
```

相关声明：[BT_MCS_SEEKING_SPEED_FACTOR_MIN](#gaf912dcbc70c81a023f8b93a4d4b0e745)。

最小搜寻速度（Minimum Seeking Speed），可取负值。

<a id="r_ga16bdf755d07c99895fa8698f9bd637a0"></a>

```c
#define BT_MCS_SEEKING_SPEED_FACTOR_ZERO 0
```

相关声明：[BT_MCS_SEEKING_SPEED_FACTOR_ZERO](#ga16bdf755d07c99895fa8698f9bd637a0)。

不搜寻（No Seeking）。

## 6.4\_播放顺序（Playing orders）

<a id="r_ga1c25a91795472a553286def379fe943b"></a>

```c
#define BT_MCS_PLAYING_ORDER_SINGLE_ONCE 0x01U
```

相关声明：[BT_MCS_PLAYING_ORDER_SINGLE_ONCE](#ga1c25a91795472a553286def379fe943b)。

单个音轨（Track）播放一次，没有下一音轨。

<a id="r_ga4698529b5268ff1c5099f4cc9d8e9966"></a>

```c
#define BT_MCS_PLAYING_ORDER_SINGLE_REPEAT 0x02U
```

相关声明：[BT_MCS_PLAYING_ORDER_SINGLE_REPEAT](#ga4698529b5268ff1c5099f4cc9d8e9966)。

重复播放单个音轨（Track），下一音轨就是当前音轨。

<a id="r_ga8b8023d46c3ce402a07c9146494ada60"></a>

```c
#define BT_MCS_PLAYING_ORDER_INORDER_ONCE 0x03U
```

相关声明：[BT_MCS_PLAYING_ORDER_INORDER_ONCE](#ga8b8023d46c3ce402a07c9146494ada60)。

按音轨顺序（Track Order）将组内音轨播放一次。

<a id="r_gaaccf440eb5df01eaa0a255e09cf7b996"></a>

```c
#define BT_MCS_PLAYING_ORDER_INORDER_REPEAT 0x04U
```

相关声明：[BT_MCS_PLAYING_ORDER_INORDER_REPEAT](#gaaccf440eb5df01eaa0a255e09cf7b996)。

按音轨顺序（Track Order）重复播放组内音轨。

<a id="r_ga260b73c14b35ee596cacca082b5dc865"></a>

```c
#define BT_MCS_PLAYING_ORDER_OLDEST_ONCE 0x05U
```

相关声明：[BT_MCS_PLAYING_ORDER_OLDEST_ONCE](#ga260b73c14b35ee596cacca082b5dc865)。

从最旧音轨开始，将组内音轨播放一次（Oldest First）。

<a id="r_ga2fb92d553aed2f680321db68ef28035f"></a>

```c
#define BT_MCS_PLAYING_ORDER_OLDEST_REPEAT 0x06U
```

相关声明：[BT_MCS_PLAYING_ORDER_OLDEST_REPEAT](#ga2fb92d553aed2f680321db68ef28035f)。

从最旧音轨开始，重复播放组内音轨（Oldest First）。

<a id="r_gaaa06525a5d53d4bf2312304208dda311"></a>

```c
#define BT_MCS_PLAYING_ORDER_NEWEST_ONCE 0x07U
```

相关声明：[BT_MCS_PLAYING_ORDER_NEWEST_ONCE](#gaaa06525a5d53d4bf2312304208dda311)。

从最新音轨开始，将组内音轨播放一次（Newest First）。

<a id="r_ga28a19c78f96b51f0e048395eb4378d61"></a>

```c
#define BT_MCS_PLAYING_ORDER_NEWEST_REPEAT 0x08U
```

相关声明：[BT_MCS_PLAYING_ORDER_NEWEST_REPEAT](#ga28a19c78f96b51f0e048395eb4378d61)。

从最新音轨开始，重复播放组内音轨（Newest First）。

<a id="r_gaa33a02e34f65021b1b7290edc76b166e"></a>

```c
#define BT_MCS_PLAYING_ORDER_SHUFFLE_ONCE 0x09U
```

相关声明：[BT_MCS_PLAYING_ORDER_SHUFFLE_ONCE](#gaa33a02e34f65021b1b7290edc76b166e)。

以随机顺序（Random Order）将组内音轨播放一次。

<a id="r_gaa231c007f0448a5ba3bd61e8528c5b1e"></a>

```c
#define BT_MCS_PLAYING_ORDER_SHUFFLE_REPEAT 0x0AU
```

相关声明：[BT_MCS_PLAYING_ORDER_SHUFFLE_REPEAT](#gaa231c007f0448a5ba3bd61e8528c5b1e)。

以随机顺序（Random Order）重复播放组内音轨。

## 6.5\_支持的播放顺序（Playing orders supported）

位图（Bitmap），其顺序与上文的播放顺序相同。

注意，播放顺序（Playing Order）1 对应位 0，依此类推。

<a id="r_ga7102f1909baea2320827ea6b47522bd8"></a>

```c
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_SINGLE_ONCE BIT(0U)
```

相关声明：[BT_MCS_PLAYING_ORDERS_SUPPORTED_SINGLE_ONCE](#ga7102f1909baea2320827ea6b47522bd8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

单个音轨（Track）播放一次，没有下一音轨。

<a id="r_gafecb7edde06dfb97939af93034690cbc"></a>

```c
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_SINGLE_REPEAT BIT(1U)
```

相关声明：[BT_MCS_PLAYING_ORDERS_SUPPORTED_SINGLE_REPEAT](#gafecb7edde06dfb97939af93034690cbc)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

重复播放单个音轨（Track），下一音轨就是当前音轨。

<a id="r_ga594daa869c6696a4cdd961f8786134a6"></a>

```c
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_INORDER_ONCE BIT(2U)
```

相关声明：[BT_MCS_PLAYING_ORDERS_SUPPORTED_INORDER_ONCE](#ga594daa869c6696a4cdd961f8786134a6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

按音轨顺序（Track Order）将组内音轨播放一次。

<a id="r_gac4bcd9b84e28a47dd23d073dd942a9c8"></a>

```c
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_INORDER_REPEAT BIT(3U)
```

相关声明：[BT_MCS_PLAYING_ORDERS_SUPPORTED_INORDER_REPEAT](#gac4bcd9b84e28a47dd23d073dd942a9c8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

按音轨顺序（Track Order）重复播放组内音轨。

<a id="r_gae1d8c34c8f9ea9fadc4da56d0d127712"></a>

```c
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_OLDEST_ONCE BIT(4U)
```

相关声明：[BT_MCS_PLAYING_ORDERS_SUPPORTED_OLDEST_ONCE](#gae1d8c34c8f9ea9fadc4da56d0d127712)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

从最旧音轨开始，将组内音轨播放一次（Oldest First）。

<a id="r_ga38bb3aa9a388fa3ae0230cb78cf2d3a5"></a>

```c
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_OLDEST_REPEAT BIT(5U)
```

相关声明：[BT_MCS_PLAYING_ORDERS_SUPPORTED_OLDEST_REPEAT](#ga38bb3aa9a388fa3ae0230cb78cf2d3a5)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

从最旧音轨开始，重复播放组内音轨（Oldest First）。

<a id="r_gabd77af4da60d1b7531d35bd543cb4df2"></a>

```c
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_NEWEST_ONCE BIT(6U)
```

相关声明：[BT_MCS_PLAYING_ORDERS_SUPPORTED_NEWEST_ONCE](#gabd77af4da60d1b7531d35bd543cb4df2)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

从最新音轨开始，将组内音轨播放一次（Newest First）。

<a id="r_ga9bb22c2c7d08032ab1d5c3ae64ce01a8"></a>

```c
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_NEWEST_REPEAT BIT(7U)
```

相关声明：[BT_MCS_PLAYING_ORDERS_SUPPORTED_NEWEST_REPEAT](#ga9bb22c2c7d08032ab1d5c3ae64ce01a8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

从最新音轨开始，重复播放组内音轨（Newest First）。

<a id="r_ga2c245ad4f76937b366770aa7afe7b684"></a>

```c
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_SHUFFLE_ONCE BIT(8U)
```

相关声明：[BT_MCS_PLAYING_ORDERS_SUPPORTED_SHUFFLE_ONCE](#ga2c245ad4f76937b366770aa7afe7b684)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

以随机顺序（Random Order）将组内音轨播放一次。

<a id="r_gae5d972a834c1b568f39df91df0febb81"></a>

```c
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_SHUFFLE_REPEAT BIT(9U)
```

相关声明：[BT_MCS_PLAYING_ORDERS_SUPPORTED_SHUFFLE_REPEAT](#gae5d972a834c1b568f39df91df0febb81)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

以随机顺序（Random Order）重复播放组内音轨。

## 6.6\_媒体状态（Media states）

<a id="r_gaa9c7d92a8aa79b1020c8b593b0edc088"></a>

```c
#define BT_MCS_MEDIA_STATE_INACTIVE 0x00U
```

相关声明：[BT_MCS_MEDIA_STATE_INACTIVE](#gaa9c7d92a8aa79b1020c8b593b0edc088)。

当前音轨无效，且未选择任何音轨（Track）。

<a id="r_gaa33b1ba9ebfd0d226df869cdc35e964c"></a>

```c
#define BT_MCS_MEDIA_STATE_PLAYING 0x01U
```

相关声明：[BT_MCS_MEDIA_STATE_PLAYING](#gaa33b1ba9ebfd0d226df869cdc35e964c)。

媒体播放器（Media Player）正在播放当前音轨。

<a id="r_gaa5a2768a288fe8058818b5f965c0d8b3"></a>

```c
#define BT_MCS_MEDIA_STATE_PAUSED 0x02U
```

相关声明：[BT_MCS_MEDIA_STATE_PAUSED](#gaa5a2768a288fe8058818b5f965c0d8b3)。

当前音轨已暂停（Paused）。

<a id="r_ga689e83131b6db63fa3a76f428a93714b"></a>

```c
#define BT_MCS_MEDIA_STATE_SEEKING 0x03U
```

相关声明：[BT_MCS_MEDIA_STATE_SEEKING](#ga689e83131b6db63fa3a76f428a93714b)。

当前音轨正在快进或快退（Fast Forwarding / Fast Rewinding）。

## 6.7\_媒体控制点操作码（Media control point opcodes）

<a id="r_ga79c4cf8292a4548bc7b9b06b1ce0f60a"></a>

```c
#define BT_MCS_OPC_PLAY 0x01U
```

相关声明：[BT_MCS_OPC_PLAY](#ga79c4cf8292a4548bc7b9b06b1ce0f60a)。

开始播放当前音轨（Track）。

<a id="r_ga8b15cb7a8a1429f83e8d1619c37becc6"></a>

```c
#define BT_MCS_OPC_PAUSE 0x02U
```

相关声明：[BT_MCS_OPC_PAUSE](#ga8b15cb7a8a1429f83e8d1619c37becc6)。

暂停播放当前音轨（Track）。

<a id="r_ga6d49190bae54e66695ea3c856d558049"></a>

```c
#define BT_MCS_OPC_FAST_REWIND 0x03U
```

相关声明：[BT_MCS_OPC_FAST_REWIND](#ga6d49190bae54e66695ea3c856d558049)。

快退（Fast Rewind）当前音轨。

<a id="r_ga9ce0d00b1cfc0d3a33762aaed3c1bb75"></a>

```c
#define BT_MCS_OPC_FAST_FORWARD 0x04U
```

相关声明：[BT_MCS_OPC_FAST_FORWARD](#ga9ce0d00b1cfc0d3a33762aaed3c1bb75)。

快进（Fast Forward）当前音轨。

<a id="r_gade874bf59dc08ddb682280b644821e11"></a>

```c
#define BT_MCS_OPC_STOP 0x05U
```

相关声明：[BT_MCS_OPC_STOP](#gade874bf59dc08ddb682280b644821e11)。

停止当前活动，回到暂停状态（Paused State），并将当前音轨位置设为当前音轨起点。

<a id="r_gada25cc85988f5988887eab0cf66e4190"></a>

```c
#define BT_MCS_OPC_MOVE_RELATIVE 0x10U
```

相关声明：[BT_MCS_OPC_MOVE_RELATIVE](#gada25cc85988f5988887eab0cf66e4190)。

相对于当前音轨位置（Current Track Position），设置新的当前位置。

<a id="r_ga454775706fe60ccd12e5ab44e6ddacba"></a>

```c
#define BT_MCS_OPC_PREV_SEGMENT 0x20U
```

相关声明：[BT_MCS_OPC_PREV_SEGMENT](#ga454775706fe60ccd12e5ab44e6ddacba)。

将当前音轨位置设为当前音轨上一段（Previous Segment）的起始位置。

<a id="r_ga9cc7b813b933b56b1f60ef0ddf8e39df"></a>

```c
#define BT_MCS_OPC_NEXT_SEGMENT 0x21U
```

相关声明：[BT_MCS_OPC_NEXT_SEGMENT](#ga9cc7b813b933b56b1f60ef0ddf8e39df)。

将当前音轨位置设为当前音轨下一段（Next Segment）的起始位置。

<a id="r_ga6148011e40389bbed998a971f44f834a"></a>

```c
#define BT_MCS_OPC_FIRST_SEGMENT 0x22U
```

相关声明：[BT_MCS_OPC_FIRST_SEGMENT](#ga6148011e40389bbed998a971f44f834a)。

将当前音轨位置设为当前音轨第一段（First Segment）的起始位置。

<a id="r_ga08421e4d26d54fe3d40edeb08fd44aac"></a>

```c
#define BT_MCS_OPC_LAST_SEGMENT 0x23U
```

相关声明：[BT_MCS_OPC_LAST_SEGMENT](#ga08421e4d26d54fe3d40edeb08fd44aac)。

将当前音轨位置设为当前音轨最后一段（Last Segment）的起始位置。

<a id="r_ga4b91b6e3e3f92619d45ecc2066e97e74"></a>

```c
#define BT_MCS_OPC_GOTO_SEGMENT 0x24U
```

相关声明：[BT_MCS_OPC_GOTO_SEGMENT](#ga4b91b6e3e3f92619d45ecc2066e97e74)。

将当前音轨位置设为当前音轨第 n 段（Nth Segment）的起始位置。

<a id="r_ga88e09cd634c2dd3068f746cc978c1568"></a>

```c
#define BT_MCS_OPC_PREV_TRACK 0x30U
```

相关声明：[BT_MCS_OPC_PREV_TRACK](#ga88e09cd634c2dd3068f746cc978c1568)。

按播放顺序（Playing Order）将当前音轨设为上一音轨。

<a id="r_ga06df0d77c7a678ca8f4f01ec64c88de7"></a>

```c
#define BT_MCS_OPC_NEXT_TRACK 0x31U
```

相关声明：[BT_MCS_OPC_NEXT_TRACK](#ga06df0d77c7a678ca8f4f01ec64c88de7)。

按播放顺序（Playing Order）将当前音轨设为下一音轨。

<a id="r_gaed893751ae2ceae3a1d5c764b9411ecc"></a>

```c
#define BT_MCS_OPC_FIRST_TRACK 0x32U
```

相关声明：[BT_MCS_OPC_FIRST_TRACK](#gaed893751ae2ceae3a1d5c764b9411ecc)。

按播放顺序（Playing Order）将当前音轨设为第一音轨。

<a id="r_gacd2e15226d20eb65962d6441c2b7d565"></a>

```c
#define BT_MCS_OPC_LAST_TRACK 0x33U
```

相关声明：[BT_MCS_OPC_LAST_TRACK](#gacd2e15226d20eb65962d6441c2b7d565)。

按播放顺序（Playing Order）将当前音轨设为最后一音轨。

<a id="r_ga4d5124b9ffc125e31c45c06a12fcc85c"></a>

```c
#define BT_MCS_OPC_GOTO_TRACK 0x34U
```

相关声明：[BT_MCS_OPC_GOTO_TRACK](#ga4d5124b9ffc125e31c45c06a12fcc85c)。

按播放顺序（Playing Order）将当前音轨设为第 n 个音轨。

<a id="r_gab7efc1fb17cc53c376f6f84bf31ef85c"></a>

```c
#define BT_MCS_OPC_PREV_GROUP 0x40U
```

相关声明：[BT_MCS_OPC_PREV_GROUP](#gab7efc1fb17cc53c376f6f84bf31ef85c)。

将当前组设为组序列（Sequence of Groups）中的上一组。

<a id="r_ga4feb6b16975ae123bc77c08509e0c809"></a>

```c
#define BT_MCS_OPC_NEXT_GROUP 0x41U
```

相关声明：[BT_MCS_OPC_NEXT_GROUP](#ga4feb6b16975ae123bc77c08509e0c809)。

将当前组设为组序列（Sequence of Groups）中的下一组。

<a id="r_ga0b6075379c9abf0911c8a1f2b8d11923"></a>

```c
#define BT_MCS_OPC_FIRST_GROUP 0x42U
```

相关声明：[BT_MCS_OPC_FIRST_GROUP](#ga0b6075379c9abf0911c8a1f2b8d11923)。

将当前组设为组序列（Sequence of Groups）中的第一组。

<a id="r_gad234093556575ac31985944a483597e8"></a>

```c
#define BT_MCS_OPC_LAST_GROUP 0x43U
```

相关声明：[BT_MCS_OPC_LAST_GROUP](#gad234093556575ac31985944a483597e8)。

将当前组设为组序列（Sequence of Groups）中的最后一组。

<a id="r_ga1911ae5e1285041a77bbd1db773c33b5"></a>

```c
#define BT_MCS_OPC_GOTO_GROUP 0x44U
```

相关声明：[BT_MCS_OPC_GOTO_GROUP](#ga1911ae5e1285041a77bbd1db773c33b5)。

将当前组设为组序列（Sequence of Groups）中的第 n 组。

## 6.8\_媒体控制点支持的操作码值（Media control point supported opcodes values）

<a id="r_ga82d1bbc5cd67ab30960bca6992116a8f"></a>

```c
#define BT_MCS_OPC_SUP_PLAY BIT(0U)
```

相关声明：[BT_MCS_OPC_SUP_PLAY](#ga82d1bbc5cd67ab30960bca6992116a8f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持播放操作码（Play Opcode）。

<a id="r_gabdca574666b964d506d96e01562875f4"></a>

```c
#define BT_MCS_OPC_SUP_PAUSE BIT(1U)
```

相关声明：[BT_MCS_OPC_SUP_PAUSE](#gabdca574666b964d506d96e01562875f4)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持暂停操作码（Pause Opcode）。

<a id="r_gaaa3b553dc8eb2de610b545f1ce88b067"></a>

```c
#define BT_MCS_OPC_SUP_FAST_REWIND BIT(2U)
```

相关声明：[BT_MCS_OPC_SUP_FAST_REWIND](#gaaa3b553dc8eb2de610b545f1ce88b067)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持快退操作码（Fast Rewind Opcode）。

<a id="r_gaa24785ccc713cb2421a55ff48f5f2c45"></a>

```c
#define BT_MCS_OPC_SUP_FAST_FORWARD BIT(3U)
```

相关声明：[BT_MCS_OPC_SUP_FAST_FORWARD](#gaa24785ccc713cb2421a55ff48f5f2c45)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持快进操作码（Fast Forward Opcode）。

<a id="r_gaec507c502c53413e510cc30f179befec"></a>

```c
#define BT_MCS_OPC_SUP_STOP BIT(4U)
```

相关声明：[BT_MCS_OPC_SUP_STOP](#gaec507c502c53413e510cc30f179befec)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持停止操作码（Stop Opcode）。

<a id="r_ga3024e1b5a5175d2f45cdc7650bb9f66a"></a>

```c
#define BT_MCS_OPC_SUP_MOVE_RELATIVE BIT(5U)
```

相关声明：[BT_MCS_OPC_SUP_MOVE_RELATIVE](#ga3024e1b5a5175d2f45cdc7650bb9f66a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持相对移动操作码（Move Relative Opcode）。

<a id="r_gae074d9404aa5c8722678d6805fb7636d"></a>

```c
#define BT_MCS_OPC_SUP_PREV_SEGMENT BIT(6U)
```

相关声明：[BT_MCS_OPC_SUP_PREV_SEGMENT](#gae074d9404aa5c8722678d6805fb7636d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持上一段操作码（Previous Segment Opcode）。

<a id="r_ga416c45a7a2ac8c744c42c19a454d6363"></a>

```c
#define BT_MCS_OPC_SUP_NEXT_SEGMENT BIT(7U)
```

相关声明：[BT_MCS_OPC_SUP_NEXT_SEGMENT](#ga416c45a7a2ac8c744c42c19a454d6363)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持下一段操作码（Next Segment Opcode）。

<a id="r_ga5434b6409f4300cd86df1f75cb699ad8"></a>

```c
#define BT_MCS_OPC_SUP_FIRST_SEGMENT BIT(8U)
```

相关声明：[BT_MCS_OPC_SUP_FIRST_SEGMENT](#ga5434b6409f4300cd86df1f75cb699ad8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持第一段操作码（First Segment Opcode）。

<a id="r_ga9c4e53c88ea8ea9eb056e9ff37b58dd1"></a>

```c
#define BT_MCS_OPC_SUP_LAST_SEGMENT BIT(9U)
```

相关声明：[BT_MCS_OPC_SUP_LAST_SEGMENT](#ga9c4e53c88ea8ea9eb056e9ff37b58dd1)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持最后一段操作码（Last Segment Opcode）。

<a id="r_ga9c576ae9a0ad2200a4b29059e88c6c28"></a>

```c
#define BT_MCS_OPC_SUP_GOTO_SEGMENT BIT(10U)
```

相关声明：[BT_MCS_OPC_SUP_GOTO_SEGMENT](#ga9c576ae9a0ad2200a4b29059e88c6c28)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持转到指定段操作码（Goto Segment Opcode）。

<a id="r_ga59794af43d1b78a1f1a52fb48769be9c"></a>

```c
#define BT_MCS_OPC_SUP_PREV_TRACK BIT(11U)
```

相关声明：[BT_MCS_OPC_SUP_PREV_TRACK](#ga59794af43d1b78a1f1a52fb48769be9c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持上一音轨操作码（Previous Track Opcode）。

<a id="r_gae213edc6b714f0a1adc744e8ff779ee6"></a>

```c
#define BT_MCS_OPC_SUP_NEXT_TRACK BIT(12U)
```

相关声明：[BT_MCS_OPC_SUP_NEXT_TRACK](#gae213edc6b714f0a1adc744e8ff779ee6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持下一音轨操作码（Next Track Opcode）。

<a id="r_ga7d79bde3dbc9044667fa2bc54cc7cec4"></a>

```c
#define BT_MCS_OPC_SUP_FIRST_TRACK BIT(13U)
```

相关声明：[BT_MCS_OPC_SUP_FIRST_TRACK](#ga7d79bde3dbc9044667fa2bc54cc7cec4)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持第一音轨操作码（First Track Opcode）。

<a id="r_ga8752a8b6ee27919025bb3e5fb4a77c46"></a>

```c
#define BT_MCS_OPC_SUP_LAST_TRACK BIT(14U)
```

相关声明：[BT_MCS_OPC_SUP_LAST_TRACK](#ga8752a8b6ee27919025bb3e5fb4a77c46)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持最后音轨操作码（Last Track Opcode）。

<a id="r_gaf8573ac7d802252076ef759575baef2f"></a>

```c
#define BT_MCS_OPC_SUP_GOTO_TRACK BIT(15U)
```

相关声明：[BT_MCS_OPC_SUP_GOTO_TRACK](#gaf8573ac7d802252076ef759575baef2f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持转到指定音轨操作码（Goto Track Opcode）。

<a id="r_ga4443a0f87750c537a6a39544bbf63111"></a>

```c
#define BT_MCS_OPC_SUP_PREV_GROUP BIT(16U)
```

相关声明：[BT_MCS_OPC_SUP_PREV_GROUP](#ga4443a0f87750c537a6a39544bbf63111)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持上一组操作码（Previous Group Opcode）。

<a id="r_gaeeeff1f344202619794af0de0cda199b"></a>

```c
#define BT_MCS_OPC_SUP_NEXT_GROUP BIT(17U)
```

相关声明：[BT_MCS_OPC_SUP_NEXT_GROUP](#gaeeeff1f344202619794af0de0cda199b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持下一组操作码（Next Group Opcode）。

<a id="r_ga57508e39d5a32ebefb0b103f805ec047"></a>

```c
#define BT_MCS_OPC_SUP_FIRST_GROUP BIT(18U)
```

相关声明：[BT_MCS_OPC_SUP_FIRST_GROUP](#ga57508e39d5a32ebefb0b103f805ec047)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持第一组操作码（First Group Opcode）。

<a id="r_ga80bf605e90dee5841d14fdbb9b39f96a"></a>

```c
#define BT_MCS_OPC_SUP_LAST_GROUP BIT(19U)
```

相关声明：[BT_MCS_OPC_SUP_LAST_GROUP](#ga80bf605e90dee5841d14fdbb9b39f96a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持最后一组操作码（Last Group Opcode）。

<a id="r_ga158df3fd1ae39fc3405e25ba7d056d80"></a>

```c
#define BT_MCS_OPC_SUP_GOTO_GROUP BIT(20U)
```

相关声明：[BT_MCS_OPC_SUP_GOTO_GROUP](#ga158df3fd1ae39fc3405e25ba7d056d80)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持转到指定组操作码（Goto Group Opcode）。

## 6.9\_媒体控制点通知结果码（Media control point notification result codes）

<a id="r_ga7507062e3fe2df221cd47546713a0d28"></a>

```c
#define BT_MCS_OPC_NTF_SUCCESS 0x01U
```

相关声明：[BT_MCS_OPC_NTF_SUCCESS](#ga7507062e3fe2df221cd47546713a0d28)。

写入操作码（Opcode Write）所请求的动作已成功完成。

<a id="r_ga72e92f172f03a64d2d4641bcdbdb614f"></a>

```c
#define BT_MCS_OPC_NTF_NOT_SUPPORTED 0x02U
```

相关声明：[BT_MCS_OPC_NTF_NOT_SUPPORTED](#ga72e92f172f03a64d2d4641bcdbdb614f)。

写入媒体控制点（Media Control Point）时使用了无效或不支持的操作码。

<a id="r_ga740d7278a770b215ae185441fb43c85b"></a>

```c
#define BT_MCS_OPC_NTF_PLAYER_INACTIVE 0x03U
```

相关声明：[BT_MCS_OPC_NTF_PLAYER_INACTIVE](#ga740d7278a770b215ae185441fb43c85b)。

收到操作码时，媒体播放器状态（Media Player State）特征值为非活动（Inactive）；或执行该操作码所请求动作的结果，使该特征值变为 Inactive。

<a id="r_gafe5d0665ae8b33428bce16c427eabcc1"></a>

```c
#define BT_MCS_OPC_NTF_CANNOT_BE_COMPLETED 0x04U
```

相关声明：[BT_MCS_OPC_NTF_CANNOT_BE_COMPLETED](#gafe5d0665ae8b33428bce16c427eabcc1)。

由于播放器内部的某种条件，无法成功完成任何媒体控制点写入（Media Control Point Write）所请求的动作。

## 6.10\_搜索控制点类型值（Search control point type values）

参考：《媒体控制服务规范》（Media Control Service Specification）v1.0 第 3.20.2 节。

<a id="r_ga5a53ce79494a2ec935a43e2cabb6496c"></a>

```c
#define BT_MCS_SEARCH_TYPE_TRACK_NAME 0x01U
```

相关声明：[BT_MCS_SEARCH_TYPE_TRACK_NAME](#ga5a53ce79494a2ec935a43e2cabb6496c)。

按音轨名称（Track Name）搜索。

<a id="r_ga3bbf3a3393fa08a8f797e7e286f4b06f"></a>

```c
#define BT_MCS_SEARCH_TYPE_ARTIST_NAME 0x02U
```

相关声明：[BT_MCS_SEARCH_TYPE_ARTIST_NAME](#ga3bbf3a3393fa08a8f797e7e286f4b06f)。

按艺人名称（Artist Name）搜索。

<a id="r_gade2b66ace813a9bf91b497fbc1dfb885"></a>

```c
#define BT_MCS_SEARCH_TYPE_ALBUM_NAME 0x03U
```

相关声明：[BT_MCS_SEARCH_TYPE_ALBUM_NAME](#gade2b66ace813a9bf91b497fbc1dfb885)。

按专辑名称（Album Name）搜索。

<a id="r_gaf98145eae298cca9e3df1dbcca9118a7"></a>

```c
#define BT_MCS_SEARCH_TYPE_GROUP_NAME 0x04U
```

相关声明：[BT_MCS_SEARCH_TYPE_GROUP_NAME](#gaf98145eae298cca9e3df1dbcca9118a7)。

按组名称（Group Name）搜索。

<a id="r_ga2befe4b4b22125a9e24ab4af6eb08f95"></a>

```c
#define BT_MCS_SEARCH_TYPE_EARLIEST_YEAR 0x05U
```

相关声明：[BT_MCS_SEARCH_TYPE_EARLIEST_YEAR](#ga2befe4b4b22125a9e24ab4af6eb08f95)。

按最早年份（Earliest Year）搜索。

<a id="r_gad120d8a4f7130762568b7c6f87a34cd4"></a>

```c
#define BT_MCS_SEARCH_TYPE_LATEST_YEAR 0x06U
```

相关声明：[BT_MCS_SEARCH_TYPE_LATEST_YEAR](#gad120d8a4f7130762568b7c6f87a34cd4)。

按最晚年份（Latest Year）搜索。

<a id="r_gae4d30046fb1f4d6ffc554fdd95946bf0"></a>

```c
#define BT_MCS_SEARCH_TYPE_GENRE 0x07U
```

相关声明：[BT_MCS_SEARCH_TYPE_GENRE](#gae4d30046fb1f4d6ffc554fdd95946bf0)。

按流派（Genre）搜索。

<a id="r_gaa99d74ce6f523185a3522f257647edce"></a>

```c
#define BT_MCS_SEARCH_TYPE_ONLY_TRACKS 0x08U
```

相关声明：[BT_MCS_SEARCH_TYPE_ONLY_TRACKS](#gaa99d74ce6f523185a3522f257647edce)。

仅搜索音轨（Tracks）。

<a id="r_gab6f6fb41e61f5b4c257e36cba71f98a2"></a>

```c
#define BT_MCS_SEARCH_TYPE_ONLY_GROUPS 0x09U
```

相关声明：[BT_MCS_SEARCH_TYPE_ONLY_GROUPS](#gab6f6fb41e61f5b4c257e36cba71f98a2)。

仅搜索组（Groups）。

## 6.11\_搜索通知结果码（Search notification result codes）

参考：《媒体控制服务规范》（Media Control Service Specification）v1.0 第 3.20.2 节。

<a id="r_gaa292c3bb4b5eeb62d5e8e6cb72e69908"></a>

```c
#define BT_MCS_SCP_NTF_SUCCESS 0x01U
```

相关声明：[BT_MCS_SCP_NTF_SUCCESS](#gaa292c3bb4b5eeb62d5e8e6cb72e69908)。

搜索请求（Search Request）已接受，搜索已开始。

<a id="r_ga0a7769ba43b5b5b20cdbce71a129fcef"></a>

```c
#define BT_MCS_SCP_NTF_FAILURE 0x02U
```

相关声明：[BT_MCS_SCP_NTF_FAILURE](#ga0a7769ba43b5b5b20cdbce71a129fcef)。

搜索请求（Search Request）无效，未开始搜索。

## 6.12\_组对象的对象类型（Group object object types）

参考：《媒体控制服务规范》（Media Control Service Specification）v1.0 第 4.4.1 节。

<a id="r_gab6f895d3001c6e896c0d9aa9fb11bbc1"></a>

```c
#define BT_MCS_GROUP_OBJECT_TRACK_TYPE 0x00U
```

相关声明：[BT_MCS_GROUP_OBJECT_TRACK_TYPE](#gab6f895d3001c6e896c0d9aa9fb11bbc1)。

组对象类型（Group Object Type）为音轨（Track）。

<a id="r_gad7a15680dcf289dfe68b3d8c5f8c9d91"></a>

```c
#define BT_MCS_GROUP_OBJECT_GROUP_TYPE 0x01U
```

相关声明：[BT_MCS_GROUP_OBJECT_GROUP_TYPE](#gad7a15680dcf289dfe68b3d8c5f8c9d91)。

组对象类型（Group Object Type）为组（Group）。

## 6.13\_详细说明（Detailed Documentation）

<a id="gab0c40404b2cd37d0a729504aa270e697"></a>

### `BT_MCS_ERR_LONG_VAL_CHANGED`

```c
#define BT_MCS_ERR_LONG_VAL_CHANGED 0x80U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

读取长特征值子过程（Read Long Value Characteristic Sub-procedure）进行期间，某个特征值发生了变化。

<a id="gad7a15680dcf289dfe68b3d8c5f8c9d91"></a>

### `BT_MCS_GROUP_OBJECT_GROUP_TYPE`

```c
#define BT_MCS_GROUP_OBJECT_GROUP_TYPE 0x01U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

组对象类型（Group Object Type）为组（Group）。

<a id="gab6f895d3001c6e896c0d9aa9fb11bbc1"></a>

### `BT_MCS_GROUP_OBJECT_TRACK_TYPE`

```c
#define BT_MCS_GROUP_OBJECT_TRACK_TYPE 0x00U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

组对象类型（Group Object Type）为音轨（Track）。

<a id="gaa9c7d92a8aa79b1020c8b593b0edc088"></a>

### `BT_MCS_MEDIA_STATE_INACTIVE`

```c
#define BT_MCS_MEDIA_STATE_INACTIVE 0x00U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

当前音轨无效，且未选择任何音轨（Track）。

<a id="gaa5a2768a288fe8058818b5f965c0d8b3"></a>

### `BT_MCS_MEDIA_STATE_PAUSED`

```c
#define BT_MCS_MEDIA_STATE_PAUSED 0x02U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

当前音轨已暂停（Paused）。

媒体播放器（Media Player）有当前音轨，但未在播放。

<a id="gaa33b1ba9ebfd0d226df869cdc35e964c"></a>

### `BT_MCS_MEDIA_STATE_PLAYING`

```c
#define BT_MCS_MEDIA_STATE_PLAYING 0x01U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

媒体播放器（Media Player）正在播放当前音轨。

<a id="ga689e83131b6db63fa3a76f428a93714b"></a>

### `BT_MCS_MEDIA_STATE_SEEKING`

```c
#define BT_MCS_MEDIA_STATE_SEEKING 0x03U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

当前音轨正在快进或快退（Fast Forwarding / Fast Rewinding）。

<a id="ga9ce0d00b1cfc0d3a33762aaed3c1bb75"></a>

### `BT_MCS_OPC_FAST_FORWARD`

```c
#define BT_MCS_OPC_FAST_FORWARD 0x04U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

快进（Fast Forward）当前音轨。

<a id="ga6d49190bae54e66695ea3c856d558049"></a>

### `BT_MCS_OPC_FAST_REWIND`

```c
#define BT_MCS_OPC_FAST_REWIND 0x03U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

快退（Fast Rewind）当前音轨。

<a id="ga0b6075379c9abf0911c8a1f2b8d11923"></a>

### `BT_MCS_OPC_FIRST_GROUP`

```c
#define BT_MCS_OPC_FIRST_GROUP 0x42U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

将当前组设为组序列（Sequence of Groups）中的第一组。

<a id="ga6148011e40389bbed998a971f44f834a"></a>

### `BT_MCS_OPC_FIRST_SEGMENT`

```c
#define BT_MCS_OPC_FIRST_SEGMENT 0x22U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

将当前音轨位置设为当前音轨第一段（First Segment）的起始位置。

<a id="gaed893751ae2ceae3a1d5c764b9411ecc"></a>

### `BT_MCS_OPC_FIRST_TRACK`

```c
#define BT_MCS_OPC_FIRST_TRACK 0x32U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

按播放顺序（Playing Order）将当前音轨设为第一音轨。

<a id="ga1911ae5e1285041a77bbd1db773c33b5"></a>

### `BT_MCS_OPC_GOTO_GROUP`

```c
#define BT_MCS_OPC_GOTO_GROUP 0x44U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

将当前组设为组序列（Sequence of Groups）中的第 n 组。

<a id="ga4b91b6e3e3f92619d45ecc2066e97e74"></a>

### `BT_MCS_OPC_GOTO_SEGMENT`

```c
#define BT_MCS_OPC_GOTO_SEGMENT 0x24U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

将当前音轨位置设为当前音轨第 n 段（Nth Segment）的起始位置。

<a id="ga4d5124b9ffc125e31c45c06a12fcc85c"></a>

### `BT_MCS_OPC_GOTO_TRACK`

```c
#define BT_MCS_OPC_GOTO_TRACK 0x34U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

按播放顺序（Playing Order）将当前音轨设为第 n 个音轨。

<a id="gad234093556575ac31985944a483597e8"></a>

### `BT_MCS_OPC_LAST_GROUP`

```c
#define BT_MCS_OPC_LAST_GROUP 0x43U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

将当前组设为组序列（Sequence of Groups）中的最后一组。

<a id="ga08421e4d26d54fe3d40edeb08fd44aac"></a>

### `BT_MCS_OPC_LAST_SEGMENT`

```c
#define BT_MCS_OPC_LAST_SEGMENT 0x23U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

将当前音轨位置设为当前音轨最后一段（Last Segment）的起始位置。

<a id="gacd2e15226d20eb65962d6441c2b7d565"></a>

### `BT_MCS_OPC_LAST_TRACK`

```c
#define BT_MCS_OPC_LAST_TRACK 0x33U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

按播放顺序（Playing Order）将当前音轨设为最后一音轨。

<a id="gada25cc85988f5988887eab0cf66e4190"></a>

### `BT_MCS_OPC_MOVE_RELATIVE`

```c
#define BT_MCS_OPC_MOVE_RELATIVE 0x10U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

相对于当前音轨位置（Current Track Position），设置新的当前位置。

<a id="ga4feb6b16975ae123bc77c08509e0c809"></a>

### `BT_MCS_OPC_NEXT_GROUP`

```c
#define BT_MCS_OPC_NEXT_GROUP 0x41U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

将当前组设为组序列（Sequence of Groups）中的下一组。

<a id="ga9cc7b813b933b56b1f60ef0ddf8e39df"></a>

### `BT_MCS_OPC_NEXT_SEGMENT`

```c
#define BT_MCS_OPC_NEXT_SEGMENT 0x21U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

将当前音轨位置设为当前音轨下一段（Next Segment）的起始位置。

<a id="ga06df0d77c7a678ca8f4f01ec64c88de7"></a>

### `BT_MCS_OPC_NEXT_TRACK`

```c
#define BT_MCS_OPC_NEXT_TRACK 0x31U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

按播放顺序（Playing Order）将当前音轨设为下一音轨。

<a id="gafe5d0665ae8b33428bce16c427eabcc1"></a>

### `BT_MCS_OPC_NTF_CANNOT_BE_COMPLETED`

```c
#define BT_MCS_OPC_NTF_CANNOT_BE_COMPLETED 0x04U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

由于播放器内部的某种条件，无法成功完成任何媒体控制点写入（Media Control Point Write）所请求的动作。

<a id="ga72e92f172f03a64d2d4641bcdbdb614f"></a>

### `BT_MCS_OPC_NTF_NOT_SUPPORTED`

```c
#define BT_MCS_OPC_NTF_NOT_SUPPORTED 0x02U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

写入媒体控制点（Media Control Point）时使用了无效或不支持的操作码。

<a id="ga740d7278a770b215ae185441fb43c85b"></a>

### `BT_MCS_OPC_NTF_PLAYER_INACTIVE`

```c
#define BT_MCS_OPC_NTF_PLAYER_INACTIVE 0x03U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

收到操作码时，媒体播放器状态（Media Player State）特征值为非活动（Inactive）；或执行该操作码所请求动作的结果，使该特征值变为 Inactive。

<a id="ga7507062e3fe2df221cd47546713a0d28"></a>

### `BT_MCS_OPC_NTF_SUCCESS`

```c
#define BT_MCS_OPC_NTF_SUCCESS 0x01U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

写入操作码（Opcode Write）所请求的动作已成功完成。

<a id="ga8b15cb7a8a1429f83e8d1619c37becc6"></a>

### `BT_MCS_OPC_PAUSE`

```c
#define BT_MCS_OPC_PAUSE 0x02U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

暂停播放当前音轨（Track）。

<a id="ga79c4cf8292a4548bc7b9b06b1ce0f60a"></a>

### `BT_MCS_OPC_PLAY`

```c
#define BT_MCS_OPC_PLAY 0x01U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

开始播放当前音轨（Track）。

<a id="gab7efc1fb17cc53c376f6f84bf31ef85c"></a>

### `BT_MCS_OPC_PREV_GROUP`

```c
#define BT_MCS_OPC_PREV_GROUP 0x40U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

将当前组设为组序列（Sequence of Groups）中的上一组。

<a id="ga454775706fe60ccd12e5ab44e6ddacba"></a>

### `BT_MCS_OPC_PREV_SEGMENT`

```c
#define BT_MCS_OPC_PREV_SEGMENT 0x20U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

将当前音轨位置设为当前音轨上一段（Previous Segment）的起始位置。

<a id="ga88e09cd634c2dd3068f746cc978c1568"></a>

### `BT_MCS_OPC_PREV_TRACK`

```c
#define BT_MCS_OPC_PREV_TRACK 0x30U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

按播放顺序（Playing Order）将当前音轨设为上一音轨。

<a id="gade874bf59dc08ddb682280b644821e11"></a>

### `BT_MCS_OPC_STOP`

```c
#define BT_MCS_OPC_STOP 0x05U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

停止当前活动，回到暂停状态（Paused State），并将当前音轨位置设为当前音轨起点。

<a id="gaa24785ccc713cb2421a55ff48f5f2c45"></a>

### `BT_MCS_OPC_SUP_FAST_FORWARD`

```c
#define BT_MCS_OPC_SUP_FAST_FORWARD BIT(3U)
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

支持快进操作码（Fast Forward Opcode）。

<a id="gaaa3b553dc8eb2de610b545f1ce88b067"></a>

### `BT_MCS_OPC_SUP_FAST_REWIND`

```c
#define BT_MCS_OPC_SUP_FAST_REWIND BIT(2U)
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

支持快退操作码（Fast Rewind Opcode）。

<a id="ga57508e39d5a32ebefb0b103f805ec047"></a>

### `BT_MCS_OPC_SUP_FIRST_GROUP`

```c
#define BT_MCS_OPC_SUP_FIRST_GROUP BIT(18U)
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

支持第一组操作码（First Group Opcode）。

<a id="ga5434b6409f4300cd86df1f75cb699ad8"></a>

### `BT_MCS_OPC_SUP_FIRST_SEGMENT`

```c
#define BT_MCS_OPC_SUP_FIRST_SEGMENT BIT(8U)
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

支持第一段操作码（First Segment Opcode）。

<a id="ga7d79bde3dbc9044667fa2bc54cc7cec4"></a>

### `BT_MCS_OPC_SUP_FIRST_TRACK`

```c
#define BT_MCS_OPC_SUP_FIRST_TRACK BIT(13U)
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

支持第一音轨操作码（First Track Opcode）。

<a id="ga158df3fd1ae39fc3405e25ba7d056d80"></a>

### `BT_MCS_OPC_SUP_GOTO_GROUP`

```c
#define BT_MCS_OPC_SUP_GOTO_GROUP BIT(20U)
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

支持转到指定组操作码（Goto Group Opcode）。

<a id="ga9c576ae9a0ad2200a4b29059e88c6c28"></a>

### `BT_MCS_OPC_SUP_GOTO_SEGMENT`

```c
#define BT_MCS_OPC_SUP_GOTO_SEGMENT BIT(10U)
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

支持转到指定段操作码（Goto Segment Opcode）。

<a id="gaf8573ac7d802252076ef759575baef2f"></a>

### `BT_MCS_OPC_SUP_GOTO_TRACK`

```c
#define BT_MCS_OPC_SUP_GOTO_TRACK BIT(15U)
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

支持转到指定音轨操作码（Goto Track Opcode）。

<a id="ga80bf605e90dee5841d14fdbb9b39f96a"></a>

### `BT_MCS_OPC_SUP_LAST_GROUP`

```c
#define BT_MCS_OPC_SUP_LAST_GROUP BIT(19U)
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

支持最后一组操作码（Last Group Opcode）。

<a id="ga9c4e53c88ea8ea9eb056e9ff37b58dd1"></a>

### `BT_MCS_OPC_SUP_LAST_SEGMENT`

```c
#define BT_MCS_OPC_SUP_LAST_SEGMENT BIT(9U)
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

支持最后一段操作码（Last Segment Opcode）。

<a id="ga8752a8b6ee27919025bb3e5fb4a77c46"></a>

### `BT_MCS_OPC_SUP_LAST_TRACK`

```c
#define BT_MCS_OPC_SUP_LAST_TRACK BIT(14U)
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

支持最后音轨操作码（Last Track Opcode）。

<a id="ga3024e1b5a5175d2f45cdc7650bb9f66a"></a>

### `BT_MCS_OPC_SUP_MOVE_RELATIVE`

```c
#define BT_MCS_OPC_SUP_MOVE_RELATIVE BIT(5U)
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

支持相对移动操作码（Move Relative Opcode）。

<a id="gaeeeff1f344202619794af0de0cda199b"></a>

### `BT_MCS_OPC_SUP_NEXT_GROUP`

```c
#define BT_MCS_OPC_SUP_NEXT_GROUP BIT(17U)
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

支持下一组操作码（Next Group Opcode）。

<a id="ga416c45a7a2ac8c744c42c19a454d6363"></a>

### `BT_MCS_OPC_SUP_NEXT_SEGMENT`

```c
#define BT_MCS_OPC_SUP_NEXT_SEGMENT BIT(7U)
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

支持下一段操作码（Next Segment Opcode）。

<a id="gae213edc6b714f0a1adc744e8ff779ee6"></a>

### `BT_MCS_OPC_SUP_NEXT_TRACK`

```c
#define BT_MCS_OPC_SUP_NEXT_TRACK BIT(12U)
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

支持下一音轨操作码（Next Track Opcode）。

<a id="gabdca574666b964d506d96e01562875f4"></a>

### `BT_MCS_OPC_SUP_PAUSE`

```c
#define BT_MCS_OPC_SUP_PAUSE BIT(1U)
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

支持暂停操作码（Pause Opcode）。

<a id="ga82d1bbc5cd67ab30960bca6992116a8f"></a>

### `BT_MCS_OPC_SUP_PLAY`

```c
#define BT_MCS_OPC_SUP_PLAY BIT(0U)
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

支持播放操作码（Play Opcode）。

<a id="ga4443a0f87750c537a6a39544bbf63111"></a>

### `BT_MCS_OPC_SUP_PREV_GROUP`

```c
#define BT_MCS_OPC_SUP_PREV_GROUP BIT(16U)
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

支持上一组操作码（Previous Group Opcode）。

<a id="gae074d9404aa5c8722678d6805fb7636d"></a>

### `BT_MCS_OPC_SUP_PREV_SEGMENT`

```c
#define BT_MCS_OPC_SUP_PREV_SEGMENT BIT(6U)
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

支持上一段操作码（Previous Segment Opcode）。

<a id="ga59794af43d1b78a1f1a52fb48769be9c"></a>

### `BT_MCS_OPC_SUP_PREV_TRACK`

```c
#define BT_MCS_OPC_SUP_PREV_TRACK BIT(11U)
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

支持上一音轨操作码（Previous Track Opcode）。

<a id="gaec507c502c53413e510cc30f179befec"></a>

### `BT_MCS_OPC_SUP_STOP`

```c
#define BT_MCS_OPC_SUP_STOP BIT(4U)
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

支持停止操作码（Stop Opcode）。

<a id="ga4ae0b32e4192ba36b3ad4d6d8354929a"></a>

### `BT_MCS_OPCODES_SUPPORTED_LEN`

```c
#define BT_MCS_OPCODES_SUPPORTED_LEN 4U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

媒体控制点（Media Control Point）支持的操作码字段长度。

<a id="ga05ec8bf9ae813c8a3755b1383030bdf0"></a>

### `BT_MCS_PLAYBACK_SPEED_DOUBLE`

```c
#define BT_MCS_PLAYBACK_SPEED_DOUBLE 64
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

双倍播放速度（Double Playback Speed），对应 200% 速度。

<a id="ga3bff45add6fbf602ad6bb07b0e64b335"></a>

### `BT_MCS_PLAYBACK_SPEED_HALF`

```c
#define BT_MCS_PLAYBACK_SPEED_HALF -64
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

半速播放（Half Playback Speed），对应 50% 速度。

<a id="gaa3299c597471a809033ec45b2c6f5b3d"></a>

### `BT_MCS_PLAYBACK_SPEED_MAX`

```c
#define BT_MCS_PLAYBACK_SPEED_MAX 127
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

最高播放速度（Max Playback Speed），对应 395.7% 速度，接近 400%。

<a id="ga5d450ac222a491b7d544cc4d3f3ffcf0"></a>

### `BT_MCS_PLAYBACK_SPEED_MIN`

```c
#define BT_MCS_PLAYBACK_SPEED_MIN -128
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

最低播放速度（Minimum Playback Speed），对应 25% 速度。

<a id="ga90e55b0230a11f752b111750e94ace4c"></a>

### `BT_MCS_PLAYBACK_SPEED_QUARTER`

```c
#define BT_MCS_PLAYBACK_SPEED_QUARTER -128
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

四分之一播放速度（Quarter Playback Speed），对应 25% 速度。

<a id="ga68c0eaa632ca581a1ab5ab144b3d7693"></a>

### `BT_MCS_PLAYBACK_SPEED_UNITY`

```c
#define BT_MCS_PLAYBACK_SPEED_UNITY 0
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

一倍播放速度（Unity Playback Speed），对应 100% 速度。

<a id="ga8b8023d46c3ce402a07c9146494ada60"></a>

### `BT_MCS_PLAYING_ORDER_INORDER_ONCE`

```c
#define BT_MCS_PLAYING_ORDER_INORDER_ONCE 0x03U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

按音轨顺序（Track Order）将组内音轨播放一次。

<a id="gaaccf440eb5df01eaa0a255e09cf7b996"></a>

### `BT_MCS_PLAYING_ORDER_INORDER_REPEAT`

```c
#define BT_MCS_PLAYING_ORDER_INORDER_REPEAT 0x04U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

按音轨顺序（Track Order）重复播放组内音轨。

<a id="gaaa06525a5d53d4bf2312304208dda311"></a>

### `BT_MCS_PLAYING_ORDER_NEWEST_ONCE`

```c
#define BT_MCS_PLAYING_ORDER_NEWEST_ONCE 0x07U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

从最新音轨开始，将组内音轨播放一次（Newest First）。

<a id="ga28a19c78f96b51f0e048395eb4378d61"></a>

### `BT_MCS_PLAYING_ORDER_NEWEST_REPEAT`

```c
#define BT_MCS_PLAYING_ORDER_NEWEST_REPEAT 0x08U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

从最新音轨开始，重复播放组内音轨（Newest First）。

<a id="ga260b73c14b35ee596cacca082b5dc865"></a>

### `BT_MCS_PLAYING_ORDER_OLDEST_ONCE`

```c
#define BT_MCS_PLAYING_ORDER_OLDEST_ONCE 0x05U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

从最旧音轨开始，将组内音轨播放一次（Oldest First）。

<a id="ga2fb92d553aed2f680321db68ef28035f"></a>

### `BT_MCS_PLAYING_ORDER_OLDEST_REPEAT`

```c
#define BT_MCS_PLAYING_ORDER_OLDEST_REPEAT 0x06U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

从最旧音轨开始，重复播放组内音轨（Oldest First）。

<a id="gaa33a02e34f65021b1b7290edc76b166e"></a>

### `BT_MCS_PLAYING_ORDER_SHUFFLE_ONCE`

```c
#define BT_MCS_PLAYING_ORDER_SHUFFLE_ONCE 0x09U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

以随机顺序（Random Order）将组内音轨播放一次。

<a id="gaa231c007f0448a5ba3bd61e8528c5b1e"></a>

### `BT_MCS_PLAYING_ORDER_SHUFFLE_REPEAT`

```c
#define BT_MCS_PLAYING_ORDER_SHUFFLE_REPEAT 0x0AU
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

以随机顺序（Random Order）重复播放组内音轨。

<a id="ga1c25a91795472a553286def379fe943b"></a>

### `BT_MCS_PLAYING_ORDER_SINGLE_ONCE`

```c
#define BT_MCS_PLAYING_ORDER_SINGLE_ONCE 0x01U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

单个音轨（Track）播放一次，没有下一音轨。

<a id="ga4698529b5268ff1c5099f4cc9d8e9966"></a>

### `BT_MCS_PLAYING_ORDER_SINGLE_REPEAT`

```c
#define BT_MCS_PLAYING_ORDER_SINGLE_REPEAT 0x02U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

重复播放单个音轨（Track），下一音轨就是当前音轨。

<a id="ga594daa869c6696a4cdd961f8786134a6"></a>

### `BT_MCS_PLAYING_ORDERS_SUPPORTED_INORDER_ONCE`

```c
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_INORDER_ONCE BIT(2U)
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

按音轨顺序（Track Order）将组内音轨播放一次。

<a id="gac4bcd9b84e28a47dd23d073dd942a9c8"></a>

### `BT_MCS_PLAYING_ORDERS_SUPPORTED_INORDER_REPEAT`

```c
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_INORDER_REPEAT BIT(3U)
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

按音轨顺序（Track Order）重复播放组内音轨。

<a id="gabd77af4da60d1b7531d35bd543cb4df2"></a>

### `BT_MCS_PLAYING_ORDERS_SUPPORTED_NEWEST_ONCE`

```c
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_NEWEST_ONCE BIT(6U)
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

从最新音轨开始，将组内音轨播放一次（Newest First）。

<a id="ga9bb22c2c7d08032ab1d5c3ae64ce01a8"></a>

### `BT_MCS_PLAYING_ORDERS_SUPPORTED_NEWEST_REPEAT`

```c
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_NEWEST_REPEAT BIT(7U)
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

从最新音轨开始，重复播放组内音轨（Newest First）。

<a id="gae1d8c34c8f9ea9fadc4da56d0d127712"></a>

### `BT_MCS_PLAYING_ORDERS_SUPPORTED_OLDEST_ONCE`

```c
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_OLDEST_ONCE BIT(4U)
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

从最旧音轨开始，将组内音轨播放一次（Oldest First）。

<a id="ga38bb3aa9a388fa3ae0230cb78cf2d3a5"></a>

### `BT_MCS_PLAYING_ORDERS_SUPPORTED_OLDEST_REPEAT`

```c
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_OLDEST_REPEAT BIT(5U)
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

从最旧音轨开始，重复播放组内音轨（Oldest First）。

<a id="ga2c245ad4f76937b366770aa7afe7b684"></a>

### `BT_MCS_PLAYING_ORDERS_SUPPORTED_SHUFFLE_ONCE`

```c
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_SHUFFLE_ONCE BIT(8U)
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

以随机顺序（Random Order）将组内音轨播放一次。

<a id="gae5d972a834c1b568f39df91df0febb81"></a>

### `BT_MCS_PLAYING_ORDERS_SUPPORTED_SHUFFLE_REPEAT`

```c
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_SHUFFLE_REPEAT BIT(9U)
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

以随机顺序（Random Order）重复播放组内音轨。

<a id="ga7102f1909baea2320827ea6b47522bd8"></a>

### `BT_MCS_PLAYING_ORDERS_SUPPORTED_SINGLE_ONCE`

```c
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_SINGLE_ONCE BIT(0U)
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

单个音轨（Track）播放一次，没有下一音轨。

<a id="gafecb7edde06dfb97939af93034690cbc"></a>

### `BT_MCS_PLAYING_ORDERS_SUPPORTED_SINGLE_REPEAT`

```c
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_SINGLE_REPEAT BIT(1U)
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

重复播放单个音轨（Track），下一音轨就是当前音轨。

<a id="ga0a7769ba43b5b5b20cdbce71a129fcef"></a>

### `BT_MCS_SCP_NTF_FAILURE`

```c
#define BT_MCS_SCP_NTF_FAILURE 0x02U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

搜索请求（Search Request）无效，未开始搜索。

<a id="gaa292c3bb4b5eeb62d5e8e6cb72e69908"></a>

### `BT_MCS_SCP_NTF_SUCCESS`

```c
#define BT_MCS_SCP_NTF_SUCCESS 0x01U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

搜索请求（Search Request）已接受，搜索已开始。

<a id="gade2b66ace813a9bf91b497fbc1dfb885"></a>

### `BT_MCS_SEARCH_TYPE_ALBUM_NAME`

```c
#define BT_MCS_SEARCH_TYPE_ALBUM_NAME 0x03U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

按专辑名称（Album Name）搜索。

<a id="ga3bbf3a3393fa08a8f797e7e286f4b06f"></a>

### `BT_MCS_SEARCH_TYPE_ARTIST_NAME`

```c
#define BT_MCS_SEARCH_TYPE_ARTIST_NAME 0x02U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

按艺人名称（Artist Name）搜索。

<a id="ga2befe4b4b22125a9e24ab4af6eb08f95"></a>

### `BT_MCS_SEARCH_TYPE_EARLIEST_YEAR`

```c
#define BT_MCS_SEARCH_TYPE_EARLIEST_YEAR 0x05U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

按最早年份（Earliest Year）搜索。

<a id="gae4d30046fb1f4d6ffc554fdd95946bf0"></a>

### `BT_MCS_SEARCH_TYPE_GENRE`

```c
#define BT_MCS_SEARCH_TYPE_GENRE 0x07U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

按流派（Genre）搜索。

<a id="gaf98145eae298cca9e3df1dbcca9118a7"></a>

### `BT_MCS_SEARCH_TYPE_GROUP_NAME`

```c
#define BT_MCS_SEARCH_TYPE_GROUP_NAME 0x04U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

按组名称（Group Name）搜索。

<a id="gad120d8a4f7130762568b7c6f87a34cd4"></a>

### `BT_MCS_SEARCH_TYPE_LATEST_YEAR`

```c
#define BT_MCS_SEARCH_TYPE_LATEST_YEAR 0x06U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

按最晚年份（Latest Year）搜索。

<a id="gab6f6fb41e61f5b4c257e36cba71f98a2"></a>

### `BT_MCS_SEARCH_TYPE_ONLY_GROUPS`

```c
#define BT_MCS_SEARCH_TYPE_ONLY_GROUPS 0x09U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

仅搜索组（Groups）。

<a id="gaa99d74ce6f523185a3522f257647edce"></a>

### `BT_MCS_SEARCH_TYPE_ONLY_TRACKS`

```c
#define BT_MCS_SEARCH_TYPE_ONLY_TRACKS 0x08U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

仅搜索音轨（Tracks）。

<a id="ga5a53ce79494a2ec935a43e2cabb6496c"></a>

### `BT_MCS_SEARCH_TYPE_TRACK_NAME`

```c
#define BT_MCS_SEARCH_TYPE_TRACK_NAME 0x01U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

按音轨名称（Track Name）搜索。

<a id="ga22c0b457d8c6e9ec119fff38205786d3"></a>

### `BT_MCS_SEEKING_SPEED_FACTOR_MAX`

```c
#define BT_MCS_SEEKING_SPEED_FACTOR_MAX 64
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

最大搜寻速度（Maximum Seeking Speed），可取负值。

<a id="gaf912dcbc70c81a023f8b93a4d4b0e745"></a>

### `BT_MCS_SEEKING_SPEED_FACTOR_MIN`

```c
#define BT_MCS_SEEKING_SPEED_FACTOR_MIN 4
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

最小搜寻速度（Minimum Seeking Speed），可取负值。

<a id="ga16bdf755d07c99895fa8698f9bd637a0"></a>

### `BT_MCS_SEEKING_SPEED_FACTOR_ZERO`

```c
#define BT_MCS_SEEKING_SPEED_FACTOR_ZERO 0
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

不搜寻（No Seeking）。

<a id="gaf771b17acd202a20450b6ea939ddee3b"></a>

### `SEARCH_LEN_MAX`

```c
#define SEARCH_LEN_MAX 64U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

搜索控制点（Search Control Point）最大长度。

<a id="gaff47bc210fdd2d4d80a0ce822ca29a67"></a>

### `SEARCH_LEN_MIN`

```c
#define SEARCH_LEN_MIN 2U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

搜索控制点（Search Control Point）最小长度。

至少一个搜索控制项（Search Control Item，SCI），由长度字节与类型字节组成；参数字段（原文标作 * parameter field）可以为空。

<a id="ga81665fd87487cbaf1c0f90f1e0b2126a"></a>

### `SEARCH_PARAM_MAX`

```c
#define SEARCH_PARAM_MAX 62U
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

搜索参数（Search Parameters）最大长度。

<a id="gab1fad64b6a1edfefce90cd4692576a5d"></a>

### `SEARCH_SCI_LEN_MIN`

```c
#define SEARCH_SCI_LEN_MIN
```

```c
#include <zephyr/bluetooth/audio/mcs.h>
```

展开值（Value）：

```c
1   /* An SCI length can be as little as one byte,
* for an SCI that has only the type field.
* (The SCI len is the length of type + param.)
*/
```

搜索控制点项（Search Control Point Item，SCI）最小长度。

对于仅包含类型字段（Type field）的 SCI，其长度可以只有一个字节。（SCI 长度是 type 与 param 的总长度。）


## 6.14\_原页交叉引用（Cross References）

- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [zephyr/bluetooth/audio/mcs.h](../api_file_bluetooth_media_reference/P006_zephyr__bluetooth__audio__mcs.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P005_媒体控制客户端（Media Control Client，MCC）.md) · [返回大纲](大纲.md) · [下一章](P007_媒体代理（Media Proxy）.md)
