---
id: learning.zephyr-docs.peripheral-bus-storage-header-reference.page-9
title: zephyr__pmci__mctp__mctp_i2c_gpio_target.h_头文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mctp__i2c__gpio__target_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_zephyr\_\_pmci\_\_mctp\_\_mctp\_i2c\_gpio\_target.h\_头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mctp__i2c__gpio__target_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

基于I2C并使用GPIO传递信号的MCTP总线绑定（Bus Binding），用于目标端。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/drivers/i2c.h>
#include <zephyr/drivers/gpio.h>
#include <zephyr/pmci/mctp/mctp_i2c_gpio_common.h>
#include <libmctp.h>
```

查看此文件的源码。

基于I2C并使用GPIO传递信号的MCTP总线绑定（Bus Binding），用于目标端。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.1\_数据结构（Data Structures）

<a id="r_mctp_5Fbinding_5Fi2c_5Fgpio_5Ftarget"></a>

```c
struct mctp_binding_i2c_gpio_target
```

相关声明：[mctp_binding_i2c_gpio_target](../peripheral_bus_storage_model_reference/P027_mctp_binding_i2c_gpio_target_结构体.md)。

使用GPIO的Zephyr I2C目标接口管理组件传输协议（MCTP）绑定。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.2\_宏定义（Macros）

<a id="r_a94ed3dfa209dd9640cf0fef7f33bcf84"></a>

```c
#define MCTP_I2C_GPIO_TARGET_DT_DEFINE(_name, _node_id)
```

相关声明：[MCTP_I2C_GPIO_TARGET_DT_DEFINE](#a94ed3dfa209dd9640cf0fef7f33bcf84)。

为带 GPIO 的 I2C 目标设备定义 MCTP 总线绑定。

## 9.3\_详细说明（Detailed Documentation）

<a id="a94ed3dfa209dd9640cf0fef7f33bcf84"></a>

### `MCTP_I2C_GPIO_TARGET_DT_DEFINE`

```c
#define MCTP_I2C_GPIO_TARGET_DT_DEFINE ( _name, _node_id )
```

展开值（Value）：

```c
K_SEM_DEFINE(_name ##_tx_lock, 1, 1);                                                      \
K_SEM_DEFINE(_name ##_tx_complete, 0, 1);                                                  \
struct mctp_binding_i2c_gpio_target _name = {                                              \
        .binding = {                                                                       \
                .name = STRINGIFY(_name), .version = 1,                                    \
                .start = mctp_i2c_gpio_target_start,                                       \
                .tx = mctp_i2c_gpio_target_tx,                                             \
                .pkt_size = MCTP_I2C_GPIO_MAX_PKT_SIZE,                                    \
                .tx_storage = _name.tx_storage,                                            \
        },                                                                                 \
        .i2c = DEVICE_DT_GET(DT_PHANDLE(_node_id, i2c)),                                   \
        .i2c_target_cfg = {                                                                \
                .address = DT_PROP(_node_id, i2c_addr),                                    \
                .callbacks = &mctp_i2c_gpio_target_callbacks,                              \
        },                                                                                 \
        .endpoint_id = DT_PROP(_node_id, endpoint_id),                                     \
        .endpoint_gpio = GPIO_DT_SPEC_GET(_node_id, endpoint_gpios),                       \
        .tx_lock = &_name##_tx_lock,                                                       \
        .tx_complete = &_name##_tx_complete,                                               \
};
```

为带 GPIO 的 I2C 目标设备定义 MCTP 总线绑定。

这是自定义绑定，并不按照 MCTP 标准预期的方式切换模式。在目标设备一侧，有待发送数据时将 GPIO 引脚置为有效电平，可以是低有效或高有效。随后，控制器应在某个时刻读取此 I2C 目标设备。目标设备随时接受读取，且每次读取应包含完整的 MCTP 数据包。

实际上，每个设备都有一对伪寄存器（Pseudo registers），用于以数据包 FIFO 的方式读写。

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


## 9.4\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/i2c.h](../i2c_driver_reference/P002_I2C驱动头文件源码.md)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P002_GPIO驱动头文件源码.md)
- [zephyr/pmci/mctp/mctp_i2c_gpio_common.h](https://docs.zephyrproject.org/latest/doxygen/html/mctp__i2c__gpio__common_8h_source.html)
- [查看此文件的源码](https://docs.zephyrproject.org/latest/doxygen/html/mctp__i2c__gpio__target_8h_source.html)
- [mctp_binding_i2c_gpio_target](../peripheral_bus_storage_model_reference/P027_mctp_binding_i2c_gpio_target_结构体.md)
- [K_SEM_DEFINE](../synchronization_reference/P008_信号量公共接口.md#ga018a8aa43e02e704deee7b6341502946)
- [DEVICE_DT_GET](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7)
- [DT_PHANDLE](../dt_property_reference/P001_设备树属性读取宏.md#ga7bd77c49472ba4547d87f00f40fd7171)
- [DT_PROP](../dt_property_reference/P001_设备树属性读取宏.md#ga8e1fd9ebacd85d2013df027d041d506b)
- [GPIO_DT_SPEC_GET](../hardware/P266_GPIO公共接口.md#ga2fa6bb5880f46984f9fc29c70f7d503e)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__device__model_html_ga9a65996ce21f43acb7db061e23b48ec7"></a>
<a id="agroup__devicetree-generic-prop_html_ga7bd77c49472ba4547d87f00f40fd7171"></a>
<a id="agroup__devicetree-generic-prop_html_ga8e1fd9ebacd85d2013df027d041d506b"></a>
<a id="agroup__gpio__interface_html_ga2fa6bb5880f46984f9fc29c70f7d503e"></a>
<a id="agroup__semaphore__apis_html_ga018a8aa43e02e704deee7b6341502946"></a>
<a id="astructmctp__binding__i2c__gpio__target_html"></a>

---

[上一章](P008_zephyr__pmci__mctp__mctp_i2c_gpio_controller.h_头文件参考.md) · [返回大纲](大纲.md) · [下一章](P010_zephyr__pmci__mctp__mctp_i3c_controller.h_头文件参考.md)
