---
id: learning.zephyr-docs.api-buffer-paging-topic-reference.page-16
title: 多路复用器（MUX）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mux__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_多路复用器（MUX）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mux__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MUX 控制器接口（MUX Controller Interface）

<a id="details"></a>

多路复用器控制器接口（MUX Controller Interface）。用于多路复用器，即信号路由控制器的通用设备模型。设备树模型源自 Linux，但本子系统明确不提供共享线路仲裁（Shared-line Arbitration）：没有 mux_control_select()/deselect()，也没有针对各控制线路的并发锁。假定每条控制线路只有一个所有者；多个使用者并发驱动同一线路时，彼此之间没有保护。引入版本（Since）：4.5；API 版本（Version）：0.1.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 16.1\_主题（Topics）

<a id="r_devicetree-mux"></a>

相关声明：[设备树多路复用器接口（Devicetree MUX API）](../dt_connection_reference/P007_设备树多路复用器宏.md)。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 16.2\_数据结构（Data Structures）

<a id="r_mux_5Fcontrol"></a>

```c
struct mux_control
```

相关声明：[mux_control](../peripheral_bus_storage_model_reference/P052_mux_control_结构体.md)。

单条多路复用器（MUX）控制线仅用于寻址的说明符。

<a id="r_mux_5Fstate"></a>

```c
struct mux_state
```

相关声明：[mux_state](../peripheral_bus_storage_model_reference/P054_mux_state_结构体.md)。

多路复用器（MUX）控制线的寻址与默认状态对。

<a id="r_mux_5Fcontrol_5Fdriver_5Fapi"></a>

```c
struct mux_control_driver_api
```

相关声明：[mux_control_driver_api](../peripheral_bus_storage_model_reference/P053_mux_control_driver_api_结构体.md)。

多路复用器（MUX）控制器驱动API。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 16.3\_宏定义（Macros）

<a id="r_ga1fcf4fd9a94643c1b778994f76b64150"></a>

```c
#define MUX_CONTROL_DT_SPEC_DEFINE_BY_IDX(node_id, idx)
```

相关声明：[MUX_CONTROL_DT_SPEC_DEFINE_BY_IDX](#ga1fcf4fd9a94643c1b778994f76b64150)。

根据 `mux-controls` 条目定义 `mux_control` 对象。

<a id="r_ga076e92976afbf9ecf39cf8536e6e31a6"></a>

```c
#define MUX_CONTROL_DT_SPEC_DEFINE(node_id)
```

相关声明：[MUX_CONTROL_DT_SPEC_DEFINE](#ga076e92976afbf9ecf39cf8536e6e31a6)。

等同于 `MUX_CONTROL_DT_SPEC_DEFINE_BY_IDX(node_id, 0)`。

<a id="r_ga332c39734d3dff70067278d29e2875b3"></a>

```c
#define MUX_CONTROL_DT_SPEC_DEFINE_BY_NAME(node_id, name)
```

相关声明：[MUX_CONTROL_DT_SPEC_DEFINE_BY_NAME](#ga332c39734d3dff70067278d29e2875b3)。

根据 `mux-control-names` 条目按名称定义 `mux_control` 对象。

<a id="r_gac162201caf07686e7c9c8cd736ebf7e2"></a>

```c
#define MUX_STATE_DT_SPEC_DEFINE_BY_IDX(node_id, idx)
```

相关声明：[MUX_STATE_DT_SPEC_DEFINE_BY_IDX](#gac162201caf07686e7c9c8cd736ebf7e2)。

根据 `mux-states` 条目定义 `mux_state` 对象。

<a id="r_gacd33ebfd1ef975152505d5ba800fd184"></a>

```c
#define MUX_STATE_DT_SPEC_DEFINE(node_id)
```

相关声明：[MUX_STATE_DT_SPEC_DEFINE](#gacd33ebfd1ef975152505d5ba800fd184)。

等同于 `MUX_STATE_DT_SPEC_DEFINE_BY_IDX(node_id, 0)`。

<a id="r_gad42cfa2560136a306b1409c4fa64596a"></a>

```c
#define MUX_STATE_DT_SPEC_DEFINE_BY_NAME(node_id, name)
```

相关声明：[MUX_STATE_DT_SPEC_DEFINE_BY_NAME](#gad42cfa2560136a306b1409c4fa64596a)。

根据 `mux-state-names` 条目按名称定义 `mux_state` 对象。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 16.4\_函数（Functions）

<a id="r_ga69b883de5e7c90f797d5a07063089bbc"></a>

```c
int mux_control_set (const struct device *dev, const struct mux_control *control, uint32_t state)
```

相关声明：[mux_control_set](#ga69b883de5e7c90f797d5a07063089bbc)、[device](../device_reference/P002_设备对象结构.md)、[mux_control](../peripheral_bus_storage_model_reference/P052_mux_control_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

将 MUX 控制线驱动到给定状态。

<a id="r_gad1b56b4430fca99f03bdf2b0ad6725c5"></a>

```c
int mux_state_apply (const struct device *dev, const struct mux_state *mstate)
```

相关声明：[mux_state_apply](#gad1b56b4430fca99f03bdf2b0ad6725c5)、[device](../device_reference/P002_设备对象结构.md)、[mux_state](../peripheral_bus_storage_model_reference/P054_mux_state_结构体.md)。

将设备树定义的默认状态应用于多路复用器（MUX）控制线。

<a id="r_ga188b04add235e080b95ea293e7cfd276"></a>

```c
int mux_state_get (const struct device *dev, const struct mux_control *control, uint32_t *state)
```

相关声明：[mux_state_get](#ga188b04add235e080b95ea293e7cfd276)、[device](../device_reference/P002_设备对象结构.md)、[mux_control](../peripheral_bus_storage_model_reference/P052_mux_control_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

读回 MUX 控制线的当前状态。

<a id="r_ga0e3cbbb7ac8796c3651b56c41dd1cec5"></a>

```c
int mux_control_disconnect (const struct device *dev, const struct mux_control *control)
```

相关声明：[mux_control_disconnect](#ga0e3cbbb7ac8796c3651b56c41dd1cec5)、[device](../device_reference/P002_设备对象结构.md)、[mux_control](../peripheral_bus_storage_model_reference/P052_mux_control_结构体.md)。

物理断开 MUX 控制线。

## 16.5\_详细说明（Detailed Documentation）

<a id="ga076e92976afbf9ecf39cf8536e6e31a6"></a>

### `MUX_CONTROL_DT_SPEC_DEFINE`

```c
#define MUX_CONTROL_DT_SPEC_DEFINE ( node_id)
```

```c
#include <zephyr/drivers/mux.h>
```

展开值（Value）：

```c
MUX_CONTROL_DT_SPEC_DEFINE_BY_IDX(node_id, 0)
```

等同于 `MUX_CONTROL_DT_SPEC_DEFINE_BY_IDX(node_id, 0)`。

设备树片段示例：

原始示例（Example）：

```c
n: node {
        mux-controls = <&mux0 5>;
};
```

使用示例：

原始示例（Example）：

```c
MUX_CONTROL_DT_SPEC_DEFINE(DT_NODELABEL(n));
const struct mux_control *m = MUX_CONTROL_DT_GET(DT_NODELABEL(n));
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 消费节点（Consumer）的设备树节点标识符。 |

另见（See Also）：MUX_CONTROL_DT_SPEC_DEFINE_BY_IDX()。

<a id="ga1fcf4fd9a94643c1b778994f76b64150"></a>

### `MUX_CONTROL_DT_SPEC_DEFINE_BY_IDX`

```c
#define MUX_CONTROL_DT_SPEC_DEFINE_BY_IDX ( node_id, idx )
```

```c
#include <zephyr/drivers/mux.h>
```

展开值（Value）：

```c
Z_MUX_CTRL_DEFINE_BY_IDX(node_id, idx)
```

根据 `mux-controls` 条目定义 `mux_control` 对象。

在文件作用域（File Scope）生成 cells 数组及引用该数组的 mux_control 对象的存储。配合 MUX_CONTROL_DT_GET_BY_IDX()（声明于 `<zephyr/devicetree/mux.h>`）获取指针。

必须在文件作用域（File Scope）调用。每个 idx 只能定义一次，以免重复生成存储。

设备树片段示例（Devicetree Fragment），以一个假想的多通道后端为例：

原始示例（Example）：

```c
mux0: mux-controller@... {
        compatible = "vendor,demux";
        #mux-control-cells = <1>;
        ...
};

n: node {
        mux-controls = <&mux0 5>, <&mux0 7>;
};
```

使用示例：

原始示例（Example）：

```c
MUX_CONTROL_DT_SPEC_DEFINE_BY_IDX(DT_NODELABEL(n), 0);
MUX_CONTROL_DT_SPEC_DEFINE_BY_IDX(DT_NODELABEL(n), 1);

const struct mux_control *m0 = MUX_CONTROL_DT_GET_BY_IDX(DT_NODELABEL(n), 0);
const struct device *d  = MUX_CONTROL_DT_DEV_GET_BY_IDX(DT_NODELABEL(n), 0);
mux_control_set(d, m0, 1);  // drive channel 5 to state 1
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 消费节点（Consumer）的设备树节点标识符。 |
| `idx` | mux-controls属性中的逻辑索引。 |

另见（See Also）：MUX_CONTROL_DT_GET_BY_IDX()。

<a id="ga332c39734d3dff70067278d29e2875b3"></a>

### `MUX_CONTROL_DT_SPEC_DEFINE_BY_NAME`

```c
#define MUX_CONTROL_DT_SPEC_DEFINE_BY_NAME ( node_id, name )
```

```c
#include <zephyr/drivers/mux.h>
```

展开值（Value）：

```c
MUX_CONTROL_DT_SPEC_DEFINE_BY_IDX(node_id,        \
        DT_PHA_ELEM_IDX_BY_NAME(node_id, mux_controls, name))
```

根据 `mux-control-names` 条目按名称定义 `mux_control` 对象。

等价于 MUX_CONTROL_DT_SPEC_DEFINE_BY_IDX()，但索引由 mux-control-names 属性解析得到。

设备树片段示例：

原始示例（Example）：

```c
n: node {
        mux-controls = <&mux0 5>, <&mux0 7>;
        mux-control-names = "phase_a", "phase_b";
};
```

使用示例：

原始示例（Example）：

```c
MUX_CONTROL_DT_SPEC_DEFINE_BY_NAME(DT_NODELABEL(n), phase_a);
const struct mux_control *ma =
        MUX_CONTROL_DT_GET_BY_NAME(DT_NODELABEL(n), phase_a);
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 消费节点（Consumer）的设备树节点标识符。 |
| `name` | mux-control-names属性中的名称，使用小写加下划线形式。 |

**参阅（See Also）**：另请参阅（See Also）：MUX_CONTROL_DT_GET_BY_NAME()。

<a id="gacd33ebfd1ef975152505d5ba800fd184"></a>

### `MUX_STATE_DT_SPEC_DEFINE`

```c
#define MUX_STATE_DT_SPEC_DEFINE ( node_id)
```

```c
#include <zephyr/drivers/mux.h>
```

展开值（Value）：

```c
MUX_STATE_DT_SPEC_DEFINE_BY_IDX(node_id, 0)
```

等同于 `MUX_STATE_DT_SPEC_DEFINE_BY_IDX(node_id, 0)`。

设备树片段示例：

原始示例（Example）：

```c
n: node {
        mux-states = <&mux0 5 2>;
};
```

使用示例：

原始示例（Example）：

```c
MUX_STATE_DT_SPEC_DEFINE(DT_NODELABEL(n));
const struct mux_state *s = MUX_STATE_DT_GET(DT_NODELABEL(n));
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 消费节点（Consumer）的设备树节点标识符。 |

另见（See Also）：MUX_STATE_DT_SPEC_DEFINE_BY_IDX()。

<a id="gac162201caf07686e7c9c8cd736ebf7e2"></a>

### `MUX_STATE_DT_SPEC_DEFINE_BY_IDX`

```c
#define MUX_STATE_DT_SPEC_DEFINE_BY_IDX ( node_id, idx )
```

```c
#include <zephyr/drivers/mux.h>
```

展开值（Value）：

```c
Z_MUX_STATE_DEFINE_BY_IDX(node_id, idx)
```

根据 `mux-states` 条目定义 `mux_state` 对象。

在文件作用域（File Scope）生成寻址单元（Addressing Cells）、内嵌 mux_control 及 mux_state 的存储。说明符前面的单元构成寻址部分 mux_state.control->cells，最后一个单元成为 mux_state.state。

必须在文件作用域（File Scope）调用。每个 idx 只能定义一次，以免重复生成存储。

设备树片段示例（Devicetree Fragment），以一个假想的多通道后端为例：

原始示例（Example）：

```c
mux0: mux-controller@... {
        compatible = "vendor,demux";
        #mux-control-cells = <1>;
        #mux-state-cells   = <2>;
        ...
};

n: node {
        // <controller channel state>
        mux-states = <&mux0 5 2>, <&mux0 7 3>;
};
```

使用示例：

原始示例（Example）：

```c
MUX_STATE_DT_SPEC_DEFINE_BY_IDX(DT_NODELABEL(n), 0);

const struct mux_state *s0 = MUX_STATE_DT_GET_BY_IDX(DT_NODELABEL(n), 0);
// s0->control->cells[0] == 5, s0->state == 2
mux_state_apply(MUX_STATE_DT_DEV_GET_BY_IDX(DT_NODELABEL(n), 0), s0);
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 消费节点（Consumer）的设备树节点标识符。 |
| `idx` | mux-states属性中的逻辑索引。 |

**参阅（See Also）**：另请参阅（See Also）：MUX_STATE_DT_GET_BY_IDX()、mux_state_apply()。

<a id="gad42cfa2560136a306b1409c4fa64596a"></a>

### `MUX_STATE_DT_SPEC_DEFINE_BY_NAME`

```c
#define MUX_STATE_DT_SPEC_DEFINE_BY_NAME ( node_id, name )
```

```c
#include <zephyr/drivers/mux.h>
```

展开值（Value）：

```c
MUX_STATE_DT_SPEC_DEFINE_BY_IDX(node_id,        \
        DT_PHA_ELEM_IDX_BY_NAME(node_id, mux_states, name))
```

根据 `mux-state-names` 条目按名称定义 `mux_state` 对象。

等价于 MUX_STATE_DT_SPEC_DEFINE_BY_IDX()，但索引由 mux-state-names 属性解析得到。

设备树片段示例：

原始示例（Example）：

```c
n: node {
        mux-states      = <&mux0 5 2>, <&mux0 7 3>;
        mux-state-names = "default", "alt";
};
```

使用示例：

原始示例（Example）：

```c
MUX_STATE_DT_SPEC_DEFINE_BY_NAME(DT_NODELABEL(n), default);
const struct mux_state *def =
        MUX_STATE_DT_GET_BY_NAME(DT_NODELABEL(n), default);
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 消费节点（Consumer）的设备树节点标识符。 |
| `name` | mux-state-names属性中的名称，使用小写加下划线形式。 |

**参阅（See Also）**：另请参阅（See Also）：MUX_STATE_DT_GET_BY_NAME()。

<a id="ga0e3cbbb7ac8796c3651b56c41dd1cec5"></a>

### `mux_control_disconnect()`

```c
int mux_control_disconnect ( const struct device * dev, const struct mux_control * control )
```

```c
#include <zephyr/drivers/mux.h>
```

物理断开 MUX 控制线。

将指定控制线路置于断开／关闭状态（Open/Off State），此时不路由任何输入。达到该状态的方式由后端决定：可以是一个专用使能门（如使能引脚），锁存先前选定的路由以供重新连接；也可以是开关阵列的全断开状态，即关闭所有底层开关。后续 mux_control_set() 会重新连接线路并应用所请求的路由；不存在单独的重新连接操作。

影响范围恰好是后端设备树绑定为指定控制线路建模的路由单元。若后端将每个通道暴露为独立控制线路，则只断开指定通道；若后端将整个设备建模为单条控制线路（#mux-control-cells = 0），则断开整个设备。

可选操作（Optional Operation）。无法达到断开状态的后端（例如没有使能线、始终输出某种模式的普通 GPIO 选择总线）将 disconnect 操作留为 NULL，此时返回 -ENOSYS。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | MUX 控制器设备（Controller Device）。 |
| `control` | 待断开控制线路的寻址信息（Addressing）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOSYS` | 驱动未实现此操作，或此实例不具备断开能力时。 |
| `-EINVAL` | 寻址超出范围时。 |
| `-errno` | 失败时返回其他负 errno 错误码。 |

<a id="ga69b883de5e7c90f797d5a07063089bbc"></a>

### `mux_control_set()`

```c
int mux_control_set ( const struct device * dev, const struct mux_control * control, uint32_t state )
```

```c
#include <zephyr/drivers/mux.h>
```

将 MUX 控制线驱动到给定状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | MUX 控制器设备（Controller Device）。 |
| `control` | 待驱动控制线路的寻址信息（Addressing）。 |
| `state` | 目标状态值（Target State Value）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | 寻址或状态超出范围时。 |
| `-EACCES` | 控制线路已锁定时。 |
| `-errno` | 失败时返回其他负 errno 错误码。 |

<a id="gad1b56b4430fca99f03bdf2b0ad6725c5"></a>

### `mux_state_apply()`

```c
int mux_state_apply ( const struct device * dev, const struct mux_state * mstate )
```

```c
#include <zephyr/drivers/mux.h>
```

将设备树定义的默认状态应用于多路复用器（MUX）控制线。

供 mux-states 使用者调用的便捷接口：从 mstate 提取默认状态（Default State），并转交 mux_control_set()。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | MUX 控制器设备（Controller Device）。 |
| `mstate` | 寻址信息与默认状态的配对（Addressing + Default State Pair）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-errno` | 失败时返回负的错误编号（errno）。 |

<a id="ga188b04add235e080b95ea293e7cfd276"></a>

### `mux_state_get()`

```c
int mux_state_get ( const struct device * dev, const struct mux_control * control, uint32_t * state )
```

```c
#include <zephyr/drivers/mux.h>
```

读回 MUX 控制线的当前状态。

可选操作（Optional Operation）：无法回读路由状态的硬件将 get_state 操作留为 NULL，此时返回 -ENOSYS。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | MUX 控制器设备（Controller Device）。 |
| `control` | 待查询控制线路的寻址信息（Addressing）。 |
| `state` | 输出：当前状态值，仅在成功时有效。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOSYS` | 驱动未实现此操作时。 |
| `-EINVAL` | 寻址超出范围时。 |
| `-errno` | 失败时返回其他负 errno 错误码。 |


## 16.6\_原页交叉引用（Cross References）

- [设备树多路复用器接口（Devicetree MUX API）](../dt_connection_reference/P007_设备树多路复用器宏.md)
- [mux_control](../peripheral_bus_storage_model_reference/P052_mux_control_结构体.md)
- [mux_state](../peripheral_bus_storage_model_reference/P054_mux_state_结构体.md)
- [mux_control_driver_api](../peripheral_bus_storage_model_reference/P053_mux_control_driver_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [zephyr/drivers/mux.h](../peripheral_bus_storage_header_reference/P019_zephyr__drivers__mux.h_头文件参考.md)
- [MUX_CONTROL_DT_GET_BY_IDX()](../dt_connection_reference/P007_设备树多路复用器宏.md#gac7963189437a884c05c3b142d0e911ad)
- [zephyr/devicetree/mux.h](../dt_connection_reference/P008_设备树多路复用器头文件参考.md)
- [DT_PHA_ELEM_IDX_BY_NAME](../dt_identity_reference/P002_设备树存在性与状态宏.md#gadd50cff371a4e44a49324c3c682b58b1)
- [MUX_CONTROL_DT_GET_BY_NAME()](../dt_connection_reference/P007_设备树多路复用器宏.md#ga8ffbc045c3a5df61e843fd5d48731701)
- [mux_state.control](../peripheral_bus_storage_model_reference/P054_mux_state_结构体.md#a89ec6f427ae2b928694d953178cfc284)
- [mux_state.state](../peripheral_bus_storage_model_reference/P054_mux_state_结构体.md#af1b91ac4571fd44b8138ca6b226d3812)
- [MUX_STATE_DT_GET_BY_IDX()](../dt_connection_reference/P007_设备树多路复用器宏.md#gaf14ffc2c2f10589f4be71c2829c59360)
- [MUX_STATE_DT_GET_BY_NAME()](../dt_connection_reference/P007_设备树多路复用器宏.md#gaeaddd8ee80b847ea60fa7a746ed23b9c)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__mux__interface_html_ga1fcf4fd9a94643c1b778994f76b64150"></a>
<a id="agroup__devicetree-generic-exist_html_gadd50cff371a4e44a49324c3c682b58b1"></a>
<a id="agroup__mux__interface_html_gac162201caf07686e7c9c8cd736ebf7e2"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P015_MSPI 设备树相关宏.md) · [返回大纲](大纲.md) · [下一章](P017_瑞昱（Realtek）RTS5912.md)
