---
id: learning.zephyr-docs.api-platform-topic-reference.page-123
title: ST87Mxx 常量（Constants）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__constants.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第123章\_ST87Mxx 常量（Constants）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__constants.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-define-members"></a>
<a id="define-members"></a>

## 123.1\_宏定义（Macros）

<a id="r_ga54b2d06b56d845ca68886b94719fe64b"></a>

```c
#define APP_MDM_CMD_TIMEOUT K_SECONDS(180)
```

相关声明：[APP_MDM_CMD_TIMEOUT](#ga54b2d06b56d845ca68886b94719fe64b)、[K_SECONDS](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gadc361472aea59267f6ea38f5e7c7ca2a)。

应用服务序列（Application Services Sequences）的默认超时（Default Timeout）。

## 123.2\_详细说明（Detailed Documentation）

<a id="ga54b2d06b56d845ca68886b94719fe64b"></a>

### `APP_MDM_CMD_TIMEOUT`

```c
#define APP_MDM_CMD_TIMEOUT K_SECONDS(180)
```

```c
#include <zephyr/drivers/modem/st87mxx_app_services.h>
```

应用服务序列（Application Services Sequences）的默认超时（Default Timeout）。


## 123.3\_原页交叉引用（Cross References）

- [K_SECONDS](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gadc361472aea59267f6ea38f5e7c7ca2a)
- [zephyr/drivers/modem/st87mxx_app_services.h](https://docs.zephyrproject.org/latest/doxygen/html/st87mxx__app__services_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P122_SENT 驱动后端 API.md) · [返回大纲](大纲.md) · [下一章](P124_USB Type-C 电源路径控制器驱动后端 API.md)
