---
id: learning.zephyr-docs.api-file-paging-wakeup-reference.page-9
title: zephyr__dt-bindings__gpio__stmod-plus-connector.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stmod-plus-connector_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_zephyr\_\_dt-bindings\_\_gpio\_\_stmod-plus-connector.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/stmod-plus-connector_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

STMod+连接器引脚常量（Connector Pin Constants）。

查看此文件的源码。

<a id="details"></a>

STMod+连接器引脚常量（Connector Pin Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.1\_宏定义（Macros）

<a id="r_ga4ccc9a06cbc022fa1992b0664f22fe19"></a>

```c
#define STMOD_PLUS_NSS_CTS 1
```

相关声明：[STMOD_PLUS_NSS_CTS](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#ga4ccc9a06cbc022fa1992b0664f22fe19)。

引脚（Pin）1：SPI 从设备选择（NSS）或 UART 清除发送（CTS）。

<a id="r_ga3d529e03b25237370a3ed7a41479c3c7"></a>

```c
#define STMOD_PLUS_MOSI_TX 2
```

相关声明：[STMOD_PLUS_MOSI_TX](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#ga3d529e03b25237370a3ed7a41479c3c7)。

引脚（Pin）2：SPI 主出从入（MOSI）或 UART 发送（TX）。

<a id="r_gac16872b004ca5e75da331988cf8df0dc"></a>

```c
#define STMOD_PLUS_MISO_RX 3
```

相关声明：[STMOD_PLUS_MISO_RX](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#gac16872b004ca5e75da331988cf8df0dc)。

引脚（Pin）3：SPI 主入从出（MISO）或 UART 接收（RX）。

<a id="r_ga82eb37ff08b92222148a7bbc2545c45a"></a>

```c
#define STMOD_PLUS_SCK_RTS 4
```

相关声明：[STMOD_PLUS_SCK_RTS](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#ga82eb37ff08b92222148a7bbc2545c45a)。

引脚（Pin）4：SPI 串行时钟（SCK）或 UART 请求发送（RTS）。

<a id="r_ga0ad79024b6a6b49f0deec4c117e5be87"></a>

```c
#define STMOD_PLUS_SCL 7
```

相关声明：[STMOD_PLUS_SCL](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#ga0ad79024b6a6b49f0deec4c117e5be87)。

引脚（Pin）7：I2C 串行时钟线（SCL）。

<a id="r_ga831f9e5735c21ad3923e440bf36b77c6"></a>

```c
#define STMOD_PLUS_MOSIS 8
```

相关声明：[STMOD_PLUS_MOSIS](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#ga831f9e5735c21ad3923e440bf36b77c6)。

引脚（Pin）8：次级 SPI 主出从入（Secondary SPI MOSI）。

<a id="r_gabef67327ffc75ffec03c5280f790176f"></a>

```c
#define STMOD_PLUS_MISOS 9
```

相关声明：[STMOD_PLUS_MISOS](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#gabef67327ffc75ffec03c5280f790176f)。

引脚（Pin）9：次级 SPI 主入从出（Secondary SPI MISO）。

<a id="r_gaf65f056444186757cc8abac51378ae81"></a>

```c
#define STMOD_PLUS_SDA 10
```

相关声明：[STMOD_PLUS_SDA](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#gaf65f056444186757cc8abac51378ae81)。

引脚（Pin）10：I2C 串行数据线（SDA）。

<a id="r_gad05629139808ee5c0fa6640a7fe9a563"></a>

```c
#define STMOD_PLUS_INT 11
```

相关声明：[STMOD_PLUS_INT](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#gad05629139808ee5c0fa6640a7fe9a563)。

引脚（Pin）11：中断（Interrupt）。

<a id="r_ga169e27d0145b4118d0ca3e79b6f1ad7b"></a>

```c
#define STMOD_PLUS_RESET 12
```

相关声明：[STMOD_PLUS_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#ga169e27d0145b4118d0ca3e79b6f1ad7b)。

引脚（Pin）12：复位（Reset）。

<a id="r_ga1464e59b68a95053ffa570a9308a101d"></a>

```c
#define STMOD_PLUS_ADC 13
```

相关声明：[STMOD_PLUS_ADC](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#ga1464e59b68a95053ffa570a9308a101d)。

引脚（Pin）13：模数转换（ADC）。

<a id="r_gacceeb4b1d9a563c4932c89930e0b2652"></a>

```c
#define STMOD_PLUS_PWM 14
```

相关声明：[STMOD_PLUS_PWM](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#gacceeb4b1d9a563c4932c89930e0b2652)。

引脚（Pin）14：脉宽调制（PWM）。

<a id="r_gaa56ffc241f79612f233d9ebd0e636fbd"></a>

```c
#define STMOD_PLUS_GPIO17 17
```

相关声明：[STMOD_PLUS_GPIO17](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#gaa56ffc241f79612f233d9ebd0e636fbd)。

引脚（Pin）17：通用输入／输出（GPIO）。

<a id="r_ga9383853ca037e76207a8bd7f433645bd"></a>

```c
#define STMOD_PLUS_GPIO18 18
```

相关声明：[STMOD_PLUS_GPIO18](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#ga9383853ca037e76207a8bd7f433645bd)。

引脚（Pin）18：通用输入／输出（GPIO）。

<a id="r_ga0d80f729c6bbd23321fb3063455de9d4"></a>

```c
#define STMOD_PLUS_GPIO19 19
```

相关声明：[STMOD_PLUS_GPIO19](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#ga0d80f729c6bbd23321fb3063455de9d4)。

引脚（Pin）19：通用输入／输出（GPIO）。

<a id="r_gaa56cf9dede254ef3807989066d757da6"></a>

```c
#define STMOD_PLUS_GPIO20 20
```

相关声明：[STMOD_PLUS_GPIO20](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#gaa56cf9dede254ef3807989066d757da6)。

引脚（Pin）20：通用输入／输出（GPIO）。


## 9.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P838_stmod-plus-connector.h_源码浏览.md)
- [STMOD_PLUS_NSS_CTS](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#ga4ccc9a06cbc022fa1992b0664f22fe19)
- [STMOD_PLUS_MOSI_TX](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#ga3d529e03b25237370a3ed7a41479c3c7)
- [STMOD_PLUS_MISO_RX](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#gac16872b004ca5e75da331988cf8df0dc)
- [STMOD_PLUS_SCK_RTS](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#ga82eb37ff08b92222148a7bbc2545c45a)
- [STMOD_PLUS_SCL](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#ga0ad79024b6a6b49f0deec4c117e5be87)
- [STMOD_PLUS_MOSIS](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#ga831f9e5735c21ad3923e440bf36b77c6)
- [STMOD_PLUS_MISOS](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#gabef67327ffc75ffec03c5280f790176f)
- [STMOD_PLUS_SDA](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#gaf65f056444186757cc8abac51378ae81)
- [STMOD_PLUS_INT](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#gad05629139808ee5c0fa6640a7fe9a563)
- [STMOD_PLUS_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#ga169e27d0145b4118d0ca3e79b6f1ad7b)
- [STMOD_PLUS_ADC](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#ga1464e59b68a95053ffa570a9308a101d)
- [STMOD_PLUS_PWM](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#gacceeb4b1d9a563c4932c89930e0b2652)
- [STMOD_PLUS_GPIO17](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#gaa56ffc241f79612f233d9ebd0e636fbd)
- [STMOD_PLUS_GPIO18](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#ga9383853ca037e76207a8bd7f433645bd)
- [STMOD_PLUS_GPIO19](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#ga0d80f729c6bbd23321fb3063455de9d4)
- [STMOD_PLUS_GPIO20](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#gaa56cf9dede254ef3807989066d757da6)

<a id="header-details"></a>

---

[上一章](P008_zephyr__dt-bindings__sensor__lsm6dso.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P010_zephyr__drivers__tee.h_文件参考.md)
