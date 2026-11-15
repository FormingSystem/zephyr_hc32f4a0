---
id: learning.zephyr-docs.api-source-reference.page-124
title: dfd.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dfd_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第124章\_dfd.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dfd_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dfd_8h.html)。

## 124.1\_原始可见代码（Source Code）

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
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00027"></a>
<a id="foldopen00029"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="foldopen00079"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="foldopen00106"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="agroup__bt__mesh__dfd_html_ga1cce8331a0876c056b25175df32188fb"></a>
<a id="agroup__bt__mesh__dfd_html_gab6562d62668ebcdb146be35b909c30c2"></a>
<a id="agroup__bt__mesh__dfd_html_gaedd84b3b4bdde360c860d3cb04b301d5"></a>
<a id="agroup__bt__mesh__dfd_html_gga1cce8331a0876c056b25175df32188fba1e4f2505c3551bb7b36c22478c900a65"></a>
<a id="agroup__bt__mesh__dfd_html_gga1cce8331a0876c056b25175df32188fba7d4e5bdc57606446e759c7c563afa06e"></a>
<a id="agroup__bt__mesh__dfd_html_gga1cce8331a0876c056b25175df32188fbaa3c554767ecab3e601aef982bbb17d14"></a>
<a id="agroup__bt__mesh__dfd_html_gga1cce8331a0876c056b25175df32188fbaffe3e8378ced39bcf39dd532bebb9ec0"></a>
<a id="agroup__bt__mesh__dfd_html_ggab6562d62668ebcdb146be35b909c30c2a3b395af5b5ba7d5eb6f48230a18cd497"></a>
<a id="agroup__bt__mesh__dfd_html_ggab6562d62668ebcdb146be35b909c30c2a45896fbd956bd968e02b93baeafbd32c"></a>
<a id="agroup__bt__mesh__dfd_html_ggab6562d62668ebcdb146be35b909c30c2a6f3bf27d5d56a7b12fb4410bc2ce02ab"></a>
<a id="agroup__bt__mesh__dfd_html_ggab6562d62668ebcdb146be35b909c30c2a7fcb7a64a38ab8f1fa183346b2622886"></a>
<a id="agroup__bt__mesh__dfd_html_ggab6562d62668ebcdb146be35b909c30c2a83ac53111b35f568e35451542b1ab817"></a>
<a id="agroup__bt__mesh__dfd_html_ggab6562d62668ebcdb146be35b909c30c2ab0427fec0c21b1de0417be100c395f46"></a>
<a id="agroup__bt__mesh__dfd_html_ggab6562d62668ebcdb146be35b909c30c2ae449e405221a66ced3dfde401a398e93"></a>
<a id="agroup__bt__mesh__dfd_html_ggab6562d62668ebcdb146be35b909c30c2aef8954a9eaa299a178661834b0cdcadf"></a>
<a id="agroup__bt__mesh__dfd_html_ggaedd84b3b4bdde360c860d3cb04b301d5a0150d6c73adf0cb02dd466adbbd6879b"></a>
<a id="agroup__bt__mesh__dfd_html_ggaedd84b3b4bdde360c860d3cb04b301d5a05d5814acf74f3242403b56387da8523"></a>
<a id="agroup__bt__mesh__dfd_html_ggaedd84b3b4bdde360c860d3cb04b301d5a135b4f6fbb028f17eff69f7f6bbbef3e"></a>
<a id="agroup__bt__mesh__dfd_html_ggaedd84b3b4bdde360c860d3cb04b301d5a560250c948218d82f30767deb730bdf7"></a>
<a id="agroup__bt__mesh__dfd_html_ggaedd84b3b4bdde360c860d3cb04b301d5a566680567a9b839760eb894014a9c99e"></a>
<a id="agroup__bt__mesh__dfd_html_ggaedd84b3b4bdde360c860d3cb04b301d5a65eec1f5cc0601824736e182ea156ced"></a>
<a id="agroup__bt__mesh__dfd_html_ggaedd84b3b4bdde360c860d3cb04b301d5a681abfc930c58bfdc1fd7faecd5be60f"></a>
<a id="agroup__bt__mesh__dfd_html_ggaedd84b3b4bdde360c860d3cb04b301d5a7c26905cacc0746e9f0fd11c807dd9da"></a>
<a id="agroup__bt__mesh__dfd_html_ggaedd84b3b4bdde360c860d3cb04b301d5aac0df490cd27124e758cb5106de5af5c"></a>
<a id="agroup__bt__mesh__dfd_html_ggaedd84b3b4bdde360c860d3cb04b301d5aaec8424606d66809dbdf00dfe085a280"></a>
<a id="agroup__bt__mesh__dfd_html_ggaedd84b3b4bdde360c860d3cb04b301d5ace8c218c64a45d321bfee5d3c56c6a65"></a>
<a id="agroup__bt__mesh__dfd_html_ggaedd84b3b4bdde360c860d3cb04b301d5ad4f4b771ab3c826df309581a414c9256"></a>
<a id="agroup__bt__mesh__dfd_html_ggaedd84b3b4bdde360c860d3cb04b301d5adfcf93ecff8e6311e59edc738824524f"></a>
<a id="agroup__bt__mesh__dfd_html_ggaedd84b3b4bdde360c860d3cb04b301d5aff40a9a0293b44032fae6e609226437a"></a>
<a id="amesh_8h_html"></a>

```c
/*
 * Copyright (c) 2020 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_DFD_H__
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_DFD_H__

#include <zephyr/bluetooth/mesh.h>

#ifdef __cplusplus
extern "C" {
#endif


enum bt_mesh_dfd_status {
        BT_MESH_DFD_SUCCESS,

        BT_MESH_DFD_ERR_INSUFFICIENT_RESOURCES,

        BT_MESH_DFD_ERR_WRONG_PHASE,

        BT_MESH_DFD_ERR_INTERNAL,

        BT_MESH_DFD_ERR_FW_NOT_FOUND,

        BT_MESH_DFD_ERR_INVALID_APPKEY_INDEX,

        BT_MESH_DFD_ERR_RECEIVERS_LIST_EMPTY,

        BT_MESH_DFD_ERR_BUSY_WITH_DISTRIBUTION,

        BT_MESH_DFD_ERR_BUSY_WITH_UPLOAD,

        BT_MESH_DFD_ERR_URI_NOT_SUPPORTED,

        BT_MESH_DFD_ERR_URI_MALFORMED,

        BT_MESH_DFD_ERR_URI_UNREACHABLE,

        BT_MESH_DFD_ERR_NEW_FW_NOT_AVAILABLE,

        BT_MESH_DFD_ERR_SUSPEND_FAILED,
};

enum bt_mesh_dfd_phase {
        BT_MESH_DFD_PHASE_IDLE,

        BT_MESH_DFD_PHASE_TRANSFER_ACTIVE,

        BT_MESH_DFD_PHASE_TRANSFER_SUCCESS,

        BT_MESH_DFD_PHASE_APPLYING_UPDATE,

        BT_MESH_DFD_PHASE_COMPLETED,

        BT_MESH_DFD_PHASE_FAILED,

        BT_MESH_DFD_PHASE_CANCELING_UPDATE,

        BT_MESH_DFD_PHASE_TRANSFER_SUSPENDED,
};

enum bt_mesh_dfd_upload_phase {
        BT_MESH_DFD_UPLOAD_PHASE_IDLE,

        BT_MESH_DFD_UPLOAD_PHASE_TRANSFER_ACTIVE,

        BT_MESH_DFD_UPLOAD_PHASE_TRANSFER_ERROR,

        BT_MESH_DFD_UPLOAD_PHASE_TRANSFER_SUCCESS,
};


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_DFD_H__ */
```

## 124.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 129 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_DFD_H__`。

## 124.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dfd_8h.html)
- [zephyr/bluetooth/mesh.h](https://docs.zephyrproject.org/latest/doxygen/html/mesh_8h.html)
- [bt_mesh_dfd_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#gaedd84b3b4bdde360c860d3cb04b301d5)
- [BT_MESH_DFD_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggaedd84b3b4bdde360c860d3cb04b301d5a681abfc930c58bfdc1fd7faecd5be60f)
- [BT_MESH_DFD_ERR_INSUFFICIENT_RESOURCES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggaedd84b3b4bdde360c860d3cb04b301d5a7c26905cacc0746e9f0fd11c807dd9da)
- [BT_MESH_DFD_ERR_WRONG_PHASE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggaedd84b3b4bdde360c860d3cb04b301d5adfcf93ecff8e6311e59edc738824524f)
- [BT_MESH_DFD_ERR_INTERNAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggaedd84b3b4bdde360c860d3cb04b301d5a65eec1f5cc0601824736e182ea156ced)
- [BT_MESH_DFD_ERR_FW_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggaedd84b3b4bdde360c860d3cb04b301d5a566680567a9b839760eb894014a9c99e)
- [BT_MESH_DFD_ERR_INVALID_APPKEY_INDEX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggaedd84b3b4bdde360c860d3cb04b301d5ace8c218c64a45d321bfee5d3c56c6a65)
- [BT_MESH_DFD_ERR_RECEIVERS_LIST_EMPTY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggaedd84b3b4bdde360c860d3cb04b301d5a0150d6c73adf0cb02dd466adbbd6879b)
- [BT_MESH_DFD_ERR_BUSY_WITH_DISTRIBUTION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggaedd84b3b4bdde360c860d3cb04b301d5aff40a9a0293b44032fae6e609226437a)
- [BT_MESH_DFD_ERR_BUSY_WITH_UPLOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggaedd84b3b4bdde360c860d3cb04b301d5aaec8424606d66809dbdf00dfe085a280)
- [BT_MESH_DFD_ERR_URI_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggaedd84b3b4bdde360c860d3cb04b301d5aac0df490cd27124e758cb5106de5af5c)
- [BT_MESH_DFD_ERR_URI_MALFORMED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggaedd84b3b4bdde360c860d3cb04b301d5a05d5814acf74f3242403b56387da8523)
- [BT_MESH_DFD_ERR_URI_UNREACHABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggaedd84b3b4bdde360c860d3cb04b301d5ad4f4b771ab3c826df309581a414c9256)
- [BT_MESH_DFD_ERR_NEW_FW_NOT_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggaedd84b3b4bdde360c860d3cb04b301d5a560250c948218d82f30767deb730bdf7)
- [BT_MESH_DFD_ERR_SUSPEND_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggaedd84b3b4bdde360c860d3cb04b301d5a135b4f6fbb028f17eff69f7f6bbbef3e)
- [bt_mesh_dfd_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#gab6562d62668ebcdb146be35b909c30c2)
- [BT_MESH_DFD_PHASE_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggab6562d62668ebcdb146be35b909c30c2ae449e405221a66ced3dfde401a398e93)
- [BT_MESH_DFD_PHASE_TRANSFER_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggab6562d62668ebcdb146be35b909c30c2a3b395af5b5ba7d5eb6f48230a18cd497)
- [BT_MESH_DFD_PHASE_TRANSFER_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggab6562d62668ebcdb146be35b909c30c2a45896fbd956bd968e02b93baeafbd32c)
- [BT_MESH_DFD_PHASE_APPLYING_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggab6562d62668ebcdb146be35b909c30c2aef8954a9eaa299a178661834b0cdcadf)
- [BT_MESH_DFD_PHASE_COMPLETED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggab6562d62668ebcdb146be35b909c30c2a83ac53111b35f568e35451542b1ab817)
- [BT_MESH_DFD_PHASE_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggab6562d62668ebcdb146be35b909c30c2a6f3bf27d5d56a7b12fb4410bc2ce02ab)
- [BT_MESH_DFD_PHASE_CANCELING_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggab6562d62668ebcdb146be35b909c30c2a7fcb7a64a38ab8f1fa183346b2622886)
- [BT_MESH_DFD_PHASE_TRANSFER_SUSPENDED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggab6562d62668ebcdb146be35b909c30c2ab0427fec0c21b1de0417be100c395f46)
- [bt_mesh_dfd_upload_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ga1cce8331a0876c056b25175df32188fb)
- [BT_MESH_DFD_UPLOAD_PHASE_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#gga1cce8331a0876c056b25175df32188fba7d4e5bdc57606446e759c7c563afa06e)
- [BT_MESH_DFD_UPLOAD_PHASE_TRANSFER_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#gga1cce8331a0876c056b25175df32188fba1e4f2505c3551bb7b36c22478c900a65)
- [BT_MESH_DFD_UPLOAD_PHASE_TRANSFER_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#gga1cce8331a0876c056b25175df32188fbaa3c554767ecab3e601aef982bbb17d14)
- [BT_MESH_DFD_UPLOAD_PHASE_TRANSFER_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#gga1cce8331a0876c056b25175df32188fbaffe3e8378ced39bcf39dd532bebb9ec0)
- [mesh.h](https://docs.zephyrproject.org/latest/doxygen/html/mesh_8h.html)

---

[上一章](P123_device_runtime.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P125_dfd_srv.h_源码浏览.md)
