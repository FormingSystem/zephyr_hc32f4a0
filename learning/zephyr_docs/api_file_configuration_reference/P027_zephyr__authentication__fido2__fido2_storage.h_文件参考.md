---
id: learning.zephyr-docs.api-file-configuration-reference.page-27
title: zephyr__authentication__fido2__fido2_storage.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fido2__storage_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_zephyr\_\_authentication\_\_fido2\_\_fido2\_storage.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/fido2__storage_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

FIDO2凭据存储（Credential Storage）的API。

<a id="details"></a>

```c
#include <zephyr/authentication/fido2/fido2_types.h>
#include <stddef.h>
```

查看此文件的源码。

FIDO2凭据存储（Credential Storage）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 27.1\_数据结构（Data Structures）

<a id="r_fido2_5Fstorage_5Fapi"></a>

```c
struct fido2_storage_api
```

相关声明：[fido2_storage_api](../platform_security_model_reference/P009_fido2_storage_api_结构体.md)。

存储后端（Storage Backend）API。

<a id="r_gad0f22c2a4c49fdd7b47ed0913115c5b2"></a>

```c
typedef int(* fido2_storage_iterate_cb_t) (const struct fido2_credential *cred, void *user_data)
```

相关声明：[fido2_storage_iterate_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gad0f22c2a4c49fdd7b47ed0913115c5b2)、[fido2_credential](../platform_security_model_reference/P007_fido2_credential_结构体.md)。

FIDO2 凭据存储（Credential Storage）。

<a id="r_ga27aa8972d17b4ee6454204d0ab527ed0"></a>

```c
const struct fido2_storage_api fido2_storage_backend
```

相关声明：[fido2_storage_api](../platform_security_model_reference/P009_fido2_storage_api_结构体.md)、[fido2_storage_backend](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga27aa8972d17b4ee6454204d0ab527ed0)。

FIDO2 存储后端实例（Storage Backend Instance）。


## 27.2\_原页交叉引用（Cross References）

- [zephyr/authentication/fido2/fido2_types.h](../api_source_reference/P262_fido2_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P260_fido2_storage.h_源码浏览.md)
- [fido2_storage_api](../platform_security_model_reference/P009_fido2_storage_api_结构体.md)
- [fido2_storage_iterate_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gad0f22c2a4c49fdd7b47ed0913115c5b2)
- [fido2_credential](../platform_security_model_reference/P007_fido2_credential_结构体.md)
- [fido2_storage_backend](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga27aa8972d17b4ee6454204d0ab527ed0)

<a id="header-details"></a>

---

[上一章](P026_zephyr__drivers__sensor__fcx_mldx5.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P028_zephyr__xen__flask.h_文件参考.md)
