---
id: learning.zephyr-docs.api-file-reference.page-163
title: zephyr__dt-bindings__gpio__infineon-xmc4xxx-gpio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/infineon-xmc4xxx-gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第163章\_zephyr\_\_dt-bindings\_\_gpio\_\_infineon-xmc4xxx-gpio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/infineon-xmc4xxx-gpio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 163.1\_宏定义（Macros）

<a id="r_a0204cbd6c151fcea59199b1c4e007eaf"></a>

```c
#define XMC4XXX_GPIO_DS_POS 9
```

相关声明：[XMC4XXX_GPIO_DS_POS](#a0204cbd6c151fcea59199b1c4e007eaf)。

<a id="r_a766a7c07cd178b9373fec28745b1e077"></a>

```c
#define XMC4XXX_GPIO_DS_MASK 0xf
```

相关声明：[XMC4XXX_GPIO_DS_MASK](#a766a7c07cd178b9373fec28745b1e077)。

<a id="r_ab820bfc6577c45c88b59260531d078d3"></a>

```c
#define XMC4XXX_GPIO_DS_STRONG_SHARP_EDGE (0x1 << XMC4XXX_GPIO_DS_POS)
```

相关声明：[XMC4XXX_GPIO_DS_STRONG_SHARP_EDGE](#ab820bfc6577c45c88b59260531d078d3)、[XMC4XXX_GPIO_DS_POS](#a0204cbd6c151fcea59199b1c4e007eaf)。

<a id="r_a6a21bcff48f4e8a4acede963a534fb95"></a>

```c
#define XMC4XXX_GPIO_DS_STRONG_MEDIUM_EDGE (0x2 << XMC4XXX_GPIO_DS_POS)
```

相关声明：[XMC4XXX_GPIO_DS_STRONG_MEDIUM_EDGE](#a6a21bcff48f4e8a4acede963a534fb95)、[XMC4XXX_GPIO_DS_POS](#a0204cbd6c151fcea59199b1c4e007eaf)。

<a id="r_a07e14898ba2a322edf9729054832c1a9"></a>

```c
#define XMC4XXX_GPIO_DS_STRONG_SOFT_EDGE (0x3 << XMC4XXX_GPIO_DS_POS)
```

相关声明：[XMC4XXX_GPIO_DS_STRONG_SOFT_EDGE](#a07e14898ba2a322edf9729054832c1a9)、[XMC4XXX_GPIO_DS_POS](#a0204cbd6c151fcea59199b1c4e007eaf)。

<a id="r_aa81ddd8894b2f3a1e991b5d95ac81a7f"></a>

```c
#define XMC4XXX_GPIO_DS_STRONG_SLOW_EDGE (0x4 << XMC4XXX_GPIO_DS_POS)
```

相关声明：[XMC4XXX_GPIO_DS_STRONG_SLOW_EDGE](#aa81ddd8894b2f3a1e991b5d95ac81a7f)、[XMC4XXX_GPIO_DS_POS](#a0204cbd6c151fcea59199b1c4e007eaf)。

<a id="r_af725ddf9a1dfaf02d478cdcf94132a24"></a>

```c
#define XMC4XXX_GPIO_DS_MEDIUM (0x5 << XMC4XXX_GPIO_DS_POS)
```

相关声明：[XMC4XXX_GPIO_DS_MEDIUM](#af725ddf9a1dfaf02d478cdcf94132a24)、[XMC4XXX_GPIO_DS_POS](#a0204cbd6c151fcea59199b1c4e007eaf)。

<a id="r_a5c307c3181d3094cadb68766b318b3e5"></a>

```c
#define XMC4XXX_GPIO_DS_WEAK (0x8 << XMC4XXX_GPIO_DS_POS)
```

相关声明：[XMC4XXX_GPIO_DS_WEAK](#a5c307c3181d3094cadb68766b318b3e5)、[XMC4XXX_GPIO_DS_POS](#a0204cbd6c151fcea59199b1c4e007eaf)。

<a id="r_a52bb9df6ed1e4ead550ceefe1b96a5b3"></a>

```c
#define XMC4XXX_GPIO_GET_DS(flags)
```

相关声明：[XMC4XXX_GPIO_GET_DS](#a52bb9df6ed1e4ead550ceefe1b96a5b3)、[flags](P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

## 163.2\_详细说明（Detailed Documentation）

<a id="a766a7c07cd178b9373fec28745b1e077"></a>

### `XMC4XXX_GPIO_DS_MASK`

```c
#define XMC4XXX_GPIO_DS_MASK 0xf
```

<a id="af725ddf9a1dfaf02d478cdcf94132a24"></a>

### `XMC4XXX_GPIO_DS_MEDIUM`

```c
#define XMC4XXX_GPIO_DS_MEDIUM (0x5 << XMC4XXX_GPIO_DS_POS)
```

<a id="a0204cbd6c151fcea59199b1c4e007eaf"></a>

### `XMC4XXX_GPIO_DS_POS`

```c
#define XMC4XXX_GPIO_DS_POS 9
```

<a id="a6a21bcff48f4e8a4acede963a534fb95"></a>

### `XMC4XXX_GPIO_DS_STRONG_MEDIUM_EDGE`

```c
#define XMC4XXX_GPIO_DS_STRONG_MEDIUM_EDGE (0x2 << XMC4XXX_GPIO_DS_POS)
```

<a id="ab820bfc6577c45c88b59260531d078d3"></a>

### `XMC4XXX_GPIO_DS_STRONG_SHARP_EDGE`

```c
#define XMC4XXX_GPIO_DS_STRONG_SHARP_EDGE (0x1 << XMC4XXX_GPIO_DS_POS)
```

<a id="aa81ddd8894b2f3a1e991b5d95ac81a7f"></a>

### `XMC4XXX_GPIO_DS_STRONG_SLOW_EDGE`

```c
#define XMC4XXX_GPIO_DS_STRONG_SLOW_EDGE (0x4 << XMC4XXX_GPIO_DS_POS)
```

<a id="a07e14898ba2a322edf9729054832c1a9"></a>

### `XMC4XXX_GPIO_DS_STRONG_SOFT_EDGE`

```c
#define XMC4XXX_GPIO_DS_STRONG_SOFT_EDGE (0x3 << XMC4XXX_GPIO_DS_POS)
```

<a id="a5c307c3181d3094cadb68766b318b3e5"></a>

### `XMC4XXX_GPIO_DS_WEAK`

```c
#define XMC4XXX_GPIO_DS_WEAK (0x8 << XMC4XXX_GPIO_DS_POS)
```

<a id="a52bb9df6ed1e4ead550ceefe1b96a5b3"></a>

### `XMC4XXX_GPIO_GET_DS`

```c
#define XMC4XXX_GPIO_GET_DS ( flags)
```

展开值（Value）：

```c
((flags >> XMC4XXX_GPIO_DS_POS) & XMC4XXX_GPIO_DS_MASK)
```


## 163.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_configuration_reference/P036_infineon-xmc4xxx-gpio.h_源码浏览.md)
- [flags](P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="ainfineon-xmc4xxx-gpio_8h_html_a0204cbd6c151fcea59199b1c4e007eaf"></a>
<a id="ainfineon-xmc4xxx-gpio_8h_html_a766a7c07cd178b9373fec28745b1e077"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>

---

[上一章](P162_zephyr__dt-bindings__dma__infineon-xmc4xxx-dma.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P164_zephyr__dt-bindings__inputmux__inputmux_trigger_ports.h_文件参考.md)
