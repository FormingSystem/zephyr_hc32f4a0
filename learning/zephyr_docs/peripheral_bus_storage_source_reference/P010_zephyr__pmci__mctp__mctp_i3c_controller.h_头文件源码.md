---
id: learning.zephyr-docs.peripheral-bus-storage-source-reference.page-10
title: zephyr__pmci__mctp__mctp_i3c_controller.h_头文件源码
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__controller_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_zephyr__pmci__mctp__mctp_i3c_controller.h_头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__controller_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应头文件参考](../peripheral_bus_storage_header_reference/P010_zephyr__pmci__mctp__mctp_i3c_controller.h_头文件参考.md)。

## 10.1\_原始可见代码（Source Code）

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
<a id="foldopen00027"></a>
<a id="l00027"></a>
<a id="l00029"></a>
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
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00046"></a>
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
<a id="l00063"></a>
<a id="foldopen00073"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
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
<a id="adevice_8h_html"></a>
<a id="ai3c_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="amctp__i3c__common_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructi3c__device__desc_html"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructk__work__delayable_html"></a>
<a id="astructmctp__binding__i3c__controller_html"></a>

```c
/*
 * Copyright (c) 2025 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 *
 */


#ifndef ZEPHYR_INCLUDE_PMCI_MCTP_MCTP_I3C_CONTROLLER_H_
#define ZEPHYR_INCLUDE_PMCI_MCTP_MCTP_I3C_CONTROLLER_H_

#include <stdint.h>
#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/drivers/i3c.h>
#include <zephyr/pmci/mctp/mctp_i3c_common.h>
#include <libmctp.h>

struct mctp_binding_i3c_controller {
        struct mctp_binding binding;
        size_t num_endpoints;
        const struct device **devices;
        uint8_t *endpoint_ids;
        struct i3c_device_desc **endpoint_i3c_devs;
        enum mctp_i3c_endpoint_state *endpoint_states;
        size_t rx_buf_len;
        uint8_t *rx_buf;
        uint8_t tx_storage[MCTP_PKTBUF_SIZE(MCTP_I3C_MAX_PKT_SIZE)] PKTBUF_STORAGE_ALIGN;
#ifdef CONFIG_MCTP_I3C_CONTROLLER_POLLING_MODE
        struct k_work_delayable poll_work;
        k_timeout_t poll_interval;
#endif
};

int mctp_i3c_controller_start(struct mctp_binding *binding);
int mctp_i3c_controller_tx(struct mctp_binding *binding, struct mctp_pktbuf *pkt);

#define MCTP_I3C_ENDPOINT_IDS(_node_id, _name)                                  \
        static uint8_t _name##_endpoint_ids[DT_PROP_LEN(_node_id, endpoints)]   \
                = DT_PROP(_node_id, endpoint_ids)

#define MCTP_I3C_ENDPOINT_DEVICE(_idx, _node_id, ...)                           \
        DEVICE_DT_GET_BY_IDX(_node_id, endpoints, _idx)

#define MCTP_I3C_CONTROLLER_DEFINE_DEVICES(_node_id, _name)                     \
        const struct device *_name##_endpoints[] = {                            \
                LISTIFY(DT_PROP_LEN(_node_id, endpoints),                       \
                        MCTP_I3C_ENDPOINT_DEVICE, (,), _node_id)                \
        }


#define MCTP_I3C_CONTROLLER_DT_DEFINE(_name, _node_id)                                          \
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

#endif /* ZEPHYR_INCLUDE_PMCI_MCTP_MCTP_I3C_CONTROLLER_H_ */
```

## 10.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 95 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_PMCI_MCTP_MCTP_I3C_CONTROLLER_H_`。

## 10.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../peripheral_bus_storage_header_reference/P010_zephyr__pmci__mctp__mctp_i3c_controller.h_头文件参考.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/i3c.h](https://docs.zephyrproject.org/latest/doxygen/html/i3c_8h.html)
- [zephyr/pmci/mctp/mctp_i3c_common.h](https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__common_8h.html)
- [mctp_binding_i3c_controller](../peripheral_bus_storage_model_reference/P028_mctp_binding_i3c_controller_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [i3c_device_desc](../hardware/P401_I3C设备描述符.md)
- [k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [i3c.h](https://docs.zephyrproject.org/latest/doxygen/html/i3c_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [mctp_i3c_common.h](https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__common_8h.html)

---

[上一章](P009_zephyr__pmci__mctp__mctp_i2c_gpio_target.h_头文件源码.md) · [返回大纲](大纲.md) · [下一章](P011_zephyr__pmci__mctp__mctp_i3c_target.h_头文件源码.md)
