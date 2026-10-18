---
id: learning.zephyr-docs.api-source-reference.page-275
title: fs_mgmt_callbacks.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fs__mgmt__callbacks_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第275章\_fs\_mgmt\_callbacks.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/fs__mgmt__callbacks_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/fs__mgmt__callbacks_8h.html)。

## 275.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00028"></a>
<a id="foldopen00032"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="foldopen00044"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="foldopen00064"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="agroup__mcumgr__callback__api__fs__mgmt_html_ga324223c20cbefe3400272e2789082c79"></a>
<a id="agroup__mcumgr__callback__api__fs__mgmt_html_ga80e18873c1f4d97ea601a33042bc21f9"></a>
<a id="agroup__mcumgr__callback__api__fs__mgmt_html_gga324223c20cbefe3400272e2789082c79a0475953c86b97afa8e4ed30da3f736d3"></a>
<a id="agroup__mcumgr__callback__api__fs__mgmt_html_gga324223c20cbefe3400272e2789082c79a9accc416aa349fd533e51d27fc46b7ee"></a>
<a id="agroup__mcumgr__callback__api__fs__mgmt_html_gga324223c20cbefe3400272e2789082c79a9d0806e3d6f0276930af97370ae23b53"></a>
<a id="agroup__mcumgr__callback__api__fs__mgmt_html_gga80e18873c1f4d97ea601a33042bc21f9a186ef60e6f795584edf7101b74499cb2"></a>
<a id="agroup__mcumgr__callback__api__fs__mgmt_html_gga80e18873c1f4d97ea601a33042bc21f9a5e418a17abdee97e017b0a18ca8dd19a"></a>
<a id="agroup__mcumgr__callback__api__fs__mgmt_html_gga80e18873c1f4d97ea601a33042bc21f9a93323901acc3c74dd6ed4752847e195c"></a>
<a id="agroup__mcumgr__callback__api__fs__mgmt_html_gga80e18873c1f4d97ea601a33042bc21f9ae500b34f64a8cefed3e9b420127564d2"></a>
<a id="agroup__mcumgr__callback__api_html_gga40ecf8933112abe76d7fedb3dcc7cdbea5504e38868b808ea6e46965bf3e6da48"></a>
<a id="astructfs__mgmt__file__access_html"></a>
<a id="astructfs__mgmt__file__access_html_a0155b69d23f3c5044e317eb236ff173c"></a>
<a id="astructfs__mgmt__file__access_html_a3aeeaf6d4243c1aaa7d6129a2ef4a064"></a>

```c
/*
 * Copyright (c) 2022 Laird Connectivity
 * Copyright (c) 2022 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_FS_MGMT_FS_MGMT_CALLBACKS_H_
#define ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_FS_MGMT_FS_MGMT_CALLBACKS_H_

#ifdef __cplusplus
extern "C" {
#endif


enum fs_mgmt_group_events {
        MGMT_EVT_OP_FS_MGMT_FILE_ACCESS         = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_FS, 0),

        MGMT_EVT_OP_FS_MGMT_FILE_ACCESS_DONE    = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_FS, 1),

        MGMT_EVT_OP_FS_MGMT_ALL                 = MGMT_DEF_EVT_OP_ALL(MGMT_EVT_GRP_FS),
};

enum fs_mgmt_file_access_types {
        FS_MGMT_FILE_ACCESS_READ,

        FS_MGMT_FILE_ACCESS_WRITE,

        FS_MGMT_FILE_ACCESS_STATUS,

        FS_MGMT_FILE_ACCESS_HASH_CHECKSUM,
};

struct fs_mgmt_file_access {
        enum fs_mgmt_file_access_types access;

        char *filename;
};


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_FS_MGMT_FS_MGMT_CALLBACKS_H_ */
```

## 275.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Laird Connectivity。

版权（Copyright）：© 2022 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 84 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_FS_MGMT_FS_MGMT_CALLBACKS_H_`。

## 275.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/fs__mgmt__callbacks_8h.html)
- [fs_mgmt_group_events](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html#ga324223c20cbefe3400272e2789082c79)
- [MGMT_EVT_OP_FS_MGMT_FILE_ACCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html#gga324223c20cbefe3400272e2789082c79a0475953c86b97afa8e4ed30da3f736d3)
- [MGMT_EVT_GRP_FS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga40ecf8933112abe76d7fedb3dcc7cdbea5504e38868b808ea6e46965bf3e6da48)
- [MGMT_EVT_OP_FS_MGMT_FILE_ACCESS_DONE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html#gga324223c20cbefe3400272e2789082c79a9accc416aa349fd533e51d27fc46b7ee)
- [MGMT_EVT_OP_FS_MGMT_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html#gga324223c20cbefe3400272e2789082c79a9d0806e3d6f0276930af97370ae23b53)
- [fs_mgmt_file_access_types](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html#ga80e18873c1f4d97ea601a33042bc21f9)
- [FS_MGMT_FILE_ACCESS_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html#gga80e18873c1f4d97ea601a33042bc21f9a5e418a17abdee97e017b0a18ca8dd19a)
- [FS_MGMT_FILE_ACCESS_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html#gga80e18873c1f4d97ea601a33042bc21f9a186ef60e6f795584edf7101b74499cb2)
- [FS_MGMT_FILE_ACCESS_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html#gga80e18873c1f4d97ea601a33042bc21f9ae500b34f64a8cefed3e9b420127564d2)
- [FS_MGMT_FILE_ACCESS_HASH_CHECKSUM](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html#gga80e18873c1f4d97ea601a33042bc21f9a93323901acc3c74dd6ed4752847e195c)
- [fs_mgmt_file_access](../system_service_model_reference/P039_fs_mgmt_file_access_结构体.md)
- [access](../system_service_model_reference/P039_fs_mgmt_file_access_结构体.md#a3aeeaf6d4243c1aaa7d6129a2ef4a064)
- [filename](../system_service_model_reference/P039_fs_mgmt_file_access_结构体.md#a0155b69d23f3c5044e317eb236ff173c)
- [fs_mgmt_file_access::filename](../system_service_model_reference/P039_fs_mgmt_file_access_结构体.md#a0155b69d23f3c5044e317eb236ff173c)
- [fs_mgmt_file_access::access](../system_service_model_reference/P039_fs_mgmt_file_access_结构体.md#a3aeeaf6d4243c1aaa7d6129a2ef4a064)

---

[上一章](P274_fs_mgmt.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P276_fs_mgmt_hash_checksum.h_源码浏览.md)
