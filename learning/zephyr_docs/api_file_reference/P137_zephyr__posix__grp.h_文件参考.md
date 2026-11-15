---
id: learning.zephyr-docs.api-file-reference.page-137
title: zephyr__posix__grp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/grp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第137章\_zephyr\_\_posix\_\_grp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/grp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/posix/sys/stat.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 137.1\_数据结构（Data Structures）

<a id="r_group"></a>

```c
struct group
```

相关声明：[group](../posix_system_model_reference/P003_group_结构体.md)。

组结构（Group Structure）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 137.2\_函数（Functions）

<a id="r_acf054c85917adbbc3687004d51317685"></a>

```c
int getgrnam_r (const char *name, struct group *grp, char *buffer, size_t bufsize, struct group **result)
```

相关声明：[getgrnam_r](#acf054c85917adbbc3687004d51317685)、[group](../posix_system_model_reference/P003_group_结构体.md)、[group](../posix_system_model_reference/P003_group_结构体.md)。

<a id="r_a64e84dfb3f386daaa7530fc8177a6056"></a>

```c
int getgrgid_r (gid_t gid, struct group *grp, char *buffer, size_t bufsize, struct group **result)
```

相关声明：[getgrgid_r](#a64e84dfb3f386daaa7530fc8177a6056)、[gid_t](P312_zephyr__posix__posix_types.h_文件参考.md#a3a7834be1a79bb0c5a65d3546c2e3bd8)、[group](../posix_system_model_reference/P003_group_结构体.md)、[group](../posix_system_model_reference/P003_group_结构体.md)。

## 137.3\_详细说明（Detailed Documentation）

<a id="a64e84dfb3f386daaa7530fc8177a6056"></a>

### `getgrgid_r()`

```c
int getgrgid_r ( gid_t gid, struct group * grp, char * buffer, size_t bufsize, struct group ** result )
```

<a id="acf054c85917adbbc3687004d51317685"></a>

### `getgrnam_r()`

```c
int getgrnam_r ( const char * name, struct group * grp, char * buffer, size_t bufsize, struct group ** result )
```


## 137.4\_原页交叉引用（Cross References）

- [zephyr/posix/sys/stat.h](https://docs.zephyrproject.org/latest/doxygen/html/stat_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P304_grp.h_源码浏览.md)
- [group](../posix_system_model_reference/P003_group_结构体.md)
- [gid_t](P312_zephyr__posix__posix_types.h_文件参考.md#a3a7834be1a79bb0c5a65d3546c2e3bd8)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P136_zephyr__drivers__gpio__gpio_rts5912.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P138_zephyr__net__http__hpack.h_文件参考.md)
