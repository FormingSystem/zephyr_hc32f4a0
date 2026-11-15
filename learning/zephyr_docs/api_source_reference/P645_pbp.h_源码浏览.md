---
id: learning.zephyr-docs.api-source-reference.page-645
title: pbp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pbp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第645章\_pbp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pbp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pbp_8h.html)。

## 645.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="foldopen00053"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="abluetooth_2audio_2audio_8h_html"></a>
<a id="abluetooth_2bluetooth_8h_html"></a>
<a id="abluetooth_2uuid_8h_html"></a>
<a id="adata_8h_html"></a>
<a id="agroup__bt__pbp_html_ga2685c082fb56bfece540c9f43bf5ba47"></a>
<a id="agroup__bt__pbp_html_ga311b1fdb0a2aa24a09e8d3b3566693ff"></a>
<a id="agroup__bt__pbp_html_gaa496ac2a3ec9dd5fc013a1f4a804b11b"></a>
<a id="agroup__bt__pbp_html_gga2685c082fb56bfece540c9f43bf5ba47a20aff6780e8f5ec5aaf0ea5500331638"></a>
<a id="agroup__bt__pbp_html_gga2685c082fb56bfece540c9f43bf5ba47a6d059892e294eec6a097d8e2813a352e"></a>
<a id="agroup__bt__pbp_html_gga2685c082fb56bfece540c9f43bf5ba47aeda548305ece142429bfa97fd9f612df"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="anet__buf_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructbt__data_html"></a>
<a id="astructnet__buf__simple_html"></a>
<a id="asys_2util_8h_html"></a>
<a id="autil__macro_8h_html"></a>

```c

/*
 * Copyright 2023 NXP
 * Copyright (c) 2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_PBP_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_PBP_H_

#include <stddef.h>
#include <stdint.h>

#include <zephyr/bluetooth/audio/audio.h>
#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/bluetooth/data.h>
#include <zephyr/bluetooth/uuid.h>
#include <zephyr/net_buf.h>
#include <zephyr/sys/util.h>
#include <zephyr/sys/util_macro.h>

#ifdef __cplusplus
extern "C" {
#endif

#define BT_PBP_MIN_PBA_SIZE             (BT_UUID_SIZE_16 + 1 + 1)

enum bt_pbp_announcement_feature {
        BT_PBP_ANNOUNCEMENT_FEATURE_ENCRYPTION = BIT(0U),
        BT_PBP_ANNOUNCEMENT_FEATURE_STANDARD_QUALITY = BIT(1U),
        BT_PBP_ANNOUNCEMENT_FEATURE_HIGH_QUALITY = BIT(2U),
};

int bt_pbp_get_announcement(const uint8_t meta[], size_t meta_len,
                            enum bt_pbp_announcement_feature features,
                            struct net_buf_simple *pba_data_buf);

int bt_pbp_parse_announcement(struct bt_data *data, enum bt_pbp_announcement_feature *features,
                              uint8_t **meta);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_PBP_H_ */
```

## 645.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：2023 NXP。

版权（Copyright）：© 2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 104 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_PBP_H_`。

## 645.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pbp_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/bluetooth/audio/audio.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2audio_8h.html)
- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [zephyr/bluetooth/data.h](https://docs.zephyrproject.org/latest/doxygen/html/data_8h.html)
- [zephyr/bluetooth/uuid.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2uuid_8h.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [bt_pbp_announcement_feature](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbp.html#ga2685c082fb56bfece540c9f43bf5ba47)
- [BT_PBP_ANNOUNCEMENT_FEATURE_ENCRYPTION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbp.html#gga2685c082fb56bfece540c9f43bf5ba47aeda548305ece142429bfa97fd9f612df)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_PBP_ANNOUNCEMENT_FEATURE_STANDARD_QUALITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbp.html#gga2685c082fb56bfece540c9f43bf5ba47a20aff6780e8f5ec5aaf0ea5500331638)
- [BT_PBP_ANNOUNCEMENT_FEATURE_HIGH_QUALITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbp.html#gga2685c082fb56bfece540c9f43bf5ba47a6d059892e294eec6a097d8e2813a352e)
- [bt_pbp_get_announcement](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbp.html#gaa496ac2a3ec9dd5fc013a1f4a804b11b)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bt_pbp_parse_announcement](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbp.html#ga311b1fdb0a2aa24a09e8d3b3566693ff)
- [bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)
- [audio.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2audio_8h.html)
- [bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [uuid.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2uuid_8h.html)
- [data.h](https://docs.zephyrproject.org/latest/doxygen/html/data_8h.html)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [util.h](../util_reference/P002_通用工具头文件参考.md)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P644_pbap.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P646_pca-series-gpio.h_源码浏览.md)
