---
id: learning.zephyr-docs.api-file-management-reference.page-13
title: zephyr__dt-bindings__sent__sent.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sent_2sent_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_zephyr\_\_dt-bindings\_\_sent\_\_sent.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sent_2sent_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 13.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 快速消息 CRC 配置标志（Fast Message CRC Configuration Flags）

<a id="r_ga9a90bf30c6bfb4a945ec74c30ea45c1c"></a>

```c
#define FAST_CRC_DISABLE 0
```

相关声明：[FAST_CRC_DISABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#ga9a90bf30c6bfb4a945ec74c30ea45c1c)。

禁用快速消息（fast message）的循环冗余校验（CRC）检查。

<a id="r_ga4eecd87726aae09803ffcc9b573e42d7"></a>

```c
#define FAST_CRC_LEGACY_IMPLEMENTATION 1
```

相关声明：[FAST_CRC_LEGACY_IMPLEMENTATION](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#ga4eecd87726aae09803ffcc9b573e42d7)。

为快速消息使用传统 CRC 算法（legacy CRC algorithm）。

<a id="r_ga62ecd1c5a6f449c6301373bbec0c9672"></a>

```c
#define FAST_CRC_RECOMMENDED_IMPLEMENTATION 2
```

相关声明：[FAST_CRC_RECOMMENDED_IMPLEMENTATION](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#ga62ecd1c5a6f449c6301373bbec0c9672)。

为快速消息使用推荐的 CRC 算法。

<a id="r_ga335f899503c1992d586d771798ded503"></a>

```c
#define FAST_CRC_STATUS_INCLUDE 4
```

相关声明：[FAST_CRC_STATUS_INCLUDE](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#ga335f899503c1992d586d771798ded503)。

在快速消息中包含 CRC 状态。

<a id="define-members-1"></a>

### 短串行消息 CRC 配置标志（Short Serial Message CRC Configuration Flags）

<a id="r_ga8d7724675d1e0b0a5dc5df5e857f147f"></a>

```c
#define SHORT_CRC_LEGACY_IMPLEMENTATION 0
```

相关声明：[SHORT_CRC_LEGACY_IMPLEMENTATION](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#ga8d7724675d1e0b0a5dc5df5e857f147f)。

短串行消息（short serial message）的传统 CRC 算法。

<a id="r_gaf5a1b613a202a6f4df67f9dadbfea3f6"></a>

```c
#define SHORT_CRC_RECOMMENDED_IMPLEMENTATION 1
```

相关声明：[SHORT_CRC_RECOMMENDED_IMPLEMENTATION](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#gaf5a1b613a202a6f4df67f9dadbfea3f6)。

短串行消息的推荐 CRC 算法。


## 13.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P214_sent.h_源码浏览.md)
- [FAST_CRC_DISABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#ga9a90bf30c6bfb4a945ec74c30ea45c1c)
- [FAST_CRC_LEGACY_IMPLEMENTATION](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#ga4eecd87726aae09803ffcc9b573e42d7)
- [FAST_CRC_RECOMMENDED_IMPLEMENTATION](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#ga62ecd1c5a6f449c6301373bbec0c9672)
- [FAST_CRC_STATUS_INCLUDE](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#ga335f899503c1992d586d771798ded503)
- [SHORT_CRC_LEGACY_IMPLEMENTATION](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#ga8d7724675d1e0b0a5dc5df5e857f147f)
- [SHORT_CRC_RECOMMENDED_IMPLEMENTATION](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#gaf5a1b613a202a6f4df67f9dadbfea3f6)

---

[上一章](P012_zephyr__drivers__haptics__drv2605.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P014_zephyr__dfu__flash_img.h_文件参考.md)
