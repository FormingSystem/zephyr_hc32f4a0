---
id: learning.zephyr-docs.api-file-configuration-reference.page-21
title: zephyr__drivers__emul_bbram.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/emul__bbram_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_zephyr\_\_drivers\_\_emul\_bbram.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/emul__bbram_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

电池备份RAM（BBRAM）仿真器的后端API。

<a id="details"></a>

```c
#include <zephyr/drivers/emul.h>
#include <stdint.h>
```

查看此文件的源码。

电池备份RAM（BBRAM）仿真器的后端API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 21.1\_函数（Functions）

<a id="r_gaeff1fa9acd765323778c42a4c3424c0b"></a>

```c
static int emul_bbram_backend_set_data (const struct emul *target, size_t offset, size_t count, const uint8_t *data)
```

相关声明：[emul_bbram_backend_set_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__emulator__backend.html#gaeff1fa9acd765323778c42a4c3424c0b)、[emul](../hardware/P477_仿真器实例结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置电池备份 RAM 区域（BBRAM Region）中的预期数据（Expected Data）。

<a id="r_ga92942f1ebe6905ad3cfe389824af5914"></a>

```c
static int emul_bbram_backend_get_data (const struct emul *target, size_t offset, size_t count, uint8_t *data)
```

相关声明：[emul_bbram_backend_get_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__emulator__backend.html#ga92942f1ebe6905ad3cfe389824af5914)、[emul](../hardware/P477_仿真器实例结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取电池备份 RAM 区域（BBRAM Region）中的预期数据（Expected Data）。


## 21.2\_原页交叉引用（Cross References）

- [zephyr/drivers/emul.h](../api_source_runtime_reference/P013_emul.h_源码浏览.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P223_emul_bbram.h_源码浏览.md)
- [emul_bbram_backend_set_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__emulator__backend.html#gaeff1fa9acd765323778c42a4c3424c0b)
- [emul](../hardware/P477_仿真器实例结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [emul_bbram_backend_get_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__emulator__backend.html#ga92942f1ebe6905ad3cfe389824af5914)

<a id="header-details"></a>

---

[上一章](P020_zephyr__dt-bindings__dma__dma_smartbond.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P022_zephyr__drivers__usb__emul_bc12.h_文件参考.md)
