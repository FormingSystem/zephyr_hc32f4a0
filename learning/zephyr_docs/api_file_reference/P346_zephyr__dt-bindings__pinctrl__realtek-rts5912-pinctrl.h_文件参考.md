---
id: learning.zephyr-docs.api-file-reference.page-346
title: zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/realtek-rts5912-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第346章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_realtek-rts5912-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/realtek-rts5912-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/dt-bindings/dt-util.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 346.1\_宏定义（Macros）

<a id="r_acaf6fce01a1687b4286a749ead4ca90c"></a>

```c
#define REALTEK_RTS5912_GPIO_INOUT BIT(0) /* IN/OUT : 0 input 1 output */
```

相关声明：[REALTEK_RTS5912_GPIO_INOUT](#acaf6fce01a1687b4286a749ead4ca90c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a37c9b457ded69e287ac79d93d75392f1"></a>

```c
#define REALTEK_RTS5912_GPIO_PINON BIT(1) /* Input_detect : 1 enable 0 disable */
```

相关声明：[REALTEK_RTS5912_GPIO_PINON](#a37c9b457ded69e287ac79d93d75392f1)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_af6ac5662dc1122df9934acdfda1a972f"></a>

```c
#define REALTEK_RTS5912_GPIO_VOLT BIT(2) /* Pin Volt : 1 1.8V 0 3.3V */
```

相关声明：[REALTEK_RTS5912_GPIO_VOLT](#af6ac5662dc1122df9934acdfda1a972f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_aa068c89b25e53c56cebaa2c292f0d496"></a>

```c
#define REALTEK_RTS5912_FUNC0 0 /* GPIO mode */
```

相关声明：[REALTEK_RTS5912_FUNC0](#aa068c89b25e53c56cebaa2c292f0d496)。

<a id="r_a320f452117e29ea363d8e92791d11a62"></a>

```c
#define REALTEK_RTS5912_FUNC1 BIT(8) /* Function mode use BIT0~2 */
```

相关声明：[REALTEK_RTS5912_FUNC1](#a320f452117e29ea363d8e92791d11a62)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a0f1aeb726f327dd57aa91fcd68fb96e7"></a>

```c
#define REALTEK_RTS5912_FUNC2 BIT(9)
```

相关声明：[REALTEK_RTS5912_FUNC2](#a0f1aeb726f327dd57aa91fcd68fb96e7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a1cf29b9a5799e9ecc455e8f304114574"></a>

```c
#define REALTEK_RTS5912_FUNC3 ((BIT(8)) | (BIT(9)))
```

相关声明：[REALTEK_RTS5912_FUNC3](#a1cf29b9a5799e9ecc455e8f304114574)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a2f9db2ea5d8996c5374eb1c314f2b206"></a>

```c
#define REALTEK_RTS5912_FUNC4 BIT(10)
```

相关声明：[REALTEK_RTS5912_FUNC4](#a2f9db2ea5d8996c5374eb1c314f2b206)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ad919b2c55c39409ce55e61c9a6c4b517"></a>

```c
#define REALTEK_RTS5912_INPUT_OUTPUT_POS 0
```

相关声明：[REALTEK_RTS5912_INPUT_OUTPUT_POS](#ad919b2c55c39409ce55e61c9a6c4b517)。

<a id="r_a126ef964f014695a4ba2bb12f80df4b7"></a>

```c
#define REALTEK_RTS5912_INPUT_DETECTION_POS 1
```

相关声明：[REALTEK_RTS5912_INPUT_DETECTION_POS](#a126ef964f014695a4ba2bb12f80df4b7)。

<a id="r_a129d1a2771427bf45ebe1d68b86d1f52"></a>

```c
#define REALTEK_RTS5912_VOLTAGE_POS 2
```

相关声明：[REALTEK_RTS5912_VOLTAGE_POS](#a129d1a2771427bf45ebe1d68b86d1f52)。

<a id="r_af2020d8bbae4e24b4e5f48ce1f4fc7f1"></a>

```c
#define REALTEK_RTS5912_DRV_STR_POS 11
```

相关声明：[REALTEK_RTS5912_DRV_STR_POS](#af2020d8bbae4e24b4e5f48ce1f4fc7f1)。

<a id="r_af5aa6f81b75e84553e31401a798266f5"></a>

```c
#define REALTEK_RTS5912_SLEW_RATE_POS 12
```

相关声明：[REALTEK_RTS5912_SLEW_RATE_POS](#af5aa6f81b75e84553e31401a798266f5)。

<a id="r_af8faf52c5ea35defe026cb4f6cc95cdc"></a>

```c
#define REALTEK_RTS5912_PD_POS 13
```

相关声明：[REALTEK_RTS5912_PD_POS](#af8faf52c5ea35defe026cb4f6cc95cdc)。

<a id="r_ae3fc4f59fc38de4f3380b13eab30842d"></a>

```c
#define REALTEK_RTS5912_PU_POS 14
```

相关声明：[REALTEK_RTS5912_PU_POS](#ae3fc4f59fc38de4f3380b13eab30842d)。

<a id="r_ac89f34fde098b5df324b3ed69f108aec"></a>

```c
#define REALTEK_RTS5912_SCHMITTER_POS 15
```

相关声明：[REALTEK_RTS5912_SCHMITTER_POS](#ac89f34fde098b5df324b3ed69f108aec)。

<a id="r_ab4802986241c477ce74d7ab082ef9ff3"></a>

```c
#define REALTEK_RTS5912_TYPE_POS 16
```

相关声明：[REALTEK_RTS5912_TYPE_POS](#ab4802986241c477ce74d7ab082ef9ff3)。

<a id="r_a67f5fb84972d53406c8c9e440815fe60"></a>

```c
#define REALTEK_RTS5912_HIGH_LOW_POS 17
```

相关声明：[REALTEK_RTS5912_HIGH_LOW_POS](#a67f5fb84972d53406c8c9e440815fe60)。

<a id="r_ab00c925ffba481594ed7216d41efa52a"></a>

```c
#define REALTEK_RTS5912_GPIO_HIGH_POS 18
```

相关声明：[REALTEK_RTS5912_GPIO_HIGH_POS](#ab00c925ffba481594ed7216d41efa52a)。

<a id="r_a7524cfe0cc5990bf5bc835d030deaf11"></a>

```c
#define REALTEK_RTS5912_GPIO_HIGH_MSK 0x3f
```

相关声明：[REALTEK_RTS5912_GPIO_HIGH_MSK](#a7524cfe0cc5990bf5bc835d030deaf11)。

<a id="r_a3f09fb1e1ad93e1fc1189ad5babbc533"></a>

```c
#define REALTEK_RTS5912_GPIO_LOW_POS 3
```

相关声明：[REALTEK_RTS5912_GPIO_LOW_POS](#a3f09fb1e1ad93e1fc1189ad5babbc533)。

<a id="r_a9cbb1539029aa9b58ffedb4b3ede0e93"></a>

```c
#define REALTEK_RTS5912_GPIO_LOW_MSK 0x1f
```

相关声明：[REALTEK_RTS5912_GPIO_LOW_MSK](#a9cbb1539029aa9b58ffedb4b3ede0e93)。

<a id="r_aa3ba064ba85ae0da9c55e7cdb8ea09b3"></a>

```c
#define FUNC0 REALTEK_RTS5912_FUNC0
```

相关声明：[FUNC0](#aa3ba064ba85ae0da9c55e7cdb8ea09b3)、[REALTEK_RTS5912_FUNC0](#aa068c89b25e53c56cebaa2c292f0d496)。

<a id="r_a3f9b8eb1b4789fef1da73f4eb041ddfc"></a>

```c
#define FUNC1 REALTEK_RTS5912_FUNC1
```

相关声明：[FUNC1](#a3f9b8eb1b4789fef1da73f4eb041ddfc)、[REALTEK_RTS5912_FUNC1](#a320f452117e29ea363d8e92791d11a62)。

<a id="r_a0e8023a25dd46655b8eda5b0476ba169"></a>

```c
#define FUNC2 REALTEK_RTS5912_FUNC2
```

相关声明：[FUNC2](#a0e8023a25dd46655b8eda5b0476ba169)、[REALTEK_RTS5912_FUNC2](#a0f1aeb726f327dd57aa91fcd68fb96e7)。

<a id="r_adeea02cdf0e8b64c27b6fad4d2b3b2b5"></a>

```c
#define FUNC3 REALTEK_RTS5912_FUNC3
```

相关声明：[FUNC3](#adeea02cdf0e8b64c27b6fad4d2b3b2b5)、[REALTEK_RTS5912_FUNC3](#a1cf29b9a5799e9ecc455e8f304114574)。

<a id="r_a769e96bef0ce818be7aa2cb0a0a67753"></a>

```c
#define FUNC4 REALTEK_RTS5912_FUNC4
```

相关声明：[FUNC4](#a769e96bef0ce818be7aa2cb0a0a67753)、[REALTEK_RTS5912_FUNC4](#a2f9db2ea5d8996c5374eb1c314f2b206)。

<a id="r_aa3e9ea3bc9606018c92e70d6728c8594"></a>

```c
#define REALTEK_RTS5912_PINMUX(n, f)
```

相关声明：[REALTEK_RTS5912_PINMUX](#aa3e9ea3bc9606018c92e70d6728c8594)。

## 346.2\_详细说明（Detailed Documentation）

<a id="aa3ba064ba85ae0da9c55e7cdb8ea09b3"></a>

### `FUNC0`

```c
#define FUNC0 REALTEK_RTS5912_FUNC0
```

<a id="a3f9b8eb1b4789fef1da73f4eb041ddfc"></a>

### `FUNC1`

```c
#define FUNC1 REALTEK_RTS5912_FUNC1
```

<a id="a0e8023a25dd46655b8eda5b0476ba169"></a>

### `FUNC2`

```c
#define FUNC2 REALTEK_RTS5912_FUNC2
```

<a id="adeea02cdf0e8b64c27b6fad4d2b3b2b5"></a>

### `FUNC3`

```c
#define FUNC3 REALTEK_RTS5912_FUNC3
```

<a id="a769e96bef0ce818be7aa2cb0a0a67753"></a>

### `FUNC4`

```c
#define FUNC4 REALTEK_RTS5912_FUNC4
```

<a id="af2020d8bbae4e24b4e5f48ce1f4fc7f1"></a>

### `REALTEK_RTS5912_DRV_STR_POS`

```c
#define REALTEK_RTS5912_DRV_STR_POS 11
```

<a id="aa068c89b25e53c56cebaa2c292f0d496"></a>

### `REALTEK_RTS5912_FUNC0`

```c
#define REALTEK_RTS5912_FUNC0 0 /* GPIO mode */
```

<a id="a320f452117e29ea363d8e92791d11a62"></a>

### `REALTEK_RTS5912_FUNC1`

```c
#define REALTEK_RTS5912_FUNC1 BIT(8) /* Function mode use BIT0~2 */
```

<a id="a0f1aeb726f327dd57aa91fcd68fb96e7"></a>

### `REALTEK_RTS5912_FUNC2`

```c
#define REALTEK_RTS5912_FUNC2 BIT(9)
```

<a id="a1cf29b9a5799e9ecc455e8f304114574"></a>

### `REALTEK_RTS5912_FUNC3`

```c
#define REALTEK_RTS5912_FUNC3 ((BIT(8)) | (BIT(9)))
```

<a id="a2f9db2ea5d8996c5374eb1c314f2b206"></a>

### `REALTEK_RTS5912_FUNC4`

```c
#define REALTEK_RTS5912_FUNC4 BIT(10)
```

<a id="a7524cfe0cc5990bf5bc835d030deaf11"></a>

### `REALTEK_RTS5912_GPIO_HIGH_MSK`

```c
#define REALTEK_RTS5912_GPIO_HIGH_MSK 0x3f
```

<a id="ab00c925ffba481594ed7216d41efa52a"></a>

### `REALTEK_RTS5912_GPIO_HIGH_POS`

```c
#define REALTEK_RTS5912_GPIO_HIGH_POS 18
```

<a id="acaf6fce01a1687b4286a749ead4ca90c"></a>

### `REALTEK_RTS5912_GPIO_INOUT`

```c
#define REALTEK_RTS5912_GPIO_INOUT BIT(0) /* IN/OUT : 0 input 1 output */
```

<a id="a9cbb1539029aa9b58ffedb4b3ede0e93"></a>

### `REALTEK_RTS5912_GPIO_LOW_MSK`

```c
#define REALTEK_RTS5912_GPIO_LOW_MSK 0x1f
```

<a id="a3f09fb1e1ad93e1fc1189ad5babbc533"></a>

### `REALTEK_RTS5912_GPIO_LOW_POS`

```c
#define REALTEK_RTS5912_GPIO_LOW_POS 3
```

<a id="a37c9b457ded69e287ac79d93d75392f1"></a>

### `REALTEK_RTS5912_GPIO_PINON`

```c
#define REALTEK_RTS5912_GPIO_PINON BIT(1) /* Input_detect : 1 enable 0 disable */
```

<a id="af6ac5662dc1122df9934acdfda1a972f"></a>

### `REALTEK_RTS5912_GPIO_VOLT`

```c
#define REALTEK_RTS5912_GPIO_VOLT BIT(2) /* Pin Volt : 1 1.8V 0 3.3V */
```

<a id="a67f5fb84972d53406c8c9e440815fe60"></a>

### `REALTEK_RTS5912_HIGH_LOW_POS`

```c
#define REALTEK_RTS5912_HIGH_LOW_POS 17
```

<a id="a126ef964f014695a4ba2bb12f80df4b7"></a>

### `REALTEK_RTS5912_INPUT_DETECTION_POS`

```c
#define REALTEK_RTS5912_INPUT_DETECTION_POS 1
```

<a id="ad919b2c55c39409ce55e61c9a6c4b517"></a>

### `REALTEK_RTS5912_INPUT_OUTPUT_POS`

```c
#define REALTEK_RTS5912_INPUT_OUTPUT_POS 0
```

<a id="af8faf52c5ea35defe026cb4f6cc95cdc"></a>

### `REALTEK_RTS5912_PD_POS`

```c
#define REALTEK_RTS5912_PD_POS 13
```

<a id="aa3e9ea3bc9606018c92e70d6728c8594"></a>

### `REALTEK_RTS5912_PINMUX`

```c
#define REALTEK_RTS5912_PINMUX ( n, f )
```

展开值（Value）：

```c
(((((n) >> 5) & REALTEK_RTS5912_GPIO_HIGH_MSK) << REALTEK_RTS5912_GPIO_HIGH_POS) |         \
 (((n) & REALTEK_RTS5912_GPIO_LOW_MSK) << REALTEK_RTS5912_GPIO_LOW_POS) | (f))
```

<a id="ae3fc4f59fc38de4f3380b13eab30842d"></a>

### `REALTEK_RTS5912_PU_POS`

```c
#define REALTEK_RTS5912_PU_POS 14
```

<a id="ac89f34fde098b5df324b3ed69f108aec"></a>

### `REALTEK_RTS5912_SCHMITTER_POS`

```c
#define REALTEK_RTS5912_SCHMITTER_POS 15
```

<a id="af5aa6f81b75e84553e31401a798266f5"></a>

### `REALTEK_RTS5912_SLEW_RATE_POS`

```c
#define REALTEK_RTS5912_SLEW_RATE_POS 12
```

<a id="ab4802986241c477ce74d7ab082ef9ff3"></a>

### `REALTEK_RTS5912_TYPE_POS`

```c
#define REALTEK_RTS5912_TYPE_POS 16
```

<a id="a129d1a2771427bf45ebe1d68b86d1f52"></a>

### `REALTEK_RTS5912_VOLTAGE_POS`

```c
#define REALTEK_RTS5912_VOLTAGE_POS 2
```


## 346.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P006_设备树绑定工具头文件源码.md)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/realtek-rts5912-pinctrl_8h_source.html)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="arealtek-rts5912-pinctrl_8h_html_a3f09fb1e1ad93e1fc1189ad5babbc533"></a>
<a id="arealtek-rts5912-pinctrl_8h_html_a7524cfe0cc5990bf5bc835d030deaf11"></a>
<a id="arealtek-rts5912-pinctrl_8h_html_a9cbb1539029aa9b58ffedb4b3ede0e93"></a>
<a id="arealtek-rts5912-pinctrl_8h_html_ab00c925ffba481594ed7216d41efa52a"></a>

---

[上一章](P345_zephyr__dt-bindings__pwm__ra_pwm.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P347_zephyr__dt-bindings__gpio__renesas-ra-gpio-ioport.h_文件参考.md)
