---
id: learning.zephyr-docs.api-file-reference.page-194
title: zephyr__drivers__led__lp50xx.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lp50xx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第194章\_zephyr\_\_drivers\_\_led\_\_lp50xx.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/lp50xx_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 194.1\_宏定义（Macros）

<a id="r_a97594c95d9c99b55de0ef7e1624e44e4"></a>

```c
#define LP50XX_COLORS_PER_LED 3
```

相关声明：[LP50XX_COLORS_PER_LED](#a97594c95d9c99b55de0ef7e1624e44e4)。

<a id="r_a0cc3344b5a859f2463bda44624cdac6a"></a>

```c
#define LP5009_MAX_LEDS 3
```

相关声明：[LP5009_MAX_LEDS](#a0cc3344b5a859f2463bda44624cdac6a)。

<a id="r_ad668908bcff262bf5a27c72cebeabb65"></a>

```c
#define LP5012_MAX_LEDS 4
```

相关声明：[LP5012_MAX_LEDS](#ad668908bcff262bf5a27c72cebeabb65)。

<a id="r_a2ca3a6eb319ad14279fca6115f5d4fca"></a>

```c
#define LP5018_MAX_LEDS 6
```

相关声明：[LP5018_MAX_LEDS](#a2ca3a6eb319ad14279fca6115f5d4fca)。

<a id="r_a45b1d97cb6478e9231a2e22c99d27e6f"></a>

```c
#define LP5024_MAX_LEDS 8
```

相关声明：[LP5024_MAX_LEDS](#a45b1d97cb6478e9231a2e22c99d27e6f)。

<a id="r_ad1c6c734b5222d0d96579c7efd96288f"></a>

```c
#define LP5030_MAX_LEDS 10
```

相关声明：[LP5030_MAX_LEDS](#ad1c6c734b5222d0d96579c7efd96288f)。

<a id="r_a45f40ffa12fa78919030081bc158bdf5"></a>

```c
#define LP5036_MAX_LEDS 12
```

相关声明：[LP5036_MAX_LEDS](#a45f40ffa12fa78919030081bc158bdf5)。

<a id="r_ad660acc79b6312608072cb21edc902d8"></a>

```c
#define LP50XX_BANK_CHAN_BASE 0
```

相关声明：[LP50XX_BANK_CHAN_BASE](#ad660acc79b6312608072cb21edc902d8)。

<a id="r_ac26b03a074670393b10826e35acc92e3"></a>

```c
#define LP50XX_BANK_BRIGHT_CHAN LP50XX_BANK_CHAN_BASE
```

相关声明：[LP50XX_BANK_BRIGHT_CHAN](#ac26b03a074670393b10826e35acc92e3)、[LP50XX_BANK_CHAN_BASE](#ad660acc79b6312608072cb21edc902d8)。

<a id="r_a3220c920a91992087a21fbbf160b5a71"></a>

```c
#define LP50XX_BANK_COL1_CHAN(led)
```

相关声明：[LP50XX_BANK_COL1_CHAN](#a3220c920a91992087a21fbbf160b5a71)。

<a id="r_a17f11dcbce0cea164a4a506566ee81b9"></a>

```c
#define LP50XX_BANK_COL2_CHAN(led)
```

相关声明：[LP50XX_BANK_COL2_CHAN](#a17f11dcbce0cea164a4a506566ee81b9)。

<a id="r_a9292372cafb9882f6e573063bdbaf99a"></a>

```c
#define LP50XX_BANK_COL3_CHAN(led)
```

相关声明：[LP50XX_BANK_COL3_CHAN](#a9292372cafb9882f6e573063bdbaf99a)。

<a id="r_aedaed7d9a9feb6c2e18ff646dd4f0741"></a>

```c
#define LP50XX_LED_BRIGHT_CHAN_BASE 4
```

相关声明：[LP50XX_LED_BRIGHT_CHAN_BASE](#aedaed7d9a9feb6c2e18ff646dd4f0741)。

<a id="r_a7421dfa3aa4a135fa6d937d467ee7b44"></a>

```c
#define LP50XX_LED_BRIGHT_CHAN(led)
```

相关声明：[LP50XX_LED_BRIGHT_CHAN](#a7421dfa3aa4a135fa6d937d467ee7b44)。

<a id="r_a46f005a17ecfeb7ea241d18ed2503029"></a>

```c
#define LP5012_LED_COL_CHAN_BASE 8
```

相关声明：[LP5012_LED_COL_CHAN_BASE](#a46f005a17ecfeb7ea241d18ed2503029)。

<a id="r_ae1461195d755ea951b6bb2ce3f45392d"></a>

```c
#define LP5012_LED_COL1_CHAN(led)
```

相关声明：[LP5012_LED_COL1_CHAN](#ae1461195d755ea951b6bb2ce3f45392d)。

<a id="r_ab70cfd7eb411f1f2f6d8370452775ccd"></a>

```c
#define LP5012_LED_COL2_CHAN(led)
```

相关声明：[LP5012_LED_COL2_CHAN](#ab70cfd7eb411f1f2f6d8370452775ccd)。

<a id="r_ae24a2d64b31fb8de59a119b6c1f63b15"></a>

```c
#define LP5012_LED_COL3_CHAN(led)
```

相关声明：[LP5012_LED_COL3_CHAN](#ae24a2d64b31fb8de59a119b6c1f63b15)。

<a id="r_ac48720b13bd1aa213a4d4951ed96066a"></a>

```c
#define LP5024_LED_COL_CHAN_BASE 12
```

相关声明：[LP5024_LED_COL_CHAN_BASE](#ac48720b13bd1aa213a4d4951ed96066a)。

<a id="r_ab86853d9f0417c2f1afba73cfacdfcd2"></a>

```c
#define LP5024_LED_COL1_CHAN(led)
```

相关声明：[LP5024_LED_COL1_CHAN](#ab86853d9f0417c2f1afba73cfacdfcd2)。

<a id="r_af0e0393357be9850c1944210f28aa32a"></a>

```c
#define LP5024_LED_COL2_CHAN(led)
```

相关声明：[LP5024_LED_COL2_CHAN](#af0e0393357be9850c1944210f28aa32a)。

<a id="r_a1df2b6f63b73b1b555a08e06f4da0c2d"></a>

```c
#define LP5024_LED_COL3_CHAN(led)
```

相关声明：[LP5024_LED_COL3_CHAN](#a1df2b6f63b73b1b555a08e06f4da0c2d)。

<a id="r_ae3dcf20db935d5cb64e62bffd44693d1"></a>

```c
#define LP5036_LED_COL_CHAN_BASE 16
```

相关声明：[LP5036_LED_COL_CHAN_BASE](#ae3dcf20db935d5cb64e62bffd44693d1)。

<a id="r_a24f8253051a6c6622c3c9d8c938a1c44"></a>

```c
#define LP5036_LED_COL1_CHAN(led)
```

相关声明：[LP5036_LED_COL1_CHAN](#a24f8253051a6c6622c3c9d8c938a1c44)。

<a id="r_a72cfa3e69e9b9a7ee16a8dd243cc0782"></a>

```c
#define LP5036_LED_COL2_CHAN(led)
```

相关声明：[LP5036_LED_COL2_CHAN](#a72cfa3e69e9b9a7ee16a8dd243cc0782)。

<a id="r_a4d4d92b15651f34f7c1d9747b10f4267"></a>

```c
#define LP5036_LED_COL3_CHAN(led)
```

相关声明：[LP5036_LED_COL3_CHAN](#a4d4d92b15651f34f7c1d9747b10f4267)。

## 194.2\_详细说明（Detailed Documentation）

<a id="a0cc3344b5a859f2463bda44624cdac6a"></a>

### `LP5009_MAX_LEDS`

```c
#define LP5009_MAX_LEDS 3
```

<a id="ae1461195d755ea951b6bb2ce3f45392d"></a>

### `LP5012_LED_COL1_CHAN`

```c
#define LP5012_LED_COL1_CHAN ( led)
```

展开值（Value）：

```c
(LP5012_LED_COL_CHAN_BASE + led * LP50XX_COLORS_PER_LED)
```

<a id="ab70cfd7eb411f1f2f6d8370452775ccd"></a>

### `LP5012_LED_COL2_CHAN`

```c
#define LP5012_LED_COL2_CHAN ( led)
```

展开值（Value）：

```c
(LP5012_LED_COL_CHAN_BASE + led * LP50XX_COLORS_PER_LED + 1)
```

<a id="ae24a2d64b31fb8de59a119b6c1f63b15"></a>

### `LP5012_LED_COL3_CHAN`

```c
#define LP5012_LED_COL3_CHAN ( led)
```

展开值（Value）：

```c
(LP5012_LED_COL_CHAN_BASE + led * LP50XX_COLORS_PER_LED + 2)
```

<a id="a46f005a17ecfeb7ea241d18ed2503029"></a>

### `LP5012_LED_COL_CHAN_BASE`

```c
#define LP5012_LED_COL_CHAN_BASE 8
```

<a id="ad668908bcff262bf5a27c72cebeabb65"></a>

### `LP5012_MAX_LEDS`

```c
#define LP5012_MAX_LEDS 4
```

<a id="a2ca3a6eb319ad14279fca6115f5d4fca"></a>

### `LP5018_MAX_LEDS`

```c
#define LP5018_MAX_LEDS 6
```

<a id="ab86853d9f0417c2f1afba73cfacdfcd2"></a>

### `LP5024_LED_COL1_CHAN`

```c
#define LP5024_LED_COL1_CHAN ( led)
```

展开值（Value）：

```c
(LP5024_LED_COL_CHAN_BASE + led * LP50XX_COLORS_PER_LED)
```

<a id="af0e0393357be9850c1944210f28aa32a"></a>

### `LP5024_LED_COL2_CHAN`

```c
#define LP5024_LED_COL2_CHAN ( led)
```

展开值（Value）：

```c
(LP5024_LED_COL_CHAN_BASE + led * LP50XX_COLORS_PER_LED + 1)
```

<a id="a1df2b6f63b73b1b555a08e06f4da0c2d"></a>

### `LP5024_LED_COL3_CHAN`

```c
#define LP5024_LED_COL3_CHAN ( led)
```

展开值（Value）：

```c
(LP5024_LED_COL_CHAN_BASE + led * LP50XX_COLORS_PER_LED + 2)
```

<a id="ac48720b13bd1aa213a4d4951ed96066a"></a>

### `LP5024_LED_COL_CHAN_BASE`

```c
#define LP5024_LED_COL_CHAN_BASE 12
```

<a id="a45b1d97cb6478e9231a2e22c99d27e6f"></a>

### `LP5024_MAX_LEDS`

```c
#define LP5024_MAX_LEDS 8
```

<a id="ad1c6c734b5222d0d96579c7efd96288f"></a>

### `LP5030_MAX_LEDS`

```c
#define LP5030_MAX_LEDS 10
```

<a id="a24f8253051a6c6622c3c9d8c938a1c44"></a>

### `LP5036_LED_COL1_CHAN`

```c
#define LP5036_LED_COL1_CHAN ( led)
```

展开值（Value）：

```c
(LP5036_LED_COL_CHAN_BASE + led * LP50XX_COLORS_PER_LED)
```

<a id="a72cfa3e69e9b9a7ee16a8dd243cc0782"></a>

### `LP5036_LED_COL2_CHAN`

```c
#define LP5036_LED_COL2_CHAN ( led)
```

展开值（Value）：

```c
(LP5036_LED_COL_CHAN_BASE + led * LP50XX_COLORS_PER_LED + 1)
```

<a id="a4d4d92b15651f34f7c1d9747b10f4267"></a>

### `LP5036_LED_COL3_CHAN`

```c
#define LP5036_LED_COL3_CHAN ( led)
```

展开值（Value）：

```c
(LP5036_LED_COL_CHAN_BASE + led * LP50XX_COLORS_PER_LED + 2)
```

<a id="ae3dcf20db935d5cb64e62bffd44693d1"></a>

### `LP5036_LED_COL_CHAN_BASE`

```c
#define LP5036_LED_COL_CHAN_BASE 16
```

<a id="a45f40ffa12fa78919030081bc158bdf5"></a>

### `LP5036_MAX_LEDS`

```c
#define LP5036_MAX_LEDS 12
```

<a id="ac26b03a074670393b10826e35acc92e3"></a>

### `LP50XX_BANK_BRIGHT_CHAN`

```c
#define LP50XX_BANK_BRIGHT_CHAN LP50XX_BANK_CHAN_BASE
```

<a id="ad660acc79b6312608072cb21edc902d8"></a>

### `LP50XX_BANK_CHAN_BASE`

```c
#define LP50XX_BANK_CHAN_BASE 0
```

<a id="a3220c920a91992087a21fbbf160b5a71"></a>

### `LP50XX_BANK_COL1_CHAN`

```c
#define LP50XX_BANK_COL1_CHAN ( led)
```

展开值（Value）：

```c
(LP50XX_BANK_CHAN_BASE + 1)
```

<a id="a17f11dcbce0cea164a4a506566ee81b9"></a>

### `LP50XX_BANK_COL2_CHAN`

```c
#define LP50XX_BANK_COL2_CHAN ( led)
```

展开值（Value）：

```c
(LP50XX_BANK_CHAN_BASE + 2)
```

<a id="a9292372cafb9882f6e573063bdbaf99a"></a>

### `LP50XX_BANK_COL3_CHAN`

```c
#define LP50XX_BANK_COL3_CHAN ( led)
```

展开值（Value）：

```c
(LP50XX_BANK_CHAN_BASE + 3)
```

<a id="a97594c95d9c99b55de0ef7e1624e44e4"></a>

### `LP50XX_COLORS_PER_LED`

```c
#define LP50XX_COLORS_PER_LED 3
```

<a id="a7421dfa3aa4a135fa6d937d467ee7b44"></a>

### `LP50XX_LED_BRIGHT_CHAN`

```c
#define LP50XX_LED_BRIGHT_CHAN ( led)
```

展开值（Value）：

```c
(LP50XX_LED_BRIGHT_CHAN_BASE + led)
```

<a id="aedaed7d9a9feb6c2e18ff646dd4f0741"></a>

### `LP50XX_LED_BRIGHT_CHAN_BASE`

```c
#define LP50XX_LED_BRIGHT_CHAN_BASE 4
```


## 194.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/lp50xx_8h_source.html)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="alp50xx_8h_html_a46f005a17ecfeb7ea241d18ed2503029"></a>
<a id="alp50xx_8h_html_a97594c95d9c99b55de0ef7e1624e44e4"></a>
<a id="alp50xx_8h_html_ac48720b13bd1aa213a4d4951ed96066a"></a>
<a id="alp50xx_8h_html_ae3dcf20db935d5cb64e62bffd44693d1"></a>
<a id="alp50xx_8h_html_ad660acc79b6312608072cb21edc902d8"></a>
<a id="alp50xx_8h_html_aedaed7d9a9feb6c2e18ff646dd4f0741"></a>

---

[上一章](P193_zephyr__misc__lorem_ipsum.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P195_zephyr__dt-bindings__clock__lpc11u6x_clock.h_文件参考.md)
