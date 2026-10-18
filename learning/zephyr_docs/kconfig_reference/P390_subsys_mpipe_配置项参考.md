---
id: learning.zephyr-docs.kconfig-reference.page-390
title: "`subsys/mpipe`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第390章\_`subsys/mpipe`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/mpipe` 的 33 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_MPIPE"></a>

## 390.1 `CONFIG_MPIPE`

**提示（Prompt）**：多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】

**说明（Help）**

将自包含处理元素（processing elements）连接成图（graph）来构建媒体流，而不必手动连接各驱动。框架在相邻元素之间协商数据格式、确定缓冲池，并由状态机（state machine）控制缓冲区沿图流动。本选项只启用框架，具体元素位于插件（plugins）中，各有独立选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_NET_BUF
CONFIG_ZBUS
CONFIG_ZBUS_RUNTIME_OBSERVERS
CONFIG_ZBUS_RUNTIME_CHANNEL_REGISTRATION
CONFIG_EXPERIMENTAL
```

**弱选择（Implies）**

```text
CONFIG_THREAD_NAME
```

**定义位置（Location）**：[`subsys/mpipe/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_NET_BUF`](P198_lib_配置项参考_2.md#CONFIG_NET_BUF)、[`CONFIG_ZBUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZBUS)、[`CONFIG_ZBUS_RUNTIME_OBSERVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZBUS_RUNTIME_OBSERVERS)、[`CONFIG_ZBUS_RUNTIME_CHANNEL_REGISTRATION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZBUS_RUNTIME_CHANNEL_REGISTRATION)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_THREAD_NAME`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_NAME)。

<a id="CONFIG_MPIPE_BASE"></a>

## 390.2 `CONFIG_MPIPE_BASE`

**提示（Prompt）**：基础元素（Base elements）

**说明（Help）**

与媒体类型无关、用于塑造处理图而非改变数据的元素：能力过滤器（caps filter）限制链路可承载的内容；分流元素（tee）把图拆为多个分支；队列（queue）将处理分配到不同线程；应用源（application source）和应用接收端（application sink）允许应用向图注入数据并接收输出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MPIPE
```

**定义位置（Location）**：[`subsys/mpipe/base/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/base/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)。

<a id="CONFIG_MPIPE_BASE_APP_SINK"></a>

## 390.3 `CONFIG_MPIPE_BASE_APP_SINK`

**提示（Prompt）**：应用接收端元素（Application sink element）

**说明（Help）**

启用 `app_sink` 元素，通过回调或拉取 API（pull API），将到达流水线末端的缓冲区交给应用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MPIPE_BASE && CONFIG_MPIPE
```

**定义位置（Location）**：[`subsys/mpipe/base/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/base/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】 → 基础元素（Base elements）

**配置项引用（Symbol References）**：[`CONFIG_MPIPE_BASE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE_BASE)、[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)。

<a id="CONFIG_MPIPE_BASE_APP_SINK_QUEUE_DEPTH"></a>

## 390.4 `CONFIG_MPIPE_BASE_APP_SINK_QUEUE_DEPTH`

**提示（Prompt）**：app_sink 可保留用于拉取的缓冲区数量

**说明（Help）**

未设置回调时，为 `mpipe_app_sink_pull()` 排队的缓冲区数量。队列已满时，新到达的缓冲区被丢弃。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MPIPE_BASE_APP_SINK && CONFIG_MPIPE_BASE && CONFIG_MPIPE
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`subsys/mpipe/base/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/base/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】 → 基础元素（Base elements） → 应用接收端元素（Application sink element）

**配置项引用（Symbol References）**：[`CONFIG_MPIPE_BASE_APP_SINK`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE_BASE_APP_SINK)、[`CONFIG_MPIPE_BASE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE_BASE)、[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)。

<a id="CONFIG_MPIPE_BASE_APP_SRC"></a>

## 390.5 `CONFIG_MPIPE_BASE_APP_SRC`

**提示（Prompt）**：应用源元素（Application source element）

**说明（Help）**

启用 `app_src` 元素，允许应用按自身节奏将载荷（payloads）推入流水线，并显式声明流结束（end of stream）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MPIPE_BASE && CONFIG_MPIPE
```

**定义位置（Location）**：[`subsys/mpipe/base/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/base/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】 → 基础元素（Base elements）

**配置项引用（Symbol References）**：[`CONFIG_MPIPE_BASE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE_BASE)、[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)。

<a id="CONFIG_MPIPE_BASE_APP_SRC_BUF_SZ"></a>

## 390.6 `CONFIG_MPIPE_BASE_APP_SRC_BUF_SZ`

**提示（Prompt）**：app_src 元素缓冲区大小（字节）

**说明（Help）**

单次推送载荷大小的上限，用于确定静态缓冲池（static buffer pool）的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MPIPE_BASE_APP_SRC && CONFIG_MPIPE_BASE && CONFIG_MPIPE
```

**默认值（Defaults）**

```text
1024
```

**取值范围（Ranges）**

```text
[1, 262144]
```

**定义位置（Location）**：[`subsys/mpipe/base/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/base/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】 → 基础元素（Base elements） → 应用源元素（Application source element）

**配置项引用（Symbol References）**：[`CONFIG_MPIPE_BASE_APP_SRC`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE_BASE_APP_SRC)、[`CONFIG_MPIPE_BASE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE_BASE)、[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)。

<a id="CONFIG_MPIPE_BASE_APP_SRC_POOL_NUM"></a>

## 390.7 `CONFIG_MPIPE_BASE_APP_SRC_POOL_NUM`

**提示（Prompt）**：app_src 池的缓冲区数量

**说明（Help）**

所有 `app_src` 元素共享的池中的缓冲区数量，即允许同时处于处理中的已推送载荷数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MPIPE_BASE_APP_SRC && CONFIG_MPIPE_BASE && CONFIG_MPIPE
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`subsys/mpipe/base/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/base/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】 → 基础元素（Base elements） → 应用源元素（Application source element）

**配置项引用（Symbol References）**：[`CONFIG_MPIPE_BASE_APP_SRC`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE_BASE_APP_SRC)、[`CONFIG_MPIPE_BASE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE_BASE)、[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)。

<a id="CONFIG_MPIPE_BASE_APP_SRC_QUEUE_DEPTH"></a>

## 390.8 `CONFIG_MPIPE_BASE_APP_SRC_QUEUE_DEPTH`

**提示（Prompt）**：app_src 可提前排队的载荷数量

**说明（Help）**

推送操作发生阻塞之前，可排队等待流水线线程处理的已推送载荷数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MPIPE_BASE_APP_SRC && CONFIG_MPIPE_BASE && CONFIG_MPIPE
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`subsys/mpipe/base/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/base/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】 → 基础元素（Base elements） → 应用源元素（Application source element）

**配置项引用（Symbol References）**：[`CONFIG_MPIPE_BASE_APP_SRC`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE_BASE_APP_SRC)、[`CONFIG_MPIPE_BASE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE_BASE)、[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)。

<a id="CONFIG_MPIPE_BASE_CAPS_FILTER"></a>

## 390.9 `CONFIG_MPIPE_BASE_CAPS_FILTER`

**提示（Prompt）**：能力过滤器元素（Caps filter element）

**说明（Help）**

启用 `caps_filter` 元素，约束其所在链路上协商的数据格式（format）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MPIPE_BASE && CONFIG_MPIPE
```

**定义位置（Location）**：[`subsys/mpipe/base/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/base/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】 → 基础元素（Base elements）

**配置项引用（Symbol References）**：[`CONFIG_MPIPE_BASE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE_BASE)、[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)。

<a id="CONFIG_MPIPE_BASE_QUEUE"></a>

## 390.10 `CONFIG_MPIPE_BASE_QUEUE`

**提示（Prompt）**：队列元素，用于流水线级线程划分（Queue element）

**说明（Help）**

启用队列（queue）元素，将其下游元素放在独立线程上运行，该线程计入 `MPIPE_THREADS_NUM`。队列满时，默认阻塞生产者（producer）；采用丢弃策略（leak policy）时，则丢弃最旧或新到达的缓冲区。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MPIPE_BASE && CONFIG_MPIPE
```

**定义位置（Location）**：[`subsys/mpipe/base/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/base/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】 → 基础元素（Base elements）

**配置项引用（Symbol References）**：[`CONFIG_MPIPE_BASE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE_BASE)、[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)。

<a id="CONFIG_MPIPE_BASE_QUEUE_MAX_SIZE"></a>

## 390.11 `CONFIG_MPIPE_BASE_QUEUE_MAX_SIZE`

**提示（Prompt）**：队列元素最大大小（Max size）

**说明（Help）**

队列元素可容纳的缓冲区数量上限。每个元素通过其 `size` 属性设置大小，本项同时也是默认值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MPIPE_BASE_QUEUE && CONFIG_MPIPE_BASE && CONFIG_MPIPE
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/mpipe/base/Kconfig:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/base/Kconfig#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】 → 基础元素（Base elements） → 队列元素，用于流水线级线程划分（Queue element）

**配置项引用（Symbol References）**：[`CONFIG_MPIPE_BASE_QUEUE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE_BASE_QUEUE)、[`CONFIG_MPIPE_BASE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE_BASE)、[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)。

<a id="CONFIG_MPIPE_BASE_TEE"></a>

## 390.12 `CONFIG_MPIPE_BASE_TEE`

**提示（Prompt）**：分流元素（Tee element）

**说明（Help）**

启用 `tee` 元素，将单个输入分支拆为多个输出分支。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MPIPE_BASE && CONFIG_MPIPE
```

**定义位置（Location）**：[`subsys/mpipe/base/Kconfig:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/base/Kconfig#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】 → 基础元素（Base elements）

**配置项引用（Symbol References）**：[`CONFIG_MPIPE_BASE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE_BASE)、[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)。

<a id="CONFIG_MPIPE_BASE_TEE_MAX_SRC_PADS_NUM"></a>

## 390.13 `CONFIG_MPIPE_BASE_TEE_MAX_SRC_PADS_NUM`

**提示（Prompt）**：分流元素源连接端口数量上限（source pads）

**说明（Help）**

`tee` 元素的源连接端口（source pads）数量上限，每个元素通过其属性设置实际数量。系统会为全部上限数量预留存储空间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MPIPE_BASE_TEE && CONFIG_MPIPE_BASE && CONFIG_MPIPE
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[2, 8]
```

**定义位置（Location）**：[`subsys/mpipe/base/Kconfig:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/base/Kconfig#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】 → 基础元素（Base elements） → 分流元素（Tee element）

**配置项引用（Symbol References）**：[`CONFIG_MPIPE_BASE_TEE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE_BASE_TEE)、[`CONFIG_MPIPE_BASE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE_BASE)、[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)。

<a id="CONFIG_MPIPE_BIN_MAX_CHILDREN"></a>

## 390.14 `CONFIG_MPIPE_BIN_MAX_CHILDREN`

**提示（Prompt）**：元素容器／流水线中的元素数量上限（bin/pipeline）

**说明（Help）**

单个元素容器（bin）或流水线（pipeline）内的最大元素数量，用于确定状态切换时拓扑排序（topological sort）所用数组大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MPIPE
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[2, 64]
```

**定义位置（Location）**：[`subsys/mpipe/Kconfig:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/Kconfig#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)。

<a id="CONFIG_MPIPE_DUMP"></a>

## 390.15 `CONFIG_MPIPE_DUMP`

**提示（Prompt）**：流水线拓扑转储（Pipeline topology dump）

**说明（Help）**

将元素容器（bin）渲染为 Graphviz 图用于调试，包含每个元素及其状态和连接端口（pads），各端口的对端，以及在链路上协商的能力（capability）。DOT 文本通过回调输出，默认写入控制台。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MPIPE
```

**主动选择（Selects）**

```text
CONFIG_MPIPE_ELEMENT_NAME
```

**定义位置（Location）**：[`subsys/mpipe/utils/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/utils/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)、[`CONFIG_MPIPE_ELEMENT_NAME`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE_ELEMENT_NAME)。

<a id="CONFIG_MPIPE_DUMP_MAX_ELEMENTS"></a>

## 390.16 `CONFIG_MPIPE_DUMP_MAX_ELEMENTS`

**提示（Prompt）**：拓扑转储可索引的最大元素数量

**说明（Help）**

转储会展开嵌套的元素容器（bins），因此可能包含超过单个容器 `MPIPE_BIN_MAX_CHILDREN` 限制的元素数量。超过本项上限的元素不会纳入图中，转储会标记为已截断（truncated）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MPIPE_DUMP && CONFIG_MPIPE
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[2, 256]
```

**定义位置（Location）**：[`subsys/mpipe/utils/Kconfig:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/utils/Kconfig#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】 → 流水线拓扑转储（Pipeline topology dump）

**配置项引用（Symbol References）**：[`CONFIG_MPIPE_DUMP`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE_DUMP)、[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)。

<a id="CONFIG_MPIPE_ELEMENT_NAME"></a>

## 390.17 `CONFIG_MPIPE_ELEMENT_NAME`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为每个元素保留名称，供打印名称的调试工具使用。由这些工具自动选择，不应手动设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MPIPE
```

**被选择（Selected by）**

```text
CONFIG_MPIPE_DUMP
```

**定义位置（Location）**：[`subsys/mpipe/Kconfig:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/Kconfig#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)、[`CONFIG_MPIPE_DUMP`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE_DUMP)。

<a id="CONFIG_MPIPE_FAKE_SRC"></a>

## 390.18 `CONFIG_MPIPE_FAKE_SRC`

**提示（Prompt）**：模拟源元素（Fake source element）

**说明（Help）**

生成合成数据缓冲区、不绑定任何设备的源（source）。在真实源需要硬件的场景下，它仍能构建并运行处理图，框架自身的测试即用于此目的。不打算用于实际应用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MPIPE
```

**定义位置（Location）**：[`subsys/mpipe/Kconfig:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/Kconfig#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)。

<a id="CONFIG_MPIPE_FAKE_SRC_BUF_SZ"></a>

## 390.19 `CONFIG_MPIPE_FAKE_SRC_BUF_SZ`

**提示（Prompt）**：模拟源元素缓冲区大小（字节）

**说明（Help）**

模拟源每次生成的缓冲区大小，单位为字节。默认 `1` 字节足以测试数据在图中的流动；测试需要接近实际大小的缓冲区时，可增大此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MPIPE_FAKE_SRC && CONFIG_MPIPE
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 1024]
```

**定义位置（Location）**：[`subsys/mpipe/Kconfig:128`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/Kconfig#L128)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】 → 模拟源元素（Fake source element）

**配置项引用（Symbol References）**：[`CONFIG_MPIPE_FAKE_SRC`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE_FAKE_SRC)、[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)。

<a id="CONFIG_MPIPE_NET_BUF_POOL_COUNT"></a>

## 390.20 `CONFIG_MPIPE_NET_BUF_POOL_COUNT`

**提示（Prompt）**：mpipe 共享 net_buf 池的缓冲区数量

**说明（Help）**

所有流水线共享池中的 `net_buf` 缓冲区数量，即各流水线允许同时在途（in flight）的缓冲区数量之和。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MPIPE
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 1024]
```

**定义位置（Location）**：[`subsys/mpipe/Kconfig:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/Kconfig#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)。

<a id="CONFIG_MPIPE_PLAYER"></a>

## 390.21 `CONFIG_MPIPE_PLAYER`

**提示（Prompt）**：多媒体流水线播放器辅助层（Multimedia Pipeline player helper）

**说明（Help）**

启用 `mpipe_player` 控制层。它是可复用、类似媒体播放器的辅助组件，负责流水线运行时生命周期：播放（play）、暂停（pause）、停止（stop）、重播（replay）及退出（quit）。启用 `SHELL` 时，还注册交互式命令 `player play|pause|stop|replay|quit|status`，以及单字符快捷命令 `p/s/r/q`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MPIPE && CONFIG_MPIPE
```

**弱选择（Implies）**

```text
CONFIG_SHELL
CONFIG_SERIAL
CONFIG_UART_CONSOLE
```

**定义位置（Location）**：[`subsys/mpipe/utils/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/utils/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)、[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UART_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_UART_CONSOLE)。

<a id="CONFIG_MPIPE_PLAYER_CMD_QUEUE_DEPTH"></a>

## 390.22 `CONFIG_MPIPE_PLAYER_CMD_QUEUE_DEPTH`

**提示（Prompt）**：播放器命令队列深度（command queue depth）

**说明（Help）**

播放器可以缓冲的待处理命令数量。提交命令从不阻塞，因此队列满后请求的命令会被丢弃并报告。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MPIPE_PLAYER && CONFIG_MPIPE
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`subsys/mpipe/utils/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/utils/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】 → 多媒体流水线播放器辅助层（Multimedia Pipeline player helper）

**配置项引用（Symbol References）**：[`CONFIG_MPIPE_PLAYER`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE_PLAYER)、[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)。

<a id="CONFIG_MPIPE_PLAYER_DUMP_ON_STATE_CHANGE"></a>

## 390.23 `CONFIG_MPIPE_PLAYER_DUMP_ON_STATE_CHANGE`

**提示（Prompt）**：每次状态改变和发生错误时转储流水线

**说明（Help）**

播放器每次完成一次状态转换后，以及任一元素报告错误时，打印流水线。转储只在转换结束后进行，绝不插在转换过程中，因此不会拖延转换；失败时，流水线停留在出错的位置，图仍反映该次失败的状态。此时不存在命令行实例，所以输出到控制台（console），而非命令行（shell）。可从捕获的日志中提取图：

```sh
sed -n '/^digraph/,/^}/p' log > pipe.dot
```

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MPIPE_DUMP && CONFIG_MPIPE_PLAYER && CONFIG_MPIPE
```

**定义位置（Location）**：[`subsys/mpipe/utils/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/utils/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】 → 多媒体流水线播放器辅助层（Multimedia Pipeline player helper）

**配置项引用（Symbol References）**：[`CONFIG_MPIPE_DUMP`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE_DUMP)、[`CONFIG_MPIPE_PLAYER`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE_PLAYER)、[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)。

<a id="CONFIG_MPIPE_PLAYER_WORKER_PRIORITY"></a>

## 390.24 `CONFIG_MPIPE_PLAYER_WORKER_PRIORITY`

**提示（Prompt）**：播放器工作线程优先级（worker thread priority）

**说明（Help）**

播放器工作线程的调度优先级（scheduling priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MPIPE_PLAYER && CONFIG_MPIPE
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`subsys/mpipe/utils/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/utils/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】 → 多媒体流水线播放器辅助层（Multimedia Pipeline player helper）

**配置项引用（Symbol References）**：[`CONFIG_MPIPE_PLAYER`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE_PLAYER)、[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)。

<a id="CONFIG_MPIPE_PLAYER_WORKER_STACK_SIZE"></a>

## 390.25 `CONFIG_MPIPE_PLAYER_WORKER_STACK_SIZE`

**提示（Prompt）**：播放器工作线程栈大小（stack size）

**说明（Help）**

负责串行化流水线状态切换的播放器工作线程栈大小，单位为字节。能力协商（capability negotiation）在此线程上运行，从源递归到各接收端（sinks）。每个元素在协商期间保持若干活动能力数据，约占 800 字节，应据此为每个元素预留空间。默认值适用于约七个元素以内的链路，较长流水线应增大栈。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MPIPE_PLAYER && CONFIG_MPIPE
```

**默认值（Defaults）**

```text
6144
```

**定义位置（Location）**：[`subsys/mpipe/utils/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/utils/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】 → 多媒体流水线播放器辅助层（Multimedia Pipeline player helper）

**配置项引用（Symbol References）**：[`CONFIG_MPIPE_PLAYER`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE_PLAYER)、[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)。

<a id="CONFIG_MPIPE_RPC"></a>

## 390.26 `CONFIG_MPIPE_RPC`

**提示（Prompt）**：变换客户端元素，远程处理（Transform client elements）

**说明（Help）**

构建在另一核心而非本地执行处理的客户端元素。变换客户端（transform client）在图中看起来像普通元素，但通过传输通道把各缓冲区转发给远程核心上的服务器，并等待结果。此处不提供传输实现，由应用通过元素的远程过程调用（RPC）钩子提供。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MPIPE
```

**定义位置（Location）**：[`subsys/mpipe/Kconfig:138`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/Kconfig#L138)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)。

<a id="CONFIG_MPIPE_STRUCTURE_MAX_FIELDS"></a>

## 390.27 `CONFIG_MPIPE_STRUCTURE_MAX_FIELDS`

**提示（Prompt）**：单个能力结构体可容纳的最大字段数（caps structure）

**说明（Help）**

单个能力结构体（caps structure）同时容纳的能力字段数量。应按一次求交（intersection）过程中可能遇到的最大字段并集设置，而不是只按某元素设置的字段数量。求交时槽位不足，会返回 `-ENOSPC`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MPIPE
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/mpipe/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)。

<a id="CONFIG_MPIPE_THREADS_NUM"></a>

## 390.28 `CONFIG_MPIPE_THREADS_NUM`

**提示（Prompt）**：流处理线程数量（Number of streaming threads）

**说明（Help）**

框架使用的线程栈池大小。线程终止后，其栈归还池中，供下一个线程复用。每条可同时运行的流水线需要一个栈，每个队列元素还额外需要一个。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MPIPE
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/mpipe/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)。

<a id="CONFIG_MPIPE_THREAD_DEFAULT_PRIORITY"></a>

## 390.29 `CONFIG_MPIPE_THREAD_DEFAULT_PRIORITY`

**提示（Prompt）**：流处理线程优先级（streaming thread priority）

**说明（Help）**

创建流处理线程时使用的 Zephyr 调度优先级，应高于流水线所供给的工作，使下游元素消费数据时，源仍可持续生产数据。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MPIPE
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`subsys/mpipe/Kconfig:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/Kconfig#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)。

<a id="CONFIG_MPIPE_THREAD_STACK_SIZE"></a>

## 390.30 `CONFIG_MPIPE_THREAD_STACK_SIZE`

**提示（Prompt）**：流处理线程栈大小（streaming thread stack size）

**说明（Help）**

每个流水线或队列元素的流处理线程栈大小，单位为字节。流处理线程只获取缓冲区并向下游推送；能力协商在驱动状态切换的线程上执行，不在此线程上执行。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MPIPE
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/mpipe/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)。

<a id="CONFIG_MPIPE_WORKQUEUE"></a>

## 390.31 `CONFIG_MPIPE_WORKQUEUE`

**提示（Prompt）**：元素级工作卸载（Element-level work offload，P4WQ）

**说明（Help）**

允许元素将解码或推理等有限工作项（finite work items）卸载到共享的池化、并行、可抢占、基于优先级的工作队列（Pooled Parallel Preemptible Priority-based Work Queue，P4WQ）线程池，每个工作项具有独立优先级。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MPIPE
```

**主动选择（Selects）**

```text
CONFIG_SCHED_DEADLINE
```

**定义位置（Location）**：[`subsys/mpipe/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)、[`CONFIG_SCHED_DEADLINE`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_DEADLINE)。

<a id="CONFIG_MPIPE_WORKQUEUE_STACK_SIZE"></a>

## 390.32 `CONFIG_MPIPE_WORKQUEUE_STACK_SIZE`

**提示（Prompt）**：mpipe 工作队列池线程的栈大小

**说明（Help）**

mpipe 工作队列池中每个线程的栈大小，单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MPIPE_WORKQUEUE && CONFIG_MPIPE
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`subsys/mpipe/Kconfig:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/Kconfig#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】 → 元素级工作卸载（Element-level work offload，P4WQ）

**配置项引用（Symbol References）**：[`CONFIG_MPIPE_WORKQUEUE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE_WORKQUEUE)、[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)。

<a id="CONFIG_MPIPE_WORKQUEUE_THREADS_NUM"></a>

## 390.33 `CONFIG_MPIPE_WORKQUEUE_THREADS_NUM`

**提示（Prompt）**：mpipe 工作队列池线程数量

**说明（Help）**

共享 P4WQ 池中的线程数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MPIPE_WORKQUEUE && CONFIG_MPIPE
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`subsys/mpipe/Kconfig:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mpipe/Kconfig#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】 → 元素级工作卸载（Element-level work offload，P4WQ）

**配置项引用（Symbol References）**：[`CONFIG_MPIPE_WORKQUEUE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE_WORKQUEUE)、[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)。

<!-- kconfig-navigation -->

[上一章](P389_subsys_modem_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P391_subsys_net_配置项参考_1.md)
