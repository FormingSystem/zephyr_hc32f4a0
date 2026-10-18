---
id: learning.zephyr-docs.api-vector-pipeline-topic-reference.page-22
title: 拓扑转储（Topology dump）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dump.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_拓扑转储（Topology dump）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dump.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

呈现容器的拓扑，以及每个端口协商得到的能力。

<a id="details"></a>

呈现容器（Bin）的拓扑，以及每个焊盘（Pad）协商得到的能力（Capability）。以 Graphviz 图显示容器：包括每个元素及其状态、作为端口的焊盘、每个焊盘链接的对端，以及该焊盘最终确定的能力。日志最难清楚展示的是协商结果，因此此工具适用于查看“每条链路达成了什么协商结果”以及“哪个焊盘仍未链接”。目标设备输出文本，主机负责排版。没有文件系统的开发板可通过控制台发送文本，再从串口采集记录中提取图形，命令见下方原始示例。

若元素存在未链接的焊盘，其边框显示为红色；没有任何路径到达的元素在布局中独立显示，因此图的断开情况无需单独报告即可看出。所呈现的是图的当前状态：例如能力过滤器（Caps Filter）在协商后会自行移除，因而运行时显示为分离，运行结束后又显示为已链接。此处不会分配内存，遍历过程也不持有锁；若在流水线改变状态时转储，得到的快照可能恰好捕获正在更新的焊盘。要读取稳定的结果，应在状态稳定后转储。

```sh
sed -n '/^digraph/,/^}/p' capture.log > pipe.dot
dot -Tpng pipe.dot -o pipe.png
```

<a id="header-files"></a>
<a id="files"></a>

## 22.1\_文件（Files）

<a id="r_mpipe_5Fdump_2Eh"></a>

```c
file mpipe_dump.h
```

相关声明：[mpipe_dump.h](../api_file_service_reference/P024_zephyr__mpipe__utils__mpipe_dump.h_文件参考.md)。

绘制流水线拓扑（Pipeline Topology），供调试使用。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 22.2\_类型定义（Typedefs）

<a id="r_ga0215d4a9be34e7a5e58f8e11334ff507"></a>

```c
typedef void(* mpipe_dump_print_t) (void *ctx, const char *str)
```

相关声明：[mpipe_dump_print_t](#ga0215d4a9be34e7a5e58f8e11334ff507)。

转储（Dump）的输出回调（Output Callback）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 22.3\_函数（Functions）

<a id="r_gaa128307bee2a9cdba726f4a59313a8b2"></a>

```c
int mpipe_dump_bin (struct mpipe_bin *bin, mpipe_dump_print_t print, void *ctx)
```

相关声明：[mpipe_dump_bin](#gaa128307bee2a9cdba726f4a59313a8b2)、[mpipe_bin](../audio_video_model_reference/P015_mpipe_bin_结构体.md)、[mpipe_dump_print_t](#ga0215d4a9be34e7a5e58f8e11334ff507)。

呈现元素容器（Bin）的拓扑（Topology）及其每个端口（Pad）的能力（Capability）。

<a id="r_gae215db838d4883132d79c08d0cec3eda"></a>

```c
int mpipe_dump_caps (const struct mpipe_structure *caps, mpipe_dump_print_t print, void *ctx)
```

相关声明：[mpipe_dump_caps](#gae215db838d4883132d79c08d0cec3eda)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)、[mpipe_dump_print_t](#ga0215d4a9be34e7a5e58f8e11334ff507)。

在单行上呈现一个能力（Capability）。

<a id="r_gab3a73a3713a5b6fbcc961474c66f4bed"></a>

```c
const char * mpipe_dump_state_str (enum mpipe_state state)
```

相关声明：[mpipe_dump_state_str](#gab3a73a3713a5b6fbcc961474c66f4bed)、[mpipe_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga7ead9fea0963f40d4db49c8008cb3366)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

返回元素状态（Element State）的名称。

## 22.4\_详细说明（Detailed Documentation）

<a id="ga0215d4a9be34e7a5e58f8e11334ff507"></a>

### `mpipe_dump_print_t`

```c
typedef void(* mpipe_dump_print_t) (void *ctx, const char *str)
```

```c
#include <zephyr/mpipe/utils/mpipe_dump.h>
```

转储（Dump）的输出回调（Output Callback）。

转储（Dump）每次呈现一行并交给回调，因此不需要自己的缓冲区，可以写入调用者指定的任意位置，例如某个 shell 实例、控制台，或供测试进行断言的缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 传给转储的上下文（Context），原样传回。 |
| `str` | 已呈现的一行，以 NUL 终止；若呈现结果在此处包含换行符，则该行也包含它。 |

<a id="gaa128307bee2a9cdba726f4a59313a8b2"></a>

### `mpipe_dump_bin()`

```c
int mpipe_dump_bin ( struct mpipe_bin * bin, mpipe_dump_print_t print, void * ctx )
```

```c
#include <zephyr/mpipe/utils/mpipe_dump.h>
```

呈现元素容器（Bin）的拓扑（Topology）及其每个端口（Pad）的能力（Capability）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bin` | 要呈现的容器（Bin）。流水线本身也是容器，可转换为 Bins。 |
| `print` | 输出位置；若为 `NULL`，则使用 `printk()` 输出到控制台。 |
| `ctx` | 原样传给 `print`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |

<a id="gae215db838d4883132d79c08d0cec3eda"></a>

### `mpipe_dump_caps()`

```c
int mpipe_dump_caps ( const struct mpipe_structure * caps, mpipe_dump_print_t print, void * ctx )
```

```c
#include <zephyr/mpipe/utils/mpipe_dump.h>
```

在单行上呈现一个能力（Capability）。

将能力写为 `<video, format=RGBP, width=640, height=480>`，将范围写为 `[min, max, step]`，将不约束任何内容的能力写为 `<any>` 或 `<empty>`。每个能力均使用相同的分隔形式，因此即使该行后面还有其他文本，也可单独提取能力。输出末尾不添加换行符，便于调用者将其放在需要的位置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `caps` | 要呈现的能力（Capability）。 |
| `print` | 输出位置；若为 `NULL`，则使用 `printk()` 输出到控制台。 |
| `ctx` | 原样传给 `print`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |

<a id="gab3a73a3713a5b6fbcc961474c66f4bed"></a>

### `mpipe_dump_state_str()`

```c
const char * mpipe_dump_state_str ( enum mpipe_state state)
```

```c
#include <zephyr/mpipe/utils/mpipe_dump.h>
```

返回元素状态（Element State）的名称。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `state` | 要获取名称的状态（State），参见 `mpipe_state`。 |

**返回（Returns）**：**返回值（Returns）：**便于人阅读的简短名称，绝不为 `NULL`。


## 22.5\_原页交叉引用（Cross References）

- [mpipe_dump.h](../api_file_service_reference/P024_zephyr__mpipe__utils__mpipe_dump.h_文件参考.md)
- [mpipe_bin](../audio_video_model_reference/P015_mpipe_bin_结构体.md)
- [mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)
- [mpipe_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga7ead9fea0963f40d4db49c8008cb3366)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [容器（Bins）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__bin.html)
- [printk()](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html#a1bce54a738ce2d9dd6d95ee842ec237c)
- [min](../numeric_reference/P001_最小最大值与限幅宏参考.md#ac6afabdc09a49a433ee19d8a9486056d)
- [max](../numeric_reference/P001_最小最大值与限幅宏参考.md#affe776513b24d84b39af8ab0930fef7f)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P021_MFD NPM2100 接口.md) · [返回大纲](大纲.md) · [下一章](P023_管线（Pipelines）.md)
