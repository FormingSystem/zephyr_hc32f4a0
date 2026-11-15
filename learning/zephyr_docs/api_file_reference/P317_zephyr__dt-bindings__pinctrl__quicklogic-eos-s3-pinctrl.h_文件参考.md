---
id: learning.zephyr-docs.api-file-reference.page-317
title: zephyr__dt-bindings__pinctrl__quicklogic-eos-s3-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/quicklogic-eos-s3-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第317章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_quicklogic-eos-s3-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/quicklogic-eos-s3-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/dt-bindings/dt-util.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 317.1\_宏定义（Macros）

<a id="r_a42e8d57fbc0ce7fea27c8e5487008c38"></a>

```c
#define IO_MUX_REG_MAX_OFFSET 107
```

相关声明：[IO_MUX_REG_MAX_OFFSET](#a42e8d57fbc0ce7fea27c8e5487008c38)。

<a id="r_ab345030af28df16546437382d1c935a9"></a>

```c
#define IO_MUX_MAX_PAD_NR 45
```

相关声明：[IO_MUX_MAX_PAD_NR](#ab345030af28df16546437382d1c935a9)。

<a id="r_a76393e634c1e77ca47d7106c27889936"></a>

```c
#define FUNC_SEL_UART_RX (77 << 13)
```

相关声明：[FUNC_SEL_UART_RX](#a76393e634c1e77ca47d7106c27889936)。

<a id="r_a32684ea1b082834fcadc1d17ab2f6ea7"></a>

```c
#define QUICKLOGIC_EOS_S3_PINMUX(pin, fun)
```

相关声明：[QUICKLOGIC_EOS_S3_PINMUX](#a32684ea1b082834fcadc1d17ab2f6ea7)。

<a id="r_ac3cce2e16d9678b674a6b73e9675cb56"></a>

```c
#define UART_TX_PAD44 QUICKLOGIC_EOS_S3_PINMUX(44, 0x3)
```

相关声明：[UART_TX_PAD44](#ac3cce2e16d9678b674a6b73e9675cb56)、[QUICKLOGIC_EOS_S3_PINMUX](#a32684ea1b082834fcadc1d17ab2f6ea7)。

<a id="r_a4c89eee6f06d8e99b1d042b385622cae"></a>

```c
#define UART_RX_PAD45 QUICKLOGIC_EOS_S3_PINMUX(45, FUNC_SEL_UART_RX | BIT(2))
```

相关声明：[UART_RX_PAD45](#a4c89eee6f06d8e99b1d042b385622cae)、[QUICKLOGIC_EOS_S3_PINMUX](#a32684ea1b082834fcadc1d17ab2f6ea7)、[FUNC_SEL_UART_RX](#a76393e634c1e77ca47d7106c27889936)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ac8ede25f5a027513c1815e1ecd59f8b7"></a>

```c
#define USB_PU_CTRL_PAD23 QUICKLOGIC_EOS_S3_PINMUX(23, 0x0)
```

相关声明：[USB_PU_CTRL_PAD23](#ac8ede25f5a027513c1815e1ecd59f8b7)、[QUICKLOGIC_EOS_S3_PINMUX](#a32684ea1b082834fcadc1d17ab2f6ea7)。

<a id="r_ac9f2cd78de5e93b13ac7683e1439b21d"></a>

```c
#define USB_DN_PAD28 QUICKLOGIC_EOS_S3_PINMUX(28, 0x0)
```

相关声明：[USB_DN_PAD28](#ac9f2cd78de5e93b13ac7683e1439b21d)、[QUICKLOGIC_EOS_S3_PINMUX](#a32684ea1b082834fcadc1d17ab2f6ea7)。

<a id="r_ac814f848b3db7d98dada168dad9e0b74"></a>

```c
#define USB_DP_PAD31 QUICKLOGIC_EOS_S3_PINMUX(31, 0x0)
```

相关声明：[USB_DP_PAD31](#ac814f848b3db7d98dada168dad9e0b74)、[QUICKLOGIC_EOS_S3_PINMUX](#a32684ea1b082834fcadc1d17ab2f6ea7)。

## 317.2\_详细说明（Detailed Documentation）

<a id="a76393e634c1e77ca47d7106c27889936"></a>

### `FUNC_SEL_UART_RX`

```c
#define FUNC_SEL_UART_RX (77 << 13)
```

<a id="ab345030af28df16546437382d1c935a9"></a>

### `IO_MUX_MAX_PAD_NR`

```c
#define IO_MUX_MAX_PAD_NR 45
```

<a id="a42e8d57fbc0ce7fea27c8e5487008c38"></a>

### `IO_MUX_REG_MAX_OFFSET`

```c
#define IO_MUX_REG_MAX_OFFSET 107
```

<a id="a32684ea1b082834fcadc1d17ab2f6ea7"></a>

### `QUICKLOGIC_EOS_S3_PINMUX`

```c
#define QUICKLOGIC_EOS_S3_PINMUX ( pin, fun )
```

展开值（Value）：

```c
(pin) (fun)
```

<a id="a4c89eee6f06d8e99b1d042b385622cae"></a>

### `UART_RX_PAD45`

```c
#define UART_RX_PAD45 QUICKLOGIC_EOS_S3_PINMUX(45, FUNC_SEL_UART_RX | BIT(2))
```

<a id="ac3cce2e16d9678b674a6b73e9675cb56"></a>

### `UART_TX_PAD44`

```c
#define UART_TX_PAD44 QUICKLOGIC_EOS_S3_PINMUX(44, 0x3)
```

<a id="ac9f2cd78de5e93b13ac7683e1439b21d"></a>

### `USB_DN_PAD28`

```c
#define USB_DN_PAD28 QUICKLOGIC_EOS_S3_PINMUX(28, 0x0)
```

<a id="ac814f848b3db7d98dada168dad9e0b74"></a>

### `USB_DP_PAD31`

```c
#define USB_DP_PAD31 QUICKLOGIC_EOS_S3_PINMUX(31, 0x0)
```

<a id="ac8ede25f5a027513c1815e1ecd59f8b7"></a>

### `USB_PU_CTRL_PAD23`

```c
#define USB_PU_CTRL_PAD23 QUICKLOGIC_EOS_S3_PINMUX(23, 0x0)
```


## 317.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P006_设备树绑定工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P692_quicklogic-eos-s3-pinctrl.h_源码浏览.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P316_zephyr__drivers__sensor__qdec_nxp_tpm.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P318_zephyr__dt-bindings__clock__r8a7795_cpg_mssr.h_文件参考.md)
