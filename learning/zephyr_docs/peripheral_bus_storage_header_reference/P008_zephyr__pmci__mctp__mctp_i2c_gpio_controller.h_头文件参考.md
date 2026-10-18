---
id: learning.zephyr-docs.peripheral-bus-storage-header-reference.page-8
title: zephyr__pmci__mctp__mctp_i2c_gpio_controller.h_头文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mctp__i2c__gpio__controller_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_zephyr\_\_pmci\_\_mctp\_\_mctp\_i2c\_gpio\_controller.h\_头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mctp__i2c__gpio__controller_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

基于I2C并使用GPIO传递信号的MCTP总线绑定（Bus Binding），用于控制器端。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/drivers/i2c.h>
#include <zephyr/drivers/gpio.h>
#include <zephyr/sys/mpsc_lockfree.h>
#include <zephyr/rtio/rtio.h>
#include <zephyr/pmci/mctp/mctp_i2c_gpio_common.h>
#include <libmctp.h>
#include <stdatomic.h>
```

查看此文件的源码。

基于I2C并使用GPIO传递信号的MCTP总线绑定（Bus Binding），用于控制器端。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 8.1\_数据结构（Data Structures）

<a id="r_mctp_5Fbinding_5Fi2c_5Fgpio_5Fcontroller"></a>

```c
struct mctp_binding_i2c_gpio_controller
```

相关声明：[mctp_binding_i2c_gpio_controller](../peripheral_bus_storage_model_reference/P026_mctp_binding_i2c_gpio_controller_结构体.md)。

使用GPIO的Zephyr I2C接口管理组件传输协议（MCTP）绑定。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 8.2\_宏定义（Macros）

<a id="r_a0918c1fccfab0fdc4a1eca8f1eff466c"></a>

```c
#define MCTP_I2C_GPIO_CONTROLLER_DT_DEFINE(_name, _node_id)
```

相关声明：[MCTP_I2C_GPIO_CONTROLLER_DT_DEFINE](#a0918c1fccfab0fdc4a1eca8f1eff466c)。

为带 GPIO 的 I2C 控制器定义 MCTP 总线绑定（Bus binding）。

## 8.3\_详细说明（Detailed Documentation）

<a id="a0918c1fccfab0fdc4a1eca8f1eff466c"></a>

### `MCTP_I2C_GPIO_CONTROLLER_DT_DEFINE`

```c
#define MCTP_I2C_GPIO_CONTROLLER_DT_DEFINE ( _name, _node_id )
```

展开值（Value）：

```c
RTIO_DEFINE(_name##_rtio_tx, 5, 5);                                                        \
RTIO_DEFINE(_name##_rtio_rx, 5, 5);                                                        \
MCTP_I2C_GPIO_CONTROLLER_DEFINE_IODEVS(_node_id, _name);                                   \
MCTP_I2C_GPIO_CONTROLLER_DEFINE_GPIOS(_node_id, _name);                                    \
MCTP_I2C_GPIO_CONTROLLER_DEFINE_IDS(_node_id, _name);                                      \
MCTP_I2C_GPIO_CONTROLLER_DEFINE_GPIO_CBS(_node_id, _name);                                 \
K_SEM_DEFINE(_name##_tx_lock, 1, 1);                                                       \
struct mctp_binding_i2c_gpio_controller _name = {                                          \
        .binding = {                                                                       \
                .name = STRINGIFY(_name), .version = 1,                                    \
                .start = mctp_i2c_gpio_controller_start,                                   \
                .tx = mctp_i2c_gpio_controller_tx,                                         \
                .pkt_size = MCTP_I2C_GPIO_MAX_PKT_SIZE,                                    \
                .tx_storage = _name.tx_storage,                                            \
        },                                                                                 \
        .i2c = DEVICE_DT_GET(DT_PHANDLE(_node_id, i2c)),                                   \
        .num_endpoints = DT_PROP_LEN(_node_id, endpoint_ids),                              \
        .endpoint_ids = _name##_endpoint_ids,                                              \
        .endpoint_gpios = _name##_endpoint_gpios,                                          \
        .endpoint_gpio_cbs = _name##_endpoint_gpio_cbs,                                    \
        .endpoint_iodevs = _name##_endpoint_iodevs,                                        \
        .r_tx = &_name##_rtio_tx,                                                          \
        .r_rx = &_name##_rtio_rx,                                                          \
        .tx_lock = &_name##_tx_lock,                                                       \
};
```

为带 GPIO 的 I2C 控制器定义 MCTP 总线绑定（Bus binding）。

这是自定义绑定，并不按照 MCTP 标准预期的方式切换模式。在控制器一侧，每个相邻设备都有一个关联的 I2C 地址和 GPIO，控制器监听该 GPIO 的触发信号。触发后，控制器读取目标设备。目标设备应提供相当于两个寄存器的接口：一个保存消息长度，另一个类似 FIFO，依次输出消息字节。

因此，I2C 目标设备发送消息的顺序如下：

- 设置长度值和消息值，即两个伪寄存器。
- 通过设置 GPIO 电平向控制器发出信号。
- 然后控制器应读取长度：先写地址 `0`，再读 1 字节。
- 然后控制器应读取消息：先写地址 `1`，再读 N 字节。
- 目标设备清除之前设置的引脚状态。
- 控制器向 MCTP 报告收到消息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 总线绑定变量的符号名称（Symbolic name）。 |
| `_node_id` | 包含此 MCTP 绑定配置的设备树节点（Devicetree Node）。 |


## 8.4\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/i2c.h](../i2c_driver_reference/P002_I2C驱动头文件源码.md)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P002_GPIO驱动头文件源码.md)
- [zephyr/sys/mpsc_lockfree.h](../intercore_reference/P162_MPSC无锁队列完整头文件.md)
- [zephyr/rtio/rtio.h](../rtio_core_reference/P003_RTIO核心头文件源码.md)
- [zephyr/pmci/mctp/mctp_i2c_gpio_common.h](https://docs.zephyrproject.org/latest/doxygen/html/mctp__i2c__gpio__common_8h_source.html)
- [查看此文件的源码](https://docs.zephyrproject.org/latest/doxygen/html/mctp__i2c__gpio__controller_8h_source.html)
- [mctp_binding_i2c_gpio_controller](../peripheral_bus_storage_model_reference/P026_mctp_binding_i2c_gpio_controller_结构体.md)
- [RTIO_DEFINE](../rtio_core_reference/P001_RTIO公共接口.md#ga338df088eabf3b8f7fefb4ac517b21d4)
- [DEVICE_DT_GET](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7)
- [DT_PHANDLE](../dt_property_reference/P001_设备树属性读取宏.md#ga7bd77c49472ba4547d87f00f40fd7171)
- [DT_PROP_LEN](../dt_property_reference/P001_设备树属性读取宏.md#gaa7f5afcedd1f54be79a5337e8e28a5b6)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__device__model_html_ga9a65996ce21f43acb7db061e23b48ec7"></a>
<a id="agroup__devicetree-generic-prop_html_ga7bd77c49472ba4547d87f00f40fd7171"></a>
<a id="agroup__devicetree-generic-prop_html_gaa7f5afcedd1f54be79a5337e8e28a5b6"></a>
<a id="agroup__rtio_html_ga338df088eabf3b8f7fefb4ac517b21d4"></a>
<a id="astructmctp__binding__i2c__gpio__controller_html"></a>

---

[上一章](P007_zephyr__drivers__lin.h_头文件参考.md) · [返回大纲](大纲.md) · [下一章](P009_zephyr__pmci__mctp__mctp_i2c_gpio_target.h_头文件参考.md)
