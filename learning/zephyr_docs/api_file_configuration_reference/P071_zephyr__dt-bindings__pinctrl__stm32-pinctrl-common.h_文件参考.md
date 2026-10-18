---
id: learning.zephyr-docs.api-file-configuration-reference.page-71
title: zephyr__dt-bindings__pinctrl__stm32-pinctrl-common.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32-pinctrl-common_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第71章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_stm32-pinctrl-common.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/stm32-pinctrl-common_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 71.1\_宏定义（Macros）

<a id="r_a031a76d5d56cbb86e5c5dffad52732b5"></a>

```c
#define STM32_PORTA 0 /* IO port A */
```

相关声明：[STM32_PORTA](#a031a76d5d56cbb86e5c5dffad52732b5)。

输入输出端口（IO Ports）的数值标识（Numerical IDs）。

<a id="r_ab5be546a1dccb589e6be842575829019"></a>

```c
#define STM32_PORTB 1 /* .. */
```

相关声明：[STM32_PORTB](#ab5be546a1dccb589e6be842575829019)。

<a id="r_ac56b63d53a5c187035e4386bdb5e6ffa"></a>

```c
#define STM32_PORTC 2
```

相关声明：[STM32_PORTC](#ac56b63d53a5c187035e4386bdb5e6ffa)。

<a id="r_a866773d51364d1821245a910c03e8686"></a>

```c
#define STM32_PORTD 3
```

相关声明：[STM32_PORTD](#a866773d51364d1821245a910c03e8686)。

<a id="r_a1402c542481316eedd39e3cda89410bf"></a>

```c
#define STM32_PORTE 4
```

相关声明：[STM32_PORTE](#a1402c542481316eedd39e3cda89410bf)。

<a id="r_aac43eb483c2b7b744c216b9e2cf62770"></a>

```c
#define STM32_PORTF 5
```

相关声明：[STM32_PORTF](#aac43eb483c2b7b744c216b9e2cf62770)。

<a id="r_ac4464e020843f97772036ae27da7abd5"></a>

```c
#define STM32_PORTG 6
```

相关声明：[STM32_PORTG](#ac4464e020843f97772036ae27da7abd5)。

<a id="r_a744d089635ebefd4bfb65b673699256a"></a>

```c
#define STM32_PORTH 7
```

相关声明：[STM32_PORTH](#a744d089635ebefd4bfb65b673699256a)。

<a id="r_ab11184138506e9df5e93a10f28f45d63"></a>

```c
#define STM32_PORTI 8
```

相关声明：[STM32_PORTI](#ab11184138506e9df5e93a10f28f45d63)。

<a id="r_a0ea163478aef753a739f96f9bf448d8b"></a>

```c
#define STM32_PORTJ 9
```

相关声明：[STM32_PORTJ](#a0ea163478aef753a739f96f9bf448d8b)。

<a id="r_a057f431270f633fedc990bb971ce6a05"></a>

```c
#define STM32_PORTK 10 /* IO port K */
```

相关声明：[STM32_PORTK](#a057f431270f633fedc990bb971ce6a05)。

<a id="r_a19abb84f712b1899d8aaadfad34301bd"></a>

```c
#define STM32_PORTM 12 /* IO port M (0xC) */
```

相关声明：[STM32_PORTM](#a19abb84f712b1899d8aaadfad34301bd)。

<a id="r_ac354044c6615887e456a65a0aa5e226c"></a>

```c
#define STM32_PORTN 13
```

相关声明：[STM32_PORTN](#ac354044c6615887e456a65a0aa5e226c)。

<a id="r_ac363d8900ccc9a9e7b022c8f558b53f7"></a>

```c
#define STM32_PORTO 14
```

相关声明：[STM32_PORTO](#ac363d8900ccc9a9e7b022c8f558b53f7)。

<a id="r_a2bc75591bd6f3010c0b58b66bead967d"></a>

```c
#define STM32_PORTP 15 /* IO port P (0xF) */
```

相关声明：[STM32_PORTP](#a2bc75591bd6f3010c0b58b66bead967d)。

<a id="r_abba293dc8f52c5ef4329037eb499fecf"></a>

```c
#define STM32_PORTQ 16 /* IO port Q (0x10) */
```

相关声明：[STM32_PORTQ](#abba293dc8f52c5ef4329037eb499fecf)。

<a id="r_a20eeae5c2adcf38dd94f31636c1ec716"></a>

```c
#define STM32_PORTZ 25 /* IO port Z (0x19) */
```

相关声明：[STM32_PORTZ](#a20eeae5c2adcf38dd94f31636c1ec716)。

<a id="r_a615b26e8931dfb9ed75e49368eac572d"></a>

```c
#define STM32_PORTS_MAX (STM32_PORTZ + 1)
```

相关声明：[STM32_PORTS_MAX](#a615b26e8931dfb9ed75e49368eac572d)、[STM32_PORTZ](#a20eeae5c2adcf38dd94f31636c1ec716)。

<a id="r_ae496c0ca2dc170f1443b6e35db2a2d1e"></a>

```c
#define STM32PIN(_port, _pin)
```

相关声明：[STM32PIN](#ae496c0ca2dc170f1443b6e35db2a2d1e)。

将输入输出端口引脚（IO Port Pin）编码为数值格式（Numerical Format）的辅助宏（Helper Macro）。

## 71.2\_详细说明（Detailed Documentation）

<a id="a031a76d5d56cbb86e5c5dffad52732b5"></a>

### `STM32_PORTA`

```c
#define STM32_PORTA 0 /* IO port A */
```

输入输出端口（IO Ports）的数值标识（Numerical IDs）。

<a id="ab5be546a1dccb589e6be842575829019"></a>

### `STM32_PORTB`

```c
#define STM32_PORTB 1 /* .. */
```

<a id="ac56b63d53a5c187035e4386bdb5e6ffa"></a>

### `STM32_PORTC`

```c
#define STM32_PORTC 2
```

<a id="a866773d51364d1821245a910c03e8686"></a>

### `STM32_PORTD`

```c
#define STM32_PORTD 3
```

<a id="a1402c542481316eedd39e3cda89410bf"></a>

### `STM32_PORTE`

```c
#define STM32_PORTE 4
```

<a id="aac43eb483c2b7b744c216b9e2cf62770"></a>

### `STM32_PORTF`

```c
#define STM32_PORTF 5
```

<a id="ac4464e020843f97772036ae27da7abd5"></a>

### `STM32_PORTG`

```c
#define STM32_PORTG 6
```

<a id="a744d089635ebefd4bfb65b673699256a"></a>

### `STM32_PORTH`

```c
#define STM32_PORTH 7
```

<a id="ab11184138506e9df5e93a10f28f45d63"></a>

### `STM32_PORTI`

```c
#define STM32_PORTI 8
```

<a id="a0ea163478aef753a739f96f9bf448d8b"></a>

### `STM32_PORTJ`

```c
#define STM32_PORTJ 9
```

<a id="a057f431270f633fedc990bb971ce6a05"></a>

### `STM32_PORTK`

```c
#define STM32_PORTK 10 /* IO port K */
```

<a id="a19abb84f712b1899d8aaadfad34301bd"></a>

### `STM32_PORTM`

```c
#define STM32_PORTM 12 /* IO port M (0xC) */
```

<a id="ac354044c6615887e456a65a0aa5e226c"></a>

### `STM32_PORTN`

```c
#define STM32_PORTN 13
```

<a id="ac363d8900ccc9a9e7b022c8f558b53f7"></a>

### `STM32_PORTO`

```c
#define STM32_PORTO 14
```

<a id="a2bc75591bd6f3010c0b58b66bead967d"></a>

### `STM32_PORTP`

```c
#define STM32_PORTP 15 /* IO port P (0xF) */
```

<a id="abba293dc8f52c5ef4329037eb499fecf"></a>

### `STM32_PORTQ`

```c
#define STM32_PORTQ 16 /* IO port Q (0x10) */
```

<a id="a615b26e8931dfb9ed75e49368eac572d"></a>

### `STM32_PORTS_MAX`

```c
#define STM32_PORTS_MAX (STM32_PORTZ + 1)
```

<a id="a20eeae5c2adcf38dd94f31636c1ec716"></a>

### `STM32_PORTZ`

```c
#define STM32_PORTZ 25 /* IO port Z (0x19) */
```

<a id="ae496c0ca2dc170f1443b6e35db2a2d1e"></a>

### `STM32PIN`

```c
#define STM32PIN ( _port, _pin )
```

展开值（Value）：

```c
(_port << 4 | _pin)
```

将输入输出端口引脚（IO Port Pin）编码为数值格式（Numerical Format）的辅助宏（Helper Macro）。


## 71.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/stm32-pinctrl-common_8h_source.html)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P070_zephyr__display__ssd16xx.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P072_zephyr__drivers__flash__stm32_flash_api_extensions.h_文件参考.md)
