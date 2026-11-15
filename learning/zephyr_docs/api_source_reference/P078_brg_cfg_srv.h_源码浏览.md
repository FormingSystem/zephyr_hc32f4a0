---
id: learning.zephyr-docs.api-source-reference.page-78
title: brg_cfg_srv.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/brg__cfg__srv_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第78章\_brg\_cfg\_srv.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/brg__cfg__srv_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/brg__cfg__srv_8h.html)。

## 78.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00025"></a>
<a id="foldopen00030"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="abrg__cfg_8h_html"></a>
<a id="astructbt__mesh__model__cb_html"></a>
<a id="astructbt__mesh__model__op_html"></a>

```c
/*
 * Copyright (c) 2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_BRG_CFG_SRV_H__
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_BRG_CFG_SRV_H__

#include <zephyr/bluetooth/mesh/brg_cfg.h>

#ifdef __cplusplus
extern "C" {
#endif


#define BT_MESH_MODEL_BRG_CFG_SRV                                                                  \
        BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_BRG_CFG_SRV, _bt_mesh_brg_cfg_srv_op, NULL, NULL,        \
                         &_bt_mesh_brg_cfg_srv_cb)

extern const struct bt_mesh_model_op _bt_mesh_brg_cfg_srv_op[];
extern const struct bt_mesh_model_cb _bt_mesh_brg_cfg_srv_cb;


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_BRG_CFG_SRV_H__ */
```

## 78.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 47 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_BRG_CFG_SRV_H__`。

## 78.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/brg__cfg__srv_8h.html)
- [zephyr/bluetooth/mesh/brg_cfg.h](https://docs.zephyrproject.org/latest/doxygen/html/brg__cfg_8h.html)
- [bt_mesh_model_op](../bluetooth_mesh_model_reference/P078_bt_mesh_model_op_结构体.md)
- [bt_mesh_model_cb](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md)
- [brg_cfg.h](https://docs.zephyrproject.org/latest/doxygen/html/brg__cfg_8h.html)

---

[上一章](P077_brg_cfg_cli.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P079_buf_loader.h_源码浏览.md)
