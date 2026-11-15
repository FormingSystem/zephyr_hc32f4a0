---
id: learning.zephyr-docs.api-source-reference.page-143
title: dmop.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dmop_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第143章\_dmop.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dmop_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dmop_8h.html)。

## 143.1\_原始可见代码（Source Code）

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
<a id="l00024"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="agroup__xen__device__model_html_ga11aa8e4e414cd36de158467c602d0648"></a>
<a id="agroup__xen__device__model_html_ga2d5158224201ab0e00f5bc646aeac6d7"></a>
<a id="agroup__xen__device__model_html_ga40415eef4694532cc74e9072c4dbf932"></a>
<a id="agroup__xen__device__model_html_ga446b7e88737168d3f9664209a8aec7ea"></a>
<a id="agroup__xen__device__model_html_ga4c1fd9b02e326c62ccd04b97647e8fff"></a>
<a id="agroup__xen__device__model_html_ga6c806ca662b075fa0ff7efec4ac114ee"></a>
<a id="agroup__xen__device__model_html_gac0649dea8445c2dc0767f559924ebb42"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>

```c
/*
 * Copyright (c) 2025 TOKITA Hiroshi
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_XEN_DMOP_H_
#define ZEPHYR_INCLUDE_XEN_DMOP_H_

#include <xen/public/hvm/dm_op.h>


int dmop_create_ioreq_server(domid_t domid, uint8_t handle_bufioreq, ioservid_t *id);

int dmop_destroy_ioreq_server(domid_t domid, ioservid_t id);

int dmop_map_io_range_to_ioreq_server(domid_t domid, ioservid_t id,
        uint32_t type,
        uint64_t start,
        uint64_t end);

int dmop_unmap_io_range_from_ioreq_server(domid_t domid, ioservid_t id, uint32_t type,
                                          uint64_t start, uint64_t end);

int dmop_set_ioreq_server_state(domid_t domid, ioservid_t id, uint8_t enabled);

int dmop_nr_vcpus(domid_t domid);

int dmop_set_irq_level(domid_t domid, uint32_t irq, uint8_t level);


#endif /* ZEPHYR_INCLUDE_XEN_DMOP_H_ */
```

## 143.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 TOKITA Hiroshi。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 145 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_XEN_DMOP_H_`。

## 143.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dmop_8h.html)
- [dmop_create_ioreq_server](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__device__model.html#ga40415eef4694532cc74e9072c4dbf932)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [dmop_destroy_ioreq_server](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__device__model.html#ga446b7e88737168d3f9664209a8aec7ea)
- [dmop_map_io_range_to_ioreq_server](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__device__model.html#gac0649dea8445c2dc0767f559924ebb42)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [dmop_unmap_io_range_from_ioreq_server](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__device__model.html#ga4c1fd9b02e326c62ccd04b97647e8fff)
- [dmop_set_ioreq_server_state](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__device__model.html#ga2d5158224201ab0e00f5bc646aeac6d7)
- [dmop_nr_vcpus](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__device__model.html#ga11aa8e4e414cd36de158467c602d0648)
- [dmop_set_irq_level](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__device__model.html#ga6c806ca662b075fa0ff7efec4ac114ee)

---

[上一章](P142_dma_xilinx_adma.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P144_dns_sd.h_源码浏览.md)
