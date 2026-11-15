---
id: learning.zephyr-docs.api-file-configuration-reference.page-28
title: zephyr__xen__flask.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/flask_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_zephyr\_\_xen\_\_flask.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/flask_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Xen XSM FLASK的操作。

<a id="details"></a>

```c
#include <xen/public/xsm/flask_op.h>
```

查看此文件的源码。

Xen XSM FLASK的操作。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 28.1\_函数（Functions）

<a id="r_gafedcdbff09ea3a91952aa011954bcae3"></a>

```c
int flask_context_to_sid (char *buf, uint32_t size, uint32_t *sid)
```

相关声明：[flask_context_to_sid](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__xsm__flask.html#gafedcdbff09ea3a91952aa011954bcae3)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将上下文字符串（Context String）转换为数值形式的安全标识（SID）。

<a id="r_gaf7c884e01c7a9bb55c248c53d9b848eb"></a>

```c
int flask_getenforce (void)
```

相关声明：[flask_getenforce](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__xsm__flask.html#gaf7c884e01c7a9bb55c248c53d9b848eb)。

获取当前 FLASK 强制模式（Enforcing Mode）。


## 28.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P265_flask.h_源码浏览.md)
- [flask_context_to_sid](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__xsm__flask.html#gafedcdbff09ea3a91952aa011954bcae3)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [flask_getenforce](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__xsm__flask.html#gaf7c884e01c7a9bb55c248c53d9b848eb)

<a id="header-details"></a>

---

[上一章](P027_zephyr__authentication__fido2__fido2_storage.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P029_zephyr__net__prometheus__formatter.h_文件参考.md)
