---
id: learning.zephyr-docs.peripheral-bus-storage-header-reference.page-11
title: zephyr__pmci__mctp__mctp_i3c_target.h_头文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__target_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_zephyr\_\_pmci\_\_mctp\_\_mctp\_i3c\_target.h\_头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__target_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

基于I3C并使用带内中断（IBI）传递信号的MCTP总线绑定，用于目标端。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/drivers/i3c.h>
#include <zephyr/pmci/mctp/mctp_i3c_common.h>
#include <libmctp.h>
```

查看此文件的源码。

基于I3C并使用带内中断（IBI）传递信号的MCTP总线绑定，用于目标端。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 11.1\_数据结构（Data Structures）

<a id="r_mctp_5Fbinding_5Fi3c_5Ftarget"></a>

```c
struct mctp_binding_i3c_target
```

相关声明：[mctp_binding_i3c_target](../peripheral_bus_storage_model_reference/P029_mctp_binding_i3c_target_结构体.md)。

使用GPIO的Zephyr I3C目标接口管理组件传输协议（MCTP）绑定。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.2\_宏定义（Macros）

<a id="r_a94e4435fb9521e07ad3475bd5a8a1f89"></a>

```c
#define MCTP_I3C_TARGET_DT_DEFINE(_name, _node_id)
```

相关声明：[MCTP_I3C_TARGET_DT_DEFINE](#a94e4435fb9521e07ad3475bd5a8a1f89)。

内部隐藏标记（INTERNAL_HIDDEN）。

## 11.3\_详细说明（Detailed Documentation）

<a id="a94e4435fb9521e07ad3475bd5a8a1f89"></a>

### `MCTP_I3C_TARGET_DT_DEFINE`

```c
#define MCTP_I3C_TARGET_DT_DEFINE ( _name, _node_id )
```

展开值（Value）：

```c
K_SEM_DEFINE(_name##_tx_lock, 1, 1);                                                       \
K_SEM_DEFINE(_name##_tx_complete, 0, 1);                                                   \
struct mctp_binding_i3c_target _name = {                                                   \
        .binding = {                                                                       \
                .name = STRINGIFY(_name), .version = 1,                                    \
                .start = mctp_i3c_target_start,                                            \
                .tx = mctp_i3c_target_tx,                                                  \
                .pkt_size = MCTP_I3C_MAX_PKT_SIZE,                                         \
                .tx_storage = _name.tx_storage,                                            \
        },                                                                                 \
        .i3c = DEVICE_DT_GET(DT_PHANDLE(_node_id, i3c)),                                   \
        .i3c_target_cfg = {                                                                \
                .callbacks = &mctp_i3c_target_callbacks,                                   \
        },                                                                                 \
        .endpoint_id = DT_PROP(_node_id, endpoint_id),                                     \
        .tx_lock = &_name##_tx_lock,                                                       \
        .tx_complete = &_name##_tx_complete,                                               \
};
```

内部隐藏标记（INTERNAL_HIDDEN）。

为使用 IBI 信号通知的 I3C 目标模式定义 MCTP 总线绑定。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 总线绑定变量的符号名称（Symbolic name）。 |
| `_node_id` | 包含此 MCTP 绑定配置的设备树节点（Devicetree Node）。 |


## 11.4\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/i3c.h](https://docs.zephyrproject.org/latest/doxygen/html/i3c_8h_source.html)
- [zephyr/pmci/mctp/mctp_i3c_common.h](https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__common_8h_source.html)
- [查看此文件的源码](https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__target_8h_source.html)
- [mctp_binding_i3c_target](../peripheral_bus_storage_model_reference/P029_mctp_binding_i3c_target_结构体.md)
- [K_SEM_DEFINE](../synchronization_reference/P008_信号量公共接口.md#ga018a8aa43e02e704deee7b6341502946)
- [DEVICE_DT_GET](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7)
- [DT_PHANDLE](../dt_property_reference/P001_设备树属性读取宏.md#ga7bd77c49472ba4547d87f00f40fd7171)
- [DT_PROP](../dt_property_reference/P001_设备树属性读取宏.md#ga8e1fd9ebacd85d2013df027d041d506b)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__device__model_html_ga9a65996ce21f43acb7db061e23b48ec7"></a>
<a id="agroup__devicetree-generic-prop_html_ga7bd77c49472ba4547d87f00f40fd7171"></a>
<a id="agroup__devicetree-generic-prop_html_ga8e1fd9ebacd85d2013df027d041d506b"></a>
<a id="agroup__semaphore__apis_html_ga018a8aa43e02e704deee7b6341502946"></a>
<a id="astructmctp__binding__i3c__target_html"></a>

---

[上一章](P010_zephyr__pmci__mctp__mctp_i3c_controller.h_头文件参考.md) · [返回大纲](大纲.md) · [下一章](P012_zephyr__pmci__mctp__mctp_uart.h_头文件参考.md)
