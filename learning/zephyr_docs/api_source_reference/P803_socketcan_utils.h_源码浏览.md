---
id: learning.zephyr-docs.api-source-reference.page-803
title: socketcan_utils.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/socketcan__utils_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第803章\_socketcan\_utils.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/socketcan__utils_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/socketcan__utils_8h.html)。

## 803.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00029"></a>
<a id="foldopen00036"></a>
<a id="l00036"></a>
<a id="l00037"></a>
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
<a id="foldopen00060"></a>
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
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="foldopen00090"></a>
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
<a id="foldopen00106"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="adrivers_2can_8h_html"></a>
<a id="agroup__can__controller_html_ga1fdf15ce4a3b333488f9b630ec836d52"></a>
<a id="agroup__can__controller_html_ga22f85e1d16b93e46200f9673abdbb589"></a>
<a id="agroup__can__controller_html_ga8314716fe2b66d567b3fd377b8ee9dc3"></a>
<a id="agroup__can__controller_html_ga9ed5a06a97db2c955a7db4b6e386d5e3"></a>
<a id="agroup__can__controller_html_gaa1d866167c0c23f8d5c0c15385589601"></a>
<a id="agroup__can__controller_html_gaed376ef16b84cd1974255fbb26dc3d7f"></a>
<a id="agroup__can__controller_html_gafa40c165d016955ec0c856a7fd53168f"></a>
<a id="agroup__socket__can_html_ga040c4882d349cdc3c568f3580e823cba"></a>
<a id="agroup__socket__can_html_ga409cae306f00226ef192320f4f01f51c"></a>
<a id="agroup__socket__can_html_ga49ffbe49124fdc472946fd0978f9a6d5"></a>
<a id="agroup__socket__can_html_gaccedf1d7bf2131797e53a16dc93cd7e1"></a>
<a id="agroup__socket__can_html_gace1d124719f8eac5f59788811c4afaf4"></a>
<a id="agroup__socket__can_html_gaf5cee7f0d6385c6fc4736e9399ed06b3"></a>
<a id="agroup__sys-util_html_ga111fe4e9d63758262fc6810a782cb32a"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__sys-util_html_ga3c12c6d36ad0aa481a3436923d21f4f8"></a>
<a id="aminmax_8h_html"></a>
<a id="aminmax_8h_html_ab1e1ffb6aa15887fa3bda4cfdef1f53a"></a>
<a id="asocketcan_8h_html"></a>
<a id="astring_8h_html_a4137694174d4ca2fad886a1db355015c"></a>
<a id="astring_8h_html_af0f01bffcd16daa9143f6014d10a25ad"></a>
<a id="astructcan__filter_html"></a>
<a id="astructcan__filter_html_a15632117f3f031fbbeb28ef562f9ac94"></a>
<a id="astructcan__filter_html_a7616e21f33be5fb43094d44530a1c5de"></a>
<a id="astructcan__filter_html_adf2b18eab11d360780707478a1f624b9"></a>
<a id="astructcan__frame_html"></a>
<a id="astructcan__frame_html_a014c42277e886906e6c761bc6f21fb47"></a>
<a id="astructcan__frame_html_a1e71125342a01a6e5a68a14cb075ce7c"></a>
<a id="astructcan__frame_html_a7ad0d8d62322affafbfd23839ee81d5d"></a>
<a id="astructcan__frame_html_ac4b43443b2a338d35f0e1d3ef8355960"></a>
<a id="astructsocketcan__filter_html"></a>
<a id="astructsocketcan__filter_html_a841857f05f1e1a887be50d8e507a03f9"></a>
<a id="astructsocketcan__filter_html_a9217950edb190dc70783d9b87676ae47"></a>
<a id="astructsocketcan__frame_html"></a>
<a id="astructsocketcan__frame_html_a43511a491c9b8cf63b4ff592eb77a6e6"></a>
<a id="astructsocketcan__frame_html_a4ab22ff419e3c7397c64a1309cbdb623"></a>
<a id="astructsocketcan__frame_html_aa21e8007363ab0183c7b9d6c59cb4731"></a>
<a id="astructsocketcan__frame_html_af9ddb322cdc3d886182cce65f673177d"></a>

```c


/*
 * Copyright (c) 2019 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_SOCKETCAN_UTILS_H_
#define ZEPHYR_INCLUDE_NET_SOCKETCAN_UTILS_H_

#include <zephyr/drivers/can.h>
#include <zephyr/net/socketcan.h>
#include <zephyr/sys/minmax.h>

#ifdef __cplusplus
extern "C" {
#endif


static inline void socketcan_to_can_frame(const struct socketcan_frame *sframe,
                                          struct can_frame *zframe)
{
        memset(zframe, 0, sizeof(*zframe));

        zframe->flags |= (sframe->can_id & BIT(31)) != 0 ? CAN_FRAME_IDE : 0;
        zframe->flags |= (sframe->can_id & BIT(30)) != 0 ? CAN_FRAME_RTR : 0;
        zframe->flags |= (sframe->flags & CANFD_FDF) != 0 ? CAN_FRAME_FDF : 0;
        zframe->flags |= (sframe->flags & CANFD_BRS) != 0 ? CAN_FRAME_BRS : 0;
        zframe->id = sframe->can_id & BIT_MASK(29);
        zframe->dlc = can_bytes_to_dlc(sframe->len);

        if ((zframe->flags & CAN_FRAME_RTR) == 0U) {
                memcpy(zframe->data, sframe->data,
                       min3(sframe->len, sizeof(sframe->data), sizeof(zframe->data)));
        }
}

static inline void socketcan_from_can_frame(const struct can_frame *zframe,
                                            struct socketcan_frame *sframe)
{
        memset(sframe, 0, sizeof(*sframe));

        sframe->can_id = zframe->id;
        sframe->can_id |= (zframe->flags & CAN_FRAME_IDE) != 0 ? BIT(31) : 0;
        sframe->can_id |= (zframe->flags & CAN_FRAME_RTR) != 0 ? BIT(30) : 0;
        sframe->len = can_dlc_to_bytes(zframe->dlc);

        if ((zframe->flags & CAN_FRAME_FDF) != 0) {
                sframe->flags |= CANFD_FDF;
        }

        if ((zframe->flags & CAN_FRAME_BRS) != 0) {
                sframe->flags |= CANFD_BRS;
        }

        if ((zframe->flags & CAN_FRAME_RTR) == 0U) {
                memcpy(sframe->data, zframe->data,
                       min3(sframe->len, sizeof(zframe->data), sizeof(sframe->data)));
        }
}

static inline void socketcan_to_can_filter(const struct socketcan_filter *sfilter,
                                           struct can_filter *zfilter)
{
        memset(zfilter, 0, sizeof(*zfilter));

        zfilter->flags |= (sfilter->can_id & BIT(31)) != 0 ? CAN_FILTER_IDE : 0;
        zfilter->id = sfilter->can_id & BIT_MASK(29);
        zfilter->mask = sfilter->can_mask & BIT_MASK(29);
}

static inline void socketcan_from_can_filter(const struct can_filter *zfilter,
                                             struct socketcan_filter *sfilter)
{
        memset(sfilter, 0, sizeof(*sfilter));

        sfilter->can_id = zfilter->id;
        sfilter->can_id |= (zfilter->flags & CAN_FILTER_IDE) != 0 ? BIT(31) : 0;

        sfilter->can_mask = zfilter->mask;
        sfilter->can_mask |= (zfilter->flags & CAN_FILTER_IDE) != 0 ? BIT(31) : 0;

        if (!IS_ENABLED(CONFIG_CAN_ACCEPT_RTR)) {
                sfilter->can_mask |= BIT(30);
        }
}


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_SOCKETCAN_H_ */
```

## 803.2\_可见注释译文（Comments）

### 注释 1：原第 7 行

版权（Copyright）：© 2019 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 130 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_SOCKETCAN_H_`。

## 803.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/socketcan__utils_8h.html)
- [zephyr/drivers/can.h](../can_driver_reference/P001_CAN驱动头文件参考.md)
- [zephyr/net/socketcan.h](https://docs.zephyrproject.org/latest/doxygen/html/socketcan_8h.html)
- [zephyr/sys/minmax.h](../numeric_reference/P001_最小最大值与限幅宏参考.md)
- [socketcan_to_can_frame](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#gaccedf1d7bf2131797e53a16dc93cd7e1)
- [socketcan_frame](../network_service_model_reference/P057_socketcan_frame_结构体.md)
- [can_frame](../hardware/P363_CAN帧结构.md)
- [memset](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#a4137694174d4ca2fad886a1db355015c)
- [flags](../hardware/P363_CAN帧结构.md#a1e71125342a01a6e5a68a14cb075ce7c)
- [can_id](../network_service_model_reference/P057_socketcan_frame_结构体.md#a43511a491c9b8cf63b4ff592eb77a6e6)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [CAN_FRAME_IDE](../hardware/P362_CAN控制器接口.md#ga9ed5a06a97db2c955a7db4b6e386d5e3)
- [CAN_FRAME_RTR](../hardware/P362_CAN控制器接口.md#gaed376ef16b84cd1974255fbb26dc3d7f)
- [flags](../network_service_model_reference/P057_socketcan_frame_结构体.md#af9ddb322cdc3d886182cce65f673177d)
- [CANFD_FDF](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#ga409cae306f00226ef192320f4f01f51c)
- [CAN_FRAME_FDF](../hardware/P362_CAN控制器接口.md#ga22f85e1d16b93e46200f9673abdbb589)
- [CANFD_BRS](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#gace1d124719f8eac5f59788811c4afaf4)
- [CAN_FRAME_BRS](../hardware/P362_CAN控制器接口.md#ga1fdf15ce4a3b333488f9b630ec836d52)
- [id](../hardware/P363_CAN帧结构.md#a7ad0d8d62322affafbfd23839ee81d5d)
- [BIT_MASK](../util_reference/P001_通用工具公共接口.md#ga3c12c6d36ad0aa481a3436923d21f4f8)
- [dlc](../hardware/P363_CAN帧结构.md#a014c42277e886906e6c761bc6f21fb47)
- [can_bytes_to_dlc](../hardware/P362_CAN控制器接口.md#ga8314716fe2b66d567b3fd377b8ee9dc3)
- [len](../network_service_model_reference/P057_socketcan_frame_结构体.md#aa21e8007363ab0183c7b9d6c59cb4731)
- [memcpy](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#af0f01bffcd16daa9143f6014d10a25ad)
- [data](../hardware/P363_CAN帧结构.md#ac4b43443b2a338d35f0e1d3ef8355960)
- [data](../network_service_model_reference/P057_socketcan_frame_结构体.md#a4ab22ff419e3c7397c64a1309cbdb623)
- [min3](../numeric_reference/P001_最小最大值与限幅宏参考.md#ab1e1ffb6aa15887fa3bda4cfdef1f53a)
- [socketcan_from_can_frame](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#ga49ffbe49124fdc472946fd0978f9a6d5)
- [can_dlc_to_bytes](../hardware/P362_CAN控制器接口.md#gaa1d866167c0c23f8d5c0c15385589601)
- [socketcan_to_can_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#ga040c4882d349cdc3c568f3580e823cba)
- [socketcan_filter](../network_service_model_reference/P056_socketcan_filter_结构体.md)
- [can_filter](../hardware/P364_CAN过滤器结构.md)
- [flags](../hardware/P364_CAN过滤器结构.md#a7616e21f33be5fb43094d44530a1c5de)
- [can_id](../network_service_model_reference/P056_socketcan_filter_结构体.md#a9217950edb190dc70783d9b87676ae47)
- [CAN_FILTER_IDE](../hardware/P362_CAN控制器接口.md#gafa40c165d016955ec0c856a7fd53168f)
- [id](../hardware/P364_CAN过滤器结构.md#adf2b18eab11d360780707478a1f624b9)
- [mask](../hardware/P364_CAN过滤器结构.md#a15632117f3f031fbbeb28ef562f9ac94)
- [can_mask](../network_service_model_reference/P056_socketcan_filter_结构体.md#a841857f05f1e1a887be50d8e507a03f9)
- [socketcan_from_can_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#gaf5cee7f0d6385c6fc4736e9399ed06b3)
- [IS_ENABLED](../util_reference/P001_通用工具公共接口.md#ga111fe4e9d63758262fc6810a782cb32a)
- [can.h](../can_driver_reference/P001_CAN驱动头文件参考.md)
- [minmax.h](../numeric_reference/P001_最小最大值与限幅宏参考.md)
- [socketcan.h](https://docs.zephyrproject.org/latest/doxygen/html/socketcan_8h.html)
- [can_filter::mask](../hardware/P364_CAN过滤器结构.md#a15632117f3f031fbbeb28ef562f9ac94)
- [can_filter::flags](../hardware/P364_CAN过滤器结构.md#a7616e21f33be5fb43094d44530a1c5de)
- [can_filter::id](../hardware/P364_CAN过滤器结构.md#adf2b18eab11d360780707478a1f624b9)
- [can_frame::dlc](../hardware/P363_CAN帧结构.md#a014c42277e886906e6c761bc6f21fb47)
- [can_frame::flags](../hardware/P363_CAN帧结构.md#a1e71125342a01a6e5a68a14cb075ce7c)
- [can_frame::id](../hardware/P363_CAN帧结构.md#a7ad0d8d62322affafbfd23839ee81d5d)
- [can_frame::data](../hardware/P363_CAN帧结构.md#ac4b43443b2a338d35f0e1d3ef8355960)
- [socketcan_filter::can_mask](../network_service_model_reference/P056_socketcan_filter_结构体.md#a841857f05f1e1a887be50d8e507a03f9)
- [socketcan_filter::can_id](../network_service_model_reference/P056_socketcan_filter_结构体.md#a9217950edb190dc70783d9b87676ae47)
- [socketcan_frame::can_id](../network_service_model_reference/P057_socketcan_frame_结构体.md#a43511a491c9b8cf63b4ff592eb77a6e6)
- [socketcan_frame::data](../network_service_model_reference/P057_socketcan_frame_结构体.md#a4ab22ff419e3c7397c64a1309cbdb623)
- [socketcan_frame::len](../network_service_model_reference/P057_socketcan_frame_结构体.md#aa21e8007363ab0183c7b9d6c59cb4731)
- [socketcan_frame::flags](../network_service_model_reference/P057_socketcan_frame_结构体.md#af9ddb322cdc3d886182cce65f673177d)

---

[上一章](P802_socket_select.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P804_socketutils.h_源码浏览.md)
