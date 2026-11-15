---
id: learning.zephyr-docs.peripheral-bus-storage-source-reference.page-11
title: zephyr__pmci__mctp__mctp_i3c_target.h_头文件源码
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__target_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_zephyr__pmci__mctp__mctp_i3c_target.h_头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__target_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应头文件参考](../peripheral_bus_storage_header_reference/P011_zephyr__pmci__mctp__mctp_i3c_target.h_头文件参考.md)。

## 11.1\_原始可见代码（Source Code）

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
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="foldopen00055"></a>
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
<a id="l00075"></a>
<a id="adevice_8h_html"></a>
<a id="ai3c_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="amctp__i3c__common_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructi3c__target__callbacks_html"></a>
<a id="astructi3c__target__config_html"></a>
<a id="astructk__sem_html"></a>
<a id="astructmctp__binding__i3c__target_html"></a>

```c
/*
 * Copyright (c) 2025 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 *
 */


#ifndef ZEPHYR_INCLUDE_PMCI_MCTP_MCTP_I3C_TARGET_H_
#define ZEPHYR_INCLUDE_PMCI_MCTP_MCTP_I3C_TARGET_H_

#include <stdint.h>
#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/drivers/i3c.h>
#include <zephyr/pmci/mctp/mctp_i3c_common.h>
#include <libmctp.h>

struct mctp_binding_i3c_target {
        struct mctp_binding binding;
        const struct device *i3c;
        struct i3c_target_config i3c_target_cfg;
        uint8_t endpoint_id;
        uint8_t dynamic_addr;
        struct mctp_pktbuf *tx_pkt;
        struct k_sem *tx_lock;
        struct k_sem *tx_complete;
        struct mctp_pktbuf *rx_pkt;
        uint8_t tx_storage[MCTP_PKTBUF_SIZE(MCTP_I3C_MAX_PKT_SIZE)] PKTBUF_STORAGE_ALIGN;
        uint8_t tx_ptr;
};

extern const struct i3c_target_callbacks mctp_i3c_target_callbacks;
int mctp_i3c_target_start(struct mctp_binding *binding);
int mctp_i3c_target_tx(struct mctp_binding *binding, struct mctp_pktbuf *pkt);

#define MCTP_I3C_TARGET_DT_DEFINE(_name, _node_id)                                                 \
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

#endif /* ZEPHYR_INCLUDE_PMCI_MCTP_MCTP_I3C_TARGET_H_ */
```

## 11.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 75 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_PMCI_MCTP_MCTP_I3C_TARGET_H_`。

## 11.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../peripheral_bus_storage_header_reference/P011_zephyr__pmci__mctp__mctp_i3c_target.h_头文件参考.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/i3c.h](https://docs.zephyrproject.org/latest/doxygen/html/i3c_8h.html)
- [zephyr/pmci/mctp/mctp_i3c_common.h](https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__common_8h.html)
- [mctp_binding_i3c_target](../peripheral_bus_storage_model_reference/P029_mctp_binding_i3c_target_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [i3c_target_config](../hardware/P388_I3C目标设备配置.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [i3c_target_callbacks](../hardware/P389_I3C目标设备回调表.md)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [i3c.h](https://docs.zephyrproject.org/latest/doxygen/html/i3c_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [mctp_i3c_common.h](https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__common_8h.html)

---

[上一章](P010_zephyr__pmci__mctp__mctp_i3c_controller.h_头文件源码.md) · [返回大纲](大纲.md) · [下一章](P012_zephyr__pmci__mctp__mctp_uart.h_头文件源码.md)
