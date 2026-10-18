---
id: learning.zephyr-docs.api-source-reference.page-127
title: dfu_metadata.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dfu__metadata_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第127章\_dfu\_metadata.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dfu__metadata_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dfu__metadata_8h.html)。

## 127.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="foldopen00034"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="foldopen00046"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="foldopen00056"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="agroup__bt__mesh__dfu__metadata_html_ga3c5de8cefc6a47805a9c1af166e956c7"></a>
<a id="agroup__bt__mesh__dfu__metadata_html_ga7f9ab277a7a47ad9cd8e616d3aa810d4"></a>
<a id="agroup__bt__mesh__dfu__metadata_html_ga94de2f3730f600d58ff2102257d7ead9"></a>
<a id="agroup__bt__mesh__dfu__metadata_html_gadc818fb83b429b0f1bef0ba83ae7a52a"></a>
<a id="agroup__bt__mesh__dfu__metadata_html_gaec5fa6e61a6ae88ac7a14f1ec09585b8"></a>
<a id="agroup__bt__mesh__dfu__metadata_html_ggaec5fa6e61a6ae88ac7a14f1ec09585b8a791a8cbc2942ede20174cfc31408f692"></a>
<a id="agroup__bt__mesh__dfu__metadata_html_ggaec5fa6e61a6ae88ac7a14f1ec09585b8aaf99e24ebcc4d00e4096bf377b441af2"></a>
<a id="agroup__bt__mesh__dfu__metadata_html_ggaec5fa6e61a6ae88ac7a14f1ec09585b8ab2025499295ce1ed1d8669c954a7b5a0"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="akernel_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__mesh__dfu__metadata__fw__ver_html"></a>
<a id="astructbt__mesh__dfu__metadata__fw__ver_html_a3386d56c363d631e4b4e77ea49bd9e8d"></a>
<a id="astructbt__mesh__dfu__metadata__fw__ver_html_a7c21ae9b7340a1f13d107bf31aeeca90"></a>
<a id="astructbt__mesh__dfu__metadata__fw__ver_html_aadeed181c571412b42fbad8111f0d53d"></a>
<a id="astructbt__mesh__dfu__metadata__fw__ver_html_ad4bcde436cbf014cf24fa84888408cc1"></a>
<a id="astructbt__mesh__dfu__metadata_html"></a>
<a id="astructbt__mesh__dfu__metadata_html_a48a680b1c3a802e15d4212865fa1d0df"></a>
<a id="astructbt__mesh__dfu__metadata_html_a624e2e30f31d2d2f2554eb22c6950ebc"></a>
<a id="astructbt__mesh__dfu__metadata_html_a82719aefc21e1fac5a6e8813af23e131"></a>
<a id="astructbt__mesh__dfu__metadata_html_ac3e6dd2b069785ae359d49162d33e104"></a>
<a id="astructbt__mesh__dfu__metadata_html_ac487e125632b55b8477f648759dbbba0"></a>
<a id="astructbt__mesh__dfu__metadata_html_ae4853b55fda6ec8c4c8609d5648890ab"></a>
<a id="astructbt__mesh__dfu__metadata_html_af4d02eeccb2537b81738ffd186c7d9ed"></a>
<a id="astructnet__buf__simple_html"></a>

```c
/*
 * Copyright (c) 2021 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */



#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_DFU_METADATA_H__
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_DFU_METADATA_H__

#include <stdint.h>

#include <sys/types.h>

#include <zephyr/kernel.h>

#ifdef __cplusplus
extern "C" {
#endif

struct bt_mesh_dfu_metadata_fw_ver {
        uint8_t major;
        uint8_t minor;
        uint16_t revision;
        uint32_t build_num;
};

enum bt_mesh_dfu_metadata_fw_core_type {
        BT_MESH_DFU_FW_CORE_TYPE_APP = BIT(0),
        BT_MESH_DFU_FW_CORE_TYPE_NETWORK = BIT(1),
        BT_MESH_DFU_FW_CORE_TYPE_APP_SPECIFIC_BLOB = BIT(2),
};

struct bt_mesh_dfu_metadata {
        struct bt_mesh_dfu_metadata_fw_ver fw_ver;
        uint32_t fw_size;
        enum bt_mesh_dfu_metadata_fw_core_type fw_core_type;
        uint32_t comp_hash;
        uint16_t elems;
        uint8_t *user_data;
        uint32_t user_data_len;
};

int bt_mesh_dfu_metadata_decode(struct net_buf_simple *buf,
                                struct bt_mesh_dfu_metadata *metadata);

int bt_mesh_dfu_metadata_encode(const struct bt_mesh_dfu_metadata *metadata,
                                struct net_buf_simple *buf);

int bt_mesh_dfu_metadata_comp_hash_get(struct net_buf_simple *buf, uint8_t *key, uint32_t *hash);

int bt_mesh_dfu_metadata_comp_hash_local_get(uint8_t *key, uint32_t *hash);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_DFU_METADATA_H__ */

```

## 127.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 118 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_DFU_METADATA_H__`。

## 127.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dfu__metadata_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [bt_mesh_dfu_metadata_fw_ver](../bluetooth_mesh_model_reference/P052_bt_mesh_dfu_metadata_fw_ver_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [major](../bluetooth_mesh_model_reference/P052_bt_mesh_dfu_metadata_fw_ver_结构体.md#ad4bcde436cbf014cf24fa84888408cc1)
- [minor](../bluetooth_mesh_model_reference/P052_bt_mesh_dfu_metadata_fw_ver_结构体.md#a3386d56c363d631e4b4e77ea49bd9e8d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [revision](../bluetooth_mesh_model_reference/P052_bt_mesh_dfu_metadata_fw_ver_结构体.md#aadeed181c571412b42fbad8111f0d53d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [build_num](../bluetooth_mesh_model_reference/P052_bt_mesh_dfu_metadata_fw_ver_结构体.md#a7c21ae9b7340a1f13d107bf31aeeca90)
- [bt_mesh_dfu_metadata_fw_core_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__metadata.html#gaec5fa6e61a6ae88ac7a14f1ec09585b8)
- [BT_MESH_DFU_FW_CORE_TYPE_APP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__metadata.html#ggaec5fa6e61a6ae88ac7a14f1ec09585b8ab2025499295ce1ed1d8669c954a7b5a0)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_MESH_DFU_FW_CORE_TYPE_NETWORK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__metadata.html#ggaec5fa6e61a6ae88ac7a14f1ec09585b8a791a8cbc2942ede20174cfc31408f692)
- [BT_MESH_DFU_FW_CORE_TYPE_APP_SPECIFIC_BLOB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__metadata.html#ggaec5fa6e61a6ae88ac7a14f1ec09585b8aaf99e24ebcc4d00e4096bf377b441af2)
- [bt_mesh_dfu_metadata](../bluetooth_mesh_model_reference/P051_bt_mesh_dfu_metadata_结构体.md)
- [fw_ver](../bluetooth_mesh_model_reference/P051_bt_mesh_dfu_metadata_结构体.md#a48a680b1c3a802e15d4212865fa1d0df)
- [fw_size](../bluetooth_mesh_model_reference/P051_bt_mesh_dfu_metadata_结构体.md#a624e2e30f31d2d2f2554eb22c6950ebc)
- [fw_core_type](../bluetooth_mesh_model_reference/P051_bt_mesh_dfu_metadata_结构体.md#a82719aefc21e1fac5a6e8813af23e131)
- [comp_hash](../bluetooth_mesh_model_reference/P051_bt_mesh_dfu_metadata_结构体.md#af4d02eeccb2537b81738ffd186c7d9ed)
- [elems](../bluetooth_mesh_model_reference/P051_bt_mesh_dfu_metadata_结构体.md#ac487e125632b55b8477f648759dbbba0)
- [user_data](../bluetooth_mesh_model_reference/P051_bt_mesh_dfu_metadata_结构体.md#ac3e6dd2b069785ae359d49162d33e104)
- [user_data_len](../bluetooth_mesh_model_reference/P051_bt_mesh_dfu_metadata_结构体.md#ae4853b55fda6ec8c4c8609d5648890ab)
- [bt_mesh_dfu_metadata_decode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__metadata.html#ga7f9ab277a7a47ad9cd8e616d3aa810d4)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bt_mesh_dfu_metadata_encode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__metadata.html#ga94de2f3730f600d58ff2102257d7ead9)
- [bt_mesh_dfu_metadata_comp_hash_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__metadata.html#ga3c5de8cefc6a47805a9c1af166e956c7)
- [bt_mesh_dfu_metadata_comp_hash_local_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__metadata.html#gadc818fb83b429b0f1bef0ba83ae7a52a)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [bt_mesh_dfu_metadata_fw_ver::minor](../bluetooth_mesh_model_reference/P052_bt_mesh_dfu_metadata_fw_ver_结构体.md#a3386d56c363d631e4b4e77ea49bd9e8d)
- [bt_mesh_dfu_metadata_fw_ver::build_num](../bluetooth_mesh_model_reference/P052_bt_mesh_dfu_metadata_fw_ver_结构体.md#a7c21ae9b7340a1f13d107bf31aeeca90)
- [bt_mesh_dfu_metadata_fw_ver::revision](../bluetooth_mesh_model_reference/P052_bt_mesh_dfu_metadata_fw_ver_结构体.md#aadeed181c571412b42fbad8111f0d53d)
- [bt_mesh_dfu_metadata_fw_ver::major](../bluetooth_mesh_model_reference/P052_bt_mesh_dfu_metadata_fw_ver_结构体.md#ad4bcde436cbf014cf24fa84888408cc1)
- [bt_mesh_dfu_metadata::fw_ver](../bluetooth_mesh_model_reference/P051_bt_mesh_dfu_metadata_结构体.md#a48a680b1c3a802e15d4212865fa1d0df)
- [bt_mesh_dfu_metadata::fw_size](../bluetooth_mesh_model_reference/P051_bt_mesh_dfu_metadata_结构体.md#a624e2e30f31d2d2f2554eb22c6950ebc)
- [bt_mesh_dfu_metadata::fw_core_type](../bluetooth_mesh_model_reference/P051_bt_mesh_dfu_metadata_结构体.md#a82719aefc21e1fac5a6e8813af23e131)
- [bt_mesh_dfu_metadata::user_data](../bluetooth_mesh_model_reference/P051_bt_mesh_dfu_metadata_结构体.md#ac3e6dd2b069785ae359d49162d33e104)
- [bt_mesh_dfu_metadata::elems](../bluetooth_mesh_model_reference/P051_bt_mesh_dfu_metadata_结构体.md#ac487e125632b55b8477f648759dbbba0)
- [bt_mesh_dfu_metadata::user_data_len](../bluetooth_mesh_model_reference/P051_bt_mesh_dfu_metadata_结构体.md#ae4853b55fda6ec8c4c8609d5648890ab)
- [bt_mesh_dfu_metadata::comp_hash](../bluetooth_mesh_model_reference/P051_bt_mesh_dfu_metadata_结构体.md#af4d02eeccb2537b81738ffd186c7d9ed)

---

[上一章](P126_dfu.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P128_dhcpv4.h_源码浏览.md)
