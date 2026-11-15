---
id: learning.zephyr-docs.api-memory-timer-topic-reference.page-7
title: 元素（Elements）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_元素（Elements）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

构成管线的单元。

<a id="details"></a>

构成管线（Pipeline）的基本单元。元素（Element）是一个处理步骤：产生缓冲区、消费缓冲区，或将一些缓冲区转换为另一些缓冲区。元素公开端口（Pad）连接点；连接两个元素，就是将一个元素的源端口（Source Pad）连接到另一个元素的接收端口（Sink Pad）。元素具体做什么由自身决定；框架要求它响应查询（Queries）、处理事件（Events）并遵守状态机（State Machine）。

状态（States）：元素处于三种状态之一，每次只在相邻状态之间移动一步：

```text
READY <-> PAUSED <-> PLAYING
```

READY 表示元素已构造并连接，但没有持有协商后的格式（Negotiated Format）或任何缓冲区。主要工作发生在 READY 到 PAUSED 的转换中：源端推动整个图的能力协商（Capability Negotiation），随后通过缓冲池查询（Buffer Pool Query）确定谁提供缓冲区及其数量，再启动各缓冲池。PAUSED 到 PLAYING 的转换允许数据流动；向下转换则按相反顺序执行，PAUSED 到 READY 时丢弃协商后的能力，使下次运行重新协商。转换完成时返回 0；元素拒绝转换时返回负 errno；-EINPROGRESS 保留给异步完成的转换。拒绝转换的元素保持原状态，已经完成转换的其他元素不会被回滚，这是有意设计的：图会直接显示哪个元素拒绝了哪一次转换。

元素特化（Specializing an Element）：源（Sources）、接收端（Sinks）、变换（Transforms）、解析器（Parsers）和容器（Bins）中的基类实现协议；具体元素将其中一个基类嵌入为首个成员，以自己的 id 调用基类 init，并且只覆盖自己关心的钩子（Hooks）。必须链式调用基类 change_state，因为它负责执行每个元素都应完成的重置（Reset）和缓冲池拆除（Pool Teardown）。

<a id="header-files"></a>
<a id="files"></a>

## 7.1\_文件（Files）

<a id="r_mpipe_5Felement_2Eh"></a>

```c
file mpipe_element.h
```

相关声明：[mpipe_element.h](../api_file_protocol_service_reference/P025_zephyr__mpipe__mpipe_element.h_文件参考.md)。

元素（Element）：构成流水线的基本单元。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.2\_数据结构（Data Structures）

<a id="r_mpipe_5Felement"></a>

```c
struct mpipe_element
```

相关声明：[mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)。

元素基类（Element Base Class）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.3\_宏定义（Macros）

<a id="r_ga0d287bf9926308d665bab9038e5c73aa"></a>

```c
#define MPIPE_STATE_GET_NEXT(cur, target)
```

相关声明：[MPIPE_STATE_GET_NEXT](#ga0d287bf9926308d665bab9038e5c73aa)。

计算下一状态（Next State）。

<a id="r_gad20f56bd84d7767a2e5f854be7d34116"></a>

```c
#define MPIPE_STATE_TRANSITION(cur, next)
```

相关声明：[MPIPE_STATE_TRANSITION](#gad20f56bd84d7767a2e5f854be7d34116)。

创建状态转换值（State Transition Value）。

<a id="r_ga4bc586dbe57b4465b1b1ad554d035fd2"></a>

```c
#define MPIPE_STATE_TRANSITION_CURRENT(trans)
```

相关声明：[MPIPE_STATE_TRANSITION_CURRENT](#ga4bc586dbe57b4465b1b1ad554d035fd2)。

从状态转换（State Transition）中提取当前状态（Current State）。

<a id="r_ga2d6a4dd0a1cdf90dcc392ac9ae2cc764"></a>

```c
#define MPIPE_STATE_TRANSITION_NEXT(trans)
```

相关声明：[MPIPE_STATE_TRANSITION_NEXT](#ga2d6a4dd0a1cdf90dcc392ac9ae2cc764)。

从状态转换（State Transition）中提取下一状态（Next State）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 7.4\_枚举（Enumerations）

<a id="r_ga7ead9fea0963f40d4db49c8008cb3366"></a>

```c
enum mpipe_state { MPIPE_STATE_READY = 0 , MPIPE_STATE_PAUSED = 1 , MPIPE_STATE_PLAYING = 2 }
```

相关声明：[mpipe_state](#ga7ead9fea0963f40d4db49c8008cb3366)、[MPIPE_STATE_READY](#gga7ead9fea0963f40d4db49c8008cb3366aade49a9842b3fa929d20c3c7c5fbba24)、[MPIPE_STATE_PAUSED](#gga7ead9fea0963f40d4db49c8008cb3366a70edf5e9b37a699f5b2ca0f6a41b5544)、[MPIPE_STATE_PLAYING](#gga7ead9fea0963f40d4db49c8008cb3366a565f1ca71525e156ade5a80b6dd28922)。

元素状态（Element States）。

<a id="r_ga219cea77697cda52503e88096029c287"></a>

```c
enum mpipe_state_change { MPIPE_STATE_CHANGE_READY_TO_PAUSED , MPIPE_STATE_CHANGE_PAUSED_TO_PLAYING , MPIPE_STATE_CHANGE_PLAYING_TO_PAUSED , MPIPE_STATE_CHANGE_PAUSED_TO_READY }
```

相关声明：[mpipe_state_change](#ga219cea77697cda52503e88096029c287)、[MPIPE_STATE_CHANGE_READY_TO_PAUSED](#gga219cea77697cda52503e88096029c287acf0326519ae7130fc6416cd6ba45a129)、[MPIPE_STATE_CHANGE_PAUSED_TO_PLAYING](#gga219cea77697cda52503e88096029c287afe96cd696feb697f5fbeecf7be3c1492)、[MPIPE_STATE_CHANGE_PLAYING_TO_PAUSED](#gga219cea77697cda52503e88096029c287a8fb4ec66001f447bca5dbfd32bf91a92)、[MPIPE_STATE_CHANGE_PAUSED_TO_READY](#gga219cea77697cda52503e88096029c287a0fe1848bff2d05ba1e9b7601537248a1)。

两个相邻状态之间的转换（Transition）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.5\_函数（Functions）

<a id="r_gaa571f5b8e78dafb71e2175f0df3c496a"></a>

```c
int mpipe_element_init (struct mpipe_element *self, uint8_t id)
```

相关声明：[mpipe_element_init](#gaa571f5b8e78dafb71e2175f0df3c496a)、[mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化元素（Element）。

<a id="r_ga89e9dc38e2cff13b63e70177732773e9"></a>

```c
static void mpipe_element_set_name (struct mpipe_element *self, const char *name)
```

相关声明：[mpipe_element_set_name](#ga89e9dc38e2cff13b63e70177732773e9)、[mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)。

为元素命名，以便在流水线转储（Pipeline Dump）中使用。

<a id="r_ga4b7bea3b1e0995ceaaebc3f8ec4e0530"></a>

```c
void mpipe_element_reset_pad_caps (struct mpipe_element *element)
```

相关声明：[mpipe_element_reset_pad_caps](#ga4b7bea3b1e0995ceaaebc3f8ec4e0530)、[mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)。

将元素的每个衬垫（Pad）重置为不施加任何约束（Constraints）的状态。

<a id="r_gaaadee8e87da20d947d8fc90e4533ef8b"></a>

```c
void mpipe_element_add_pad (struct mpipe_element *element, struct mpipe_pad *pad)
```

相关声明：[mpipe_element_add_pad](#gaaadee8e87da20d947d8fc90e4533ef8b)、[mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)、[mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)。

将衬垫（Pad）附加到元素（Element）。

<a id="r_ga5b478364e7baec25fef972ab3fee0807"></a>

```c
int mpipe_element_link (struct mpipe_element *element_1, struct mpipe_element *element_2,...)
```

相关声明：[mpipe_element_link](#ga5b478364e7baec25fef972ab3fee0807)、[mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)、[mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)。

连接多个元素（Link Elements）。

<a id="r_gafb59f995c7a2bd799316d187ec252632"></a>

```c
int mpipe_element_set_state (struct mpipe_element *element, enum mpipe_state state)
```

相关声明：[mpipe_element_set_state](#gafb59f995c7a2bd799316d187ec252632)、[mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)、[mpipe_state](#ga7ead9fea0963f40d4db49c8008cb3366)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

设置元素状态（Element State）。

<a id="r_gadd1c172f5ce2f4eb6fffeb40ecc931b6"></a>

```c
struct zbus_channel * mpipe_element_get_bus_chan (struct mpipe_element *element)
```

相关声明：[zbus_channel](../intercore_reference/P206_zbus通道结构.md)、[mpipe_element_get_bus_chan](#gadd1c172f5ce2f4eb6fffeb40ecc931b6)、[mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)。

获取元素的总线通道（Bus Channel）。

## 7.6\_详细说明（Detailed Documentation）

<a id="ga0d287bf9926308d665bab9038e5c73aa"></a>

### `MPIPE_STATE_GET_NEXT`

```c
#define MPIPE_STATE_GET_NEXT ( cur, target )
```

```c
#include <zephyr/mpipe/mpipe_element.h>
```

展开值（Value）：

```c
((enum mpipe_state)((int)cur + SYS_SIGN((int)target - (int)cur)))
```

计算下一状态（Next State）。

给定当前状态（Current State）和目标状态（Target State），计算下一个中间状态（Intermediate State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cur` | 当前状态（Current State），参见 mpipe_state。 |
| `target` | 目标状态（Target State），参见 mpipe_state。 |

返回（Returns）：下一个中间状态（Intermediate State）。

<a id="gad20f56bd84d7767a2e5f854be7d34116"></a>

### `MPIPE_STATE_TRANSITION`

```c
#define MPIPE_STATE_TRANSITION ( cur, next )
```

```c
#include <zephyr/mpipe/mpipe_element.h>
```

展开值（Value）：

```c
(((cur) << 2) | (next))
```

创建状态转换值（State Transition Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cur` | 当前状态（Current State）。 |
| `next` | 下一个状态（Next State）。 |

返回（Returns）：状态转换值（State Transition Value）。

<a id="ga4bc586dbe57b4465b1b1ad554d035fd2"></a>

### `MPIPE_STATE_TRANSITION_CURRENT`

```c
#define MPIPE_STATE_TRANSITION_CURRENT ( trans)
```

```c
#include <zephyr/mpipe/mpipe_element.h>
```

展开值（Value）：

```c
((enum mpipe_state)((trans) >> 2))
```

从状态转换（State Transition）中提取当前状态（Current State）。

给定状态转换（State Transition），提取当前状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `trans` | 转换状态（Transition State），参见 mpipe_state_change。 |

返回（Returns）：当前状态（Current State）。

<a id="ga2d6a4dd0a1cdf90dcc392ac9ae2cc764"></a>

### `MPIPE_STATE_TRANSITION_NEXT`

```c
#define MPIPE_STATE_TRANSITION_NEXT ( trans)
```

```c
#include <zephyr/mpipe/mpipe_element.h>
```

展开值（Value）：

```c
((enum mpipe_state)((trans) & 0x3))
```

从状态转换（State Transition）中提取下一状态（Next State）。

给定状态转换（State Transition），提取下一个状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `trans` | 转换状态（Transition State），参见 mpipe_state_change。 |

返回（Returns）：下一个状态（Next State）。

<a id="ga7ead9fea0963f40d4db49c8008cb3366"></a>

### `mpipe_state`

```c
enum mpipe_state
```

```c
#include <zephyr/mpipe/mpipe_element.h>
```

元素状态（Element States）。

元素（Element）可能处于的所有状态（States）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MPIPE_STATE_READY` | 元素已初始化为 READY，准备转入 PAUSED。 |
| `MPIPE_STATE_PAUSED` | 元素处于 PAUSED，准备接收、处理或传输数据。 |
| `MPIPE_STATE_PLAYING` | 元素处于 PLAYING，数据正在流经元素。 |

<a id="ga219cea77697cda52503e88096029c287"></a>

### `mpipe_state_change`

```c
enum mpipe_state_change
```

```c
#include <zephyr/mpipe/mpipe_element.h>
```

两个相邻状态之间的转换（Transition）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MPIPE_STATE_CHANGE_READY_TO_PAUSED` | 从 READY 到 PAUSED 的状态转换（State Change）。 |
| `MPIPE_STATE_CHANGE_PAUSED_TO_PLAYING` | 从 PAUSED 到 PLAYING 的状态转换（State Change）。 |
| `MPIPE_STATE_CHANGE_PLAYING_TO_PAUSED` | 从 PLAYING 到 PAUSED 的状态转换（State Change）。 |
| `MPIPE_STATE_CHANGE_PAUSED_TO_READY` | 从 PAUSED 到 READY 的状态转换（State Change）。 |

<a id="gaaadee8e87da20d947d8fc90e4533ef8b"></a>

### `mpipe_element_add_pad()`

```c
void mpipe_element_add_pad ( struct mpipe_element * element, struct mpipe_pad * pad )
```

```c
#include <zephyr/mpipe/mpipe_element.h>
```

将衬垫（Pad）附加到元素（Element）。

将端口（Pad）加入元素的端口列表，并将元素设置为端口的容器（Container），使端口回调能够访问拥有它的元素。基类为其声明的端口调用此函数，因此元素只需为自己新增的端口调用它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `element` | 指向要附接端口（Pad）的目标元素的指针。 |
| `pad` | 指向待附接端口（Pad）的指针。 |

<a id="gadd1c172f5ce2f4eb6fffeb40ecc931b6"></a>

### `mpipe_element_get_bus_chan()`

```c
struct zbus_channel * mpipe_element_get_bus_chan ( struct mpipe_element * element)
```

```c
#include <zephyr/mpipe/mpipe_element.h>
```

获取元素的总线通道（Bus Channel）。

获取与元素关联的 zbus_channel，即包含该元素的最近一层容器（Bin）的总线通道（Bus Channel）。应用通过它找到要附加观察者（Observer）的通道，而不依赖容器存储通道的具体位置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `element` | 指向要从中获取通道（Channel）的元素（Elements）的指针。 |

返回（Returns）：指向 zbus_channel 的指针；找不到总线通道（Bus Channel）时为 NULL。

<a id="gaa571f5b8e78dafb71e2175f0df3c496a"></a>

### `mpipe_element_init()`

```c
int mpipe_element_init ( struct mpipe_element * self, uint8_t id )
```

```c
#include <zephyr/mpipe/mpipe_element.h>
```

初始化元素（Element）。

初始化基础元素结构体（Base Elements Structure）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `self` | 指向待初始化元素（Elements）的指针。 |
| `id` | 元素标识符（Element Identifier），在其容器（Bin）内唯一；UINT8_MAX 为保留值。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。

<a id="ga5b478364e7baec25fef972ab3fee0807"></a>

### `mpipe_element_link()`

```c
int mpipe_element_link ( struct mpipe_element * element_1, struct mpipe_element * element_2, ... )
```

```c
#include <zephyr/mpipe/mpipe_element.h>
```

连接多个元素（Link Elements）。

通过各元素首个未连接的源端口（Source Pad）和接收端口（Sink Pad），依次将元素连接到下一个元素。端口能力无法求交（Intersect）时，拒绝该连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `element_1` | 链中的第一个元素（First Element）。 |
| `element_2` | 链中的第二个元素（Second Element）。 |
| `...` | 其他要连接的元素（Elements），以 NULL 终止。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | 元素在所需方向上没有未连接端口（Unlinked Pad）。 |
| `-ENOTSUP` | 两个端口的能力（Capabilities）无法求交。 |

<a id="ga4b7bea3b1e0995ceaaebc3f8ec4e0530"></a>

### `mpipe_element_reset_pad_caps()`

```c
void mpipe_element_reset_pad_caps ( struct mpipe_element * element)
```

```c
#include <zephyr/mpipe/mpipe_element.h>
```

将元素的每个衬垫（Pad）重置为不施加任何约束（Constraints）的状态。

丢弃元素各端口（Pads）上协商后的能力（Negotiated Capability），使后续重新协商从头开始。基类在 PAUSED 到 READY 的转换中调用此函数；覆盖 change_state 的派生元素必须链式调用其基类函数，才能继承此重置行为。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `element` | 指向要重置其端口（Pads）的元素的指针。 |

<a id="ga89e9dc38e2cff13b63e70177732773e9"></a>

### `mpipe_element_set_name()`

```c
void mpipe_element_set_name ( struct mpipe_element * self, const char * name )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/mpipe/mpipe_element.h>
```

为元素命名，以便在流水线转储（Pipeline Dump）中使用。

每个元素的 init 函数都按其类型为元素命名，因此转储（Dump）会显示 vid_transform 这样的名称，而非地址。随后调用此函数可为某个实例设置独有名称，使转储能够区分同类型的两个元素。

原始示例（Example）：

```c
ret = mpipe_queue_init(&queue, QUEUE_ID);
mpipe_element_set_name(&queue.transform.element, "video_queue");
```

禁用 CONFIG_MPIPE_ELEMENT_NAME 时，此函数编译后不产生代码，因此不包含转储功能的构建不会因名称（Name）而占用 ROM。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `self` | 要命名的元素（Element）。 |
| `name` | 要报告的名称（Name），其生命周期必须长于元素；字符串字面量满足这一要求。 |

<a id="gafb59f995c7a2bd799316d187ec252632"></a>

### `mpipe_element_set_state()`

```c
int mpipe_element_set_state ( struct mpipe_element * element, enum mpipe_state state )
```

```c
#include <zephyr/mpipe/mpipe_element.h>
```

设置元素状态（Element State）。

设置元素状态（Element State）。此函数尝试逐步经过所有中间状态，并为每一步调用元素的状态变更函数，以到达请求的状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `element` | 要更改状态的元素（Element）。 |
| `state` | 元素的新 mpipe_state。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 元素没有 set_state 钩子（Hook）。 |
| `-EINPROGRESS` | 保留值：转换异步完成（Asynchronous Completion）。 |

返回（Returns）：成功时为 0，否则为拒绝转换的那个元素的 errno。


## 7.7\_原页交叉引用（Cross References）

- [mpipe_element.h](../api_file_protocol_service_reference/P025_zephyr__mpipe__mpipe_element.h_文件参考.md)
- [mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [zbus_channel](../intercore_reference/P206_zbus通道结构.md)
- [连接端口（Pad）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html)
- [源（Sources）](../api_security_memory_topic_reference/P009_源（Sources）.md)
- [接收端（Sinks）](../api_device_topic_reference/P019_接收端（Sinks）.md)
- [变换元素（Transforms）](../api_lifecycle_capability_topic_reference/P013_变换元素（Transforms）.md)
- [解析器（Parsers）](../api_protocol_topic_reference/P035_解析器（Parsers）.md)
- [容器（Bins）](../api_hid_pipeline_topic_reference/P008_容器（Bins）.md)
- [SYS_SIGN](../util_reference/P001_通用工具公共接口.md#gac6ae21ff0a02c18ec301eb286c0de771)
- [元素（Elements）](P007_元素（Elements）.md)
- [mpipe_queue_init](../api_device_topic_reference/P018_队列（Queues）.md#ga6cade533253c3f6d31aaede6bfe5e152)
- [CONFIG_MPIPE_ELEMENT_NAME](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MPIPE_ELEMENT_NAME)

<a id="header-details"></a>
<a id="mpipe_element_states"></a>
<a id="mpipe_element_subclass"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__mpipe__element_html_ga7ead9fea0963f40d4db49c8008cb3366"></a>
<a id="agroup__sys-util_html_gac6ae21ff0a02c18ec301eb286c0de771"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga7ead9fea0963f40d4db49c8008cb3366aade49a9842b3fa929d20c3c7c5fbba24"></a>
<a id="gga7ead9fea0963f40d4db49c8008cb3366a70edf5e9b37a699f5b2ca0f6a41b5544"></a>
<a id="gga7ead9fea0963f40d4db49c8008cb3366a565f1ca71525e156ade5a80b6dd28922"></a>
<a id="gga219cea77697cda52503e88096029c287acf0326519ae7130fc6416cd6ba45a129"></a>
<a id="gga219cea77697cda52503e88096029c287afe96cd696feb697f5fbeecf7be3c1492"></a>
<a id="gga219cea77697cda52503e88096029c287a8fb4ec66001f447bca5dbfd32bf91a92"></a>
<a id="gga219cea77697cda52503e88096029c287a0fe1848bff2d05ba1e9b7601537248a1"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>
<a id="agroup__mpipe__element_html_ga89e9dc38e2cff13b63e70177732773e9"></a>
<a id="agroup__mpipe__queue_html_ga6cade533253c3f6d31aaede6bfe5e152"></a>

---

[上一章](P006_内存管理（Memory Management）的驱动API。.md) · [返回大纲](大纲.md) · [下一章](P008_PCIe 主机（PCIe Host）.md)
