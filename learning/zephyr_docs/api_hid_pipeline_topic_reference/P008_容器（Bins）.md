---
id: learning.zephyr-docs.api-hid-pipeline-topic-reference.page-8
title: 容器（Bins）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__bin.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_容器（Bins）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__bin.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

包含其他元素的元素。

<a id="details"></a>

包含其他元素（Elements）的元素，即容器（Bin）。容器本身也是一个元素，因此从外部可将整个图视为一个元素。它负责保存子元素，并以安全顺序向它们传递状态变化（State Change）；此顺序并非添加顺序。容器根据连接关系对子元素进行拓扑排序（Topological Sorting）：状态向上转换时，从接收端（Sink）向数据源（Source）遍历，使下游元素在被推入数据前就绪；状态向下转换时，从数据源向接收端遍历，避免继续向已拆除的元素生产数据。`CONFIG_MPIPE_BIN_MAX_CHILDREN` 限制排序所用数组的容量。容器还拥有供子元素报告的消息通道（Message Channel），借此将图深处的故障传递给应用。参见消息（Messages）。

<a id="header-files"></a>
<a id="files"></a>

## 8.1\_文件（Files）

<a id="r_mpipe_5Fbin_2Eh"></a>

```c
file mpipe_bin.h
```

相关声明：[mpipe_bin.h](../api_file_service_reference/P023_zephyr__mpipe__mpipe_bin.h_文件参考.md)。

容器（Bin）：包含其他元素的元素。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 8.2\_数据结构（Data Structures）

<a id="r_mpipe_5Fbin"></a>

```c
struct mpipe_bin
```

相关声明：[mpipe_bin](../audio_video_model_reference/P015_mpipe_bin_结构体.md)。

容器（Bin）结构。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.3\_函数（Functions）

<a id="r_gab9a27c7642bd57189aa1f62da3c080e3"></a>

```c
int mpipe_bin_init (struct mpipe_bin *bin, uint8_t id)
```

相关声明：[mpipe_bin_init](#gab9a27c7642bd57189aa1f62da3c080e3)、[mpipe_bin](../audio_video_model_reference/P015_mpipe_bin_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化元素容器（Bin）。

<a id="r_ga57d13bc1cb4c8f3095e3acbe08f7b6d4"></a>

```c
int mpipe_bin_set_bus_validator (struct mpipe_bin *bin, zbus_validator bus_validator, void *user_data)
```

相关声明：[mpipe_bin_set_bus_validator](#ga57d13bc1cb4c8f3095e3acbe08f7b6d4)、[mpipe_bin](../audio_video_model_reference/P015_mpipe_bin_结构体.md)、[zbus_validator](https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__apis.html#ga44ca2e52a4f1bcf298888a7ebf9b5cf7)。

在元素容器（Bin）的总线（Bus）上安装验证器（Validator）和用户数据（User Data）。

<a id="r_ga0029c3da6a9bfca02c22673e4622a957"></a>

```c
int mpipe_bin_add (struct mpipe_bin *bin, struct mpipe_element *element,...)
```

相关声明：[mpipe_bin_add](#ga0029c3da6a9bfca02c22673e4622a957)、[mpipe_bin](../audio_video_model_reference/P015_mpipe_bin_结构体.md)、[mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)。

向元素容器（Bin）添加元素（Elements）。

<a id="r_ga564685f39d56de259d9df1257a57b1b7"></a>

```c
int mpipe_bin_change_state_func (struct mpipe_element *element, enum mpipe_state_change transition)
```

相关声明：[mpipe_bin_change_state_func](#ga564685f39d56de259d9df1257a57b1b7)、[mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)、[mpipe_state_change](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga219cea77697cda52503e88096029c287)。

元素容器（Bin）的状态切换函数（State Change Function）。

## 8.4\_详细说明（Detailed Documentation）

<a id="ga0029c3da6a9bfca02c22673e4622a957"></a>

### `mpipe_bin_add()`

```c
int mpipe_bin_add ( struct mpipe_bin * bin, struct mpipe_element * element, ... )
```

```c
#include <zephyr/mpipe/mpipe_bin.h>
```

向元素容器（Bin）添加元素（Elements）。

将所给元素（Elements）添加到容器（Bin）。

一个元素只能加入一个容器（Bin）。元素 ID 在容器内必须唯一。

此函数接收数量可变的元素（Elements），以 `NULL` 结束。

添加元素不会改变其连接端口（Pads），因此可以先添加再连接，也可以先连接再添加。若某个元素被拒绝，在它之前已添加的元素仍保留在容器中。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bin` | 指向要向其添加元素的容器（Bin）的指针。 |
| `element` | 第一个要添加的元素（Element）。 |
| `...` | 其余 `mpipe_element` 指针，以 `NULL` 结束。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EBUSY` | 某个元素已位于一个容器（Bin）中。 |
| `-EEXIST` | 某个元素的 ID 与容器中已有元素的 ID 相同。 |
| `-ENOSPC` | 容器已包含 `CONFIG_MPIPE_BIN_MAX_CHILDREN` 个元素。 |

<a id="ga564685f39d56de259d9df1257a57b1b7"></a>

### `mpipe_bin_change_state_func()`

```c
int mpipe_bin_change_state_func ( struct mpipe_element * element, enum mpipe_state_change transition )
```

```c
#include <zephyr/mpipe/mpipe_bin.h>
```

元素容器（Bin）的状态切换函数（State Change Function）。

以适当顺序将状态变化（State Change）传播给所有子元素，从而处理容器（Bin）的状态切换。容器管理拓扑关系（Topology），确保状态变化的顺序正确。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `element` | 指向正在改变状态的元素，即容器（Bin）的指针。 |
| `transition` | 正在执行的状态转换（State Transition）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSPC` | 容器包含的子元素数量超过可容纳的数量。 |
| `-EINVAL` | 无法对子元素排序（Order Children）。 |

**返回（Returns）**：返回值：成功返回 0，否则返回拒绝操作的子元素的 errno 错误码。

<a id="gab9a27c7642bd57189aa1f62da3c080e3"></a>

### `mpipe_bin_init()`

```c
int mpipe_bin_init ( struct mpipe_bin * bin, uint8_t id )
```

```c
#include <zephyr/mpipe/mpipe_bin.h>
```

初始化元素容器（Bin）。

初始化容器结构体（Bin Structure），并设置所需函数指针和数据结构。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bin` | 指向要初始化的容器（Bin）的指针。 |
| `id` | 唯一元素标识（Unique Element Identifier）。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。

<a id="ga57d13bc1cb4c8f3095e3acbe08f7b6d4"></a>

### `mpipe_bin_set_bus_validator()`

```c
int mpipe_bin_set_bus_validator ( struct mpipe_bin * bin, zbus_validator bus_validator, void * user_data )
```

```c
#include <zephyr/mpipe/mpipe_bin.h>
```

在元素容器（Bin）的总线（Bus）上安装验证器（Validator）和用户数据（User Data）。

`mpipe_bin_init` 建立通道时不设置验证器（Validator），因为容器不对经过它的消息施加要求。封装容器的元素，例如管线（Pipeline），可通过此接口安装自己的验证器。

只有这两个字段会改变，修改在通道自身的锁（Lock）保护下进行。已附加的观察者（Observers）仍保持附加；可在此调用之前或之后附加观察者。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bin` | 指向容器（Bin）的指针。 |
| `bus_validator` | 要安装的消息验证器（Message Validator）；为 `NULL` 时不验证。 |
| `user_data` | 与总线关联的用户数据（User Data），验证器／观察者可通过 `zbus_chan_user_data()` 获取；不使用时为 `NULL`。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。


## 8.5\_原页交叉引用（Cross References）

- [mpipe_bin.h](../api_file_service_reference/P023_zephyr__mpipe__mpipe_bin.h_文件参考.md)
- [mpipe_bin](../audio_video_model_reference/P015_mpipe_bin_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [zbus_validator](https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__apis.html#ga44ca2e52a4f1bcf298888a7ebf9b5cf7)
- [mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)
- [mpipe_state_change](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga219cea77697cda52503e88096029c287)
- [元素（Elements）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html)
- [CONFIG_MPIPE_BIN_MAX_CHILDREN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MPIPE_BIN_MAX_CHILDREN)
- [消息（Messages）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html)
- [容器（Bins）](P008_容器（Bins）.md)
- [zbus_chan_user_data()](https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__apis.html#gac0b0ed0356fca5a8b65a3332931a369a)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P007_回调（Callbacks）.md) · [返回大纲](大纲.md) · [下一章](P009_脉冲 I_O（Pulse IO）.md)
