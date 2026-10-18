---
id: learning.zephyr-docs.api-file-reference.page-253
title: zephyr__dt-bindings__flash_controller__npcx_fiu_qspi.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/npcx__fiu__qspi_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第253章\_zephyr\_\_dt-bindings\_\_flash\_controller\_\_npcx\_fiu\_qspi.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/npcx__fiu__qspi_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/dt-bindings/dt-util.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 253.1\_宏定义（Macros）

<a id="r_ab2702585eae967c9749836860a1475b9"></a>

```c
#define NPCX_QSPI_SW_CS0 BIT(0)
```

相关声明：[NPCX_QSPI_SW_CS0](#ab2702585eae967c9749836860a1475b9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a8273de16e9b279e5fbfe63db34d398cb"></a>

```c
#define NPCX_QSPI_SW_CS1 BIT(1)
```

相关声明：[NPCX_QSPI_SW_CS1](#a8273de16e9b279e5fbfe63db34d398cb)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a146d0d39da877413dd09637ef4243414"></a>

```c
#define NPCX_QSPI_SW_CS2 BIT(2)
```

相关声明：[NPCX_QSPI_SW_CS2](#a146d0d39da877413dd09637ef4243414)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_abe20f1ebc30af0e7d951a35d7dc4261e"></a>

```c
#define NPCX_QSPI_SW_CS_MASK (NPCX_QSPI_SW_CS0 | NPCX_QSPI_SW_CS1 | NPCX_QSPI_SW_CS2)
```

相关声明：[NPCX_QSPI_SW_CS_MASK](#abe20f1ebc30af0e7d951a35d7dc4261e)、[NPCX_QSPI_SW_CS0](#ab2702585eae967c9749836860a1475b9)、[NPCX_QSPI_SW_CS1](#a8273de16e9b279e5fbfe63db34d398cb)、[NPCX_QSPI_SW_CS2](#a146d0d39da877413dd09637ef4243414)。

<a id="r_a48455b5bf574e67c6463c69ebb8b348b"></a>

```c
#define NPCX_QSPI_SEC_FLASH_SL BIT(4)
```

相关声明：[NPCX_QSPI_SEC_FLASH_SL](#a48455b5bf574e67c6463c69ebb8b348b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_af944da160fb5e04c9ede27d1de20ea79"></a>

```c
#define NPCX_QSPI_PVT_FLASH_SL BIT(5)
```

相关声明：[NPCX_QSPI_PVT_FLASH_SL](#af944da160fb5e04c9ede27d1de20ea79)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ae0526ad39c71a8362516757db2c73b95"></a>

```c
#define NPCX_QSPI_SHD_FLASH_SL BIT(6)
```

相关声明：[NPCX_QSPI_SHD_FLASH_SL](#ae0526ad39c71a8362516757db2c73b95)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a8e1e8cfe9bbcd94d9fdb460875839f30"></a>

```c
#define NPCX_QSPI_BKP_FLASH_SL BIT(7)
```

相关声明：[NPCX_QSPI_BKP_FLASH_SL](#a8e1e8cfe9bbcd94d9fdb460875839f30)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a2197dbcc86f29bb20e8445e52a31d18b"></a>

```c
#define NPCX_RD_MODE_NORMAL 0
```

相关声明：[NPCX_RD_MODE_NORMAL](#a2197dbcc86f29bb20e8445e52a31d18b)。

<a id="r_aef0c37fff59a0b1c17c495d2be6f3665"></a>

```c
#define NPCX_RD_MODE_FAST 1
```

相关声明：[NPCX_RD_MODE_FAST](#aef0c37fff59a0b1c17c495d2be6f3665)。

<a id="r_a9b766e793cc32a60785b93385752085d"></a>

```c
#define NPCX_RD_MODE_FAST_DUAL 3
```

相关声明：[NPCX_RD_MODE_FAST_DUAL](#a9b766e793cc32a60785b93385752085d)。

## 253.2\_详细说明（Detailed Documentation）

<a id="a8e1e8cfe9bbcd94d9fdb460875839f30"></a>

### `NPCX_QSPI_BKP_FLASH_SL`

```c
#define NPCX_QSPI_BKP_FLASH_SL BIT(7)
```

<a id="af944da160fb5e04c9ede27d1de20ea79"></a>

### `NPCX_QSPI_PVT_FLASH_SL`

```c
#define NPCX_QSPI_PVT_FLASH_SL BIT(5)
```

<a id="a48455b5bf574e67c6463c69ebb8b348b"></a>

### `NPCX_QSPI_SEC_FLASH_SL`

```c
#define NPCX_QSPI_SEC_FLASH_SL BIT(4)
```

<a id="ae0526ad39c71a8362516757db2c73b95"></a>

### `NPCX_QSPI_SHD_FLASH_SL`

```c
#define NPCX_QSPI_SHD_FLASH_SL BIT(6)
```

<a id="ab2702585eae967c9749836860a1475b9"></a>

### `NPCX_QSPI_SW_CS0`

```c
#define NPCX_QSPI_SW_CS0 BIT(0)
```

<a id="a8273de16e9b279e5fbfe63db34d398cb"></a>

### `NPCX_QSPI_SW_CS1`

```c
#define NPCX_QSPI_SW_CS1 BIT(1)
```

<a id="a146d0d39da877413dd09637ef4243414"></a>

### `NPCX_QSPI_SW_CS2`

```c
#define NPCX_QSPI_SW_CS2 BIT(2)
```

<a id="abe20f1ebc30af0e7d951a35d7dc4261e"></a>

### `NPCX_QSPI_SW_CS_MASK`

```c
#define NPCX_QSPI_SW_CS_MASK (NPCX_QSPI_SW_CS0 | NPCX_QSPI_SW_CS1 | NPCX_QSPI_SW_CS2)
```

<a id="aef0c37fff59a0b1c17c495d2be6f3665"></a>

### `NPCX_RD_MODE_FAST`

```c
#define NPCX_RD_MODE_FAST 1
```

<a id="a9b766e793cc32a60785b93385752085d"></a>

### `NPCX_RD_MODE_FAST_DUAL`

```c
#define NPCX_RD_MODE_FAST_DUAL 3
```

<a id="a2197dbcc86f29bb20e8445e52a31d18b"></a>

### `NPCX_RD_MODE_NORMAL`

```c
#define NPCX_RD_MODE_NORMAL 0
```


## 253.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P006_设备树绑定工具头文件源码.md)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/npcx__fiu__qspi_8h_source.html)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P252_zephyr__dt-bindings__espi__npcx_espi.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P254_zephyr__drivers__sensor__npm13xx_charger.h_文件参考.md)
