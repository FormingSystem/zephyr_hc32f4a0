---
id: learning.zephyr-docs.api-file-system-device-reference.page-54
title: zephyr__mgmt__updatehub.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/updatehub_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第54章\_zephyr\_\_mgmt\_\_updatehub.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/updatehub_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/syscalls/updatehub.h>
```

查看此文件的源码。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 54.1\_枚举（Enumerations）

<a id="r_ga6e6eb49b1e4b558cd8be0da8b45a07b8"></a>

```c
enum updatehub_response { UPDATEHUB_NETWORKING_ERROR = 0 , UPDATEHUB_INCOMPATIBLE_HARDWARE , UPDATEHUB_UNCONFIRMED_IMAGE , UPDATEHUB_METADATA_ERROR , UPDATEHUB_DOWNLOAD_ERROR , UPDATEHUB_INSTALL_ERROR , UPDATEHUB_FLASH_INIT_ERROR , UPDATEHUB_OK , UPDATEHUB_HAS_UPDATE , UPDATEHUB_NO_UPDATE }
```

相关声明：[updatehub_response](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#ga6e6eb49b1e4b558cd8be0da8b45a07b8)、[UPDATEHUB_NETWORKING_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gga6e6eb49b1e4b558cd8be0da8b45a07b8aa0d2256936bee57106ccffe48c3d080a)、[UPDATEHUB_INCOMPATIBLE_HARDWARE](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gga6e6eb49b1e4b558cd8be0da8b45a07b8a75c0d76cdc28948d09a6512c3e316e76)、[UPDATEHUB_UNCONFIRMED_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gga6e6eb49b1e4b558cd8be0da8b45a07b8a5f5ae5102a0d8e318652067b2a097037)、[UPDATEHUB_METADATA_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gga6e6eb49b1e4b558cd8be0da8b45a07b8a5c7ed853ebe09b62b8c6348a695a6171)、[UPDATEHUB_DOWNLOAD_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gga6e6eb49b1e4b558cd8be0da8b45a07b8ae610dad426920bb70a42eae7bdb6b00f)、[UPDATEHUB_INSTALL_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gga6e6eb49b1e4b558cd8be0da8b45a07b8a5ec33576cdc17687e0e26aaf45f4382f)、[UPDATEHUB_FLASH_INIT_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gga6e6eb49b1e4b558cd8be0da8b45a07b8afeea264fa5140271de9ff5e6196c80a2)、[UPDATEHUB_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gga6e6eb49b1e4b558cd8be0da8b45a07b8a8ec40cbba06d67803fa611bf30984f43)、[UPDATEHUB_HAS_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gga6e6eb49b1e4b558cd8be0da8b45a07b8a458c9aab40f11bb32e492e9dec1f362c)、[UPDATEHUB_NO_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gga6e6eb49b1e4b558cd8be0da8b45a07b8a6bfb08c9056ed87c58025419280af730)。

来自 UpdateHub 的响应消息（response messages）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 54.2\_函数（Functions）

<a id="r_ga2a1665a1fe1b191bbc7d80c4bbaa4299"></a>

```c
void updatehub_autohandler (void)
```

相关声明：[updatehub_autohandler](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#ga2a1665a1fe1b191bbc7d80c4bbaa4299)。

自动执行 UpdateHub 探测（probe）和更新（update）。

<a id="r_ga89d1715033200c89a7587dd229944a23"></a>

```c
enum updatehub_response updatehub_probe (void)
```

相关声明：[updatehub_response](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#ga6e6eb49b1e4b558cd8be0da8b45a07b8)、[updatehub_probe](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#ga89d1715033200c89a7587dd229944a23)。

UpdateHub 探测检查是否存在需要执行的更新。

<a id="r_gabb00cf9b63ce13554c26286c0c37fa8a"></a>

```c
enum updatehub_response updatehub_update (void)
```

相关声明：[updatehub_response](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#ga6e6eb49b1e4b558cd8be0da8b45a07b8)、[updatehub_update](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gabb00cf9b63ce13554c26286c0c37fa8a)。

应用更新包（update package）。

<a id="r_gad1a3f6b1d91a7c9969a3411e0fd74f72"></a>

```c
int updatehub_confirm (void)
```

相关声明：[updatehub_confirm](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gad1a3f6b1d91a7c9969a3411e0fd74f72)。

确认映像按预期运行。

<a id="r_gac433e995a18418771cac9fe4559ce84b"></a>

```c
int updatehub_reboot (void)
```

相关声明：[updatehub_reboot](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gac433e995a18418771cac9fe4559ce84b)。

请求系统重新启动（reboot）。

<a id="r_gaa3606855ac680341e7b568421562e165"></a>

```c
int updatehub_report_error (void)
```

相关声明：[updatehub_report_error](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gaa3606855ac680341e7b568421562e165)。

向 UpdateHub 服务器报告更新失败。


## 54.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P887_updatehub.h_源码浏览.md)
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

[上一章](P053_zephyr__dt-bindings__sensor__tmp114.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P055_zephyr__drivers__usb__usb_buf.h_文件参考.md)
