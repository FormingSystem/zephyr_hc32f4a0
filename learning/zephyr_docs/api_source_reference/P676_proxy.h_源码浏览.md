---
id: learning.zephyr-docs.api-source-reference.page-676
title: proxy.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/proxy_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第676章\_proxy.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/proxy_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/proxy_8h.html)。

## 676.1\_原始可见代码（Source Code）

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
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="foldopen00033"></a>
<a id="l00033"></a>
<a id="l00039"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="foldopen00056"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="agroup__bt__mesh__proxy_html_ga07d4edf80bdbc39f626f66720035c98b"></a>
<a id="agroup__bt__mesh__proxy_html_ga7fb3c76f1be6943dd4a18f26e8dd18e7"></a>
<a id="agroup__bt__mesh__proxy_html_ga9a72515992af4f93a34a6c1aaf69d8df"></a>
<a id="agroup__bt__mesh__proxy_html_gaa9978d460b31412c96c6c1685729ec4f"></a>
<a id="agroup__bt__mesh__proxy_html_gaecd529a9fd0df83b3d775d32885802f1"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__mesh__proxy__cb_html"></a>
<a id="astructbt__mesh__proxy__cb_html_a207ebf7e3f1f1e732d4540af000bf2ef"></a>
<a id="astructbt__mesh__proxy__cb_html_ae6f129ae511681d2f1fccafedba47918"></a>
<a id="asys_2iterable__sections_8h_html"></a>

```c


/*
 * Copyright (c) 2017 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_PROXY_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_PROXY_H_

#include <stdint.h>

#include <zephyr/kernel.h>
#include <zephyr/sys/iterable_sections.h>


#ifdef __cplusplus
extern "C" {
#endif

struct bt_mesh_proxy_cb {
        void (*identity_enabled)(uint16_t net_idx);
        void (*identity_disabled)(uint16_t net_idx);
};

#define BT_MESH_PROXY_CB_DEFINE(_name)                                         \
        static const STRUCT_SECTION_ITERABLE(                                  \
                bt_mesh_proxy_cb, _CONCAT(bt_mesh_proxy_cb_, _name))

int bt_mesh_proxy_identity_enable(void);

int bt_mesh_proxy_private_identity_enable(void);

int bt_mesh_proxy_connect(uint16_t net_idx);

int bt_mesh_proxy_disconnect(uint16_t net_idx);

int bt_mesh_proxy_solicit(uint16_t net_idx);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_PROXY_H_ */
```

## 676.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2017 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 123 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_PROXY_H_`。

## 676.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/proxy_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [bt_mesh_proxy_cb](../bluetooth_mesh_model_reference/P089_bt_mesh_proxy_cb_结构体.md)
- [identity_enabled](../bluetooth_mesh_model_reference/P089_bt_mesh_proxy_cb_结构体.md#ae6f129ae511681d2f1fccafedba47918)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [identity_disabled](../bluetooth_mesh_model_reference/P089_bt_mesh_proxy_cb_结构体.md#a207ebf7e3f1f1e732d4540af000bf2ef)
- [bt_mesh_proxy_identity_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__proxy.html#ga7fb3c76f1be6943dd4a18f26e8dd18e7)
- [bt_mesh_proxy_private_identity_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__proxy.html#gaecd529a9fd0df83b3d775d32885802f1)
- [bt_mesh_proxy_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__proxy.html#ga07d4edf80bdbc39f626f66720035c98b)
- [bt_mesh_proxy_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__proxy.html#gaa9978d460b31412c96c6c1685729ec4f)
- [bt_mesh_proxy_solicit](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__proxy.html#ga9a72515992af4f93a34a6c1aaf69d8df)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [bt_mesh_proxy_cb::identity_disabled](../bluetooth_mesh_model_reference/P089_bt_mesh_proxy_cb_结构体.md#a207ebf7e3f1f1e732d4540af000bf2ef)
- [bt_mesh_proxy_cb::identity_enabled](../bluetooth_mesh_model_reference/P089_bt_mesh_proxy_cb_结构体.md#ae6f129ae511681d2f1fccafedba47918)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)

---

[上一章](P675_protected_storage.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P677_ps.h_源码浏览.md)
