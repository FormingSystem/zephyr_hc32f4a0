---
id: learning.zephyr-docs.peripheral-bus-storage-source-reference.page-9
title: zephyr__pmci__mctp__mctp_i2c_gpio_target.h_头文件源码
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mctp__i2c__gpio__target_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_zephyr__pmci__mctp__mctp_i2c_gpio_target.h_头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mctp__i2c__gpio__target_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应头文件参考](../peripheral_bus_storage_header_reference/P009_zephyr__pmci__mctp__mctp_i2c_gpio_target.h_头文件参考.md)。

## 9.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="foldopen00028"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="foldopen00079"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="adevice_8h_html"></a>
<a id="adrivers_2gpio_8h_html"></a>
<a id="adrivers_2i2c_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="amctp__i2c__gpio__common_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructgpio__dt__spec_html"></a>
<a id="astructi2c__target__callbacks_html"></a>
<a id="astructi2c__target__config_html"></a>
<a id="astructk__sem_html"></a>
<a id="astructmctp__binding__i2c__gpio__target_html"></a>

```c
/*
 * Copyright (c) 2025 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 *
 */


#ifndef ZEPHYR_INCLUDE_PMCI_MCTP_MCTP_I2C_GPIO_TARGET_H_
#define ZEPHYR_INCLUDE_PMCI_MCTP_MCTP_I2C_GPIO_TARGET_H_

#include <stdint.h>
#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/drivers/i2c.h>
#include <zephyr/drivers/gpio.h>
#include <zephyr/pmci/mctp/mctp_i2c_gpio_common.h>
#include <libmctp.h>

struct mctp_binding_i2c_gpio_target {
        struct mctp_binding binding;
        const struct device *i2c;
        struct i2c_target_config i2c_target_cfg;
        uint8_t endpoint_id;
        const struct gpio_dt_spec endpoint_gpio;
        uint8_t reg_addr;
        bool rxtx;
        uint8_t rx_idx;
        uint8_t rx_exp_len;
        struct mctp_pktbuf *rx_pkt;
        struct k_sem *tx_lock;
        struct k_sem *tx_complete;
        uint8_t tx_idx;
        struct mctp_pktbuf *tx_pkt;
        uint8_t tx_storage[MCTP_PKTBUF_SIZE(MCTP_I2C_GPIO_MAX_PKT_SIZE)] PKTBUF_STORAGE_ALIGN;
};

extern const struct i2c_target_callbacks mctp_i2c_gpio_target_callbacks;
int mctp_i2c_gpio_target_start(struct mctp_binding *binding);
int mctp_i2c_gpio_target_tx(struct mctp_binding *binding, struct mctp_pktbuf *pkt);
int mctp_i2c_gpio_target_unregister(struct mctp_binding_i2c_gpio_target *b);

#define MCTP_I2C_GPIO_TARGET_DT_DEFINE(_name, _node_id)                                            \
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

#endif /* ZEPHYR_INCLUDE_PMCI_MCTP_MCTP_I2C_GPIO_TARGET_H_ */
```

## 9.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 101 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_PMCI_MCTP_MCTP_I2C_GPIO_TARGET_H_`。

## 9.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../peripheral_bus_storage_header_reference/P009_zephyr__pmci__mctp__mctp_i2c_gpio_target.h_头文件参考.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/i2c.h](../i2c_driver_reference/P001_I2C驱动头文件参考.md)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
- [zephyr/pmci/mctp/mctp_i2c_gpio_common.h](https://docs.zephyrproject.org/latest/doxygen/html/mctp__i2c__gpio__common_8h.html)
- [mctp_binding_i2c_gpio_target](../peripheral_bus_storage_model_reference/P027_mctp_binding_i2c_gpio_target_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [i2c_target_config](../hardware/P309_I2C目标配置.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [i2c_target_callbacks](../hardware/P308_I2C目标回调表.md)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
- [i2c.h](../i2c_driver_reference/P001_I2C驱动头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [mctp_i2c_gpio_common.h](https://docs.zephyrproject.org/latest/doxygen/html/mctp__i2c__gpio__common_8h.html)

---

[上一章](P008_zephyr__pmci__mctp__mctp_i2c_gpio_controller.h_头文件源码.md) · [返回大纲](大纲.md) · [下一章](P010_zephyr__pmci__mctp__mctp_i3c_controller.h_头文件源码.md)
