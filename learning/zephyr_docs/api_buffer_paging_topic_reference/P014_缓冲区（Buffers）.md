---
id: learning.zephyr-docs.api-buffer-paging-topic-reference.page-14
title: 缓冲区（Buffers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_缓冲区（Buffers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于承载数据的对象，以及这些对象的提供者。

<a id="details"></a>

数据由什么承载、由谁提供。数据以 Zephyr net_buf 缓冲区传递。mpipe 在缓冲区的用户数据区域添加 mpipe_buffer_meta，记录所属缓冲池、有效字节数、时间戳，以及在存在底层驱动缓冲区时被封装的驱动自有缓冲区。最后一个字段实现了零拷贝（Zero-copy）路径：摄像头写入的一帧无需搬移即可到达显示器。缓冲区来自 mpipe_buffer_pool，从不来自堆（Heap）。缓冲池是某种后备存储上的小型虚函数表（Vtable），因此插件可交付驱动已有的缓冲区，而非其副本；框架通过辅助函数驱动缓冲池，不直接调用钩子（Hooks）。

确定缓冲区提供方：格式确定后，一次查询沿图传播，以确定缓冲区配置，包括数量、大小、对齐要求以及使用谁的池。查询向下游传至接收端（Sink），在向上返回时写入提案（Proposals），因此每个元素作出决定前均已获得下游的提案。提案可以是完整的缓冲池，也可以是按值传递的独立配置。这一区别关系到所有权（Ownership）：需求只能通过 mpipe_buffer_pool_set_config 传入提案元素仍然拥有的池，池的所有者可以约束或拒绝该需求。任何元素都不得直接写入其他池的配置字段；启动池的一方也负责停止它。池中的 req_config 和 config 两份配置防止某次运行协商出的需求影响下一次运行；参见下文字段。

<a id="header-files"></a>
<a id="files"></a>

## 14.1\_文件（Files）

<a id="r_mpipe_5Fbuffer_2Eh"></a>

```c
file mpipe_buffer.h
```

相关声明：[mpipe_buffer.h](../api_file_service_interface_reference/P040_zephyr__mpipe__mpipe_buffer.h_文件参考.md)。

缓冲区和缓冲池（Buffer and Buffer Pool）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 14.2\_数据结构（Data Structures）

<a id="r_mpipe_5Fbuffer_5Fpool_5Fconfig"></a>

```c
struct mpipe_buffer_pool_config
```

相关声明：[mpipe_buffer_pool_config](../audio_video_model_reference/P018_mpipe_buffer_pool_config_结构体.md)。

缓冲池（Buffer Pool）的配置结构。

<a id="r_mpipe_5Fbuffer_5Fpool"></a>

```c
struct mpipe_buffer_pool
```

相关声明：[mpipe_buffer_pool](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md)。

缓冲池（Buffer Pool）结构。

<a id="r_mpipe_5Fbuffer_5Fmeta"></a>

```c
struct mpipe_buffer_meta
```

相关声明：[mpipe_buffer_meta](../audio_video_model_reference/P016_mpipe_buffer_meta_结构体.md)。

存储在net_buf user_data中的通用缓冲区元数据（Buffer Metadata）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 14.3\_函数（Functions）

<a id="r_gaa7c45d601a5891ad7a19d2b107086947"></a>

```c
static struct mpipe_buffer_meta * mpipe_buffer_get_meta (const struct net_buf *buf)
```

相关声明：[mpipe_buffer_meta](../audio_video_model_reference/P016_mpipe_buffer_meta_结构体.md)、[mpipe_buffer_get_meta](#gaa7c45d601a5891ad7a19d2b107086947)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

获取缓冲区承载的 mpipe 元数据（Metadata）。

<a id="r_gad0509018241d2b69c8188b22a61530c1"></a>

```c
void mpipe_buffer_destroy (struct net_buf *buf)
```

相关声明：[mpipe_buffer_destroy](#gad0509018241d2b69c8188b22a61530c1)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

`net_buf` 的销毁回调（Destroy Callback）。

<a id="r_gaca82ba8fed0f9b21281e9d89a8715378"></a>

```c
int mpipe_buffer_pool_configure (struct mpipe_buffer_pool *pool, const struct mpipe_structure *caps)
```

相关声明：[mpipe_buffer_pool_configure](#gaca82ba8fed0f9b21281e9d89a8715378)、[mpipe_buffer_pool](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)。

配置缓冲池（Buffer Pool）。

<a id="r_ga8a80231824e6cbb7748e80df8d504e93"></a>

```c
int mpipe_buffer_pool_set_req_config (struct mpipe_buffer_pool *pool, const struct mpipe_buffer_pool_config *cfg)
```

相关声明：[mpipe_buffer_pool_set_req_config](#ga8a80231824e6cbb7748e80df8d504e93)、[mpipe_buffer_pool](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md)、[mpipe_buffer_pool_config](../audio_video_model_reference/P018_mpipe_buffer_pool_config_结构体.md)。

声明缓冲池（Buffer Pool）自身提出的要求。

<a id="r_gab718120f2a3c3f2a13107fd14d9385ec"></a>

```c
int mpipe_buffer_pool_set_config (struct mpipe_buffer_pool *pool, const struct mpipe_buffer_pool_config *cfg)
```

相关声明：[mpipe_buffer_pool_set_config](#gab718120f2a3c3f2a13107fd14d9385ec)、[mpipe_buffer_pool](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md)、[mpipe_buffer_pool_config](../audio_video_model_reference/P018_mpipe_buffer_pool_config_结构体.md)。

将协商后的配置（Negotiated Configuration）应用到缓冲池。

<a id="r_ga74d5d359f4880059485689e085887b74"></a>

```c
int mpipe_buffer_pool_start (struct mpipe_buffer_pool *pool)
```

相关声明：[mpipe_buffer_pool_start](#ga74d5d359f4880059485689e085887b74)、[mpipe_buffer_pool](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md)。

启动缓冲池（Buffer Pool）。

<a id="r_ga7ed6b0b1108097583138a61402c077ff"></a>

```c
int mpipe_buffer_pool_stop (struct mpipe_buffer_pool *pool)
```

相关声明：[mpipe_buffer_pool_stop](#ga7ed6b0b1108097583138a61402c077ff)、[mpipe_buffer_pool](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md)。

停止缓冲池（Buffer Pool）。

<a id="r_gabdb544b2a289a767976ecb9d97357eca"></a>

```c
void mpipe_buffer_pool_init (struct mpipe_buffer_pool *pool)
```

相关声明：[mpipe_buffer_pool_init](#gabdb544b2a289a767976ecb9d97357eca)、[mpipe_buffer_pool](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md)。

初始化缓冲池（Buffer Pool）。

## 14.4\_详细说明（Detailed Documentation）

<a id="gad0509018241d2b69c8188b22a61530c1"></a>

### `mpipe_buffer_destroy()`

```c
void mpipe_buffer_destroy ( struct net_buf * buf)
```

```c
#include <zephyr/mpipe/mpipe_buffer.h>
```

`net_buf` 的销毁回调（Destroy Callback）。

缓冲区引用计数（Reference Count）降至零时自动调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向待销毁 net_buf 的指针。 |

<a id="gaa7c45d601a5891ad7a19d2b107086947"></a>

### `mpipe_buffer_get_meta()`

```c
struct mpipe_buffer_meta * mpipe_buffer_get_meta ( const struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/mpipe/mpipe_buffer.h>
```

获取缓冲区承载的 mpipe 元数据（Metadata）。

元数据（Metadata）位于缓冲区的用户数据区域，因此返回的指针在缓冲区存续期间始终有效。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要读取其元数据（Metadata）的缓冲区。 |

**返回（Returns）**：返回值（Returns）：指向缓冲区 mpipe_buffer_meta 的指针。

<a id="gaca82ba8fed0f9b21281e9d89a8715378"></a>

### `mpipe_buffer_pool_configure()`

```c
int mpipe_buffer_pool_configure ( struct mpipe_buffer_pool * pool, const struct mpipe_structure * caps )
```

```c
#include <zephyr/mpipe/mpipe_buffer.h>
```

配置缓冲池（Buffer Pool）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pool` | 指向待配置缓冲池（Buffer Pool）的指针 |
| `caps` | 池中缓冲区必须满足的能力要求（Capability） |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ENOSYS` | 缓冲池没有 configure 钩子（Hook）。 |

**返回（Returns）**：返回值（Returns）：钩子返回的任意负 errno 错误码。

<a id="gabdb544b2a289a767976ecb9d97357eca"></a>

### `mpipe_buffer_pool_init()`

```c
void mpipe_buffer_pool_init ( struct mpipe_buffer_pool * pool)
```

```c
#include <zephyr/mpipe/mpipe_buffer.h>
```

初始化缓冲池（Buffer Pool）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pool` | 指向待初始化缓冲池（Buffer Pool）的指针 |

<a id="gab718120f2a3c3f2a13107fd14d9385ec"></a>

### `mpipe_buffer_pool_set_config()`

```c
int mpipe_buffer_pool_set_config ( struct mpipe_buffer_pool * pool, const struct mpipe_buffer_pool_config * cfg )
```

```c
#include <zephyr/mpipe/mpipe_buffer.h>
```

将协商后的配置（Negotiated Configuration）应用到缓冲池。

这是通过缓冲池查询协商出的配置传入池的唯一途径：调用方交付配置值，由池的所有者验证。元素不得写入其不拥有的缓冲池的 mpipe_buffer_pool::config 字段。

若实现了 mpipe_buffer_pool::set_config，则由池决定接受、约束或拒绝该配置。若未实现，则原样复制配置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pool` | 指向缓冲池（Buffer Pool）的指针 |
| `cfg` | 要应用的协商配置（Negotiated Config） |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功；池的 config 反映已接受的值。 |
| `-EBUSY` | 缓冲池已启动；重新配置之前须先停止。 |

**返回（Returns）**：返回值（Returns）：池的 set_config 为拒绝配置而返回的任意负 errno 错误码。

<a id="ga8a80231824e6cbb7748e80df8d504e93"></a>

### `mpipe_buffer_pool_set_req_config()`

```c
int mpipe_buffer_pool_set_req_config ( struct mpipe_buffer_pool * pool, const struct mpipe_buffer_pool_config * cfg )
```

```c
#include <zephyr/mpipe/mpipe_buffer.h>
```

声明缓冲池（Buffer Pool）自身提出的要求。

池的所有者在设置阶段调用一次此函数，指定无论以后要求承载什么数据都成立的固有要求：硬件要求的最少缓冲区数量、分配器要求的对齐，或应用固定的大小。协商过程不会修改该要求，因此它始终作为每次运行的最低基线：框架在拆除（Teardown）时据此恢复 mpipe_buffer_pool::config；向自有池合并需求的元素无需另行记忆原始要求。

将 mpipe_buffer_pool::config 设为相同的值，使首次运行与后续每次运行一样从固有要求开始。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pool` | 指向缓冲池（Buffer Pool）的指针 |
| `cfg` | 缓冲池的固有要求（Requirement） |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EBUSY` | 缓冲池已启动；重新声明其固有要求前须先停止。 |

<a id="ga74d5d359f4880059485689e085887b74"></a>

### `mpipe_buffer_pool_start()`

```c
int mpipe_buffer_pool_start ( struct mpipe_buffer_pool * pool)
```

```c
#include <zephyr/mpipe/mpipe_buffer.h>
```

启动缓冲池（Buffer Pool）。

已启动的缓冲池保持不变。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pool` | 指向待启动缓冲池（Buffer Pool）的指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ENOSYS` | 缓冲池没有 start 钩子（Hook）；仍将其标为已启动。 |

**返回（Returns）**：返回值（Returns）：钩子返回的任意负 errno 错误码。

<a id="ga7ed6b0b1108097583138a61402c077ff"></a>

### `mpipe_buffer_pool_stop()`

```c
int mpipe_buffer_pool_stop ( struct mpipe_buffer_pool * pool)
```

```c
#include <zephyr/mpipe/mpipe_buffer.h>
```

停止缓冲池（Buffer Pool）。

同时从 mpipe_buffer_pool::req_config 恢复 mpipe_buffer_pool::config，以防止某次运行协商出的需求影响下一次运行。无论池是否曾启动过都会恢复，因此即使池被提议后遭拒绝，也会被重置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pool` | 指向待停止缓冲池（Buffer Pool）的指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ENOSYS` | 缓冲池此前已启动，且没有 stop 钩子（Hook）。 |

**返回（Returns）**：返回值（Returns）：钩子返回的任意负 errno 错误码。


## 14.5\_原页交叉引用（Cross References）

- [mpipe_buffer.h](../api_file_service_interface_reference/P040_zephyr__mpipe__mpipe_buffer.h_文件参考.md)
- [mpipe_buffer_pool_config](../audio_video_model_reference/P018_mpipe_buffer_pool_config_结构体.md)
- [mpipe_buffer_pool](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md)
- [mpipe_buffer_meta](../audio_video_model_reference/P016_mpipe_buffer_meta_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)
- [mpipe_buffer_pool::config](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md#a2d3b29d91616908739e3d1e61628f8ec)
- [mpipe_buffer_pool::set_config](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md#a0393683ad4c617362d302e43697f7bbe)
- [mpipe_buffer_pool::req_config](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md#a4e4dd42ddcf7b0a76fc8db650940ade3)

<a id="header-details"></a>
<a id="mpipe_buffer_negotiation"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P013_MFD TLA2528 接口.md) · [返回大纲](大纲.md) · [下一章](P015_MSPI 设备树相关宏.md)
