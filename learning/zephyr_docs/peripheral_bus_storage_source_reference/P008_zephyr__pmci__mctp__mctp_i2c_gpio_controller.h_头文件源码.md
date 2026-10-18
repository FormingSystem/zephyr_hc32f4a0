---
id: learning.zephyr-docs.peripheral-bus-storage-source-reference.page-8
title: zephyr__pmci__mctp__mctp_i2c_gpio_controller.h_头文件源码
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mctp__i2c__gpio__controller_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_zephyr__pmci__mctp__mctp_i2c_gpio_controller.h_头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mctp__i2c__gpio__controller_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应头文件参考](../peripheral_bus_storage_header_reference/P008_zephyr__pmci__mctp__mctp_i2c_gpio_controller.h_头文件参考.md)。

## 8.1\_原始可见代码（Source Code）

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
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
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
<a id="l00041"></a>
<a id="foldopen00045"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00077"></a>
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
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="foldopen00135"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="adevice_8h_html"></a>
<a id="adrivers_2gpio_8h_html"></a>
<a id="adrivers_2i2c_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="amctp__i2c__gpio__common_8h_html"></a>
<a id="ampsc__lockfree_8h_html"></a>
<a id="artio_2rtio_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructgpio__dt__spec_html"></a>
<a id="astructk__sem_html"></a>
<a id="astructk__spinlock_html"></a>
<a id="astructmctp__binding__i2c__gpio__controller_html"></a>
<a id="astructmpsc_html"></a>
<a id="astructrtio__iodev_html"></a>
<a id="astructrtio_html"></a>

```c
/*
 * Copyright (c) 2025 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 *
 */


#ifndef ZEPHYR_INCLUDE_PMCI_MCTP_MCTP_I2C_GPIO_CONTROLLER_H_
#define ZEPHYR_INCLUDE_PMCI_MCTP_MCTP_I2C_GPIO_CONTROLLER_H_

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


struct mctp_binding_i2c_gpio_controller;

struct mctp_i2c_gpio_controller_cb {
        struct mpsc_node q;
        struct gpio_callback callback;
        struct mctp_binding_i2c_gpio_controller *binding;
        uint8_t index;
};


struct mctp_binding_i2c_gpio_controller {
        struct mctp_binding binding;
        const struct device *i2c;

        uint8_t rx_buf_len;
        uint8_t rx_buf[MCTP_I2C_GPIO_MAX_PKT_SIZE];
        uint8_t tx_buf[MCTP_I2C_GPIO_MAX_PKT_SIZE];

        struct mctp_pktbuf *rx_pkt;

        /* Avoid needing a thread or work queue task by using RTIO */
        struct k_sem *tx_lock;
        struct rtio *r_tx;

        /* Mapping of endpoints to i2c targets with gpios */
        size_t num_endpoints;
        const uint8_t *endpoint_ids;
        const struct rtio_iodev **endpoint_iodevs;
        const struct gpio_dt_spec *endpoint_gpios;
        struct mctp_i2c_gpio_controller_cb *endpoint_gpio_cbs;

        /* Ongoing request from a particular gpio */
        struct k_spinlock rx_lock;
        struct rtio *r_rx;
        struct mpsc rx_q;
        struct mctp_i2c_gpio_controller_cb *inflight_rx;

        uint8_t tx_storage[MCTP_PKTBUF_SIZE(MCTP_I2C_GPIO_MAX_PKT_SIZE)] PKTBUF_STORAGE_ALIGN;

};

int mctp_i2c_gpio_controller_start(struct mctp_binding *binding);
int mctp_i2c_gpio_controller_tx(struct mctp_binding *binding, struct mctp_pktbuf *pkt);

#define MCTP_I2C_GPIO_CONTROLLER_IODEV_NAME(_idx, _name) _name##_idx

#define MCTP_I2C_GPIO_CONTROLLER_IODEV_DEFINE(_node_id, addrs, _idx, _name)                        \
        I2C_IODEV_DEFINE(MCTP_I2C_GPIO_CONTROLLER_IODEV_NAME(_idx, _name),                         \
                DT_PHANDLE(_node_id, i2c),                                                         \
                DT_PROP_BY_IDX(_node_id, addrs, _idx));


#define MCTP_I2C_GPIO_CONTROLLER_DEFINE_GPIOS(_node_id, _name)                                     \
        const struct gpio_dt_spec _name##_endpoint_gpios[] = {                                     \
                DT_FOREACH_PROP_ELEM_SEP(_node_id, endpoint_gpios, GPIO_DT_SPEC_GET_BY_IDX, (,))   \
        }

#define MCTP_I2C_GPIO_CONTROLLER_DEFINE_IDS(_node_id, _name)                                       \
        const uint8_t _name##_endpoint_ids[] = DT_PROP(_node_id, endpoint_ids);

#define MCTP_I2C_GPIO_CONTROLLER_DEFINE_GPIO_CBS(_node_id, _name)                                  \
        struct mctp_i2c_gpio_controller_cb \
                _name##_endpoint_gpio_cbs[DT_PROP_LEN(_node_id, endpoint_ids)]


#define MCTP_I2C_GPIO_CONTROLLER_DEFINE_IODEVS(_node_id, _name)                                    \
        DT_FOREACH_PROP_ELEM_VARGS(_node_id, endpoint_addrs,                                       \
                        MCTP_I2C_GPIO_CONTROLLER_IODEV_DEFINE, _name)                              \
                const struct rtio_iodev *_name##_endpoint_iodevs[] = {                             \
                LISTIFY(DT_PROP_LEN(_node_id, endpoint_ids), &MCTP_I2C_GPIO_CONTROLLER_IODEV_NAME, \
                                (,), _name)                                                        \
        }


#define MCTP_I2C_GPIO_CONTROLLER_DT_DEFINE(_name, _node_id)                                        \
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

#endif /* ZEPHYR_INCLUDE_PMCI_MCTP_MCTP_I2C_GPIO_CONTROLLER_H_ */
```

## 8.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 56 行

通过实时 I/O（RTIO）避免需要额外的线程或工作队列任务。

### 注释 3：原第 60 行

端点（Endpoints）到带 GPIO 的 I2C 目标设备的映射。

### 注释 4：原第 67 行

来自特定 GPIO 的进行中请求（Ongoing request）。

### 注释 5：原第 162 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_PMCI_MCTP_MCTP_I2C_GPIO_CONTROLLER_H_`。

## 8.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../peripheral_bus_storage_header_reference/P008_zephyr__pmci__mctp__mctp_i2c_gpio_controller.h_头文件参考.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/i2c.h](../i2c_driver_reference/P001_I2C驱动头文件参考.md)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
- [zephyr/sys/mpsc_lockfree.h](../intercore_reference/P161_MPSC无锁队列头文件参考.md)
- [zephyr/rtio/rtio.h](../rtio_core_reference/P002_RTIO核心头文件参考.md)
- [zephyr/pmci/mctp/mctp_i2c_gpio_common.h](https://docs.zephyrproject.org/latest/doxygen/html/mctp__i2c__gpio__common_8h.html)
- [mctp_binding_i2c_gpio_controller](../peripheral_bus_storage_model_reference/P026_mctp_binding_i2c_gpio_controller_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [device](../device_reference/P002_设备对象结构.md)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [rtio](../rtio_model_reference/P001_RTIO上下文.md)
- [rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)
- [gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)
- [k_spinlock](../kernel/P066_自旋锁结构参考.md)
- [mpsc](../intercore_reference/P159_MPSC无锁队列结构.md)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
- [i2c.h](../i2c_driver_reference/P001_I2C驱动头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [mctp_i2c_gpio_common.h](https://docs.zephyrproject.org/latest/doxygen/html/mctp__i2c__gpio__common_8h.html)
- [mpsc_lockfree.h](../intercore_reference/P161_MPSC无锁队列头文件参考.md)
- [rtio.h](../rtio_core_reference/P002_RTIO核心头文件参考.md)

---

[上一章](P007_zephyr__drivers__lin.h_头文件源码.md) · [返回大纲](大纲.md) · [下一章](P009_zephyr__pmci__mctp__mctp_i2c_gpio_target.h_头文件源码.md)
