---
id: learning.zephyr-docs.api-source-compiler-device-reference.page-5
title: dap_link.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dap__link_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_dap\_link.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dap__link_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_service_reference/P005_zephyr__dap__dap_link.h_文件参考.md)。

## 5.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
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
<a id="l00032"></a>
<a id="foldopen00036"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
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
<a id="l00058"></a>
<a id="l00059"></a>
<a id="foldopen00073"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__dap__link__interface_html_ga6748c204c222c52155263592713e2291"></a>
<a id="agroup__dap__link__interface_html_gaa2057dca6fdac21d4fe7dd919c37af1b"></a>
<a id="agroup__dap__link__interface_html_gaebd8b888c2befaa8674247850f040145"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdap__link__context_html"></a>
<a id="astructdevice_html"></a>
<a id="aswdp_8h_html"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DAP_DAP_LINK_H
#define ZEPHYR_INCLUDE_DAP_DAP_LINK_H

#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/drivers/swdp.h>

#ifdef __cplusplus
extern "C" {
#endif


struct dap_link_context {
        /* Pointer to SWD or JTAG device. Only SWD is supported yet. */
        const struct device *dev;
        atomic_t state;
        /* Runtime debug port type */
        uint8_t debug_port;
        /* Debug port capabilities */
        uint8_t capabilities;
        /* Packet size used by a backend */
        uint16_t pkt_size;
        struct {
                /* Idle cycles after transfer */
                uint8_t idle_cycles;
                /* Number of retries after WAIT response */
                uint16_t retry_count;
                /* Number of retries if read value does not match */
                uint16_t match_retry;
                /* Match Mask */
                uint32_t match_mask;
        } transfer;
};

#define DAP_LINK_CONTEXT_DEFINE(ctx_name, ctx_dev)                              \
        static struct dap_link_context ctx_name = {                             \
                .dev = ctx_dev,                                                 \
        }

int dap_link_init(struct dap_link_context *const dap_link_ctx);

void dap_link_set_pkt_size(struct dap_link_context *const dap_link_ctx,
                           const uint16_t pkt_size);

int dap_link_backend_usb_init(struct dap_link_context *const dap_link_ctx);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DAP_DAP_LINK_H */
```

## 5.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors SPDX-License-Identifier: Apache-2.0.

### 注释 2：原第 38 行

指向串行线调试（SWD）或 JTAG 设备的指针。目前仅支持 SWD。

### 注释 3：原第 41 行

运行时调试端口类型（debug port type）。

### 注释 4：原第 43 行

调试端口能力（debug port capabilities）。

### 注释 5：原第 45 行

后端（backend）使用的数据包大小。

### 注释 6：原第 48 行

传输后的空闲周期（idle cycles）。

### 注释 7：原第 50 行

收到 WAIT 响应后的重试次数。

### 注释 8：原第 52 行

读取值不匹配时的重试次数。

### 注释 9：原第 54 行

匹配掩码（Match Mask）。

### 注释 10：原第 114 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DAP_DAP_LINK_H`。

## 5.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_service_reference/P005_zephyr__dap__dap_link.h_文件参考.md)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/swdp.h](../peripheral_bus_storage_header_reference/P028_zephyr__drivers__swdp.h_头文件参考.md)
- [dap_link_context](../system_service_model_reference/P006_dap_link_context_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [dap_link_init](https://docs.zephyrproject.org/latest/doxygen/html/group__dap__link__interface.html#gaebd8b888c2befaa8674247850f040145)
- [dap_link_set_pkt_size](https://docs.zephyrproject.org/latest/doxygen/html/group__dap__link__interface.html#gaa2057dca6fdac21d4fe7dd919c37af1b)
- [dap_link_backend_usb_init](https://docs.zephyrproject.org/latest/doxygen/html/group__dap__link__interface.html#ga6748c204c222c52155263592713e2291)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [swdp.h](../peripheral_bus_storage_header_reference/P028_zephyr__drivers__swdp.h_头文件参考.md)

---

[上一章](P004_coap_client_tcp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P006_esp32_clock.h_源码浏览.md)
