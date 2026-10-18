---
id: learning.zephyr-docs.api-file-configuration-reference.page-79
title: zephyr__xen__version.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/version_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第79章\_zephyr\_\_xen\_\_version.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/version_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Xen版本查询（Version Queries）。

<a id="details"></a>

```c
#include <zephyr/xen/generic.h>
#include <xen/public/version.h>
#include <xen/public/xen.h>
```

查看此文件的源码。

Xen版本查询（Version Queries）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 79.1\_函数（Functions）

<a id="r_ga1a790f668be1f721823419393a62201b"></a>

```c
int xen_version (void)
```

相关声明：[xen_version](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__version__queries.html#ga1a790f668be1f721823419393a62201b)。

获取按主版本号和次版本号（Major and Minor Numbers）编码的 Xen 版本（Version）。

<a id="r_ga9ed44decd02728419b557c1db7d86635"></a>

```c
int xen_version_extraversion (char *extra, int len)
```

相关声明：[xen_version_extraversion](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__version__queries.html#ga9ed44decd02728419b557c1db7d86635)。

获取 Xen 附加版本字符串（Extra Version String）。


## 79.2\_原页交叉引用（Cross References）

- [zephyr/xen/generic.h](../api_source_supplement_reference/P078_generic.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P906_version.h_源码浏览.md)
- [xen_version](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__version__queries.html#ga1a790f668be1f721823419393a62201b)
- [xen_version_extraversion](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__version__queries.html#ga9ed44decd02728419b557c1db7d86635)

<a id="header-details"></a>

---

[上一章](P078_zephyr__usb__usbd_msg.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P080_zephyr__drivers__sensor__wsen_pads_2511020213301.h_文件参考.md)
