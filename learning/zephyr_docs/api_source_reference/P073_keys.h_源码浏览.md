---
id: learning.zephyr-docs.api-source-reference.page-73
title: keys.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2mesh_2keys_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第73章\_keys.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2mesh_2keys_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2mesh_2keys_8h.html)。

## 73.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="foldopen00022"></a>
<a id="l00022"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="akey__ids_8h_html_a11e986351c65bd3dc3c0fe2cd9926e4b"></a>
<a id="astdint_8h_html"></a>
<a id="astructbt__mesh__key_html"></a>
<a id="astructbt__mesh__key_html_a50acd9d36423b22aab033795b9d29d78"></a>

```c


/*
 * Copyright (c) 2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_KEYS_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_KEYS_H_

#include <stdint.h>
#include <psa/crypto.h>

#ifdef __cplusplus
extern "C" {
#endif

struct bt_mesh_key {
        psa_key_id_t key;
};

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_KEYS_H_ */
```

## 73.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 31 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_KEYS_H_`。

## 73.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2mesh_2keys_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [bt_mesh_key](../bluetooth_mesh_model_reference/P068_bt_mesh_key_结构体.md)
- [psa_key_id_t](https://docs.zephyrproject.org/latest/doxygen/html/key__ids_8h.html#a11e986351c65bd3dc3c0fe2cd9926e4b)
- [key](../bluetooth_mesh_model_reference/P068_bt_mesh_key_结构体.md#a50acd9d36423b22aab033795b9d29d78)
- [bt_mesh_key::key](../bluetooth_mesh_model_reference/P068_bt_mesh_key_结构体.md#a50acd9d36423b22aab033795b9d29d78)

---

[上一章](P072_crypto.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P074_bmm350.h_源码浏览.md)
