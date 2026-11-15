---
id: learning.zephyr-docs.api-file-system-power-reference.page-33
title: zephyr__dt-bindings__usb-c__pd.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pd_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_zephyr\_\_dt-bindings\_\_usb-c\_\_pd.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pd_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

USB电力传输（Power Delivery）的电源数据对象（PDO）定义。

查看此文件的源码。

<a id="details"></a>

USB电力传输（Power Delivery）的电源数据对象（PDO）定义。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 33.1\_宏定义（Macros）

<a id="r_ga9fa615ab7f38385c21277d4e9e6a1441"></a>

```c
#define PDO_FIXED(mv, ma, flags)
```

相关声明：[PDO_FIXED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery__pdo.html#ga9fa615ab7f38385c21277d4e9e6a1441)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

构造固定供电电源数据对象（Fixed Supply PDO）。

<a id="r_gae3c4f39fb7ff5b00bdc25676af3b88f7"></a>

```c
#define VSAFE5V 5000
```

相关声明：[VSAFE5V](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery__pdo.html#gae3c4f39fb7ff5b00bdc25676af3b88f7)。

`vSafe5V`：默认 5 V 供电，单位为毫伏（Millivolts）。

<a id="r_ga37daa9cc2b8482e127d31c2f3ea4e7ed"></a>

```c
#define PDO_BATT(min_mv, max_mv, max_mw)
```

相关声明：[PDO_BATT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery__pdo.html#ga37daa9cc2b8482e127d31c2f3ea4e7ed)。

构造电池供电电源数据对象（Battery Supply PDO）。

<a id="r_ga359cf8ce52c69924cd2962b2a766f794"></a>

```c
#define PDO_VAR(min_mv, max_mv, max_ma)
```

相关声明：[PDO_VAR](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery__pdo.html#ga359cf8ce52c69924cd2962b2a766f794)。

构造可变供电、非电池类电源数据对象（Variable Supply, Non-Battery PDO）。

<a id="r_ga48f8ae89ab76eae6f27585b389f2b33b"></a>

```c
#define PDO_PPS_APDO(min_mv, max_mv, max_ma)
```

相关声明：[PDO_PPS_APDO](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery__pdo.html#ga48f8ae89ab76eae6f27585b389f2b33b)。

构造可编程电源（Programmable Power Supply，PPS）增强型电源数据对象（Augmented PDO）。

<a id="define-members-0"></a>

### 固定供电 PDO 能力标志（Fixed Supply PDO Capability Flags）

<a id="r_ga06df29b5b810f22013ad2135cb0238ea"></a>

```c
#define PDO_FIXED_DUAL_ROLE (1 << 29)
```

相关声明：[PDO_FIXED_DUAL_ROLE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery__pdo.html#ga06df29b5b810f22013ad2135cb0238ea)。

支持供电角色交换（Power Role Swap）。

<a id="r_ga869842bccecddf1941826fba3399f735"></a>

```c
#define PDO_FIXED_SUSPEND (1 << 28)
```

相关声明：[PDO_FIXED_SUSPEND](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery__pdo.html#ga869842bccecddf1941826fba3399f735)。

支持 USB 挂起（USB Suspend），适用于供电端（Source）。

<a id="r_gae7692e9c32e7c6ee2cf8e4c84d0752d8"></a>

```c
#define PDO_FIXED_HIGHER_CAP (1 << 28)
```

相关声明：[PDO_FIXED_HIGHER_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery__pdo.html#gae7692e9c32e7c6ee2cf8e4c84d0752d8)。

需要高于 `vSafe5V` 的供电，适用于受电端（Sink）。

<a id="r_ga9e098ecbd9e7b74052fcbf302a0f6a41"></a>

```c
#define PDO_FIXED_EXTPOWER (1 << 27)
```

相关声明：[PDO_FIXED_EXTPOWER](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery__pdo.html#ga9e098ecbd9e7b74052fcbf302a0f6a41)。

由外部供电（Externally Powered）。

<a id="r_ga398ebc832c89bd8cbccd08b3def758dd"></a>

```c
#define PDO_FIXED_USB_COMM (1 << 26)
```

相关声明：[PDO_FIXED_USB_COMM](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery__pdo.html#ga398ebc832c89bd8cbccd08b3def758dd)。

具备 USB 通信能力（USB Communications Capable）。

<a id="r_ga17760e6fb2761a8d14d41f1f44993c3b"></a>

```c
#define PDO_FIXED_DATA_SWAP (1 << 25)
```

相关声明：[PDO_FIXED_DATA_SWAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery__pdo.html#ga17760e6fb2761a8d14d41f1f44993c3b)。

支持数据角色交换（Data Role Swap）。


## 33.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_compiler_device_reference/P019_pd.h_源码浏览.md)
- [PDO_FIXED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery__pdo.html#ga9fa615ab7f38385c21277d4e9e6a1441)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [VSAFE5V](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery__pdo.html#gae3c4f39fb7ff5b00bdc25676af3b88f7)
- [PDO_BATT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery__pdo.html#ga37daa9cc2b8482e127d31c2f3ea4e7ed)
- [PDO_VAR](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery__pdo.html#ga359cf8ce52c69924cd2962b2a766f794)
- [PDO_PPS_APDO](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery__pdo.html#ga48f8ae89ab76eae6f27585b389f2b33b)
- [PDO_FIXED_DUAL_ROLE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery__pdo.html#ga06df29b5b810f22013ad2135cb0238ea)
- [PDO_FIXED_SUSPEND](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery__pdo.html#ga869842bccecddf1941826fba3399f735)
- [PDO_FIXED_HIGHER_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery__pdo.html#gae7692e9c32e7c6ee2cf8e4c84d0752d8)
- [PDO_FIXED_EXTPOWER](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery__pdo.html#ga9e098ecbd9e7b74052fcbf302a0f6a41)
- [PDO_FIXED_USB_COMM](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery__pdo.html#ga398ebc832c89bd8cbccd08b3def758dd)
- [PDO_FIXED_DATA_SWAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery__pdo.html#ga17760e6fb2761a8d14d41f1f44993c3b)

<a id="header-details"></a>

---

[上一章](P032_zephyr__bluetooth__audio__pacs.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P034_zephyr__posix__sys__eventfd.h_文件参考.md)
