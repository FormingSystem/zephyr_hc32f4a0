---
id: learning.zephyr-docs.api-file-service-interface-reference.page-19
title: zephyr__xen__fdt.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fdt_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_zephyr\_\_xen\_\_fdt.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/fdt_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Xen引导设备树（Boot Device Tree）的访问。

<a id="details"></a>

```c
#include <stdint.h>
```

查看此文件的源码。

Xen引导设备树（Boot Device Tree）的访问。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 19.1\_函数（Functions）

<a id="r_a1986171e6c2697b4914a2109b2eea281"></a>

```c
int xen_fdt_get (const uint8_t **fdt, uint32_t *fdt_size)
```

相关声明：[xen_fdt_get](#a1986171e6c2697b4914a2109b2eea281)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取已复制的 Xen 启动设备树（Boot Device Tree）。

## 19.2\_详细说明（Detailed Documentation）

<a id="a1986171e6c2697b4914a2109b2eea281"></a>

### `xen_fdt_get()`

```c
int xen_fdt_get ( const uint8_t ** fdt, uint32_t * fdt_size )
```

获取已复制的 Xen 启动设备树（Boot Device Tree）。

返回的指针引用早期启动（Early Boot）期间从 Xen 启动固件参数复制而来、由 Zephyr 拥有的副本。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fdt` | 输出复制后的扁平设备树（FDT）指针。 |
| `fdt_size` | 输出复制后的扁平设备树（FDT）大小，单位为字节。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 复制后的扁平设备树（FDT）可用时。 |
| `-EINVAL` | `fdt` 或 `fdt_size` 为 `NULL` 时。 |
| `-ENOENT` | 没有记录有效的扁平设备树（FDT）副本时。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 `CONFIG_XEN_FDT` Kconfig 选项时可用。


## 19.3\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P257_fdt.h_源码浏览.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [CONFIG_XEN_FDT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN_FDT)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P018_zephyr__drivers__espi_emul.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P020_zephyr__authentication__fido2__fido2.h_文件参考.md)
