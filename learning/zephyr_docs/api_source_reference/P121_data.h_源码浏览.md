---
id: learning.zephyr-docs.api-source-reference.page-121
title: data.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/data_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第121章\_data.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/data_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/data_8h.html)。

## 121.1\_原始可见代码（Source Code）

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
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="foldopen00040"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="foldopen00059"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="foldopen00075"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="adata_8h_html_a3c067b16468ebd17973faeded0fc83c9"></a>
<a id="adata_8h_html_a3d2c6adc42eb9510734630f38d921b9a"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructbt__data_html"></a>
<a id="astructbt__data_html_a984aecb40a4993ffa113be53942db065"></a>
<a id="astructbt__data_html_abda19091a1b8f99d385f11772ef34d5f"></a>
<a id="astructbt__data_html_ac80ec10101ad69a86f703a4e652c7826"></a>

```c


/*
 * Copyright (c) 2017 Nordic Semiconductor ASA
 * Copyright (c) 2015-2016 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_DATA_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_DATA_H_

#include <stddef.h>
#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

#define BT_DATA_SERIALIZED_SIZE(data_len) ((data_len) + 2)

struct bt_data {
        uint8_t type;
        uint8_t data_len;
        const uint8_t *data;
};

#define BT_DATA(_type, _data, _data_len) \
        { \
                .type = (_type), \
                .data_len = (_data_len), \
                .data = (const uint8_t *)(_data), \
        }

#define BT_DATA_BYTES(_type, _bytes...) \
        BT_DATA(_type, ((uint8_t []) { _bytes }), \
                sizeof((uint8_t []) { _bytes }))

size_t bt_data_get_len(const struct bt_data data[], size_t data_count);

size_t bt_data_serialize(const struct bt_data *input, uint8_t *output);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_DATA_H_ */
```

## 121.2\_可见注释译文（Comments）

### 注释 1：原第 6 行

版权（Copyright）：© 2017 Nordic Semiconductor ASA。

版权（Copyright）：© 2015-2016 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 112 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_DATA_H_`。

## 121.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/data_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [type](../bluetooth_connection_model_reference/P041_bt_data_结构体.md#a984aecb40a4993ffa113be53942db065)
- [data_len](../bluetooth_connection_model_reference/P041_bt_data_结构体.md#abda19091a1b8f99d385f11772ef34d5f)
- [data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md#ac80ec10101ad69a86f703a4e652c7826)
- [bt_data_get_len](https://docs.zephyrproject.org/latest/doxygen/html/data_8h.html#a3d2c6adc42eb9510734630f38d921b9a)
- [bt_data_serialize](https://docs.zephyrproject.org/latest/doxygen/html/data_8h.html#a3c067b16468ebd17973faeded0fc83c9)
- [bt_data::type](../bluetooth_connection_model_reference/P041_bt_data_结构体.md#a984aecb40a4993ffa113be53942db065)
- [bt_data::data_len](../bluetooth_connection_model_reference/P041_bt_data_结构体.md#abda19091a1b8f99d385f11772ef34d5f)
- [bt_data::data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md#ac80ec10101ad69a86f703a4e652c7826)

---

[上一章](P120_dai.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P122_decoder.h_源码浏览.md)
