---
id: learning.zephyr-docs.peripheral-bus-storage-header-reference.page-10
title: zephyr__pmci__mctp__mctp_i3c_controller.h_头文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__controller_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_zephyr\_\_pmci\_\_mctp\_\_mctp\_i3c\_controller.h\_头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__controller_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

基于I3C并使用带内中断（IBI）传递信号的MCTP总线绑定，用于控制器端。

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

基于I3C并使用带内中断（IBI）传递信号的MCTP总线绑定，用于控制器端。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 10.1\_数据结构（Data Structures）

<a id="r_mctp_5Fbinding_5Fi3c_5Fcontroller"></a>

```c
struct mctp_binding_i3c_controller
```

相关声明：[mctp_binding_i3c_controller](../peripheral_bus_storage_model_reference/P028_mctp_binding_i3c_controller_结构体.md)。

使用带内中断（IBI）传递信号的Zephyr I3C接口MCTP绑定。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 10.2\_宏定义（Macros）

<a id="r_a0742316a75294cbaa8200cfe077065ac"></a>

```c
#define MCTP_I3C_CONTROLLER_DT_DEFINE(_name, _node_id)
```

相关声明：[MCTP_I3C_CONTROLLER_DT_DEFINE](#a0742316a75294cbaa8200cfe077065ac)。

内部隐藏标记（INTERNAL_HIDDEN）。

## 10.3\_详细说明（Detailed Documentation）

<a id="a0742316a75294cbaa8200cfe077065ac"></a>

### `MCTP_I3C_CONTROLLER_DT_DEFINE`

```c
#define MCTP_I3C_CONTROLLER_DT_DEFINE ( _name, _node_id )
```

展开值（Value）：

```c
MCTP_I3C_CONTROLLER_DEFINE_DEVICES(_node_id, _name);                                    \
MCTP_I3C_ENDPOINT_IDS(_node_id, _name);                                                 \
static struct i3c_device_desc                                                           \
        *_name##_endpoint_i3c_devs[DT_PROP_LEN(_node_id, endpoints)];                   \
static struct mctp_binding_i3c_controller _name = {                                     \
        .binding = {                                                                    \
                .name = STRINGIFY(_name), .version = 1,                                 \
                .start = mctp_i3c_controller_start,                                     \
                .tx = mctp_i3c_controller_tx,                                           \
                .pkt_size = MCTP_I3C_MAX_PKT_SIZE,                                      \
                .tx_storage = _name.tx_storage,                                         \
        },                                                                              \
        .num_endpoints = DT_PROP_LEN(_node_id, endpoints),                              \
        .devices = _name##_endpoints,                                                   \
        .endpoint_ids = _name##_endpoint_ids,                                           \
        .endpoint_i3c_devs = _name##_endpoint_i3c_devs,                                 \
        COND_CODE_1(CONFIG_MCTP_I3C_CONTROLLER_POLLING_MODE,                            \
                (.poll_interval =                                                       \
                        K_MSEC(CONFIG_MCTP_I3C_CONTROLLER_POLL_INTERVAL_MS)), ())       \
};
```

内部隐藏标记（INTERNAL_HIDDEN）。

为 I3C 控制器定义 MCTP 总线绑定。

此总线绑定支持目标设备通过带内中断（In-Band Interrupt，IBI）表明其希望发送消息；启用相应配置时，也支持可选的轮询模式（Polling mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 总线绑定变量的符号名称（Symbolic name）。 |
| `_node_id` | 包含此 MCTP 绑定配置的设备树节点（Devicetree Node）。 |


## 10.4\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/i3c.h](https://docs.zephyrproject.org/latest/doxygen/html/i3c_8h_source.html)
- [zephyr/pmci/mctp/mctp_i3c_common.h](https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__common_8h_source.html)
- [查看此文件的源码](https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__controller_8h_source.html)
- [mctp_binding_i3c_controller](../peripheral_bus_storage_model_reference/P028_mctp_binding_i3c_controller_结构体.md)
- [i3c_device_desc](../hardware/P401_I3C设备描述符.md)
- [DT_PROP_LEN](../dt_property_reference/P001_设备树属性读取宏.md#gaa7f5afcedd1f54be79a5337e8e28a5b6)
- [K_MSEC](../timer_reference/P086_系统时钟公共接口.md#ga302af954e87b10a9b731f1ad07775e9f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__clock__apis_html_ga302af954e87b10a9b731f1ad07775e9f"></a>
<a id="agroup__devicetree-generic-prop_html_gaa7f5afcedd1f54be79a5337e8e28a5b6"></a>
<a id="astructi3c__device__desc_html"></a>
<a id="astructmctp__binding__i3c__controller_html"></a>

---

[上一章](P009_zephyr__pmci__mctp__mctp_i2c_gpio_target.h_头文件参考.md) · [返回大纲](大纲.md) · [下一章](P011_zephyr__pmci__mctp__mctp_i3c_target.h_头文件参考.md)
