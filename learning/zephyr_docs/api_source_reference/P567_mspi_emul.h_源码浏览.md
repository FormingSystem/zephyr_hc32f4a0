---
id: learning.zephyr-docs.api-source-reference.page-567
title: mspi_emul.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mspi__emul_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第567章\_mspi\_emul.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mspi__emul_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mspi__emul_8h.html)。

## 567.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00022"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="foldopen00084"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="foldopen00090"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="foldopen00102"></a>
<a id="l00102"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a2b0530c13706c66229d35977c6553db9"></a>
<a id="adrivers_2emul_8h_html"></a>
<a id="agroup__mspi__emul__interface_html_ga15df8cc9ccc2831c5446002e864f1717"></a>
<a id="agroup__mspi__emul__interface_html_ga98c9a359f3385f49fbfe52b27254d261"></a>
<a id="agroup__mspi__emul__interface_html_gaaa0c99ea6582cacba89f8630d8d554be"></a>
<a id="agroup__mspi__emul__interface_html_gabecb33236ed3a6a93a28edef0a4c3ae7"></a>
<a id="agroup__mspi__interface_html_ga4cd05950729893e08ef0d4a12e2242d5"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="amspi_8h_html"></a>
<a id="aslist_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructemul__mspi__device__api_html"></a>
<a id="astructemul__mspi__device__api_html_afb3852793d752722841739fc486c6e4f"></a>
<a id="astructemul__mspi__driver__api_html"></a>
<a id="astructemul__mspi__driver__api_html_a0fe96769384075e9aee7daa1c30e32a6"></a>
<a id="astructemul__mspi__driver__api_html_a2b5aef76272e620fcb77ba9532f0aee6"></a>
<a id="astructemul__mspi__driver__api_html_a7b2ab7da5d949ab05dda7cc0dbc24ff9"></a>
<a id="astructemul_html"></a>
<a id="astructmspi__driver__api_html"></a>
<a id="astructmspi__emul_html"></a>
<a id="astructmspi__emul_html_a2d247195c375c1aac30beec32dc11099"></a>
<a id="astructmspi__emul_html_a5386510f101d186581abbde6b624be09"></a>
<a id="astructmspi__emul_html_aa2b65e70ab7c2218929a6042bd0fd548"></a>
<a id="astructmspi__emul_html_aa3e45d11717b737ea8c6b4b19459991a"></a>
<a id="astructmspi__xfer__packet_html"></a>

```c
/*
 * Copyright 2020 Google LLC
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_MSPI_EMUL_H_
#define ZEPHYR_INCLUDE_DRIVERS_MSPI_EMUL_H_

#include <zephyr/device.h>
#include <zephyr/drivers/emul.h>
#include <zephyr/drivers/mspi.h>
#include <zephyr/sys/slist.h>
#include <zephyr/types.h>



#ifdef __cplusplus
extern "C" {
#endif

struct mspi_emul;

typedef struct mspi_emul *(*mspi_emul_find_emul)(const struct device *dev,
                                                 uint16_t dev_idx);

typedef int (*mspi_emul_trigger_event)(const struct device *dev,
                                       enum mspi_bus_event evt_type);

typedef int (*emul_mspi_dev_api_transceive)(const struct emul *target,
                                            const struct mspi_xfer_packet *packets,
                                            uint32_t num_packet,
                                            bool async,
                                            uint32_t timeout);

struct emul_mspi_device_api {
        emul_mspi_dev_api_transceive transceive;
};

struct mspi_emul {
        sys_snode_t                  node;
        const struct emul            *target;
        const struct emul_mspi_device_api *api;
        uint16_t                     dev_idx;
};

__subsystem struct emul_mspi_driver_api {
        struct mspi_driver_api       mspi_api;
        mspi_emul_trigger_event      trigger_event;
        mspi_emul_find_emul          find_emul;
};

DEVICE_API_EXTENDS(emul_mspi, mspi, mspi_api);

int mspi_emul_register(const struct device *dev, struct mspi_emul *emul);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_MSPI_EMUL_H_ */
```

## 567.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2020 Google LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 135 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MSPI_EMUL_H_`。

## 567.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mspi__emul_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/emul.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2emul_8h.html)
- [zephyr/drivers/mspi.h](../peripheral_bus_storage_header_reference/P017_zephyr__drivers__mspi.h_头文件参考.md)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [mspi_emul](../hardware/P489_MSPI仿真器链表节点.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [mspi_emul_trigger_event](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__emul__interface.html#gaaa0c99ea6582cacba89f8630d8d554be)
- [mspi_bus_event](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga4cd05950729893e08ef0d4a12e2242d5)
- [emul_mspi_dev_api_transceive](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__emul__interface.html#ga15df8cc9ccc2831c5446002e864f1717)
- [emul](../hardware/P477_仿真器实例结构.md)
- [mspi_xfer_packet](../peripheral_bus_storage_model_reference/P051_mspi_xfer_packet_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [emul_mspi_device_api](../hardware/P483_MSPI仿真设备API结构.md)
- [transceive](https://docs.zephyrproject.org/latest/doxygen/html/structemul__mspi__device__api.html#afb3852793d752722841739fc486c6e4f)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__emul.html#aa3e45d11717b737ea8c6b4b19459991a)
- [target](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__emul.html#aa2b65e70ab7c2218929a6042bd0fd548)
- [api](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__emul.html#a2d247195c375c1aac30beec32dc11099)
- [dev_idx](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__emul.html#a5386510f101d186581abbde6b624be09)
- [emul_mspi_driver_api](../hardware/P484_MSPI仿真驱动API结构.md)
- [mspi_driver_api](../peripheral_bus_storage_model_reference/P042_mspi_driver_api_结构体.md)
- [mspi_api](https://docs.zephyrproject.org/latest/doxygen/html/structemul__mspi__driver__api.html#a2b5aef76272e620fcb77ba9532f0aee6)
- [trigger_event](https://docs.zephyrproject.org/latest/doxygen/html/structemul__mspi__driver__api.html#a7b2ab7da5d949ab05dda7cc0dbc24ff9)
- [mspi_emul_find_emul](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__emul__interface.html#gabecb33236ed3a6a93a28edef0a4c3ae7)
- [find_emul](https://docs.zephyrproject.org/latest/doxygen/html/structemul__mspi__driver__api.html#a0fe96769384075e9aee7daa1c30e32a6)
- [DEVICE_API_EXTENDS](../device_reference/P007_设备模型头文件参考.md#a2b0530c13706c66229d35977c6553db9)
- [mspi_emul_register](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__emul__interface.html#ga98c9a359f3385f49fbfe52b27254d261)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [emul.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2emul_8h.html)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [mspi.h](../peripheral_bus_storage_header_reference/P017_zephyr__drivers__mspi.h_头文件参考.md)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [emul_mspi_device_api::transceive](https://docs.zephyrproject.org/latest/doxygen/html/structemul__mspi__device__api.html#afb3852793d752722841739fc486c6e4f)
- [emul_mspi_driver_api::find_emul](https://docs.zephyrproject.org/latest/doxygen/html/structemul__mspi__driver__api.html#a0fe96769384075e9aee7daa1c30e32a6)
- [emul_mspi_driver_api::mspi_api](https://docs.zephyrproject.org/latest/doxygen/html/structemul__mspi__driver__api.html#a2b5aef76272e620fcb77ba9532f0aee6)
- [emul_mspi_driver_api::trigger_event](https://docs.zephyrproject.org/latest/doxygen/html/structemul__mspi__driver__api.html#a7b2ab7da5d949ab05dda7cc0dbc24ff9)
- [mspi_emul::api](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__emul.html#a2d247195c375c1aac30beec32dc11099)
- [mspi_emul::dev_idx](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__emul.html#a5386510f101d186581abbde6b624be09)
- [mspi_emul::target](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__emul.html#aa2b65e70ab7c2218929a6042bd0fd548)
- [mspi_emul::node](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__emul.html#aa3e45d11717b737ea8c6b4b19459991a)

---

[上一章](P566_msg.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P568_mspm0_clock_control.h_源码浏览.md)
