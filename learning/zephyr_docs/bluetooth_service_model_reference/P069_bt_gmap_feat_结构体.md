---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-69
title: bt_gmap_feat_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__gmap__feat.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第69章\_bt\_gmap\_feat\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__gmap__feat.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

广播游戏接收端（Broadcast Game Receiver）的功能位域（Feature Bitfield）。

```c
#include <zephyr/bluetooth/audio/gmap.h>
```

<a id="details"></a>

广播游戏接收端（Broadcast Game Receiver）的功能位域（Feature Bitfield）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 69.1\_数据成员（Data Fields）

<a id="r_a7e57da1f8aa0a6ac8e7f929f5ba7e9cd"></a>

```c
enum bt_gmap_ugg_feat ugg_feat
```

相关声明：[bt_gmap_ugg_feat](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga3ef43378bad84bbcd726e318cf0bc145)、[ugg_feat](#a7e57da1f8aa0a6ac8e7f929f5ba7e9cd)。

单播游戏网关特性（Unicast Game Gateway features）。

<a id="r_a3793984ce81ff90aab8eb6ad635e24d5"></a>

```c
enum bt_gmap_ugt_feat ugt_feat
```

相关声明：[bt_gmap_ugt_feat](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga0fe87d6d1412c15564ba7de29e3d7a48)、[ugt_feat](#a3793984ce81ff90aab8eb6ad635e24d5)。

单播游戏终端特性（Unicast Game Terminal features）。

<a id="r_a0ef9878ffcd04a6b88cc8364173cfc10"></a>

```c
enum bt_gmap_bgs_feat bgs_feat
```

相关声明：[bt_gmap_bgs_feat](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga3a79c408b283864616a522b1f04cacaf)、[bgs_feat](#a0ef9878ffcd04a6b88cc8364173cfc10)。

远端广播游戏发送方特性（Broadcast Game Sender features）。

<a id="r_a918d35e89da086321d728f61deb0c962"></a>

```c
enum bt_gmap_bgr_feat bgr_feat
```

相关声明：[bt_gmap_bgr_feat](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga9c1145ad5334e14d4978b6d7d3c84b6c)、[bgr_feat](#a918d35e89da086321d728f61deb0c962)。

远端广播游戏接收方特性（Broadcast Game Receiver features）。

## 69.2\_详细说明（Detailed Documentation）

<a id="a918d35e89da086321d728f61deb0c962"></a>

### `bgr_feat`

```c
enum bt_gmap_bgr_feat bt_gmap_feat::bgr_feat
```

远端广播游戏接收方特性（Broadcast Game Receiver features）。

<a id="a0ef9878ffcd04a6b88cc8364173cfc10"></a>

### `bgs_feat`

```c
enum bt_gmap_bgs_feat bt_gmap_feat::bgs_feat
```

远端广播游戏发送方特性（Broadcast Game Sender features）。

<a id="a7e57da1f8aa0a6ac8e7f929f5ba7e9cd"></a>

### `ugg_feat`

```c
enum bt_gmap_ugg_feat bt_gmap_feat::ugg_feat
```

单播游戏网关特性（Unicast Game Gateway features）。

<a id="a3793984ce81ff90aab8eb6ad635e24d5"></a>

### `ugt_feat`

```c
enum bt_gmap_ugt_feat bt_gmap_feat::ugt_feat
```

单播游戏终端特性（Unicast Game Terminal features）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/gmap.h`

## 69.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/gmap.h](https://docs.zephyrproject.org/latest/doxygen/html/gmap_8h_source.html)
- [bt_gmap_ugg_feat](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga3ef43378bad84bbcd726e318cf0bc145)
- [bt_gmap_ugt_feat](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga0fe87d6d1412c15564ba7de29e3d7a48)
- [bt_gmap_bgs_feat](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga3a79c408b283864616a522b1f04cacaf)
- [bt_gmap_bgr_feat](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga9c1145ad5334e14d4978b6d7d3c84b6c)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P068_bt_gmap_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P070_bt_goep_结构体.md)
