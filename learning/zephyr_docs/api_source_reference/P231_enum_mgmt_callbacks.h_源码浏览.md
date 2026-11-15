---
id: learning.zephyr-docs.api-source-reference.page-231
title: enum_mgmt_callbacks.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/enum__mgmt__callbacks_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第231章\_enum\_mgmt\_callbacks.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/enum__mgmt__callbacks_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/enum__mgmt__callbacks_8h.html)。

## 231.1\_原始可见代码（Source Code）

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
<a id="l00027"></a>
<a id="foldopen00031"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="foldopen00044"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="agroup__mcumgr__callback__api__enum__mgmt_html_ga7ddc4c031948a2fee56fcbdb7d675a1d"></a>
<a id="agroup__mcumgr__callback__api__enum__mgmt_html_gga7ddc4c031948a2fee56fcbdb7d675a1da5f19a62b627e602db48748c91ce2354b"></a>
<a id="agroup__mcumgr__callback__api__enum__mgmt_html_gga7ddc4c031948a2fee56fcbdb7d675a1da749daeaef01327a881f91671b9222abf"></a>
<a id="agroup__mcumgr__callback__api_html_gga40ecf8933112abe76d7fedb3dcc7cdbeac23aa88bc1047404e2d75f7c5de7a6a3"></a>
<a id="astructenum__mgmt__detail__output_html"></a>
<a id="astructenum__mgmt__detail__output_html_a140d1f5cd4e4f7a88c5a1da98a927161"></a>
<a id="astructenum__mgmt__detail__output_html_a787c1a41fbe135b85176d3b0bb6ccd92"></a>
<a id="astructmgmt__group_html"></a>

```c
/*
 * Copyright (c) 2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_ENUM_MGMT_ENUM_MGMT_CALLBACKS_H_
#define ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_ENUM_MGMT_ENUM_MGMT_CALLBACKS_H_

#ifdef __cplusplus
extern "C" {
#endif


enum enum_mgmt_group_events {
        MGMT_EVT_OP_ENUM_MGMT_DETAILS           = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_ENUM, 0),

        MGMT_EVT_OP_ENUM_MGMT_ALL               = MGMT_DEF_EVT_OP_ALL(MGMT_EVT_GRP_ENUM),
};

struct enum_mgmt_detail_output {
        const struct mgmt_group *group;

        zcbor_state_t *zse;
};


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_ENUM_MGMT_ENUM_MGMT_CALLBACKS_H_ */
```

## 231.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 63 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_ENUM_MGMT_ENUM_MGMT_CALLBACKS_H_`。

## 231.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/enum__mgmt__callbacks_8h.html)
- [enum_mgmt_group_events](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__enum__mgmt.html#ga7ddc4c031948a2fee56fcbdb7d675a1d)
- [MGMT_EVT_OP_ENUM_MGMT_DETAILS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__enum__mgmt.html#gga7ddc4c031948a2fee56fcbdb7d675a1da749daeaef01327a881f91671b9222abf)
- [MGMT_EVT_GRP_ENUM](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga40ecf8933112abe76d7fedb3dcc7cdbeac23aa88bc1047404e2d75f7c5de7a6a3)
- [MGMT_EVT_OP_ENUM_MGMT_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__enum__mgmt.html#gga7ddc4c031948a2fee56fcbdb7d675a1da5f19a62b627e602db48748c91ce2354b)
- [enum_mgmt_detail_output](../system_service_model_reference/P026_enum_mgmt_detail_output_结构体.md)
- [mgmt_group](../system_service_model_reference/P068_mgmt_group_结构体.md)
- [group](../system_service_model_reference/P026_enum_mgmt_detail_output_结构体.md#a787c1a41fbe135b85176d3b0bb6ccd92)
- [zse](../system_service_model_reference/P026_enum_mgmt_detail_output_结构体.md#a140d1f5cd4e4f7a88c5a1da98a927161)
- [enum_mgmt_detail_output::zse](../system_service_model_reference/P026_enum_mgmt_detail_output_结构体.md#a140d1f5cd4e4f7a88c5a1da98a927161)
- [enum_mgmt_detail_output::group](../system_service_model_reference/P026_enum_mgmt_detail_output_结构体.md#a787c1a41fbe135b85176d3b0bb6ccd92)

---

[上一章](P230_enum_mgmt.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P232_eqdc_mcux.h_源码浏览.md)
