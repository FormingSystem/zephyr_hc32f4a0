---
id: learning.zephyr-docs.api-file-runtime-reference.page-15
title: zephyr__authentication__fido2__fido2_up.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fido2__up_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_zephyr\_\_authentication\_\_fido2\_\_fido2\_up.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/fido2__up_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

FIDO2用户在场（User Presence）抽象API。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
```

查看此文件的源码。

FIDO2用户在场（User Presence）抽象API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 15.1\_函数（Functions）

<a id="func-members-0"></a>

<a id="r_gab782d78847a38dd7aeac52a806879dfb"></a>

```c
int fido2_up_wait (void)
```

相关声明：[fido2_up_wait](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gab782d78847a38dd7aeac52a806879dfb)。

FIDO2 用户在场（User Presence）。

<a id="r_gae7fb0da6d327ef0be220d32558ea6be2"></a>

```c
void fido2_up_reset (void)
```

相关声明：[fido2_up_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gae7fb0da6d327ef0be220d32558ea6be2)。

为新请求（Request）重置用户在场状态（User-Presence State）。

<a id="r_gaf6d50aa0022f56350a927149086d7838"></a>

```c
void fido2_up_cancel (void)
```

相关声明：[fido2_up_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaf6d50aa0022f56350a927149086d7838)。

取消尚未完成的用户在场等待（Pending User Presence Wait）。


## 15.2\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P263_fido2_up.h_源码浏览.md)
- [fido2_up_wait](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gab782d78847a38dd7aeac52a806879dfb)
- [fido2_up_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gae7fb0da6d327ef0be220d32558ea6be2)
- [fido2_up_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaf6d50aa0022f56350a927149086d7838)

<a id="header-details"></a>

---

[上一章](P014_zephyr__mgmt__hawkbit__event.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P016_zephyr__drivers__gpio__gpio_nrf.h_文件参考.md)
