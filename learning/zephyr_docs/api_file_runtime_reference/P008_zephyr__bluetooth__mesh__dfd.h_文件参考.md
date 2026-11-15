---
id: learning.zephyr-docs.api-file-runtime-reference.page-8
title: zephyr__bluetooth__mesh__dfd.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dfd_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_zephyr\_\_bluetooth\_\_mesh\_\_dfd.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dfd_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙Mesh固件分发模型（Firmware Distribution Models）API的头文件。

<a id="details"></a>

```c
#include <zephyr/bluetooth/mesh.h>
```

查看此文件的源码。

蓝牙Mesh固件分发模型（Firmware Distribution Models）API的头文件。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 8.1\_枚举（Enumerations）

<a id="r_gaedd84b3b4bdde360c860d3cb04b301d5"></a>

```c
enum bt_mesh_dfd_status { BT_MESH_DFD_SUCCESS , BT_MESH_DFD_ERR_INSUFFICIENT_RESOURCES , BT_MESH_DFD_ERR_WRONG_PHASE , BT_MESH_DFD_ERR_INTERNAL , BT_MESH_DFD_ERR_FW_NOT_FOUND , BT_MESH_DFD_ERR_INVALID_APPKEY_INDEX , BT_MESH_DFD_ERR_RECEIVERS_LIST_EMPTY , BT_MESH_DFD_ERR_BUSY_WITH_DISTRIBUTION , BT_MESH_DFD_ERR_BUSY_WITH_UPLOAD , BT_MESH_DFD_ERR_URI_NOT_SUPPORTED , BT_MESH_DFD_ERR_URI_MALFORMED , BT_MESH_DFD_ERR_URI_UNREACHABLE , BT_MESH_DFD_ERR_NEW_FW_NOT_AVAILABLE , BT_MESH_DFD_ERR_SUSPEND_FAILED }
```

相关声明：[bt_mesh_dfd_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#gaedd84b3b4bdde360c860d3cb04b301d5)、[BT_MESH_DFD_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggaedd84b3b4bdde360c860d3cb04b301d5a681abfc930c58bfdc1fd7faecd5be60f)、[BT_MESH_DFD_ERR_INSUFFICIENT_RESOURCES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggaedd84b3b4bdde360c860d3cb04b301d5a7c26905cacc0746e9f0fd11c807dd9da)、[BT_MESH_DFD_ERR_WRONG_PHASE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggaedd84b3b4bdde360c860d3cb04b301d5adfcf93ecff8e6311e59edc738824524f)、[BT_MESH_DFD_ERR_INTERNAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggaedd84b3b4bdde360c860d3cb04b301d5a65eec1f5cc0601824736e182ea156ced)、[BT_MESH_DFD_ERR_FW_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggaedd84b3b4bdde360c860d3cb04b301d5a566680567a9b839760eb894014a9c99e)、[BT_MESH_DFD_ERR_INVALID_APPKEY_INDEX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggaedd84b3b4bdde360c860d3cb04b301d5ace8c218c64a45d321bfee5d3c56c6a65)、[BT_MESH_DFD_ERR_RECEIVERS_LIST_EMPTY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggaedd84b3b4bdde360c860d3cb04b301d5a0150d6c73adf0cb02dd466adbbd6879b)、[BT_MESH_DFD_ERR_BUSY_WITH_DISTRIBUTION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggaedd84b3b4bdde360c860d3cb04b301d5aff40a9a0293b44032fae6e609226437a)、[BT_MESH_DFD_ERR_BUSY_WITH_UPLOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggaedd84b3b4bdde360c860d3cb04b301d5aaec8424606d66809dbdf00dfe085a280)、[BT_MESH_DFD_ERR_URI_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggaedd84b3b4bdde360c860d3cb04b301d5aac0df490cd27124e758cb5106de5af5c)、[BT_MESH_DFD_ERR_URI_MALFORMED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggaedd84b3b4bdde360c860d3cb04b301d5a05d5814acf74f3242403b56387da8523)、[BT_MESH_DFD_ERR_URI_UNREACHABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggaedd84b3b4bdde360c860d3cb04b301d5ad4f4b771ab3c826df309581a414c9256)、[BT_MESH_DFD_ERR_NEW_FW_NOT_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggaedd84b3b4bdde360c860d3cb04b301d5a560250c948218d82f30767deb730bdf7)、[BT_MESH_DFD_ERR_SUSPEND_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggaedd84b3b4bdde360c860d3cb04b301d5a135b4f6fbb028f17eff69f7f6bbbef3e)。

固件分发状态（Firmware Distribution Status）。

<a id="r_gab6562d62668ebcdb146be35b909c30c2"></a>

```c
enum bt_mesh_dfd_phase { BT_MESH_DFD_PHASE_IDLE , BT_MESH_DFD_PHASE_TRANSFER_ACTIVE , BT_MESH_DFD_PHASE_TRANSFER_SUCCESS , BT_MESH_DFD_PHASE_APPLYING_UPDATE , BT_MESH_DFD_PHASE_COMPLETED , BT_MESH_DFD_PHASE_FAILED , BT_MESH_DFD_PHASE_CANCELING_UPDATE , BT_MESH_DFD_PHASE_TRANSFER_SUSPENDED }
```

相关声明：[bt_mesh_dfd_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#gab6562d62668ebcdb146be35b909c30c2)、[BT_MESH_DFD_PHASE_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggab6562d62668ebcdb146be35b909c30c2ae449e405221a66ced3dfde401a398e93)、[BT_MESH_DFD_PHASE_TRANSFER_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggab6562d62668ebcdb146be35b909c30c2a3b395af5b5ba7d5eb6f48230a18cd497)、[BT_MESH_DFD_PHASE_TRANSFER_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggab6562d62668ebcdb146be35b909c30c2a45896fbd956bd968e02b93baeafbd32c)、[BT_MESH_DFD_PHASE_APPLYING_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggab6562d62668ebcdb146be35b909c30c2aef8954a9eaa299a178661834b0cdcadf)、[BT_MESH_DFD_PHASE_COMPLETED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggab6562d62668ebcdb146be35b909c30c2a83ac53111b35f568e35451542b1ab817)、[BT_MESH_DFD_PHASE_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggab6562d62668ebcdb146be35b909c30c2a6f3bf27d5d56a7b12fb4410bc2ce02ab)、[BT_MESH_DFD_PHASE_CANCELING_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggab6562d62668ebcdb146be35b909c30c2a7fcb7a64a38ab8f1fa183346b2622886)、[BT_MESH_DFD_PHASE_TRANSFER_SUSPENDED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ggab6562d62668ebcdb146be35b909c30c2ab0427fec0c21b1de0417be100c395f46)。

固件分发阶段（Firmware Distribution Phases）。

<a id="r_ga1cce8331a0876c056b25175df32188fb"></a>

```c
enum bt_mesh_dfd_upload_phase { BT_MESH_DFD_UPLOAD_PHASE_IDLE , BT_MESH_DFD_UPLOAD_PHASE_TRANSFER_ACTIVE , BT_MESH_DFD_UPLOAD_PHASE_TRANSFER_ERROR , BT_MESH_DFD_UPLOAD_PHASE_TRANSFER_SUCCESS }
```

相关声明：[bt_mesh_dfd_upload_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ga1cce8331a0876c056b25175df32188fb)、[BT_MESH_DFD_UPLOAD_PHASE_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#gga1cce8331a0876c056b25175df32188fba7d4e5bdc57606446e759c7c563afa06e)、[BT_MESH_DFD_UPLOAD_PHASE_TRANSFER_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#gga1cce8331a0876c056b25175df32188fba1e4f2505c3551bb7b36c22478c900a65)、[BT_MESH_DFD_UPLOAD_PHASE_TRANSFER_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#gga1cce8331a0876c056b25175df32188fbaa3c554767ecab3e601aef982bbb17d14)、[BT_MESH_DFD_UPLOAD_PHASE_TRANSFER_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#gga1cce8331a0876c056b25175df32188fbaffe3e8378ced39bcf39dd532bebb9ec0)。

固件上传阶段（Firmware Upload Phases）。


## 8.2\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh.h](../api_source_reference/P514_mesh.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P124_dfd.h_源码浏览.md)
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

<a id="header-details"></a>

---

[上一章](P007_zephyr__net__conn_mgr__connectivity_wifi_mgmt.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P009_zephyr__net__dhcpv6.h_文件参考.md)
