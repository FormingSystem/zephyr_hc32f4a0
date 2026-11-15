---
id: learning.zephyr-docs.api-file-interface-reference.page-57
title: ____w__zephyr__zephyr__subsys__secure_storage__include__internal__zephyr__secure_storage__its__store__settings.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2store_2settings_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第57章\_\_\_\_\_w\_\_zephyr\_\_zephyr\_\_subsys\_\_secure\_storage\_\_include\_\_internal\_\_zephyr\_\_secure\_storage\_\_its\_\_store\_\_settings.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2store_2settings_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

设置系统（Settings）的内部可信存储（ITS）存储模块API。

<a id="details"></a>

```c
#include <zephyr/secure_storage/its/common.h>
```

查看此文件的源码。

基于设置（settings）的 ITS 存储模块 API。本头文件声明的函数允许自定义 ITS 存储模块的 settings 实现。除 settings ITS 存储模块外，其他代码不应直接调用这些函数。提供其中一个或多个函数的自定义实现（`CONFIG_SECURE_STORAGE_ITS_STORE_SETTINGS_.*_CUSTOM`）时，可以且必须包含此头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 57.1\_宏定义（Macros）

<a id="r_aeb04a9d9f92c3dfae97bf2049729517b"></a>

```c
#define SECURE_STORAGE_ITS_STORE_SETTINGS_NAME_BUF_SIZE (CONFIG_SECURE_STORAGE_ITS_STORE_SETTINGS_NAME_MAX_LEN + 1)
```

相关声明：[SECURE_STORAGE_ITS_STORE_SETTINGS_NAME_BUF_SIZE](#aeb04a9d9f92c3dfae97bf2049729517b)。

ITS 存储设置项名称的缓冲区大小。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 57.2\_函数（Functions）

<a id="r_ab034dcdbc69cad67f1f6eddb561fb099"></a>

```c
void secure_storage_its_store_settings_get_name (secure_storage_its_uid_t uid, char name[static(CONFIG_SECURE_STORAGE_ITS_STORE_SETTINGS_NAME_MAX_LEN+1)])
```

相关声明：[secure_storage_its_store_settings_get_name](#ab034dcdbc69cad67f1f6eddb561fb099)、[secure_storage_its_uid_t](../platform_security_model_reference/P053_secure_storage_its_uid_t_结构体.md)。

返回用于 ITS 条目的设置项名称（setting name）。

## 57.3\_详细说明（Detailed Documentation）

<a id="aeb04a9d9f92c3dfae97bf2049729517b"></a>

### `SECURE_STORAGE_ITS_STORE_SETTINGS_NAME_BUF_SIZE`

```c
#define SECURE_STORAGE_ITS_STORE_SETTINGS_NAME_BUF_SIZE (CONFIG_SECURE_STORAGE_ITS_STORE_SETTINGS_NAME_MAX_LEN + 1)
```

ITS 存储设置项名称的缓冲区大小。

<a id="ab034dcdbc69cad67f1f6eddb561fb099"></a>

### `secure_storage_its_store_settings_get_name()`

```c
void secure_storage_its_store_settings_get_name ( secure_storage_its_uid_t uid, char name[static(CONFIG_SECURE_STORAGE_ITS_STORE_SETTINGS_NAME_MAX_LEN+1)] )
```

返回用于 ITS 条目的设置项名称（setting name）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uid` | 使用该设置项名称的 ITS 条目的唯一标识符（UID）。 |
| `[out] name` | 设置项名称。 |


## 57.4\_原页交叉引用（Cross References）

- [zephyr/secure_storage/its/common.h](../api_source_reference/P843_common.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P844_settings.h_源码浏览.md)
- [secure_storage_its_uid_t](../platform_security_model_reference/P053_secure_storage_its_uid_t_结构体.md)
- [CONFIG_SECURE_STORAGE_ITS_STORE_SETTINGS_.*_CUSTOM](https://docs.zephyrproject.org/latest/kconfig.html#!CONFIG_SECURE_STORAGE_ITS_STORE_SETTINGS_.%2A_CUSTOM)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P056_____w__zephyr__zephyr__subsys__secure_storage__include__internal__zephyr__secure_storage__its__common.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P058_zephyr__bluetooth__audio__tmap.h_文件参考.md)
