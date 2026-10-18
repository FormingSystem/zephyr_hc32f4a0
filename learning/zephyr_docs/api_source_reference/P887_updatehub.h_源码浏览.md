---
id: learning.zephyr-docs.api-source-reference.page-887
title: updatehub.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/updatehub_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第887章\_updatehub.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/updatehub_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/updatehub_8h.html)。

## 887.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="foldopen00029"></a>
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
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="agroup__updatehub_html_ga2a1665a1fe1b191bbc7d80c4bbaa4299"></a>
<a id="agroup__updatehub_html_ga6e6eb49b1e4b558cd8be0da8b45a07b8"></a>
<a id="agroup__updatehub_html_ga89d1715033200c89a7587dd229944a23"></a>
<a id="agroup__updatehub_html_gaa3606855ac680341e7b568421562e165"></a>
<a id="agroup__updatehub_html_gabb00cf9b63ce13554c26286c0c37fa8a"></a>
<a id="agroup__updatehub_html_gac433e995a18418771cac9fe4559ce84b"></a>
<a id="agroup__updatehub_html_gad1a3f6b1d91a7c9969a3411e0fd74f72"></a>
<a id="agroup__updatehub_html_gga6e6eb49b1e4b558cd8be0da8b45a07b8a458c9aab40f11bb32e492e9dec1f362c"></a>
<a id="agroup__updatehub_html_gga6e6eb49b1e4b558cd8be0da8b45a07b8a5c7ed853ebe09b62b8c6348a695a6171"></a>
<a id="agroup__updatehub_html_gga6e6eb49b1e4b558cd8be0da8b45a07b8a5ec33576cdc17687e0e26aaf45f4382f"></a>
<a id="agroup__updatehub_html_gga6e6eb49b1e4b558cd8be0da8b45a07b8a5f5ae5102a0d8e318652067b2a097037"></a>
<a id="agroup__updatehub_html_gga6e6eb49b1e4b558cd8be0da8b45a07b8a6bfb08c9056ed87c58025419280af730"></a>
<a id="agroup__updatehub_html_gga6e6eb49b1e4b558cd8be0da8b45a07b8a75c0d76cdc28948d09a6512c3e316e76"></a>
<a id="agroup__updatehub_html_gga6e6eb49b1e4b558cd8be0da8b45a07b8a8ec40cbba06d67803fa611bf30984f43"></a>
<a id="agroup__updatehub_html_gga6e6eb49b1e4b558cd8be0da8b45a07b8aa0d2256936bee57106ccffe48c3d080a"></a>
<a id="agroup__updatehub_html_gga6e6eb49b1e4b558cd8be0da8b45a07b8ae610dad426920bb70a42eae7bdb6b00f"></a>
<a id="agroup__updatehub_html_gga6e6eb49b1e4b558cd8be0da8b45a07b8afeea264fa5140271de9ff5e6196c80a2"></a>

```c
/*
 * Copyright (c) 2018-2023 O.S.Systems
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MGMT_UPDATEHUB_H_
#define ZEPHYR_INCLUDE_MGMT_UPDATEHUB_H_

#ifdef __cplusplus
extern "C" {
#endif

enum updatehub_response {
        UPDATEHUB_NETWORKING_ERROR = 0,
        UPDATEHUB_INCOMPATIBLE_HARDWARE,
        UPDATEHUB_UNCONFIRMED_IMAGE,
        UPDATEHUB_METADATA_ERROR,
        UPDATEHUB_DOWNLOAD_ERROR,
        UPDATEHUB_INSTALL_ERROR,
        UPDATEHUB_FLASH_INIT_ERROR,
        UPDATEHUB_OK,
        UPDATEHUB_HAS_UPDATE,
        UPDATEHUB_NO_UPDATE,
};

__syscall void updatehub_autohandler(void);

__syscall enum updatehub_response updatehub_probe(void);

__syscall enum updatehub_response updatehub_update(void);

__syscall int updatehub_confirm(void);

__syscall int updatehub_reboot(void);

__syscall int updatehub_report_error(void);

#ifdef __cplusplus
}
#endif


#include <zephyr/syscalls/updatehub.h>
#endif /* ZEPHYR_INCLUDE_MGMT_UPDATEHUB_H_ */
```

## 887.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018-2023 O.S.Systems。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 111 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_UPDATEHUB_H_`。

## 887.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/updatehub_8h.html)
- [updatehub_response](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#ga6e6eb49b1e4b558cd8be0da8b45a07b8)
- [UPDATEHUB_NETWORKING_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gga6e6eb49b1e4b558cd8be0da8b45a07b8aa0d2256936bee57106ccffe48c3d080a)
- [UPDATEHUB_INCOMPATIBLE_HARDWARE](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gga6e6eb49b1e4b558cd8be0da8b45a07b8a75c0d76cdc28948d09a6512c3e316e76)
- [UPDATEHUB_UNCONFIRMED_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gga6e6eb49b1e4b558cd8be0da8b45a07b8a5f5ae5102a0d8e318652067b2a097037)
- [UPDATEHUB_METADATA_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gga6e6eb49b1e4b558cd8be0da8b45a07b8a5c7ed853ebe09b62b8c6348a695a6171)
- [UPDATEHUB_DOWNLOAD_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gga6e6eb49b1e4b558cd8be0da8b45a07b8ae610dad426920bb70a42eae7bdb6b00f)
- [UPDATEHUB_INSTALL_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gga6e6eb49b1e4b558cd8be0da8b45a07b8a5ec33576cdc17687e0e26aaf45f4382f)
- [UPDATEHUB_FLASH_INIT_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gga6e6eb49b1e4b558cd8be0da8b45a07b8afeea264fa5140271de9ff5e6196c80a2)
- [UPDATEHUB_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gga6e6eb49b1e4b558cd8be0da8b45a07b8a8ec40cbba06d67803fa611bf30984f43)
- [UPDATEHUB_HAS_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gga6e6eb49b1e4b558cd8be0da8b45a07b8a458c9aab40f11bb32e492e9dec1f362c)
- [UPDATEHUB_NO_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gga6e6eb49b1e4b558cd8be0da8b45a07b8a6bfb08c9056ed87c58025419280af730)
- [updatehub_autohandler](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#ga2a1665a1fe1b191bbc7d80c4bbaa4299)
- [updatehub_probe](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#ga89d1715033200c89a7587dd229944a23)
- [updatehub_update](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gabb00cf9b63ce13554c26286c0c37fa8a)
- [updatehub_confirm](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gad1a3f6b1d91a7c9969a3411e0fd74f72)
- [updatehub_reboot](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gac433e995a18418771cac9fe4559ce84b)
- [updatehub_report_error](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gaa3606855ac680341e7b568421562e165)

---

[上一章](P886_ump_stream_responder.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P888_usb_hub.h_源码浏览.md)
