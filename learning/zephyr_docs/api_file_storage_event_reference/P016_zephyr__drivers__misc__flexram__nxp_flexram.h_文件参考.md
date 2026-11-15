---
id: learning.zephyr-docs.api-file-storage-event-reference.page-16
title: zephyr__drivers__misc__flexram__nxp_flexram.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nxp__flexram_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_zephyr\_\_drivers\_\_misc\_\_flexram\_\_nxp\_flexram.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/nxp__flexram_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/devicetree.h>
#include <soc.h>
```

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 16.1\_函数（Functions）

<a id="r_ac4ed80d0460f7765e9b9f2b58a0ec7cb"></a>

```c
int flexram_set_ocram_magic_addr (uint32_t ocram_addr)
```

相关声明：[flexram_set_ocram_magic_addr](#ac4ed80d0460f7765e9b9f2b58a0ec7cb)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

为 OCRAM 设置特殊地址（Magic Address）。

<a id="r_a374d43fc963ce2a7665f8c8bde58c7bf"></a>

```c
int flexram_set_itcm_magic_addr (uint32_t itcm_addr)
```

相关声明：[flexram_set_itcm_magic_addr](#a374d43fc963ce2a7665f8c8bde58c7bf)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

为 ITCM 设置特殊地址（Magic Address）。

<a id="r_a89a618d3a7cce4eedd2520ddfa5cfe43"></a>

```c
int flexram_set_dtcm_magic_addr (uint32_t dtcm_addr)
```

相关声明：[flexram_set_dtcm_magic_addr](#a89a618d3a7cce4eedd2520ddfa5cfe43)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

为 DTCM 设置特殊地址（Magic Address）。

## 16.2\_详细说明（Detailed Documentation）

<a id="a89a618d3a7cce4eedd2520ddfa5cfe43"></a>

### `flexram_set_dtcm_magic_addr()`

```c
int flexram_set_dtcm_magic_addr ( uint32_t dtcm_addr)
```

为 DTCM 设置特殊地址（Magic Address）。

访问特殊地址（Magic Address）时，可由 FlexRAM 向内核触发中断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dtcm_addr` | DTCM 内要设置特殊功能（Magic Function）的地址。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | `dtcm_addr` 不位于 DTCM 中时。 |
| `-ENODEV` | FlexRAM 中未分配 DTCM 时。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 Kconfig 选项 `CONFIG_NXP_FLEXRAM_MAGIC_ADDR_API` 时可用。

<a id="a374d43fc963ce2a7665f8c8bde58c7bf"></a>

### `flexram_set_itcm_magic_addr()`

```c
int flexram_set_itcm_magic_addr ( uint32_t itcm_addr)
```

为 ITCM 设置特殊地址（Magic Address）。

访问特殊地址（Magic Address）时，可由 FlexRAM 向内核触发中断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `itcm_addr` | ITCM 内要设置特殊功能（Magic Function）的地址。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | `itcm_addr` 不位于 ITCM 中时。 |
| `-ENODEV` | FlexRAM 中未分配 ITCM 时。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 Kconfig 选项 `CONFIG_NXP_FLEXRAM_MAGIC_ADDR_API` 时可用。

<a id="ac4ed80d0460f7765e9b9f2b58a0ec7cb"></a>

### `flexram_set_ocram_magic_addr()`

```c
int flexram_set_ocram_magic_addr ( uint32_t ocram_addr)
```

为 OCRAM 设置特殊地址（Magic Address）。

访问特殊地址（Magic Address）时，可由 FlexRAM 向内核触发中断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ocram_addr` | OCRAM 内要设置特殊功能（Magic Function）的地址。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | `ocram_addr` 不位于 OCRAM 中时。 |
| `-ENODEV` | FlexRAM 中未分配 OCRAM 时。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 Kconfig 选项 `CONFIG_NXP_FLEXRAM_MAGIC_ADDR_API` 时可用。


## 16.3\_原页交叉引用（Cross References）

- [zephyr/devicetree.h](../dt_main_reference/P002_设备树主头文件源码.md)
- [查看此文件的源码。](../api_source_system_reference/P033_nxp_flexram.h_源码浏览.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [CONFIG_NXP_FLEXRAM_MAGIC_ADDR_API](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_FLEXRAM_MAGIC_ADDR_API)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P015_zephyr__net__net_mgmt.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P017_zephyr__sensing__sensing.h_文件参考.md)
