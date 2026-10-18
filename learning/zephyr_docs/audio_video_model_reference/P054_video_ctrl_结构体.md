---
id: learning.zephyr-docs.audio-video-model-reference.page-54
title: video_ctrl_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structvideo__ctrl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第54章\_video\_ctrl\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structvideo__ctrl.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

视频控制项（Video Controls）的存储类型。

```c
#include <zephyr/drivers/video.h>
```

<a id="details"></a>

视频控制项的存储类型。另见公共 API 中使用的 `video_control` 结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 54.1\_数据成员（Data Fields）

<a id="r_ae85ae0efdd09df92416947515b0e395a"></a>

```c
struct video_ctrl * cluster
```

相关声明：[video_ctrl](P054_video_ctrl_结构体.md)、[cluster](#ae85ae0efdd09df92416947515b0e395a)。

内部使用，用于视频控制项分组。

<a id="r_a53aff4307d71d871064c9b7d26bba3e4"></a>

```c
uint8_t cluster_sz
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cluster_sz](#a53aff4307d71d871064c9b7d26bba3e4)。

内部使用，用于视频控制项分组。

<a id="r_a027ae7809789cc010ec43cc4179428f9"></a>

```c
bool is_auto
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[is_auto](#a027ae7809789cc010ec43cc4179428f9)。

内部使用，用于自动控制项处理。

<a id="r_ae0444d742950563cb13ae6cf4e0e5cd1"></a>

```c
bool has_volatiles
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_volatiles](#ae0444d742950563cb13ae6cf4e0e5cd1)。

内部使用，用于易变控制项（volatile control）处理。

<a id="r_ad3f25f434106a14be692a8846a21bf75"></a>

```c
const struct video_device * vdev
```

相关声明：[video_device](P057_video_device_结构体.md)、[vdev](#ad3f25f434106a14be692a8846a21bf75)。

与此控制项关联的视频设备。

<a id="r_a65ae06ab9371b2f9108d79a2f12ba1b9"></a>

```c
uint32_t id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[id](#a65ae06ab9371b2f9108d79a2f12ba1b9)。

控制项 ID，参见视频控制 ID（Video Control IDs）。

<a id="r_a3353754b98aac187d3e7305fed0b0d83"></a>

```c
enum video_ctrl_type type
```

相关声明：[video_ctrl_type](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__ctrls.html#gaf6e4edb13feb3bd422e19c438b435687)、[type](#a3353754b98aac187d3e7305fed0b0d83)。

控制项类型。

<a id="r_a5130c8a873bcde98ec6722d1da7c238a"></a>

```c
unsigned long flags
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[flags](#a5130c8a873bcde98ec6722d1da7c238a)。

与此控制项关联的标志。

<a id="r_a96e406f3cf4bb48eec604ae9656b6206"></a>

```c
struct video_ctrl_range range
```

相关声明：[video_ctrl_range](P056_video_ctrl_range_结构体.md)、[range](#a96e406f3cf4bb48eec604ae9656b6206)。

此控制项可接受的取值范围。

```c
union {
```

<a id="r_aae71aaeca37d3f31c91c412ae8ec34b6"></a>

```c
int32_t val
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[val](#a959eb36670223091c55743b8c3dfb288)。

用于 32 位控制项类型。

<a id="r_adf575e26fe5c5fd719421d4f2d5d073e"></a>

```c
int64_t val64
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[val64](#a5e6741dde912d912a1c50048e96e274b)。

用于 64 位控制项类型。

<a id="r_abc48c6cc2333dcd69863b337b7c30401"></a>

```c
};
```

此控制项的当前值。

```c
union {
```

<a id="r_af2942f0b22d7f070bf02800f90f292c8"></a>

```c
const char *const * menu
```

相关声明：[menu](#a77de7d9413b14fb33dc85232d14eaa5b)。

用于菜单控制项（menu control）类型。

<a id="r_afe828d739a82a2025a26289387e806fc"></a>

```c
const int64_t * int_menu
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[int_menu](#ac67db8a3797161a75389ced1d485375e)。

用于整数菜单控制项（integer menu control）类型。

<a id="r_afdd97dc57931de12c8a4c62df8c1a168"></a>

```c
};
```

指向菜单控制项类型可选值列表的引用。

<a id="r_ae62f16d3a3be845e512ba5e920f6c5d4"></a>

```c
sys_dnode_t node
```

相关声明：[sys_dnode_t](../dlist_reference/P001_双向链表公共接口.md#ga57fdb936802a617d16c00ab08cd2ad98)、[node](#ae62f16d3a3be845e512ba5e920f6c5d4)。

用于将此控制项放入列表的节点。

## 54.2\_详细说明（Detailed Documentation）

<a id="abc48c6cc2333dcd69863b337b7c30401"></a>

### `[union]`

```c
union { ... } video_ctrl
```

此控制项的当前值。

<a id="afdd97dc57931de12c8a4c62df8c1a168"></a>

### `[union]`

```c
union { ... } video_ctrl
```

指向菜单控制项类型可选值列表的引用。

<a id="ae85ae0efdd09df92416947515b0e395a"></a>

### `cluster`

```c
struct video_ctrl* video_ctrl::cluster
```

内部使用，用于视频控制项分组。

<a id="a53aff4307d71d871064c9b7d26bba3e4"></a>

### `cluster_sz`

```c
uint8_t video_ctrl::cluster_sz
```

内部使用，用于视频控制项分组。

<a id="a5130c8a873bcde98ec6722d1da7c238a"></a>

### `flags`

```c
unsigned long video_ctrl::flags
```

与此控制项关联的标志。

<a id="ae0444d742950563cb13ae6cf4e0e5cd1"></a>

### `has_volatiles`

```c
bool video_ctrl::has_volatiles
```

内部使用，用于易变控制项（volatile control）处理。

<a id="a65ae06ab9371b2f9108d79a2f12ba1b9"></a>

### `id`

```c
uint32_t video_ctrl::id
```

控制项 ID，参见视频控制 ID（Video Control IDs）。

<a id="ac67db8a3797161a75389ced1d485375e"></a>

### `int_menu`

```c
const int64_t* video_ctrl::int_menu
```

用于整数菜单控制项（integer menu control）类型。

<a id="a027ae7809789cc010ec43cc4179428f9"></a>

### `is_auto`

```c
bool video_ctrl::is_auto
```

内部使用，用于自动控制项处理。

<a id="a77de7d9413b14fb33dc85232d14eaa5b"></a>

### `menu`

```c
const char* const* video_ctrl::menu
```

用于菜单控制项（menu control）类型。

<a id="ae62f16d3a3be845e512ba5e920f6c5d4"></a>

### `node`

```c
sys_dnode_t video_ctrl::node
```

用于将此控制项放入列表的节点。

<a id="a96e406f3cf4bb48eec604ae9656b6206"></a>

### `range`

```c
struct video_ctrl_range video_ctrl::range
```

此控制项可接受的取值范围。

<a id="a3353754b98aac187d3e7305fed0b0d83"></a>

### `type`

```c
enum video_ctrl_type video_ctrl::type
```

控制项类型。

<a id="a959eb36670223091c55743b8c3dfb288"></a>

### `val`

```c
int32_t video_ctrl::val
```

用于 32 位控制项类型。

<a id="a5e6741dde912d912a1c50048e96e274b"></a>

### `val64`

```c
int64_t video_ctrl::val64
```

用于 64 位控制项类型。

<a id="ad3f25f434106a14be692a8846a21bf75"></a>

### `vdev`

```c
const struct video_device* video_ctrl::vdev
```

与此控制项关联的视频设备。

本数据类型文档由以下文件生成：

- `zephyr/drivers/video.h`

## 54.3\_原页交叉引用（Cross References）

- [zephyr/drivers/video.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2video_8h_source.html)
- [video_ctrl](P054_video_ctrl_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [video_device](P057_video_device_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [视频控制 ID（Video Control IDs）](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html)
- [video_ctrl_type](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__ctrls.html#gaf6e4edb13feb3bd422e19c438b435687)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [video_ctrl_range](P056_video_ctrl_range_结构体.md)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [sys_dnode_t](../dlist_reference/P001_双向链表公共接口.md#ga57fdb936802a617d16c00ab08cd2ad98)
- [video_control](P053_video_control_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P053_video_control_结构体.md) · [返回大纲](大纲.md) · [下一章](P055_video_ctrl_query_结构体.md)
