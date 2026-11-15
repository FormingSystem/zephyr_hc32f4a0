---
id: learning.zephyr-docs.api-file-reference.page-78
title: zephyr__dt-bindings__dai__esai.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/esai_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第78章\_zephyr\_\_dt-bindings\_\_dai\_\_esai.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/esai_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 78.1\_宏定义（Macros）

<a id="r_a0ecf07d3d8c2c903415855b8f965acb0"></a>

```c
#define ESAI_PIN_SCKR 0
```

相关声明：[ESAI_PIN_SCKR](#a0ecf07d3d8c2c903415855b8f965acb0)。

<a id="r_aaa068c1d85f68a1920c09869f0357fb0"></a>

```c
#define ESAI_PIN_FSR 1
```

相关声明：[ESAI_PIN_FSR](#aaa068c1d85f68a1920c09869f0357fb0)。

<a id="r_a51c7d00b37bc05083003cd6dbced3729"></a>

```c
#define ESAI_PIN_HCKR 2
```

相关声明：[ESAI_PIN_HCKR](#a51c7d00b37bc05083003cd6dbced3729)。

<a id="r_af7b3a20b6d2bd2d5981fdbbf2b0aa724"></a>

```c
#define ESAI_PIN_SCKT 3
```

相关声明：[ESAI_PIN_SCKT](#af7b3a20b6d2bd2d5981fdbbf2b0aa724)。

<a id="r_a39a776b51d482d1d3703687d1245707b"></a>

```c
#define ESAI_PIN_FST 4
```

相关声明：[ESAI_PIN_FST](#a39a776b51d482d1d3703687d1245707b)。

<a id="r_a8d1d03217fa1c8a34b4da979fd9109f6"></a>

```c
#define ESAI_PIN_HCKT 5
```

相关声明：[ESAI_PIN_HCKT](#a8d1d03217fa1c8a34b4da979fd9109f6)。

<a id="r_a0be21dd83a00fb159ebaab72d0167963"></a>

```c
#define ESAI_PIN_SDO5_SDI0 6
```

相关声明：[ESAI_PIN_SDO5_SDI0](#a0be21dd83a00fb159ebaab72d0167963)。

<a id="r_ad37097a420f0c7a3a02b91e4dba4ff30"></a>

```c
#define ESAI_PIN_SDO4_SDI1 7
```

相关声明：[ESAI_PIN_SDO4_SDI1](#ad37097a420f0c7a3a02b91e4dba4ff30)。

<a id="r_afef3657ae9abe5b87825130e339da830"></a>

```c
#define ESAI_PIN_SDO3_SDI2 8
```

相关声明：[ESAI_PIN_SDO3_SDI2](#afef3657ae9abe5b87825130e339da830)。

<a id="r_a7123d6105473a424d5e19ef9a19b0199"></a>

```c
#define ESAI_PIN_SDO2_SDI3 9
```

相关声明：[ESAI_PIN_SDO2_SDI3](#a7123d6105473a424d5e19ef9a19b0199)。

<a id="r_aa17e5a390c45ea4178099101ac237a69"></a>

```c
#define ESAI_PIN_SDO1 10
```

相关声明：[ESAI_PIN_SDO1](#aa17e5a390c45ea4178099101ac237a69)。

<a id="r_a07435a87e30cf1515e531e4c8d2dba9c"></a>

```c
#define ESAI_PIN_SDO0 11
```

相关声明：[ESAI_PIN_SDO0](#a07435a87e30cf1515e531e4c8d2dba9c)。

<a id="r_ac56cf8438edfd9a85874e483ce60c735"></a>

```c
#define ESAI_PIN_DISCONNECTED 0
```

相关声明：[ESAI_PIN_DISCONNECTED](#ac56cf8438edfd9a85874e483ce60c735)。

<a id="r_af8daf7391a773a57c7ec12533dc37311"></a>

```c
#define ESAI_PIN_GPIO_INPUT 1
```

相关声明：[ESAI_PIN_GPIO_INPUT](#af8daf7391a773a57c7ec12533dc37311)。

<a id="r_a44ed57556dec275c32655a744d9a73e1"></a>

```c
#define ESAI_PIN_GPIO_OUTPUT 2
```

相关声明：[ESAI_PIN_GPIO_OUTPUT](#a44ed57556dec275c32655a744d9a73e1)。

<a id="r_a6b646d2a0fca23ae6d64fc23e7f22b82"></a>

```c
#define ESAI_PIN_ESAI 3
```

相关声明：[ESAI_PIN_ESAI](#a6b646d2a0fca23ae6d64fc23e7f22b82)。

<a id="r_a4e42ff9c73e9c4fea3dd64094c2dbe4b"></a>

```c
#define ESAI_CLOCK_HCKT 0
```

相关声明：[ESAI_CLOCK_HCKT](#a4e42ff9c73e9c4fea3dd64094c2dbe4b)。

<a id="r_a17e8525d3614a83135c1db5e4c01cfb9"></a>

```c
#define ESAI_CLOCK_HCKR 1
```

相关声明：[ESAI_CLOCK_HCKR](#a17e8525d3614a83135c1db5e4c01cfb9)。

<a id="r_a1ee9d84226904ec56d5c0b0a3cdc4029"></a>

```c
#define ESAI_CLOCK_SCKR 2
```

相关声明：[ESAI_CLOCK_SCKR](#a1ee9d84226904ec56d5c0b0a3cdc4029)。

<a id="r_ae88b5ef4c02cc0295370bd3eadbbed4d"></a>

```c
#define ESAI_CLOCK_SCKT 3
```

相关声明：[ESAI_CLOCK_SCKT](#ae88b5ef4c02cc0295370bd3eadbbed4d)。

<a id="r_af276b6b50ad3547a86781ad62046559f"></a>

```c
#define ESAI_CLOCK_FSR 4
```

相关声明：[ESAI_CLOCK_FSR](#af276b6b50ad3547a86781ad62046559f)。

<a id="r_af6b2e21a927badb50d300d77c80a8a87"></a>

```c
#define ESAI_CLOCK_FST 5
```

相关声明：[ESAI_CLOCK_FST](#af6b2e21a927badb50d300d77c80a8a87)。

<a id="r_a7a507b5077c73ffd5b283edbb468d083"></a>

```c
#define ESAI_CLOCK_INPUT 0
```

相关声明：[ESAI_CLOCK_INPUT](#a7a507b5077c73ffd5b283edbb468d083)。

<a id="r_a6396996ca6821c8dba963c013e7496f3"></a>

```c
#define ESAI_CLOCK_OUTPUT 1
```

相关声明：[ESAI_CLOCK_OUTPUT](#a6396996ca6821c8dba963c013e7496f3)。

## 78.2\_详细说明（Detailed Documentation）

<a id="af276b6b50ad3547a86781ad62046559f"></a>

### `ESAI_CLOCK_FSR`

```c
#define ESAI_CLOCK_FSR 4
```

<a id="af6b2e21a927badb50d300d77c80a8a87"></a>

### `ESAI_CLOCK_FST`

```c
#define ESAI_CLOCK_FST 5
```

<a id="a17e8525d3614a83135c1db5e4c01cfb9"></a>

### `ESAI_CLOCK_HCKR`

```c
#define ESAI_CLOCK_HCKR 1
```

<a id="a4e42ff9c73e9c4fea3dd64094c2dbe4b"></a>

### `ESAI_CLOCK_HCKT`

```c
#define ESAI_CLOCK_HCKT 0
```

<a id="a7a507b5077c73ffd5b283edbb468d083"></a>

### `ESAI_CLOCK_INPUT`

```c
#define ESAI_CLOCK_INPUT 0
```

<a id="a6396996ca6821c8dba963c013e7496f3"></a>

### `ESAI_CLOCK_OUTPUT`

```c
#define ESAI_CLOCK_OUTPUT 1
```

<a id="a1ee9d84226904ec56d5c0b0a3cdc4029"></a>

### `ESAI_CLOCK_SCKR`

```c
#define ESAI_CLOCK_SCKR 2
```

<a id="ae88b5ef4c02cc0295370bd3eadbbed4d"></a>

### `ESAI_CLOCK_SCKT`

```c
#define ESAI_CLOCK_SCKT 3
```

<a id="ac56cf8438edfd9a85874e483ce60c735"></a>

### `ESAI_PIN_DISCONNECTED`

```c
#define ESAI_PIN_DISCONNECTED 0
```

<a id="a6b646d2a0fca23ae6d64fc23e7f22b82"></a>

### `ESAI_PIN_ESAI`

```c
#define ESAI_PIN_ESAI 3
```

<a id="aaa068c1d85f68a1920c09869f0357fb0"></a>

### `ESAI_PIN_FSR`

```c
#define ESAI_PIN_FSR 1
```

<a id="a39a776b51d482d1d3703687d1245707b"></a>

### `ESAI_PIN_FST`

```c
#define ESAI_PIN_FST 4
```

<a id="af8daf7391a773a57c7ec12533dc37311"></a>

### `ESAI_PIN_GPIO_INPUT`

```c
#define ESAI_PIN_GPIO_INPUT 1
```

<a id="a44ed57556dec275c32655a744d9a73e1"></a>

### `ESAI_PIN_GPIO_OUTPUT`

```c
#define ESAI_PIN_GPIO_OUTPUT 2
```

<a id="a51c7d00b37bc05083003cd6dbced3729"></a>

### `ESAI_PIN_HCKR`

```c
#define ESAI_PIN_HCKR 2
```

<a id="a8d1d03217fa1c8a34b4da979fd9109f6"></a>

### `ESAI_PIN_HCKT`

```c
#define ESAI_PIN_HCKT 5
```

<a id="a0ecf07d3d8c2c903415855b8f965acb0"></a>

### `ESAI_PIN_SCKR`

```c
#define ESAI_PIN_SCKR 0
```

<a id="af7b3a20b6d2bd2d5981fdbbf2b0aa724"></a>

### `ESAI_PIN_SCKT`

```c
#define ESAI_PIN_SCKT 3
```

<a id="a07435a87e30cf1515e531e4c8d2dba9c"></a>

### `ESAI_PIN_SDO0`

```c
#define ESAI_PIN_SDO0 11
```

<a id="aa17e5a390c45ea4178099101ac237a69"></a>

### `ESAI_PIN_SDO1`

```c
#define ESAI_PIN_SDO1 10
```

<a id="a7123d6105473a424d5e19ef9a19b0199"></a>

### `ESAI_PIN_SDO2_SDI3`

```c
#define ESAI_PIN_SDO2_SDI3 9
```

<a id="afef3657ae9abe5b87825130e339da830"></a>

### `ESAI_PIN_SDO3_SDI2`

```c
#define ESAI_PIN_SDO3_SDI2 8
```

<a id="ad37097a420f0c7a3a02b91e4dba4ff30"></a>

### `ESAI_PIN_SDO4_SDI1`

```c
#define ESAI_PIN_SDO4_SDI1 7
```

<a id="a0be21dd83a00fb159ebaab72d0167963"></a>

### `ESAI_PIN_SDO5_SDI0`

```c
#define ESAI_PIN_SDO5_SDI0 6
```


## 78.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/esai_8h_source.html)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P077_zephyr__dt-bindings__pinctrl__ene-kb1200-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P079_zephyr__dt-bindings__interrupt-controller__esp-esp32c2-intmux.h_文件参考.md)
